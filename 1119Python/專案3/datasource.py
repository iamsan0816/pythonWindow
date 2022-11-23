# 自訂的module (模組) 下載資料和處理資料
# pipy 成千上萬的套件可以使用  reuests
import requests


api_key = "6c88d8b593da55e5d8bf61855950dee6"
cityName = "Taipei"


def get_forcast_data():
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={cityName},tw&APPID={api_key}&lang=zh_tw&units=metric"


    response = requests.get(url=url)

    if response.ok:
        print("下載成功")
        # print(response.text)
        return response.json()
    else:
        print("下載失敗")


# url 瀏覽器開啟 json code copy to online json viewer
