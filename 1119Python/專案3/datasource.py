# 自訂的module (模組) 下載資料和處理資料
# pipy 成千上萬的套件可以使用  reuests
import requests

tw_county_names = {"台北": "Taipei",
                   "台中": "Taichung",
                   "基隆": "Keelung",
                   "台南": "Tainan",
                   "高雄": "Kaohsiung",
                   "新北": "New Taipei",
                   "宜蘭": "Yilan",
                   "桃園": "Taoyuan",
                   "嘉義": "Chiayi",
                   "新竹": "Hsinchu",
                   "苗栗": "Miaoli",
                   "南投": "Nantou",
                   "彰化": "Changhua",
                   "雲林": "Yunlin",
                   "屏東": "Pingtung",
                   "花蓮": "Hualien",
                   "台東": "Taitung",
                   "金門": "Kinmen",
                   "澎湖": "Penghu",
                   "連江": "Lienchiang"
                   }


cityName = "Taipei"

def get_forcast_data(cityName,api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cityName},tw&APPID={api_key}&lang=zh_tw&units=metric"


    response = requests.get(url=url)

    if response.ok:
        print("下載成功")
        # print(response.text)
        return response.json()['list']
    else:
        # print("下載失敗")
        raise Exception(f"{cityName}下載失敗")


# url 瀏覽器開啟 json code copy to online json viewer
