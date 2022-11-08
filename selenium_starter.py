from selenium import webdriver
import os
import time


def chrome_test(path_to_chromedriver):
    # Requires the chromedriver executable to be in the chromedriver folder of this lab
    driver = webdriver.Chrome(path_to_chromedriver)

    # URL from Postman Step
    driver.get('https://www.indeed.com/jobs?q=Software+Engineer&l=Charlotte')
    print(driver.page_source)

    time.sleep(5)  # Time delay so the page can be seen for longer
    driver.quit()  # Always remember to quit the driver


def main():
    cwd = os.getcwd()
    path_to_chromedriver = os.path.join(cwd, 'chromedriver/chromedriver')
    chrome_test(path_to_chromedriver)


if __name__ == '__main__':
    main()
