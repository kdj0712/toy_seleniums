def Connect(): # 전체 과정을 통합한 function의 이름으로 Connect라는 이름을 지정한다
    from pymongo import MongoClient  #몽고 DB 콤파스를 Python 과 연동시킴
    mongoClient = MongoClient("mongodb://192.168.10.239:27017") # 몽고 DB 콤파스의 포트에 연결하는 변수 지정
    database = mongoClient["gatheringdatas"] # 해당 포트에 접속해서 database에 연결
    first_collection = database['items']
    second_collection = database['olive_coments']
    return first_collection,second_collection

from selenium.webdriver.common.by import By

# 상품 브랜드명, 상품명, 이미지url, 가격 등 정보 가져오는 함수 실행
def get_item(browser,first_collection,second_collection):
    import time
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
    browser.find_element(by=By.CSS_SELECTOR, value = "#reviewInfo").click()
    pass
    get_review(browser,items_id,second_collection)  
    pass
    time.sleep(3)
    return items_id

# 리뷰(작성자, 별점, 옵션정보, 내용 등) 정보 가져오는 함수 실행
def get_review(browser,items_id,second_collection):
    import time
    reviews = []    
    review = browser.find_elements(by=By.CSS_SELECTOR, value="#gdasList > li")
    time.sleep(3)  
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
    return 


if __name__ == "__main__":
    get_item(browser,first_collection)
# for review in reviews:
 
#     # # function이 동작하면서 반환된 내용을 result라는 변수에 담아서 그 갯수만큼 반복적으로 실행하도록 구문을 작성한다.
#     # writer = writer.get("writer", '기본값')
#     # # 추출된 데이터를 가져올 때 깔끔한 정리를 위해, 작동하지 않는 \n 을 빈칸으로 치환하도록 선언하여 number라는 변수로 지정
#     # grade = grade.get("grade", '기본값')
#     # # 추출된 데이터를 가져올 때 깔끔한 정리를 위해, 작동하지 않는 \n 을 빈칸으로 치환하도록 선언하여 locate라는 변수로 지정
#     # option = option.get("option", '기본값')
#     # comments = comments.get("comments", '기본값')
