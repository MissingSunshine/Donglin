from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . import config
from .data_create import create_data
# Create your views here.
from .models import (
    DongYing, LinYi, SimulationHistory, BinZhou, User
)
from .chart import (
    draw_dongying_chart,draw_binzhou_chart
)
from django.utils import timezone
from .forms import (
    LoginForm, RegisterForm
)


def index(request):
    # create_data()
    name = config.DONG_YING
    return render(request, "Donglin/index.html", locals())


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.data.get("email")
            password = form.data.get("password")
            print(email)
            print(password)

            users = User.objects.filter(email=email, password=password).all()

            for user in users:
                print(user.email)
                print(user.password)
                print("=============================")
            if users:
                return JsonResponse({"code": 200, "message": "登录成功"})
            else:
                return JsonResponse({"code": 400, "message": "用户不存在"})

        return JsonResponse({"code": 400, "message": "校验错误"})
    return render(request, "MyLogin/index.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.data.get("email")
            username = form.data.get("username")
            password = form.data.get("password")
            User.objects.create(
                email=email,
                username=username,
                password=password,
            )
            return JsonResponse({"code": 200, "message": "success"})

    return render(request, "MyLogin/index.html")


def search(request):
    content = request.GET.get("content")
    position_name = request.GET.get("position_name")
    MyObject = None
    if position_name == "东营":
        # MyObject = DongYing
        return redirect("donglin:dong_ying", page_num=1)

    if position_name == "滨州":
        # MyObject = BinZhou
        return redirect("donglin:bin_zhou", page_num=1)

    if position_name == "临邑":
        # MyObject = LinYi
        return redirect("donglin:lin_yi", page_num=1)

    datas = MyObject.objects.filter(detect_time__gt=timezone.datetime(year=int(content), month=1, day=1)).order_by("detect_time").all()
    datas = [dict(data) for data in datas]

    return JsonResponse({"code": 200, "datas": datas, "message": "success"})


def controlpanel(request):
    name = config.DONG_YING
    return render(request, "Donglin/controlpanel.html", locals())


def return_data(request, string, page_num, properties, MyObject):
    name = string
    start = (page_num - 1) * config.MULTIPLE_NUMBER
    end = page_num * config.MULTIPLE_NUMBER
    datas = MyObject.objects.order_by("-detect_time").all()[start:end]
    pages = [i for i in range(1, config.PAGE_NUM + 1, 1)]

    return render(request, "Donglin/base_iframe.html", locals())


def dongying(request, page_num):
    properties = config.DONG_YING_PROPERTIES
    return return_data(request, config.DONG_YING, page_num, properties, DongYing)


def dongying_chart(request):
    datas = DongYing.objects.order_by("detect_time").distinct().all()
    _dict = dict(
        title="东营站各项数据折线图",
        name1=config.DONG_YING_PROPERTIES[0],
        name2=config.DONG_YING_PROPERTIES[1],
        name3=config.DONG_YING_PROPERTIES[2],
        name="dongying",
    )
    return draw_dongying_chart(request, datas, **_dict)


def binzhou(request, page_num):
    properties = config.BIN_ZHOU_PROPERTIES
    return return_data(request, config.BIN_ZHOU, page_num, properties, BinZhou)


def binzhou_data(request):
    datas = BinZhou.objects.order_by("detect_time").distinct().all()
    _dict = dict(
        title="滨州站各项数据折线图",
        name1=config.BIN_ZHOU_PROPERTIES[0],
        name2=config.BIN_ZHOU_PROPERTIES[1],
        name3=config.BIN_ZHOU_PROPERTIES[2],
        name4=config.BIN_ZHOU_PROPERTIES[3],
        name5=config.BIN_ZHOU_PROPERTIES[4],
        name6=config.BIN_ZHOU_PROPERTIES[5],
    )
    return draw_binzhou_chart(request, datas, **_dict)


def linyi(request, page_num):
    properties = config.LIN_YI_PROPERTIES
    return return_data(request, config.LIN_YI, page_num, properties, LinYi)


def linyi_data(request):
    datas = LinYi.objects.order_by("detect_time").distinct().all()
    _dict = dict(
        title="临邑站各项数据折线图",
        name1=config.LIN_YI_PROPERTIES[0],
        name2=config.LIN_YI_PROPERTIES[1],
        name3=config.LIN_YI_PROPERTIES[2],
        name="linyi",
    )
    return draw_dongying_chart(request, datas, **_dict)


def simulation_history(request, page_num):
    properties = config.SIMULATION_HISTORY_PROPERTIES
    return return_data(request, config.SIMULATION_HISTORY, page_num, properties, SimulationHistory)