import datetime

from django.test import TestCase
from .models import DongYing, BinZhou, LinYi, SimulationHistory
# Create your tests here.
import random
from .data_create import create_data
from . import config





class MyTest(TestCase):

    # def test_model(self):
    #     dongying = DongYing.objects.create(
    #         in_pressure=random.randint(0, config.MAX_VALUE),
    #         in_flow=random.randint(0, config.MAX_VALUE),
    #         in_temperature=random.randint(0, config.MAX_VALUE),
    #     )
    #
    #     binzhou = BinZhou.objects.create(
    #         in_pressure=random.randint(0, config.MAX_VALUE),
    #         out_pressure=random.randint(0, config.MAX_VALUE),
    #         in_flow=random.randint(0, config.MAX_VALUE),
    #         out_flow=random.randint(0, config.MAX_VALUE),
    #         in_temperature=random.randint(0, config.MAX_VALUE),
    #         out_temperature=random.randint(0, config.MAX_VALUE),
    #     )
    #
    #     linyi = LinYi.objects.create(
    #         in_pressure=random.randint(0, config.MAX_VALUE),
    #         in_flow=random.randint(0, config.MAX_VALUE),
    #         in_temperature=random.randint(0, config.MAX_VALUE),
    #     )
    #
    #     simulation_history = SimulationHistory.objects.create(
    #         condition="asdf",
    #         DY="东营",
    #         BZ="滨州",
    #         LY="临邑",
    #     )

    # def test_create_data(self):
    #     create_data()

    def test_data(self):
        create_data()
        datas = DongYing.objects.all()[:20]
        print(type(datas))
        for data in datas:
            print(type(data))
            print(help(data))
            break
