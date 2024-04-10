import random

from . import config
from .models import DongYing, LinYi, BinZhou, SimulationHistory
from django.utils import timezone


def create_dongying():
    """创建东营虚拟数据"""

    for i in range(100):
        DongYing.objects.create(
            out_pressure=random.randint(config.PRESSURE_LOWER_LIMIT, config.PRESSURE_UPPER_LIMIT),
            out_flow=random.randint(config.FLOW_LOWER_LIMIT, config.FLOW_UPPER_LIMIT),
            out_temperature=random.randint(config.TEMPERATURE_LOWER_LIMIT, config.TEMPERATURE_UPPER_LIMIT),
            detect_time=timezone.datetime(
                year=random.randint(config.YEAR_LOWER_LIMIT, config.YEAR_UPPER_LIMIT),
                month=random.randint(config.MONTH_LOWER_LIMIT, config.MONTH_UPPER_LIMIT),
                day=random.randint(config.DAY_LOWER_LIMIT, config.DAY_UPPER_LIMIT),
            )
        )

    print("东营数据创建完成")


def create_Linyi():
    for i in range(100):
        LinYi.objects.create(
            in_pressure=random.randint(config.PRESSURE_LOWER_LIMIT, config.PRESSURE_UPPER_LIMIT),
            in_flow=random.randint(config.FLOW_LOWER_LIMIT, config.FLOW_UPPER_LIMIT),
            in_temperature=random.randint(config.TEMPERATURE_LOWER_LIMIT, config.TEMPERATURE_UPPER_LIMIT),
            detect_time=timezone.datetime(
                year=random.randint(config.YEAR_LOWER_LIMIT, config.YEAR_UPPER_LIMIT),
                month=random.randint(config.MONTH_LOWER_LIMIT, config.MONTH_UPPER_LIMIT),
                day=random.randint(config.DAY_LOWER_LIMIT, config.DAY_UPPER_LIMIT),
            )
        )

    print("临沂站数据创建完成")


def create_binzhou():
    for i in range(100):
        BinZhou.objects.create(
            in_pressure=random.randint(config.PRESSURE_LOWER_LIMIT, config.PRESSURE_UPPER_LIMIT),
            out_pressure=random.randint(config.PRESSURE_LOWER_LIMIT, config.PRESSURE_UPPER_LIMIT),
            in_flow=random.randint(config.FLOW_LOWER_LIMIT, config.FLOW_UPPER_LIMIT),
            out_flow=random.randint(config.FLOW_LOWER_LIMIT, config.FLOW_UPPER_LIMIT),
            in_temperature=random.randint(config.TEMPERATURE_LOWER_LIMIT, config.TEMPERATURE_UPPER_LIMIT),
            out_temperature=random.randint(config.TEMPERATURE_LOWER_LIMIT, config.TEMPERATURE_UPPER_LIMIT),
            detect_time=timezone.datetime(
                year=random.randint(config.YEAR_LOWER_LIMIT, config.YEAR_UPPER_LIMIT),
                month=random.randint(config.MONTH_LOWER_LIMIT, config.MONTH_UPPER_LIMIT),
                day=random.randint(config.DAY_LOWER_LIMIT, config.DAY_UPPER_LIMIT),
            )
        )

    print("滨州数据创建成功")


def create_history():
    for i in range(100):
        SimulationHistory.objects.create(
            condition="",
            DY="",
            BZ="",
            LY="",
        )


def create_data():
    create_dongying()
    create_binzhou()
    create_Linyi()
    # create_history()

