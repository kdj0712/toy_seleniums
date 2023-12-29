# 상품 품목 리스트 긁어올 항목
# 1) 브랜드
# 2) 상품명
# 3) 썸네일 이미지
# 4) 가격(현판매가)

# 리뷰에 긁어올 항목
# 리스트명 : review
# 1) 닉네임
# 2) 별점
# 3) 옵션
# 4) 코멘트

# * 웹 크롤링 동작
from selenium import webdriver
import time
# - chrome browser 열기
browser = webdriver.Chrome()
# - 주소 입력
browser.get("https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=1000001001200040001&fltDispCatNo=&prdSort=01&pageIdx=1&rowsPerPage=24&searchTypeSort=btn_thumb&plusButtonFlag=N&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0&trackingCd=Cat1000001001200040001_Small&amplitudePageGubun=SMALL_CATE&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EC%83%81%EC%84%B8_%EC%86%8C%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC&midCategory=%EB%84%A4%EC%9D%BC%EC%BC%80%EC%96%B4&smallCategory=%EC%86%8C_%EB%B2%A0%EC%9D%B4%EC%8A%A4%2F%ED%83%91%EC%BD%94%ED%8A%B8&checkBrnds=&lastChkBrnd=&t_3rd_category_type=%EC%86%8C_%EB%B2%A0%EC%9D%B4%EC%8A%A4%2F%ED%83%91%EC%BD%94%ED%8A%B8")

from selenium.webdriver.common.by import By



item = browser.find_elements(by=By.CSS_SELECTOR, value = "div.prd_info")
for i in item:
    element_brand = browser.find_element(by=By.CSS_SELECTOR, value="#moveBrandShop")
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="p.prd_name")
    img = browser.find_element(by=By.CSS_SELECTOR, value="#mainImg")
    element_img = img.get_attribute('src')
    element_price = browser.find_element(by=By.CSS_SELECTOR, value="span.price-2")

    try : 
        element_writer = i.find_element(by=By.CSS_SELECTOR, value=".info_user")
        element_writer = element_writer.text
    except : 
        element_writer = ""
    try : 
        element_grade = i.find_element(by=By.CSS_SELECTOR, value="span.point")
        element_grade = element_grade.text
    except : 
        element_grade = ""
    try : 
        element_option = i.find_element(by=By.CSS_SELECTOR, value="p.item_option")
        element_option = element_option.text
    except : 
        element_option = ""
    try : 
        element_comments = i.find_element(by=By.CSS_SELECTOR, value="div.txt_inner")
        element_comments = element_comments.text
    except : 
        element_comments = ""
    pass
page = []
browser.find_element(by=By.CSS_SELECTOR, value="div.pageing > a").click()
time.sleep(3)