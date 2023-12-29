from selenium import webdriver                                          # 통상과 동일 
from selenium.webdriver.chrome.service import Service as ChromeService  #
from webdriver_manager.chrome import ChromeDriverManager           # 웹드라이버 매니저 패키지의 chrome 브라우저 관련 설치 기능
import time
webdriver_manager_directory = ChromeDriverManager().install()                    # 23.12.16 추가 구간
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = browser.capabilities

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://192.168.10.236:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["gatheringdatas"] # 해당 포트에 접속해서 database에 연결
    return database # collection이 반환되도록 지정
collections = Connect()
collection = collections['courtaction_ui_select']
browser.get("https://www.courtauction.go.kr/")
time.sleep(2)
html = browser.page_source
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def get_source():
    # 아래 동작을 수행할 function을 get_source라는 이름으로 지정한다.
    element_numbers = browser.find_elements(by=By.CSS_SELECTOR,value="table.Ltbl_list > tbody > tr > td:nth-child(2)")
    # 반복할 횟수를 지정하기 위해 방문하는 페이지의 컨텐츠의 개수를 사전 파악해서 element_numbers 라는 변수로 지정한다.
    results = []
    # 빈 리스트인 results를 생성한다.
    for j in range(len(element_numbers)): # 컨텐츠의 개수를 영역 설정하여 J라는 변수로 지정한다
        auction_number = browser.find_elements(by=By.CSS_SELECTOR,value="table.Ltbl_list > tbody > tr > td:nth-child(2)")
        # 경매 문건 번호의 정보를 가져와서 auction_number라는 변수로 담아낸다.
        number = auction_number[j].text
        # 현재 반복문의 회차와 동일한 위치값의 경매 문건 번호를 나중에 반환하기 위해 number라는 변수로 지정한다.
        element_locate = browser.find_elements(by=By.CSS_SELECTOR,value="td:nth-child(4)")
        # 경매 물건 소재지의 정보를 가져와서 element_locate라는 변수로 담아낸다.
        locate = element_locate[j].text
        # 현재 반복문의 회차와 동일한 위치값의 경매 물건 소재지를 나중에 반환하기 위해 locate라는 변수로 지정한다.
        results.append((number,locate))
        # 나중에 사용할 값인 number와 locate를 딕셔너리 형태로 반복적으로 보낸다.
        pass
    return results 
    # 나중에 사용할 값으로 number와 locate를 results라는 변수로 반환한다.

def check_pages(sta_dep):
    # 아래 동작을 수행할 function을 check_pages라는 이름으로 지정한다.
    page_numbers = browser.find_elements(by=By.CSS_SELECTOR,value="form:nth-child(2) > div > div.page2 > a > span")
    # 반복할 횟수를 지정하기 위해 방문하는 페이지의 이동 가능한 페이지 개수를 사전 파악해서 page_numbers 라는 변수로 지정한다.
    results = [] # 빈 리스트인 results를 생성한다.
    for page_number in range(len(page_numbers)+1) : # 선택한 페이지의 총 개수를 조회한 뒤 조건이 맞으면 계속 반복 하도록 설정
        number_locates = get_source() # 사전에 선언한 function 을 호출하여 기능을 이용한다. 이를 numver_locates라는 변수로 지정한다.
        for number, locate in number_locates: 
            #  앞선 get_source function에서 가져온 results 리스트의 정보를 각각 number와 locate로 나눠준다.
            results.append({
                '법원 / 소재지 정보': sta_dep,
                '사건 번호': number,
                '소재지 및 내역': locate,
            })
            # 위의 정보를 for구문이 돌면서 가져온 sta_dep 정보까지 활용해서 딕셔너리 형태로 각 각 key값과 value값으로 반복적으로 저장한다.
        page_numbers = browser.find_elements(by=By.CSS_SELECTOR,value="form:nth-child(2) > div > div.page2 > a > span")
        # 페이지의 개수가 있는 위치값을 지정하여 해당 정보를 가져와서 page_numbers라는 변수 선언
        if page_number < len(page_numbers): # 반복하는 와중에 현재 페이지의 번호와 남아있는 페이지의 번호를 서로 비교한다.
            page_numbers[page_number].click() # 남아있는 페이지가 존재하면 다음 페이지를 클릭한다.
        else: # 만약 남아있는 페이지가 없다면 
            break # 반복문을 벗어난다.
    return results # 추출된 정보를 사용할 수 있도록 results라는 변수를 지정하여 반환토록 한다.

browser.switch_to.frame('indexFrame')
# 해당 페이지가 이동없이 URL이 고정된 주소이므로, 정보를 추출할 페이지가 위치한 frame을 타겟팅하는 명령어를 선언한다.
element_menu = browser.find_element(by=By.CSS_SELECTOR,value="#menu > h1:nth-child(5) > a > img")
# 메뉴바에 위치한 다음 진행 위치의 버튼의 정보를 가져와 element_menu라는 변수로 지정한다.
element_menu.click()
# 해당 버튼을 클릭한다.
element_body = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > form") 
# 이동된 페이지에서 셀렉트 메뉴의 위치 정보를 가져오는 값을 element_body라는 변수로 지정한다.
index = [7,11,15] # 위치한 셀렉트 항목에서 이동할 위치 중 사전 선정한 위치 값을 index라는 변수로 지정한다.
for i in index:
    # 반복분이 수행할 횟수를 부여하기 위해 이전에 지정한 위치값을 i라는 변수로 선언한다.
    state_select = browser.find_element(by=By.CSS_SELECTOR,value="#idJiwonNm")
    # 셀렉트 메뉴의 정보를 가져 와서 그 값을 state_select라는 변수로 저장한다.
    selects = Select(state_select)
    # 셀렉트 메뉴의 정보를 선택할 기능인 Select를 적용하고, 그 과정을 selects라는 변수로 지정한다.
    selects.select_by_index(i)
    # 셀렉트 메뉴에서 위에 선언한 값인 회차의 위치값과 동일한 위치에 존재하는 값을 선택한다.
    state = selects.first_selected_option.text
    # 위에서 실행한 과정에서, Select 클래스에 있던 값중 text 정보를 가져와 state라는 변수로 선언한다.
    department_select = browser.find_element(by=By.CSS_SELECTOR,value="#idJpDeptCode")
    # 다른 위치의 셀렉트 메뉴의 정보를 가져 와서 그 값을 department_select라는 변수로 저장한다.
    dep_select= Select(department_select)
    # 담당 부서 셀렉트 메뉴의 정보를 선택할 기능인 Select를 적용하고, 그 과정을 dep_select라는 변수로 지정한다.
    dep_select.select_by_index(2)
    # 셀렉트 메뉴에서 미리 선언한 값인 3번쨰의 위치값과 동일한 위치에 존재하는 값을 선택한다.
    depart = dep_select.first_selected_option.text
    # 위에서 실행한 과정에서, Select 클래스에 있던 값중 text 정보를 가져와 depart라는 변수로 선언한다.
    sta_dep = state + " " + depart
    # 추출한 법원 지역정보와 담당 부서의 정보를 결합시키고, 원활한 구분을 위해 띄어쓰기 정보로 빈 칸을 추가해 준다.
    element_search = browser.find_element(by=By.CSS_SELECTOR,value=" div.tbl_btn > a:nth-child(1)")
    # 법원과 담당 부서가 선정되면 해당 내용을 검색할 페이지로 넘어가는 검색 버튼의 위치 정보를 element_search라는 변수로 지정한다.
    element_search.click()
    # 문건을 검색하는 버튼을 클릭한다.
    results = check_pages(sta_dep)
    # 위에 지정한 functions을 실행할 때 for 구문에서 나온 sta_dep이라는 변수를 가져가서 사용하고 그 실행 결과를 results라는 변수로 지정한다.
    for result in results:
        # function이 동작하면서 반환된 내용을 result라는 변수에 담아서 그 갯수만큼 반복적으로 실행하도록 구문을 작성한다.
        number = result.get('사건 번호', '기본값').replace('\n', '')
        # 추출된 데이터를 가져올 때 깔끔한 정리를 위해, 작동하지 않는 \n 을 빈칸으로 치환하도록 선언하여 number라는 변수로 지정
        locate = result.get('소재지 및 내역', '기본값').replace('\n', '')
        # 추출된 데이터를 가져올 때 깔끔한 정리를 위해, 작동하지 않는 \n 을 빈칸으로 치환하도록 선언하여 locate라는 변수로 지정
        collection.insert_one({
            '법원 / 소재지 정보': sta_dep,
            '사건 번호': number,
            '소재지 및 내역': locate,
        })
        # 추출한 정보를 지정한 collection에 저장
    element_back = browser.find_element(by=By.CSS_SELECTOR,value=" div > div > a:nth-child(5) > img")
    # 이전으로 돌아가는 기능이 있는 버튼의 위치 정보를 찾아서 element_back이라는 변수로 지정한다.
    element_back.click()
    # 위의 동작이 완료되는 조건을 만족하면 이전 으로 돌아가는 기능이 저장된 버튼을 클릭하도록 한다.

pass
