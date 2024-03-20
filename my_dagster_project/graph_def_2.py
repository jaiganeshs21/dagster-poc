from dagster import GraphDefinition, DependencyDefinition
from sample_ops import expression_evaluate, if_exp, else_exp, then_exp

graph_def = GraphDefinition(
    name="basic_v1",
    node_defs=[expression_evaluate, if_exp, else_exp, then_exp],
    dependencies={
        "if_exp": {
            "num": DependencyDefinition(
                node="expression_evaluate", output="result", description=None
            )
        },
        "else_exp": {
            "num": DependencyDefinition(
                node="if_exp", output="result", description=None
            )
        },
        "then_exp": {
            "num": DependencyDefinition(
                node="else_exp", output="result", description=None
            )
        },
    },
)
