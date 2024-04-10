from django.contrib import admin
from .models import DongYing, LinYi, BinZhou, SimulationHistory, User
# Register your models here.


@admin.register(DongYing)
class DonglinAdmin(admin.ModelAdmin):
    pass


@admin.register(LinYi)
class DonglinAdmin(admin.ModelAdmin):
    pass


@admin.register(BinZhou)
class DonglinAdmin(admin.ModelAdmin):
    pass


@admin.register(SimulationHistory)
class DonglinAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
