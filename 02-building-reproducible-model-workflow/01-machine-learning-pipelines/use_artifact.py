# -*- coding: utf-8 -*-
"""Download part of Versioning Data & Artifacts in Weights & Biases.

Created on: 3/15/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import argparse
import logging
import pathlib
import wandb

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def main(artifact_name:str) -> None:

    logger.info("Creating run in project exercise_1")
    with wandb.init(project="exercise_1", job_type="use_file") as run:

        logger.info("Getting artifact")

        artifact = run.use_artifact(
            artifact_name,
            type='text_file')

        artifact.download()

        artifact_path = artifact.file()

    logger.info("Artifact content:")
    with open(artifact_path, "r") as fp:
        content = fp.read()

    print(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Use an artifact from W&B", fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name and version of W&B artifact",
        required=True
    )

    args = parser.parse_args()

    main(args.artifact_name)