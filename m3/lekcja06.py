from selenium import webdriver
from time import sleep

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless') 
    driver = webdriver.Chrome(options=chrome_options)
    url = 'http://127.0.0.1/login'
    try:
        driver.get(url)
        sleep(2)

        login = driver.find_element_by_name("login")
        login.send_keys('user')

        pwd = driver.find_element_by_name("password")
        pwd.send_keys('pass')

        form = driver.find_element_by_tag_name('form')
        form.submit()

        sleep(5)

    finally:
        driver.close()

    