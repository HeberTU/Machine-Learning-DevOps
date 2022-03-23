# -*- coding: utf-8 -*-
"""Clean and Pre-process the Data.

Created on: 3/23/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import argparse
import logging
import pandas as pd
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

def main(
        input_artifact: str,
        artifact_name: str,
        artifact_type: str,
        artifact_description: str
)->None:
    """This function Pre-precess the raw data.

    Args:
        input_artifact: Input artifact.
        artifact_name: Artifact name.
        artifact_type: Artifact type.
        artifact_description: Artifact description.

    return:
        None
    """

    with wandb.init(
            project="exercise_5",
            job_type="process_data"
    ) as run:

        try:
            artifact = run.use_artifact(
                artifact_or_name=input_artifact)
        except wandb.errors.error.CommError:
            logger.error(f"ERROR: {input_artifact} does not exists")
            return None

        df = pd.read_parquet(artifact.file())

        initial_rows =df.shape[0]

        df = df.\
            drop_duplicates().\
            reset_index(drop=True)

        duplicates = initial_rows - df.shape[0]

        logger.info(f"INFO: {duplicates} duplicated rows were removed")

        for col in ['title', 'song_name']:

            missing_values = df[col].isna().sum()

            df[col].fillna(
                value='',
                inplace=True
            )
            logger.info(f"INFO: filling {missing_values} rows "
                        f"with missing value at {col}")

        df['text_feature'] = df['title'] + ' ' + df['song_name']

        artifact = wandb.Artifact(
            name=artifact_name,
            type=artifact_type,
            description=artifact_description
        )
        wandb_table = wandb.Table(data=df)

        artifact.add(
            obj=wandb_table,
            name=artifact_name)

        run.log_artifact(artifact)

    logger.info(f"INFO: File {artifact_name} logged.")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Preprocess a dataset",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "-I", "--input_artifact",
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True,
    )

    parser.add_argument(
        "-N", "--artifact_name", type=str, help="Name for the artifact", required=True
    )

    parser.add_argument(
        "-T", "--artifact_type", type=str, help="Type for the artifact", required=True
    )

    parser.add_argument(
        "-D", "--artifact_description",
        type=str,
        help="Description for the artifact",
        required=True,
    )

    args = parser.parse_args()

    main(
        input_artifact=args.input_artifact,
        artifact_name=args.artifact_name,
        artifact_type=args.artifact_type,
        artifact_description=args.artifact_description
    )