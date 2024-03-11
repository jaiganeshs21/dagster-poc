from dagster import op, job
from everstage_api_task import submit_task_to_everstage, task_status_checker


@op
def submit_task():
    print("DAGSTER: inside submit_task function")
    job_id = submit_task_to_everstage()
    print("DAGSTER: job_id", job_id)
    status = task_status_checker(e2e_sync_run_id=job_id)
    total = 0
    while(status != "complete" and total < 10):
        status = task_status_checker(e2e_sync_run_id=job_id)
        print("DAGSTER submit_task4353333", status)
        import time
        time.sleep(5)
        total=total+5
    
@job
def my_pipeline():
    submit_task()