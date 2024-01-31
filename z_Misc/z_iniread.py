import configparser


def get_data():
    data = configparser.ConfigParser()
    data.read("../z_Misc/zdata.ini")
    # data.read("E:/python_projects/Project_Transform/data/data.ini")
    print(data.sections())
    return data


login_data = get_data()
print(login_data['app_login_page']["user_id"])
