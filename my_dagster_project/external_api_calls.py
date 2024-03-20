from dagster import op, job
from everstage_api_task import (
    commission_task_to_everstage,
    databook_task_to_everstage,
    task_status_checker,
)
import time


@op
def submit_databook_sync_task():
    print("BEGIN: Inside submit_databook_sync_task function")
    databook_ids = ["6a33079b-4fa7-430e-8031-fdbcc8ea2658"]
    job_id = databook_task_to_everstage(databook_ids=databook_ids)
    print("job_id:", job_id)

    task_status = get_task_status(
        job_id=job_id, timeout=1000, interval=5, task_name="DATASHEET"
    )
    if task_status == "complete":
        print("Databook task completed")
    else:
        raise Exception("Task is not complete, marking pipeline as failed.")


@op
def submit_commission_sync_task(databook_task):
    print("BEGIN: Inside submit_commission_sync_task function")
    job_id = commission_task_to_everstage()
    print("job_id:", job_id)

    task_status = get_task_status(
        job_id=job_id, timeout=1000, interval=5, task_name="COMMISSION"
    )
    if task_status == "complete":
        print("Commission task completed")
    else:
        raise Exception("Task is not complete, marking pipeline as failed.")


def get_task_status(job_id, timeout, interval, task_name):
    """
    This function checks the status of a task in Everstage and returns the status
    """
    total_time = 0
    status = ""

    while total_time < timeout:
        status = task_status_checker(e2e_sync_run_id=job_id, task_name=task_name)
        print("Current status:", status)

        if status == "complete":
            print("Task complete.")
            return status
        elif status in ["failed", "partially_failed"]:
            print("Task failed.")
            return status

        time.sleep(interval)
        total_time += interval

    print("Timeout exceeded. Task incomplete.")
    return "timeout_exceeded"


@job
def my_pipeline():
    databook_task = submit_databook_sync_task()
    commission_task = submit_commission_sync_task(databook_task)
