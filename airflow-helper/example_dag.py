"""#### example_dag

This an example dag used for getting started.

"""  # noqa: D415

import os
import sys
from datetime import datetime, timedelta

from airflow.decorators import task, task_group
from airflow.models import DAG
from airflow.providers.google.cloud.operators.dataform import (
    DataformCreateCompilationResultOperator,
    DataformCreateWorkflowInvocationOperator,
)

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from config import settings # noqa: I001

default_args = {
    "owner": "Example Owner",
    "start_date": datetime(2022, 1, 1),
    "retries": 0,
    "retry_delay": timedelta(seconds=60),
    "email_on_failure": True,
    "email_on_retry": False
}


with DAG(
    "example_dag",
    description="This an example dag used for getting started.",
    tags=["example-theme"],
    doc_md=__doc__,
    schedule="@daily",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
) as dag:

    @task()
    def example_task():
        """An example task."""
        pass

    @task_group()
    def run_dataform():
        """Compile and run the dataform pipeline."""
        create_compilation_result = DataformCreateCompilationResultOperator(
            task_id="create_compilation_result",
            retries=2,
            project_id=settings.pipeline.gcp_project,
            region=settings.pipeline.dataform_region,
            repository_id=settings.pipeline.dataform_repository,
            compilation_result={
                "git_commitish": settings.pipeline.dataform_branch,
            },
        )

        create_workflow_invocation = DataformCreateWorkflowInvocationOperator(
            task_id="create_workflow_invocation",
            project_id=settings.pipeline.gcp_project,
            region=settings.pipeline.dataform_region,
            repository_id=settings.pipeline.dataform_repository,
            workflow_invocation={
                "compilation_result": "{{ ti.xcom_pull('%s')['name'] }}" # noqa: UP031
                % (create_compilation_result.task_id)
            },
        )

        create_compilation_result >> create_workflow_invocation

    example_task() >> run_dataform()
