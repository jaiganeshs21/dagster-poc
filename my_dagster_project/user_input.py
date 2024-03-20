import random
import time
from dagster import op, graph


@op
def random_sleep_1(context, sleep_time: int):
    context.log.info(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)


@op
def report(origin):
    print("BEGIN: report task origin - ", origin)
    time.sleep(random.randint(5, 10))
    print("END: report task origin - ", origin)


@op
def datasheet(origin: str):
    """
    This is a task that will be used to generate datasheet
    """

    print("BEGIN: datasheet task origin - ", origin)
    time.sleep(random.randint(5, 10))
    print("END: datasheet task origin - ", origin)


@op
def upstream():
    """
    This is a task that will be used to generate all the upstream data
    """

    print("BEGIN: Upstream task")
    time.sleep(random.randint(5, 10))
    print("END: Upstream task")


@op
def commission():
    """
    This is a task that will be used to generate all the commission data
    """

    print("BEGIN: commission task")
    time.sleep(random.randint(5, 10))
    print("END: commission task")


@graph
def daily_etl():
    upstream()

    report(origin="system")

    datasheet(origin="system_custom")

    commission()

    report(origin="commission")

    datasheet(origin="commission")


daily_etl = daily_etl.to_job()
