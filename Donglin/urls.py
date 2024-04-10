from django.urls import path
from . import views
app_name = "donglin"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("controlpanel/", views.controlpanel, name="controlpanel"),
    path("dong_ying/<int:page_num>/", views.dongying, name="dong_ying"),
    path("dong_ying_chart/", views.dongying_chart, name="dong_ying_chart"),
    path("bin_zhou/<int:page_num>/", views.binzhou, name="bin_zhou"),
    path("bin_zhou_data/", views.binzhou_data, name="bin_zhou_Data"),
    path("lin_yi/<int:page_num>/", views.linyi, name="lin_yi"),
    path("lin_yi_data/", views.linyi_data, name="lin_yi_data"),
    path("simulation_history/<int:page_num>/", views.simulation_history, name="simulation_history"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("search/", views.search, name="search")
]
