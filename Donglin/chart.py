import pyecharts.options as opts
from pyecharts.charts import Line, Grid
from django.shortcuts import render
from . import config


def draw_dongying_chart(request, datas, title, name1, name2, name3, name):
    timeData = [data.detect_time for data in datas]
    if name=="linyi":
        pressureData = [data.in_pressure for data in datas]
        flowData = [data.in_flow for data in datas]
        temperatureData = [data.in_temperature for data in datas]

    else:
        pressureData = [data.out_pressure for data in datas]
        flowData = [data.out_flow for data in datas]
        temperatureData = [data.out_temperature for data in datas]

    chart1 = Line()
    chart1.add_xaxis(xaxis_data=timeData)
    chart1.add_yaxis(
        series_name=name1,
        y_axis=pressureData,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart1.set_global_opts(
        title_opts=opts.TitleOpts(
            title=title, subtitle="", pos_left="center"
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_show=True,
                is_realtime=True,
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        xaxis_opts=opts.AxisOpts(
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
        ),
        yaxis_opts=opts.AxisOpts(max_=config.PRESSURE_UPPER_LIMIT, name="MPa"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "dataZoom": {"yAxisIndex": "none"},
                "restore": {},
                "saveAsImage": {},
            },
        ),
    )

    chart2 = Line()
    chart2.add_xaxis(xaxis_data=timeData)
    chart2.add_yaxis(
        series_name=name2,
        y_axis=flowData,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart2.set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        # tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name="m**3/h"),
        legend_opts=opts.LegendOpts(pos_left="7%"),
    )

    chart3 = Line()
    chart3.add_xaxis(xaxis_data=timeData)
    chart3.add_yaxis(
        series_name=name3,
        y_axis=temperatureData,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart3.set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name=name3),
        legend_opts=opts.LegendOpts(pos_left="14%"),
    )

    grid = Grid(init_opts=opts.InitOpts(width="1024px", height="1152px"))
    grid.add(chart=chart1, grid_opts=opts.GridOpts(pos_left=50, pos_right=50, height="30%"))
    grid.add(
        chart=chart2,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="35%", height="30%"),
    )

    grid.add(
        chart=chart3,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="70%", height="30%"),
    )

    grid.render("templates/Donglin/chart.html")
    return render(request, "Donglin/chart.html")


def draw_binzhou_chart(request, datas, title, name1, name2, name3, name4,name5, name6,):
    timeData = [data.detect_time for data in datas]
    pressureData = [data.out_pressure for data in datas]
    inPressureData = [data.in_pressure for data in datas]
    flowData = [data.out_flow for data in datas]
    inFlowData = [data.in_flow for data in datas]
    temperatureData = [data.out_temperature for data in datas]
    inTemperatureData = [data.in_temperature for data in datas]

    chart1 = Line()
    chart1.add_xaxis(xaxis_data=timeData)
    chart1.add_yaxis(
        series_name=name4,
        y_axis=inPressureData,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart1.set_global_opts(
        title_opts=opts.TitleOpts(
            title=title, subtitle="", pos_left="center"
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_show=True,
                is_realtime=True,
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        xaxis_opts=opts.AxisOpts(
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
        ),
        yaxis_opts=opts.AxisOpts(max_=config.PRESSURE_UPPER_LIMIT, name="MPa"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "dataZoom": {"yAxisIndex": "none"},
                "restore": {},
                "saveAsImage": {},
            },
        ),
    )

    chart2 = Line()
    chart2.add_xaxis(xaxis_data=timeData)
    chart2.add_yaxis(
        series_name=name1,
        y_axis=pressureData,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart2.set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        # tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name="m**3/h"),
        legend_opts=opts.LegendOpts(pos_left="7%"),
    )

    chart3 = Line()
    chart3.add_xaxis(xaxis_data=timeData)
    chart3.add_yaxis(
        series_name=name5,
        y_axis=inFlowData,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart3.set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name=name5),
        legend_opts=opts.LegendOpts(pos_left="14%"),
    )

    chart4 = Line()
    chart4.add_xaxis(xaxis_data=timeData)
    chart4.add_yaxis(
        series_name=name2,
        y_axis=flowData,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart4.set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name=name2),
        legend_opts=opts.LegendOpts(pos_left="14%"),
    )

    chart5 = Line()
    chart5.add_xaxis(xaxis_data=timeData)
    chart5.add_yaxis(
        series_name=name6,
        y_axis=inTemperatureData,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart5.set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name=name6),
        legend_opts=opts.LegendOpts(pos_left="14%"),
    )

    chart6 = Line()
    chart6.add_xaxis(xaxis_data=timeData)
    chart6.add_yaxis(
        series_name=name3,
        y_axis=temperatureData,
        xaxis_index=1,
        yaxis_index=1,
        symbol_size=8,
        is_hover_animation=False,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1.5),
        is_smooth=True,
    )
    chart6.set_global_opts(
        axispointer_opts=opts.AxisPointerOpts(
            is_show=True, link=[{"xAxisIndex": "all"}]
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            grid_index=1,
            type_="category",
            boundary_gap=False,
            axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            position="top",
        ),
        datazoom_opts=[
            opts.DataZoomOpts(
                is_realtime=True,
                type_="inside",
                range_start=90,
                range_end=100,
                xaxis_index=[0, 2]
            )
        ],
        yaxis_opts=opts.AxisOpts(is_inverse=True, name=name3),
        legend_opts=opts.LegendOpts(pos_left="14%"),
    )

    grid = Grid(init_opts=opts.InitOpts(width="1024px", height="2304px"))
    grid.add(chart=chart1, grid_opts=opts.GridOpts(pos_left=50, pos_right=50, height="15%"))
    grid.add(
        chart=chart2,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="17%", height="15%"),
    )

    grid.add(
        chart=chart3,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="35%", height="15%"),
    )

    grid.add(
        chart=chart4,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="52%", height="15%"),
    )
    grid.add(
        chart=chart5,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="70%", height="15%"),
    )
    grid.add(
        chart=chart6,
        grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="87%", height="15%"),
    )

    grid.render("templates/Donglin/chart.html")
    return render(request, "Donglin/chart.html")
