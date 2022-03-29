# -*- coding: utf-8 -*-
"""Test the Final Model.

Created on: 3/29/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import argparse
import logging
import pandas as pd
import wandb
import mlflow.sklearn
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, plot_confusion_matrix

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def main(
        model_export: str,
        test_data: str
) -> None:

    run = wandb.init(project="exercise_13", job_type="test")

    logger.info("Downloading and reading test artifact")
    ## Get the args.test_data artifact from W&B locally
    test_data_path = run.\
        use_artifact(
            artifact_or_name=test_data).\
        file()

    df = pd.read_csv(test_data_path, low_memory=False)

    # Extract the target from the features
    logger.info("Extracting target from dataframe")
    X_test = df.copy()
    y_test = X_test.pop("genre")

    logger.info("Downloading and reading the exported model")

    model_export_path = run.\
        use_artifact(
            artifact_or_name=model_export).\
        download()

    # Load the model using mlflow.sklearn.load_model
    pipe = mlflow.sklearn.load_model(
        model_uri=model_export_path
    )
    
    #input_schema: mlflow.types.schema.Schema = \
    #    mlflow.pyfunc.load_model(model_export_path).\
    #        model_meta._signature.inputs

    # Compute the prediction from the model using .predict_proba on the test set
    # pred_proba = pipe.predict_proba(X_test[[x.name for x in input_schema._inputs]])
    pred_proba = pipe.predict_proba(X_test)

    logger.info("Scoring")
    score = roc_auc_score(y_test, pred_proba, average="macro", multi_class="ovo")

    run.summary["AUC"] = score

    logger.info("Computing confusion matrix")
    fig_cm, sub_cm = plt.subplots(figsize=(10, 10))
    plot_confusion_matrix(
        pipe,
        X_test,
        y_test,
        ax=sub_cm,
        normalize="true",
        values_format=".1f",
        xticks_rotation=90,
    )
    fig_cm.tight_layout()

    run.log(
        {
            "confusion_matrix": wandb.Image(fig_cm)
        }
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Test the provided model on the test artifact",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--model_export",
        type=str,
        help="Fully-qualified artifact name for the exported model to evaluate",
        required=True,
    )

    parser.add_argument(
        "--test_data",
        type=str,
        help="Fully-qualified artifact name for the test data",
        required=True,
    )

    args = parser.parse_args()

    main(
        model_export=args.model_export,
        test_data=args.test_data
    )