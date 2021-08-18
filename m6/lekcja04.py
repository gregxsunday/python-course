from selenium import webdriver
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import colored
from time import sleep

def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless') 
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def is_alert_present(driver, payload):
    url = f'http://localhost/?name={payload}'

    try:
        try:
            driver.get(url)
        except InvalidSessionIdException:
            driver = create_driver()
            driver.get(url)

        try:
            action = ActionChains(driver) 
            xsslink = driver.find_element_by_name("xss")
            action.move_to_element(xsslink).click().perform()
        except NoSuchElementException:
            pass

        try:
            WebDriverWait(driver, 0.5).until(expected_conditions.alert_is_present())
            sleep(5)
            driver.switch_to.alert.accept()
            return True
        except TimeoutException:
            sleep(3)
            return False
    finally:
        driver.close()


if __name__ == '__main__':
    payloads = [
        '<script>alert(1)</script>',
        '<img src=x onerror=alert(1)>',
        '<input name="xss" onpointerenter=alert(1)>'
    ]
    driver = create_driver()
    try:
        for payload in payloads:
            alert = is_alert_present(driver, payload)
            print(payload, colored('VULNERABLE', 'red') if alert else colored('NOT VULNERABLE', 'green'))
    finally:
        driver.quit()
    