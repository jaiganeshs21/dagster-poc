from dagster import In
import random
import time
from dagster import op, graph



@op
def report(task_dep, origin):
    print("BEGIN: report task origin - ", origin)
    time.sleep(random.randint(5,10))
    print("END: report task origin - ", origin)
    return origin

@op
def datasheet(task_dep, origin: str):
    print("BEGIN: datasheet task origin - ", origin)
    time.sleep(random.randint(5,10))
    print("END: datasheet task origin - ", origin)
    return origin

@op
def upstream():
    print("BEGIN: Upstream task")
    time.sleep(random.randint(5,10))
    print("END: Upstream task")
    return "upstream"

@op
def commission(task_dep):
    print("BEGIN: commission task")
    time.sleep(random.randint(5,10))
    print("END: commission task")
    return "commission"



@graph
def daily_etl(report_origin_1: str, report_origin_2: str, datasheet_origin_1: str, datasheet_origin_2: str):
    a = upstream()
    b = report(a, report_origin_1)
    c = datasheet(b, datasheet_origin_1)
    d = commission(c)
    e = report(d,report_origin_2)
    f = datasheet(e, datasheet_origin_2)