from dagster import op, graph

@op
def when_trigger():
    print("everstageTest when_trigger")
    return 0

@op
def expression_evaluate(dummy) -> int:
    print("everstageTest expression_evaluate")
    return 1

@op
def then_action(dummy) -> int:
    print("everstageTest then_action")
    return 2


def generate_dagster_graph_from_json(dataset):

    tasks = {}

    @graph
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


records = {
    "id_1": {
        "name": "WHEN_TRIGGER!",
        "function_to_call": "when_trigger",
        "depends_on": [],
    },
    "id_2": {
        "name": "IFBLOCK_1",
        "function_to_call": "expression_evaluate",
        "depends_on": ["id_1"],
    },
    "id_3": {
        "name": "IFBLOCK_2",
        "function_to_call": "expression_evaluate",
        "depends_on": ["id_1"],
    },
    "id_4": {
        "name": "THEN_ACTION_3",
        "function_to_call": "then_action",
        "depends_on": ["id_2"],
    },
    "id_5": {
        "name": "THEN_ACTION_4",
        "function_to_call": "then_action",
        "depends_on": ["id_3"],
    }
}

# Generate dagster_graph from JSON
dagster_graph = generate_dagster_graph_from_json(records)

# Create dagster_job
dagster_job = dagster_graph.to_job()
