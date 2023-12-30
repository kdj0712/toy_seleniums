from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = browser.capabilities
uri="https://www.oliveyoung.co.kr/store/main/main.do?oy=0"
browser.get(uri)
from selenium.webdriver.common.by import By
element_categories = browser.find_element(by=By.CSS_SELECTOR, value="#btnGnbOpen").click()
element_nail_cair = browser.find_element(by=By.CSS_SELECTOR, value="li:nth-child(1) > div:nth-child(3) > ul:nth-child(2) > li:nth-child(4) > a").click()
element_nail_cairin = browser.find_element(by=By.CSS_SELECTOR, value="#Contents > ul.cate_list_box > li:nth-child(2) > a").click()
time.sleep(1)

def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://192.168.10.236:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["gatheringdatas"] # 해당 포트에 접속해서 database에 연결
    return database # collection이 반환되도록 지정
collections = Connect()

first_collection = collections['items']
second_collection = collections['olive_coments']

element_nail_items = browser.find_elements(by=By.CSS_SELECTOR, value="#Contents >ul > li > div > a > img")
for index in range(len(element_nail_items)) :
    element_nail_items = browser.find_elements(by=By.CSS_SELECTOR, value="#Contents >ul > li > div > a > img")
    element_nail_items[index].click()
    time.sleep(1)
    item = browser.find_elements(by=By.CSS_SELECTOR, value = "#Contents > div.prd_detail_box.renew")
    items = []
    for i in item:
        element_brand = browser.find_element(by=By.CSS_SELECTOR, value="#moveBrandShop")
        brand = element_brand.text
        
        element_title = browser.find_element(by=By.CSS_SELECTOR, value="p.prd_name")
        title = element_title.text
        
        img = browser.find_element(by=By.CSS_SELECTOR, value="#mainImg")
        element_img = img.get_attribute('src')
        
        element_price = browser.find_element(by=By.CSS_SELECTOR, value="span.price-2 > strong")
        price = element_price.text
        items.append({"brand" : brand,
                        "title" : title,
                        "element_img" : element_img,
                        "price" : price})
        for item in range(len(items)):
            first_collections = first_collection.insert_one({
                '브랜드' : brand,
                '품목명' : title,
                '이미지 링크' : element_img,
                '판매가' : price
            })
            items_id = []
            items_id = first_collections.inserted_id
    element_reviews = browser.find_element(by=By.CSS_SELECTOR, value="#reviewInfo > a") 
    element_reviews.click()
    time.sleep(3)
    for page_number in range(0,10) :  # page number
        reviews = []    
        review = browser.find_elements(by=By.CSS_SELECTOR, value="#gdasList > li")
        pages = browser.find_elements(by=By.CSS_SELECTOR, value="div > div.pageing > a") 
        for x in review:
            try : 
                element_writer = x.find_element(by=By.CSS_SELECTOR, value="div.user.clrfix")
                writer = element_writer.text
            except : 
                writer = ""
            try : 
                element_grade = x.find_element(by=By.CSS_SELECTOR, value="span.review_point > span.point")
                grade = element_grade.text
            except : 
                grade = ""
            try : 
                element_option = x.find_element(by=By.CSS_SELECTOR, value="p.item_option")
                option = element_option.text
            except : 
                option = ""
            try : 
                element_comments = x.find_element(by=By.CSS_SELECTOR, value="div.txt_inner")
                comments = element_comments.text
            except : 
                comments = ""
            pass
            reviews.append({"품목ID" : items_id,
                        "writer" : writer,
                        "grade" : grade,
                        "option" : option,  
                        "comments" : comments})
        for review in reviews:
            items_id = review.get( "품목ID" , '기본값')
            writer = review.get('writer', '기본값').replace('\n', '')
            grade = review.get('grade','기본값').replace('\n', '')
            option = review.get('option','기본값').replace('\n', '')
            comments = review.get('comments','기본값').replace('\n', '')

            second_collection.insert_one({
                "품목ID" : items_id,
                '작성자' : writer,
                '점수' : grade,
                '옵션' : option,
                '댓글' : comments
                })
        pages = browser.find_elements(by=By.CSS_SELECTOR, value="div > div.pageing > a") 
        if page_number < len(pages):
            time.sleep(2)
            pages[page_number].click()
            time.sleep(3)   
        else:
            break

    browser.back()      
    time.sleep(1)   
browser.quit()