import datasource as ds
from secrets import api_key

def main():
    # print("這裏是main function")
    # all_data = datasource.get_forcast_data()
    try:
        list_data = ds.get_forcast_data(ds.tw_county_names["基隆"],api_key)
    except Exception as e:
        print(e)
        return
    # print(type(all_data))

    for item in list_data:
        print(item['dt_txt'])

if __name__ == "__main__":
    print("這裏是程式的執行點")
    main()
