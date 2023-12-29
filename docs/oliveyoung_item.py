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
browser.get("https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000184922&dispCatNo=1000001001200040001&trackingCd=Cat1000001001200040001_Small&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EB%B2%A0%EC%9D%B4%EC%8A%A4/%ED%83%91%EC%BD%94%ED%8A%B8_%EC%86%8C_%EB%B2%A0%EC%9D%B4%EC%8A%A4/%ED%83%91%EC%BD%94%ED%8A%B8__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=1")

from selenium.webdriver.common.by import By

item = browser.find_elements(by=By.CSS_SELECTOR, value = "#Contents > div.prd_detail_box.renew")
for i in item:
    element_brand = browser.find_element(by=By.CSS_SELECTOR, value="#moveBrandShop")
    brand = element_brand.text
    
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="p.prd_name")
    title = element_title.text
    
    img = browser.find_element(by=By.CSS_SELECTOR, value="#mainImg")
    element_img = img.get_attribute('src')
    
    element_price = browser.find_element(by=By.CSS_SELECTOR, value="span.price-2 > strong")
    price = element_price.text

    review_click = browser.find_element(by=By.CSS_SELECTOR, value = "#reviewInfo").click()
    time.sleep(3)
    review = browser.find_elements(by=By.CSS_SELECTOR, value="#gdasList > li")
    for x in review:
        try : 
            element_writer = x.find_element(by=By.CSS_SELECTOR, value="div.user.clrfix")
            element_writer = element_writer.text
        except : 
            element_writer = ""
        try : 
            element_grade = x.find_element(by=By.CSS_SELECTOR, value="span.review_point > span.point")
            element_grade = element_grade.text
        except : 
            element_grade = ""
        try : 
            element_option = x.find_element(by=By.CSS_SELECTOR, value="p.item_option")
            element_option = element_option.text
        except : 
            element_option = ""
        try : 
            element_comments = x.find_element(by=By.CSS_SELECTOR, value="div.txt_inner")
            element_comments = element_comments.text
        except : 
            element_comments = ""
        pass

time.sleep(3)