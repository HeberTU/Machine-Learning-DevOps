Machine-Learning-DevOps
==============================
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

- [Origin](https://github.com/HeberTU/Machine-Learning-DevOps)
- Author: Heber Trujillo <heber.trj.urt@gmail.com>
- Date of last README.md update: 01.03.2022

## Repo Overview

The Machine Learning DevOps Engineer Repository is focused on the software 
engineering fundamentals needed to successfully streamline the deployment 
of data and machine-learning models in a production-level environment.

Concretely, the content covers the following ideas:

* Implement production-ready Python code/processes for deploying ML models outside of
cloud-based environments facilitated by tools such as AWS SageMaker, Azure ML, etc.


* Engineer automated data workflows that perform continuous training (CT) and model
validation within a CI/CD pipeline based on updated data versioning.


* Create multi-step pipelines that automatically retrain and deploy models 
after data updates.


* Track model summary statistics and monitor model online performance over time to prevent
model-degradation.

### Content

1. Clean Code Principles.
2. Building a Reproducible Model Workflow.
3. Deploying a Scalable ML Pipeline in Production.
4. Automated model scoring and monitoring.


## How to Run Scripts 

### Dependencies Installation 

1. Create and activate a virtual environment for the project. For example:
    ```bash
    python3 -m venv ./.venv
    ./.venv/Scripts/activate
    ```
   
2. Install Poetry, the tool used for dependency management. To install it, run from a terminal:
    ```bash
    pip install poetry
    ```

3. From the virtual environment, install the required dependencies with:
    ```bash
    poetry install --no-root
    ```

   
## How to Contribute 

### Conventions

#### Linting

All valid python files (*.py) must pass scripts/batch/bach-lint.bat ./Path_to/FILENAME. It takes care of code format, 
style, documentation and imports via flake8, black, isort, pydocstyle.
