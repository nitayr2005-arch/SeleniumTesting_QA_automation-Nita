import pytest
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless=new')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        )

        time.sleep(2)

        driver.find_element(By.ID, "username").send_keys(data["username"])
        driver.find_element(By.ID, "password").send_keys(data["password"])
        driver.find_element(By.ID, "submit").click()

        time.sleep(2)

        success = "Logged In Successfully" in driver.page_source

        if data["expected"] == "PASS":
            assert success
        else:
            assert not success

    except Exception as e:
        os.makedirs("reports", exist_ok=True)
        screenshot_name = f'reports/{data["username"]}_fail.png'
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot disimpan: {screenshot_name}")
        raise e

    finally:
        driver.quit()