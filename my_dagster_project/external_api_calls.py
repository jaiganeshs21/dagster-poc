from dagster import op, sensor, RunRequest, job
from everstage_api_task import everstage_api_task

@op
def start_long_running_job():
    print("DAGSTER: inside start_long_running_job()")
    everstage_api_task()

@job
def my_pipeline():
    job_id = start_long_running_job()
    print("Job ID: ", job_id)


# @sensor(job_name="process_job_results")
# def long_running_job_sensor(context):
#     job_status = external_service.check_job_status()  # Check the status of the job
#     if job_status == "COMPLETED":
#         yield RunRequest(run_key="unique_run_key", run_config={})
#     elif job_status == "FAILED":
#         context.log.error("Long-running job failed.")
