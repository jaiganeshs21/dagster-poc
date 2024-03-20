from dagster import op, GraphDefinition, DependencyDefinition


# @op
# def expression_evaluate():
#     return 1

# @op
# def the_action(num):
#     return num + 1

# graph_def = GraphDefinition(
#     name='basic_v1',
#     node_defs=[expression_evaluate, the_action],
#     dependencies={'the_action': {'num': DependencyDefinition('expression_evaluate')}},
# )


@op
def expression_evaluate():
    print("Inside expression_evaluate")
    return "DONE"


@op
def if_exp(num):
    print("Inside if_exp")
    return "DONE"


@op
def else_exp(num):
    print("Inside else_exp")
    return "DONE"


@op
def then_exp(num):
    print("Inside then_exp")
    return "DONE"


graph_def = GraphDefinition(
    name="basic_v1",
    node_defs=[expression_evaluate, if_exp, else_exp, then_exp],
    dependencies={
        "if_exp": {"num": DependencyDefinition("expression_evaluate")},
        "else_exp": {"num": DependencyDefinition("if_exp")},
        "then_exp": {"num": DependencyDefinition("else_exp")},
    },
)
