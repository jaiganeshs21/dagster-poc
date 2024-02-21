import json
from everstage_api_wrapper import EverstageAPIWrapper



def submit_task_to_everstage():
    """
    This function submits a task to Everstage and returns the job_id
    """
    url = "http://localhost:8000/airflow/submit-task"
    email = "test@datasheet.graph"
    client_id = 3001

    payload = json.dumps({"email": email, "client_id": client_id})

    api_invoker = EverstageAPIWrapper()
    response = api_invoker.session.get(url, data=payload)

    if response.ok:
        print("AIRFLOW: submitted task to Everstage")
        response_json = response.json()
        return response_json.get('job_id')
    else:
        print("AIRFLOW: Failed to submit task to Everstage")
        
        
        
def everstage_task_status_checker():
    """
    This function checks the status of a task in Everstage and returns the status
    """
    base_url = "http://localhost:8000/airflow/status-checker"
    email = "test@datasheet.graph"
    client_id = 3001

    # Add job_id as a query parameter to the URL
    url = f"{base_url}?job_id={123}"

    payload = json.dumps({"email": email, "client_id": client_id})

    api_invoker = EverstageAPIWrapper()
    response = api_invoker.session.get(url, data=payload)

    if response.ok:
        response_json = response.json()
        print("AIRFLOW: received task status from Everstage", response_json.get('status'))  
        return response_json.get('status')
    else:
        print("AIRFLOW: Failed to submit task to Everstage")
        
        