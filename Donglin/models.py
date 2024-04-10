from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    email = models.EmailField()
    username = models.CharField(
        max_length=11
    )
    password = models.CharField(
        max_length=16
    )



class DongYing(models.Model):
    out_pressure = models.BigIntegerField()
    out_flow = models.SmallIntegerField()
    out_temperature = models.SmallIntegerField()
    detect_time = models.DateField(
        default=timezone.now,
    )

    class Meta:
        db_table = "donglin_dongying"


class BinZhou(models.Model):
    in_pressure = models.SmallIntegerField()
    out_pressure = models.SmallIntegerField()
    in_flow = models.SmallIntegerField()
    out_flow = models.SmallIntegerField()
    in_temperature = models.SmallIntegerField()
    out_temperature = models.SmallIntegerField()
    detect_time = models.DateField(
        default=timezone.now,
    )

    class Meta:
        db_table = "donglin_binzhou"


class LinYi(models.Model):
    in_pressure = models.BigIntegerField()
    in_flow = models.SmallIntegerField()
    in_temperature = models.SmallIntegerField()
    detect_time = models.DateField(
        default=timezone.now,
    )
    class Meta:
        db_table = "donglin_linyi"


class SimulationHistory(models.Model):
    condition = models.TextField()
    DY = models.TextField()  # 东营站
    BZ = models.TextField()  # 滨洲站
    LY = models.TextField()  # 临邑站

    class Meta:
        db_table = "donglin_simulationhistory"
    
    