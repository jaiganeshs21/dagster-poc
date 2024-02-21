from typing import List

from dagster import asset
from dagster import AssetExecutionContext
from dagster import AssetIn
from dagster import AssetSelection
from dagster import define_asset_job
from dagster import Definitions
from dagster import ScheduleDefinition


@asset(key="first_asset", group_name="group1")
def first_asset():
    """
    This is our first asset for testing purposes
    """
    print("INSIDE FIRST ASSET FUNCTION")
    return [1, 2, 3]


@asset(
    ins={"upstream": AssetIn(key="my_awesome_first_asset")},
    group_name="group1",
)
def second_asset(context: AssetExecutionContext, upstream: List):
    """
    This is our second asset
    """
    data = upstream + [4, 5, 6]
    context.log.info(f"Output data is: {data}")
    return data


@asset(
    ins={
        "first_upstream": AssetIn("first_asset"),
        "second_upstream": AssetIn("second_asset"),
    },
    group_name="group1",
)
def third_asset(first_upstream: List, second_upstream: List
):
    """
    This is our third asset
    """
    data = {
        "first_asset": first_upstream,
        "second_asset": second_upstream,
        "third_asset": second_upstream + [7, 8],
    }
    print(f"INSIDE THIRD ASSERT: {data}")
    return data


defs = Definitions(
    assets=[first_asset, second_asset, third_asset],
    jobs=[
        define_asset_job(
            name="asset_job",
            selection=AssetSelection.groups("group1"),
        )
    ],
    schedules=[
        ScheduleDefinition(
            name="asset_job",
            job_name="asset_job",
            cron_schedule="10 * * * *",
        )
    ],
)