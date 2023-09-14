from controllers import Github_Controller
from utils.charts import pie_chart
from utils.markdown import modify_by_mark


gc = Github_Controller()

gc.init()

pie_chart(gc.language_percentage, "languague-percentage")

modify_by_mark("updatetime", "https://github.com/Yin-FR/Yin-FR/blob/main/assets/charts/languague-percentage.png?raw=true", insert_height=100)