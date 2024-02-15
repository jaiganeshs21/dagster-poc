import random
import time
from dagster import op, graph

@op
def random_sleep(sleep_time: int):
    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)

@graph
def random_sleep_graph(sleep_time: int):
    random_sleep(sleep_time)
    random_sleep(sleep_time)
    random_sleep(sleep_time)
    random_sleep(sleep_time)

random_sleep_job = random_sleep_graph.to_job()