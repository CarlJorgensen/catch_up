#!/usr/bin/env python3

import re

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def search(course) -> str:
    driver = webdriver.Firefox()

    try:
        # Go to the website
        driver.get("https://cloud.timeedit.net/liu/web/schema/ri1Q7.html")

        # Find the search box and fill it with the course code
        elem = driver.find_element(By.ID, "ffsearchname")
        elem.clear()
        elem.send_keys(course)
        
        # Search for courses
        seek_and_click(driver, "class_name" ,"ffsearchbutton", 1)

        # Add course to basket
        seek_and_click(driver, "css_selector", ".addallbutton", 2)

        # Find the search button and click it
        seek_and_click(driver, "id", "objectbasketgo", 1)

        return driver.current_url

    except (TimeoutException, NoSuchElementException) as e:
        print(f"An error occurred: {e}")
        return "Error occurred"

    finally:
        driver.quit()


def get_classes(url: str, group: str) -> int:
    driver = webdriver.Firefox()

    try:
        # Go to the website
        driver.get(url)

        # Fill in student group and class boxes
        seek_and_click(driver, "css_selector", "a.rightHeader:nth-child(2)", 1)
        seek_and_click(driver, "css_selector", ".select2-container--focus > span:nth-child(1) > span:nth-child(1)", 1)
        seek_and_click(driver, "id", "select2-te_link_39-result-7pne-153309.212", 1)
        


    except NoSuchElementException as e:
        print(f"An error occurred: {e}")
        return "Error occurred"

    finally:
        print("yes")
        #driver.quit()

def seek_and_click(driver: WebDriver, locator: str, element_id: str, iter: int)-> None:
    try:
        locator_attr = getattr(By, locator.upper())
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((locator_attr, element_id))
        )

        for i in range(iter):
            print(f"Clicking on element with {locator} = {element_id}", i)
            element.click()

        else:
            print(f"Clicking on element with {locator} = {element_id}")
            element.click()

    except TimeoutException:
        print("Loading took too much time!")



def main() -> None:
    while True:
        course = input("Enter course code: ")
        group = input("Enter group: ")

        if len(course) == 6 and re.match(r"^Y[123]\.[abc]$", group):
            break

        print("Invalid input! Please enter a valid course code and group.")
            
    url = search(course)
    get_classes(url, group)

if __name__ == "__main__":
    main()