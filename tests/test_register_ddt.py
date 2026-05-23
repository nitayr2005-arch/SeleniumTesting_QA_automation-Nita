import pytest
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def load_data():
    data = []

    file_path = os.path.join(
        os.path.dirname(__file__),
        "../data/register_data.csv"
    )

    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


@pytest.mark.parametrize("data", load_data())
def test_register(data):

    options = Options()
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    try:

        driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        )

        time.sleep(2)

        # input username
        driver.find_element(
            By.ID,
            "username"
        ).send_keys(data["username"])

        # input password
        driver.find_element(
            By.ID,
            "password"
        ).send_keys(data["password"])

        # klik login
        driver.find_element(
            By.ID,
            "submit"
        ).click()

        time.sleep(2)

        # validasi sederhana
        success = "Logged In Successfully" in driver.page_source

        # expected PASS
        if data["expected"] == "PASS":
            assert success

        # expected FAIL
        else:
            assert not success

    except Exception as e:

        # buat folder reports
        os.makedirs("reports", exist_ok=True)

        # nama screenshot
        screenshot_name = f'reports/{data["username"]}_fail.png'

        # simpan screenshot
        driver.save_screenshot(screenshot_name)

        print(f"Screenshot disimpan: {screenshot_name}")

        raise e

    finally:
        driver.quit()