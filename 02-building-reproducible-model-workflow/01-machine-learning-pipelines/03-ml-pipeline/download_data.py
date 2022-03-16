# -*- coding: utf-8 -*-
"""ML Pipeline Components in MLflow example.

Created on: 3/16/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import argparse
import logging
import pathlib
import wandb
import requests
import tempfile


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def mian(
        file_url: str,
        artifact_name: str,
        artifact_type: str,
        artifact_description: str
) -> None:

    # Derive the base name of the file from the URL
    basename = pathlib.Path(file_url).name.split("?")[0].split("#")[0]

    # Download file, streaming so we can download files larger than
    # the available memory. We use a named temporary file that gets
    # destroyed at the end of the context, so we don't leave anything
    # behind and the file gets removed even in case of errors
    logger.info(f"Downloading {file_url} ...")
    with tempfile.NamedTemporaryFile(mode='wb+', delete=False) as fp:

        logger.info("Creating run exercise_2")
        with wandb.init(project="exercise_2", job_type="download_data") as run:
            # Download the file streaming and write to open temp file
            with requests.get(file_url, stream=True) as r:
                for chunk in r.iter_content(chunk_size=8192):
                    fp.write(chunk)

            # Make sure the file has been written to disk before uploading
            # to W&B
            fp.flush()

            logger.info("Creating artifact")
            artifact = wandb.Artifact(
                name=artifact_name,
                type=artifact_type,
                description=artifact_description,
                metadata={'original_url': file_url}
            )
            artifact.add_file(fp.name, name=basename)

            logger.info("Logging artifact")
            run.log_artifact(artifact)

            # This makes sure that the artifact is uploaded before the
            # tempfile is destroyed
            artifact.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a file and upload it as an artifact to W&B",
        fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--file_url", type=str, help="URL to the input file", required=True
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name for the artifact",
        required=True
    )

    parser.add_argument(
        "--artifact_type", type=str, help="Type for the artifact",
        required=True
    )

    parser.add_argument(
        "--artifact_description",
        type=str,
        help="Description for the artifact",
        required=True,
    )

    args = parser.parse_args()

    mian(
        file_url=args.file_url,
        artifact_name=args.artifact_name,
        artifact_type=args.artifact_type,
        artifact_description=args.artifact_description
        )