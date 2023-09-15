from controllers import Github_Controller, Wakatime_Controller
from utils.charts import pie_chart
from utils.markdown import modify_by_mark_image, modify_by_mark_lines
from utils.text import generate_language_line
import datetime

gc = Github_Controller()

gc.init()

pie_chart(gc.language_percentage, "languague-percentage")

modify_by_mark_image("language", "https://github.com/Yin-FR/Yin-FR/blob/main/assets/charts/languague-percentage.png?raw=true", insert_height=200)

wt = Wakatime_Controller()

wt.init()

hour, minute = wt.total_time["digital"].split(":")
hout, minute = int(hour), int(minute)

lines = ["```text\n"]
for language, value in wt.language_week.items():
    if value["percentage"] >= 1:
        lines.append(generate_language_line(language, value["time"], value["percentage"]) + "\n")
lines.append("```\n")
current_utc_time = datetime.datetime.utcnow()
formatted_utc_time = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")
lines.append("Update on: {}\n".format(formatted_utc_time))

modify_by_mark_lines("languageweek", lines)
modify_by_mark_image("workingtime", "https://img.shields.io/badge/Code%20Time-{}%20hrs%20{}%20mins-blue".format(hour, minute))