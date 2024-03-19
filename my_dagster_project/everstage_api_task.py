import json
from everstage_api_wrapper import EverstageAPIWrapper
import json

EMAIL = "super.admin@everstageinc.com"
CLIENT_ID = 3011

def databook_task_to_everstage(databook_ids) -> str:
    """
    This function submits a databook task to Everstage and returns the job_id
    """
    print("BEGIN: Inside submit_databook_task_to_everstage")
    
    base_url = "http://localhost:8000/dagster/trigger-datasheet-sync"
    url: str = f"{base_url}?databook_ids={databook_ids}"

    payload = json.dumps({"email": EMAIL, "client_id": CLIENT_ID})

    api_invoker = EverstageAPIWrapper()
    response = api_invoker.session.get(url, data=payload)

    response_json = response.json()
    
    print("END: Inside submit_databook_task_to_everstage", json.dumps(response_json, indent=4))
    return response_json.get('e2eSyncRunId')
        
def commission_task_to_everstage() -> str:
    """
    This function submits commission task to Everstage and returns the job_id
    """
    print("BEGIN: Inside submit_commission_task_to_everstage")
    
    url = "http://localhost:8000/dagster/trigger-commission-sync"

    payload = json.dumps({"email": EMAIL, "client_id": CLIENT_ID})

    api_invoker = EverstageAPIWrapper()
    response = api_invoker.session.get(url, data=payload)

    response_json = response.json()
    
    print("END: Inside submit_commission_task_to_everstage:", json.dumps(response_json, indent=4))
    return response_json.get('e2eSyncRunId')


def task_status_checker(e2e_sync_run_id, task_name) -> str:
    """
    This function checks the status of a task in Everstage and returns the status
    """
    print("BEGIN: task_status_checker e2e_sync_run_id", e2e_sync_run_id, task_name)
     
    base_url = "http://localhost:8000/dagster/get-sync-task-status"
    
    url: str = f"{base_url}?e2e_sync_run_id={e2e_sync_run_id}&task_name={task_name}"

    payload = json.dumps({"email": EMAIL, "client_id": CLIENT_ID})

    api_invoker = EverstageAPIWrapper()
    response = api_invoker.session.get(url, data=payload)

    response_json = response.json()
    
    print("task_status_checker result ", json.dumps(response_json, indent=4))
        
    print("END: task_status_checker e2e_sync_run_id", e2e_sync_run_id, task_name)
    return response_json.get('status')
