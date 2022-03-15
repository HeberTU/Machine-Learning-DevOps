# -*- coding: utf-8 -*-
"""Demo: Versioning Data and Artifacts in Weights & Biases

Created on: 3/15/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import wandb

with open("./data/artifact_test.txt", "w+") as file:
    file.write("This is an example of an artifact")

run = wandb.init(
    project='demo_artifact_1',
    group="experiment_1"
)

artifact = wandb.Artifact(
    name='artifact_test.txt',  # This name does note necessarily need to be
    # the same of the file
    type='data',
    description='This is an example of an artifact',
    metadata={
        'key_1': 'value_1'
    }
)

artifact.add_file('./data/artifact_test.txt')

run.log_artifact(artifact)

run.finish()

# Generate a new version by changing the artifact
# NOTE: In practice, you will never do this copying and pasting.

with open("./data/artifact_test.txt", "w+") as file:
    file.write("This is an example of an artifact -- V2")

run = wandb.init(
    project='demo_artifact_1',
    group="experiment_1"
)

artifact = wandb.Artifact(
    name='artifact_test.txt',  # This name does note necessarily need to be
    # the same of the file
    type='data',
    description='This is an example of an artifact',
    metadata={
        'key_1': 'value_1'
    }
)

artifact.add_file('./data/artifact_test.txt')

run.log_artifact(artifact)

run.finish()

# Re-Upload the same file will not generate a new version, i.e. v2
# NOTE: In practice, you will never do this copying and pasting.

with open("./data/artifact_test.txt", "w+") as file:
    file.write("This is an example of an artifact -- V2")

run = wandb.init(
    project='demo_artifact_1',
    group="experiment_1"
)

artifact = wandb.Artifact(
    name='artifact_test.txt',  # This name does note necessarily need to be
    # the same of the file
    type='data',
    description='This is an example of an artifact',
    metadata={
        'key_1': 'value_1'
    }
)

artifact.add_file('./data/artifact_test.txt')

run.log_artifact(artifact)

run.finish()

# Using context managers
# NOTE: In practice, you will never do this copying and pasting.

with wandb.init(
    project='demo_artifact_1',
    group="experiment_1"
) as run:

    artifact = wandb.Artifact(
        name='artifact_test.txt',  # This name does note necessarily need to be
        # the same of the file
        type='data',
        description='This is an example of an artifact',
        metadata={
            'key_1': 'value_1'
        }
    )

    artifact.add_file('./data/artifact_test.txt')

    run.log_artifact(artifact)

