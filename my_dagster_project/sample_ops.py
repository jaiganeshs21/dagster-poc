from dagster import op

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
