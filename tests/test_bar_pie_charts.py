import time

import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.regression
@pytest.mark.smoke
def test_bar_pie_charts(bar_pie_charts_setup):
    driver = bar_pie_charts_setup
    obj_actions = ActionChains(driver)

    scroll_to_element = driver.find_element(by=By.XPATH, value="//label[text() = 'Schedule showing EMI payments starting from']")

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

    table_chart_data = {"principal": [], 'interest': [], 'total_payment': []}

    # Table Data
    for row in range(1, total_rows + 1):
        # print("For loop row count:::: ", row)
        # print("================ Row : " + str(row) + " ================")

        column_element_path_text = "//table//tr[@class = 'row no-margin yearlypaymentdetails'][" + str(row) + "]/td"
        table_each_row_column_elements = driver.find_elements(by=By.XPATH, value="//table//tr[@class = 'row no-margin yearlypaymentdetails'][" + str(row) + "]/td")
        total_columns_in_each_row = len(table_each_row_column_elements)
        # print("Col count: ", total_columns_in_each_row)
        for col_num in range(2, total_columns_in_each_row - 1):
            # print("//table//tr[@class = 'row no-margin yearlypaymentdetails'][" + str(row) + "]/td" + "[" + str(col_num) + "]")
            column_element = driver.find_element(by=By.XPATH, value="//table//tr[@class = 'row no-margin yearlypaymentdetails'][" + str(row) + "]/td" + "[" + str(col_num) + "]")
            # print("Column Number in Row: " + str(row) + " is : ", col_num)
            # print(column_element.text)
            if col_num == 2:
                table_chart_data['principal'].append(column_element.text)
            elif col_num == 3:
                table_chart_data['interest'].append(column_element.text)
            else:
                table_chart_data['total_payment'].append(column_element.text)
    print(table_chart_data)

    time.sleep(3)
    driver.execute_script("arguments[0].scrollIntoView(true);", scroll_to_element)
    time.sleep(3)

    bar_chart_data = {"principal": [], 'interest': [], 'total_payment': []}
    count = 1

    # Bar Chart Data
    for each_bar in bars:
        time.sleep(0.5)
        obj_actions.move_to_element(each_bar).perform()
        # print(bar_tooltip_path)
        bar_tooltip_elements = driver.find_elements(by=By.XPATH, value=bar_tooltip_path)
        # print(len(bar_tooltip_elements))

        # print("=================")
        for item in range(2, len(bar_tooltip_elements) + 1):
            tooltip_each_item_path = bar_tooltip_path + "[" + str(item) + "]"
            # print(tooltip_each_item_path)
            bar_tooltip_element_text = driver.find_element(by=By.XPATH, value=tooltip_each_item_path).text
            bar_tooltip_element_text = bar_tooltip_element_text.split(":")[1].strip()
            # print(bar_tooltip_element_text)

            if item == 2:
                if count <= 21:
                    bar_chart_data['interest'].append(bar_tooltip_element_text)
                else:
                    bar_chart_data['principal'].append(bar_tooltip_element_text)
            else:
                if count <= 21:
                    bar_chart_data['total_payment'].append(bar_tooltip_element_text)
        count = count + 1
        # print("=================")
    print(bar_chart_data)

    if table_chart_data == bar_chart_data:
        print("Success")
    else:
        print("FAIL")
        if bar_chart_data['interest'] == table_chart_data['interest']:
            print("Interest - Success")
        else:
            print("Interest FAIL")
        if bar_chart_data['principal'] == table_chart_data['principal']:
            print("Principal - Success")
        else:
            print("Principal FAIL")
        if bar_chart_data['total_payment'] == table_chart_data['total_payment']:
            print("Total Payment - Success")
        else:
            print("Total Payment FAIL")

    time.sleep(5)
