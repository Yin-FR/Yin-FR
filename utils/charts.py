import os

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot as driver
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "./js/v5/"

def pie_chart(data_dict, chart_name):
    print(data_dict)
    pie = Pie().add("",
                    [list((key, value)) for (key, value) in data_dict.items()],
                    center=["35%", "50%"]
                ).set_global_opts(
                    legend_opts=opts.LegendOpts(is_show=False)
                ).set_series_opts(
                    label_opts=opts.LabelOpts(formatter="{b}: {c}%")
                )
    img_path = os.path.join("./assets/charts", chart_name + ".png")
    make_snapshot(driver, pie.render(chart_name + ".html"), img_path)
    os.remove(chart_name + ".html")
    return pie

