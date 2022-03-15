# -*- coding: utf-8 -*-
"""Versioning Data & Artifacts in Weights & Biases.

Created on: 3/15/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
from os import path
import argparse
import logging
import pathlib
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def main(
        input_file: str,
        artifact_name: str,
        artifact_type: str,
        artifact_description: str
) -> None:

    if not path.exists(input_file):
        logger.warning(f"File {input_file} does not exists, finishing process")
        return None

    logger.info("Creating run exercise_1")

    with wandb.init(
            project='exercise_1',
            group='experiment_1',
            job_type='upload_file'
    ) as run:

        artifact = wandb.Artifact(
            name=artifact_name,
            type=artifact_type,
            description=artifact_description
        )

        artifact.add_file(input_file)

        run.log_artifact(artifact)

    logger.info(f"File {input_file} logged.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Upload an artifact to W&B", fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--input_file", type=pathlib.Path, help="Path to the input file", required=True
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_type", type=str, help="Type for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_description",
        type=str,
        help="Description for the artifact",
        required=True,
    )

    args = parser.parse_args()

    main(
        input_file=args.input_file,
        artifact_name=args.artifact_name,
        artifact_type=args.artifact_type,
        artifact_description=args.artifact_description
    )