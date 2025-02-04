"""Configuration structures for Airflow pipeline."""

import os
from dataclasses import dataclass


@dataclass
class PipelineConfiguration:
    """Configuration for Airflow pipeline.

    Attributes:
        gcp_project (str):
            GCP project that pipeline runs in.
        bigquery_dataset (str):
            BigQuery dataset used by project.
        bucket (str):
            Bucket used by project.
        dataform_repository (str):
            Dataform repository to use.
        dataform_region (str):
            Region dataform repository sits in.
        dataform_branch (str):
            Branch of dataform repository to run.

        generic_account_username (str):
            Generic account username.
        generic_account_password_variable_name (str):
            Variable containing the password for the account.
    """

    gcp_project: str
    bigquery_dataset: str
    bucket: str
    dataform_repository: str
    dataform_region: str
    dataform_branch: str


development = PipelineConfiguration(
    gcp_project="<your dev gcp project>",
    bigquery_dataset="<your dev dataset>",
    dataform_repository="<your dev dataform repository name>",
    dataform_region="<your dev dataform repository region>",
    dataform_branch="<your dev dataform branch>",
    bucket="<your dev bucket>",
)

production = PipelineConfiguration(
    gcp_project="<your prod gcp project>",
    bigquery_dataset="<your prod dataset>",
    dataform_repository="<your prod dataform repository name>",
    dataform_region="<your prod dataform repository region>",
    dataform_branch="<your prod dataform branch>",
    bucket="<your prod bucket>",
)


def get_pipeline_config() -> PipelineConfiguration:
    """Get pipeline configuration for current environment.

    Determines which pipeline configuration to used based on
    APP_ENV environment variable.


    Raises:
        ValueError: If no matching pipeline for APP_ENV.

    Returns:
        PipelineConfiguration: Configuration for current environment.
    """
    app_env = os.getenv("APP_ENV", "development")

    if app_env == "development":
        return development
    if app_env == "production":
        return production

    raise ValueError(f"Pipeline configuration not found for APP_ENV: {app_env}")


pipeline = get_pipeline_config()
