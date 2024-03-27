import os
from graph_def_4 import generate_dagster_graph_from_json, save_dag_to_file


# Example dataset
dataset = {
    "id_1": {
        "name": "WHEN_TRIGGER!",
        "function_to_call": "test_dummy",
        "depends_on": [],
    },
    "id_2": {
        "name": "IFBLOCK_1",
        "function_to_call": "subtraction",
        "depends_on": ["id_1"],
    },
    # Add more records as needed
}


file_name = "generated_dag_1.py"

# Generate dagster_graph from JSON
dagster_graph = generate_dagster_graph_from_json(dataset, name=f"dynamic_graph_{count}")

# Save the DAG to a Python file
save_dag_to_file(dagster_graph, file_name)

print(f"DAG saved to {file_name}")
