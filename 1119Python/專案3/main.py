import datasource as ds


def main():
    # print("這裏是main function")
    # all_data = datasource.get_forcast_data()
    list_data = ds.get_forcast_data(ds.tw_county_names["基隆"])
    # print(type(all_data))
    for item in list_data:
        print(item['dt_txt'])

if __name__ == "__main__":
    print("這裏是程式的執行點")
    main()
