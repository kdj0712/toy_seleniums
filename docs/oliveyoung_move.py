import oliveyoung_item as item
# oliveyoung_item.py에 있는 function들을 인용하고 이를 item이라는 이름으로 치환한다.

def getOliveYoung(uri="https://www.oliveyoung.co.kr/store/main/main.do?oy=0"):
    # 기본구동을 위하여 필요한 내용을 getOliveYoung이라는 function으로 선언하고, 이 function이 동작할때 URI 변수의 값을 인용할 수 있도록 한다.
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    webdriver_manager_directory = ChromeDriverManager().install()
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities
    browser.get(uri)
    return browser #기본 구동 과정들이 진행된 값인 browser를 반환한다.

def go_nail_care(browser):
    # nailcare 항목이 있는 페이지까지 이동하도록 위에서 반환된 값인 browser를 이용해 후속 작업을 설계, 이를 go_nail_care라는 function으로 선언한다.
    from selenium.webdriver.common.by import By
    import time
    time.sleep(2)
    element_categories = browser.find_element(by=By.CSS_SELECTOR, value="#btnGnbOpen").click()
    time.sleep(2)
    element_nail_care = browser.find_element(by=By.CSS_SELECTOR, value="li:nth-child(1) > div:nth-child(3) > ul:nth-child(2) > li:nth-child(4) > a").click()
    time.sleep(2)
    element_nail_care_in = browser.find_element(by=By.CSS_SELECTOR, value="#Contents > ul.cate_list_box > li:nth-child(2) > a").click()
    time.sleep(2)
    return browser

def page_shift(browser,items_id,second_collection):
    # 댓글 페이지를 넘길 때마다 리뷰 글들을 수집할 수 있도록 다른 파일의 펑션에서 리턴되는 값을 인용해와서 작업할 것을 page_shift라는 이름으로 선언한다.
    from selenium.webdriver.common.by import By
    import time
    pages = browser.find_elements(by=By.CSS_SELECTOR, value="div > div.pageing > a")
    # 리뷰 페이지에 페이지 넘버링을 확인하는 값을 pages라고 선언한다.
    for page_number in range(0,10):
        # 해당 페이지가 통상적으로 10개씩 있으므로(이후는 next페이지 버튼) 범위를 설정해 둔 뒤 page_number라는 변수에 담아 순차적으로 반복되도록 for 구문을 설계
        item.get_review(browser,items_id,second_collection)
        # item파일의 get_review라는 펑션을 호출하여 작동시킨다. 이 때, 아까 인용할 값인 browser,items_id,second_collection도 같이 사용하여 펑션이 제대로 작동될 수 있도록 한다.
        pages = browser.find_elements(by=By.CSS_SELECTOR, value="div > div.pageing > a") 
        # 페이지가 전환될 때마다 값이 초기화 될 수 있으므로 아까 조사한 값을 재 사용해서 초기화를 방지한다.
        if page_number < len(pages):
            # 총 페이지 넘버의 값의 개수보다, 현재 페이지 넘버의 위치값이 작다면
            time.sleep(2)
            pages[page_number].click()
            # 다음 페이지 버튼을 클릭한다.
            time.sleep(3)   
        else:
            break
        # 총 페이지 넘버의 값의 개수보다, 현재 페이지 넘버의 위치값이 작지 않다면 동작을 종료한다.

def roof(browser):
    # 앞선 과정에서 타켓 페이지로 들어왔을 때, browser에 표시되는 아이템을 클릭하고 다음 아이템으로 넘길 떄마다 아래의 행동을 반복할 수 있도록 roof라는 이름의 function을 선언한다.
    from selenium.webdriver.common.by import By
    import time
    element_nail_items = browser.find_elements(by=By.CSS_SELECTOR, value="#Contents >ul > li > div > a > img")
    # 타겟 페이지에 있는 품목의 갯수의 정보를 추출하고 이것을 element_nail_items라는 변수에 저장한다.
    for index in range(len(element_nail_items)):
        # element_nail_items의 개수만큼을 영역으로 설정하여, 이것을 index라는 변수에 담고, 해당 영역만큼 아래의 행동을 반복하는 for 구문을 설계한다.
        element_nail_items = browser.find_elements(by=By.CSS_SELECTOR, value="#Contents >ul > li > div > a > img")
        # 페이지가 전환될 때마다 값이 초기화 될 수 있으므로 아까 조사한 값을 재 사용해서 초기화를 방지한다.
        element_nail_items[index].click()
        # 반복될 때 마다 index의 변경된 순서에 위치한 품목을 클릭한다.
        first_collection,second_collection = item.Connect()
        # item 파일의 Connect 펑션을 호출하고, 해당 펑션의 두 값을 사용하기 위해 각각 first_collection,second_collection이라는 변수에 저장한다.
        items_id = item.get_item(browser,first_collection,second_collection)
        # item 파일의 get_item 펑션을 사용하고 이 때 앞에서 만든 변수인 browser,first_collection,second_collection을 사용하여 리턴되는 값을 items_id라는 변수에 저장한다.
        page_shift(browser,items_id,second_collection)
        # 그렇게 생선된 items_id와 재사용할 browser,second_collection을 사용해서, 앞서 만든 page_shift 펑션을 호출하고 실행시킨다.
        time.sleep(2)
        browser.back()
        # 과정이 끝나면 뒷 페이지로 돌아간다.
        time.sleep(2)       
        pass
    pass
    return
def quitBrowser(browser):
    # 브라우저 종료하는 펑션
    browser.quit()
    return 0