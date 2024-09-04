import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_bar_pie_charts(bar_pie_charts_setup):
    driver = bar_pie_charts_setup
    obj_actions = ActionChains(driver)

    bars = driver.find_elements(by=By.XPATH, value="//*[local-name() = 'svg']//*[name() = 'g' and @class = 'highcharts-series-group']//*[name() = 'rect']")
    bar_tooltip_path = "//*[local-name() = 'svg']//*[name() = 'g' and @class = 'highcharts-label highcharts-tooltip highcharts-color-undefined']//*[name() = 'text']//*[name() = 'tspan']"
    # bar_tooltip_path = "//*[local-name() = 'svg']//*[name() = 'g' and @class = 'highcharts-label highcharts-tooltip highcharts-color-undefined']//*[name() = 'text']"

    total_bars = len(bars)/2
    print("Total bars in Bar Graph: ", total_bars)

    table_rows = driver.find_elements(by=By.XPATH, value="//table//tr[@class = 'row no-margin yearlypaymentdetails']")
    total_rows = len(table_rows)
    print("Total rows in Table: ", total_rows)

    assert total_bars == total_rows, "Bars in graph and Rows in Table are not equal"
    print("Bars in graph and Rows in Table are equal")

    # Table Data
    for row in range(1, total_rows + 1):
        print("For loop row count:::: ", row)
        print("================ Row : " + str(row) + " ================")

        column_element_path_text = "//table//tr[@class = 'row no-margin yearlypaymentdetails'][" + str(row) + "]/td"
        table_each_row_column_elements = driver.find_elements(by=By.XPATH, value="//table//tr[@class = 'row no-margin yearlypaymentdetails'][" + str(row) + "]/td")
        total_columns_in_each_row = len(table_each_row_column_elements)
        print("Col count: ", total_columns_in_each_row)
        for col_num in range(1, total_columns_in_each_row - 1):
            print("//table//tr[@class = 'row no-margin yearlypaymentdetails'][" + str(row) + "]/td" + "[" + str(col_num) + "]")
            column_element = driver.find_element(by=By.XPATH, value="//table//tr[@class = 'row no-margin yearlypaymentdetails'][" + str(row) + "]/td" + "[" + str(col_num) + "]")
            print("Column Number in Row: " + str(row) + " is : ", col_num)
            print(column_element.text)

    # Bar Chart Data
    for each_bar in bars:
        obj_actions.move_to_element(each_bar).perform()
        time.sleep(1)
        print(bar_tooltip_path)
        bar_tooltip_elements = driver.find_elements(by=By.XPATH, value=bar_tooltip_path)
        print(len(bar_tooltip_elements))
        y = bar_tooltip_path + "[1]"
        bar_tooltip_element_text = driver.find_element(by=By.XPATH, value=y).text
        print(bar_tooltip_element_text)
        # print(bar_tooltip_elements)
        # x = driver.find_element(by=By.XPATH, value="//*[local-name() = 'svg']//*[name() = 'g' and @class = 'highcharts-label highcharts-tooltip highcharts-color-undefined']//*[name() = 'text']//*[name() = 'tspan'][1]").text
        # print(x)

        # print(">>>>>>>>>>>>>>>>---->>> ", bar_tooltip_text)
        # time.sleep(3)

    time.sleep(15)
