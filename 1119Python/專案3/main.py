import datasource as ds
from secrets import api_key
import tkinter as tk

class Window(tk.Tk):
    def __init__(self, cities_dict):
        super().__init__()
        tk.Label(self, text="各縣市4天天氣預測", font=(
            'Arial', 20)).pack(padx=30, pady=30)

        # 建立存放按鈕的容器
        buttons_frame = tk.Frame(
            self, background="#FFF", width=1200, height=500)
        buttons_frame.pack(padx=80, pady=(0, 30))

        for index, key in enumerate(cities_dict):
            tk.Button(buttons_frame, text=key, font=('arial', 15),
                      padx=20, pady=5).grid(row=index % 3, column=index // 3)


def main():
    # print("這裏是main function")
    # all_data = datasource.get_forcast_data()
    window = Window(ds.tw_county_names)
    window.title("各縣市4天天氣預測")
    window.mainloop()
    """
    try:
        list_data = ds.get_forcast_data(ds.tw_county_names["基隆"],api_key)
    except Exception as e:
        print(e)
        return
    # print(type(all_data))

    for item in list_data:
        print(item['dt_txt'])
    """
if __name__ == "__main__":
    # print("這裏是程式的執行點")
    main()

