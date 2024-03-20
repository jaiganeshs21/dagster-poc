# from dagster import op, graph, Out, In, Output

# @op(out=Out(int))
# def addition(context, a: int, b: int):
#     return Output(a + b)

# @op(ins={"a": In(int), "b": In(int)}, out=Out(int))
# def subtraction(context, a: int, b: int):
#     return Output(a - b)

# @graph
# def dagster_graph(a: int, b: int):
#     task1 = addition(a=a, b=b)
#     task2 = subtraction(a=task1, b=a)
#     task3 = addition(a=b, b=a)
#     task4 = subtraction(a=task3, b=b)
#     task5 = addition(a=task2, b=task4)
    
# dagster_job = dagster_graph.to_job()






from dagster import op, graph, Output, In, Out
import json

# Define static operations

@op
def test_dummy():
    print("everstageTest test_dummy")
    return 0

@op
def addition(dummy) -> int:
    return 1

@op
def subtraction(dummy) -> int:
    return 2


def generate_dagster_graph_from_json(json_data):
    # Parse JSON data
    graph_data = json.loads(json_data)
    
    @graph
    def dynamic_graph():
        tasks = {}
        for task_name, task_info in graph_data.items():
            function_to_call = globals()[task_info['function_to_call']]
            depends_on = task_info['depends_on']
            if len(depends_on) == 0:
                task = function_to_call()
            else:
                # Pass the output of the previous operation
                task = function_to_call(dummy=tasks[depends_on[0]])
            tasks[task_name] = task

    return dynamic_graph
# Example JSON data describing task dependencies
json_data = '''
{
    "task_1": {
        "function_to_call": "test_dummy",
        "depends_on": []
    },
    "task_2": {
        "function_to_call": "subtraction",
        "depends_on": ["task_1"]
    },
    "task_3": {
        "function_to_call": "addition",
        "depends_on": ["task_2"]
    }
}
'''

# Generate dagster_graph from JSON
dagster_graph = generate_dagster_graph_from_json(json_data)

# Create dagster_job
dagster_job = dagster_graph.to_job()
