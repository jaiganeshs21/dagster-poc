from dagster import graph

def generate_dagster_graph_from_json(dataset, name="dynamic_graph"):
    tasks = {}

    @graph(name=name)
    def dynamic_graph():
        for record_id, record in dataset.items():
            function_to_call = globals()[record['function_to_call']]
            depends_on = record['depends_on']
            if not depends_on:
                task = function_to_call()
            else:
                # Pass the output of the previous operation
                task = function_to_call(dummy=tasks[depends_on[0]])
            tasks[record_id] = task

    return dynamic_graph

def save_dag_to_file(dag_function, file_name):
    with open(file_name, 'w') as f:
        f.write(dag_function.to_python())
