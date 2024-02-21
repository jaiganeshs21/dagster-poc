from dagster import op, sensor, RunRequest, job
from everstage_api_task import submit_task_to_everstage, everstage_task_status_checker


@op
def submit_task():
    print("AIRFLOW: inside submit_task function")
    job_id = submit_task_to_everstage()
    print("AIRFLOW: job_id", job_id)

@sensor(job_name="process_job_results")
def sensor_task():
    print("AIRFLOW: inside sensor_task function")
    job_status = everstage_task_status_checker()
    if job_status == "FAILED":
        print("AIRFLOW: Job failed")
        return
    # yield RunRequest(run_key=None)

@job
def my_pipeline():
    submit_task()
    sensor_task()