
def getOliveYoung(uri="https://www.oliveyoung.co.kr/store/main/main.do?oy=0"):
    # * 웹 크롤링 동작
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    webdriver_manager_directory = ChromeDriverManager().install()
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities
    browser.get(uri)
    return browser

def go_nail_care(browser):
    from selenium.webdriver.common.by import By
    element_categories = browser.find_element(by=By.CSS_SELECTOR, value="#btnGnbOpen").click()
    element_nail_care = browser.find_element(by=By.CSS_SELECTOR, value="li:nth-child(1) > div:nth-child(3) > ul:nth-child(2) > li:nth-child(4) > a").click()
    element_nail_care_in = browser.find_element(by=By.CSS_SELECTOR, value="#Contents > ul.cate_list_box > li:nth-child(2) > a").click()
    return browser

def roof(browser):
    from selenium.webdriver.common.by import By
    import time
    element_nail_items = browser.find_elements(by=By.CSS_SELECTOR, value="#Contents >ul > li > div > a > img")
    for index in range(len(element_nail_items)) :
        element_nail_items = browser.find_elements(by=By.CSS_SELECTOR, value="#Contents >ul > li > div > a > img")
        element_nail_items[index].click()
        time.sleep(1)
        browser.back()      
        time.sleep(1)       
        pass
    pass
    return

def quitBrowser(browser):
    # 브라우저 종료
    browser.quit()
    return 0

browser = getOliveYoung()
browser = go_nail_care(browser)
roof(browser)

