import json
from everstage_api_wrapper import EverstageAPIWrapper



def submit_task_to_everstage() -> None:
    """
    This function submits a task to Everstage and returns the job_id
    """
    base_url = "http://localhost:8000/dagster/trigger-datasheet-sync"
    email = "everstage.admin@linking-ds.com"
    client_id = 3018
    databook_ids= ["6a33079b-4fa7-430e-8031-fdbcc8ea2658"]
    url: str = f"{base_url}?databook_ids={databook_ids}"

    payload = json.dumps({"email": email, "client_id": client_id})

    api_invoker = EverstageAPIWrapper()
    response = api_invoker.session.get(url, data=payload)

    response_json = response.json()
    
    print("DAGSTER: submit_task_to_everstage JSON response:", json.dumps(response_json, indent=4))
    return response_json.get('e2eSyncRunId')
        

        
        
def task_status_checker(e2e_sync_run_id):
    """
    This function checks the status of a task in Everstage and returns the status
    """
    base_url = "http://localhost:8000/dagster/datasheet-sync-task-status"
    email = "everstage.admin@linking-ds.com"
    client_id = 3018
    
    print("DAGSTER: task_status_checker e2e_sync_run_id", e2e_sync_run_id)
    url: str = f"{base_url}?e2e_sync_run_id={e2e_sync_run_id}"

    payload = json.dumps({"email": email, "client_id": client_id})

    api_invoker = EverstageAPIWrapper()
    response = api_invoker.session.get(url, data=payload)

    if response.ok:
        print("DAGSTER: submitted task to Everstage")
        
        response_json = response.json()
        
        print("DAGSTER: JSON response:", json.dumps(response_json, indent=4))
        return response_json.get('status')
    else:
        print("DAGSTER: Failed to submit task to Everstage")