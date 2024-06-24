import random
import string
from faker import Faker
from datetime import datetime, timedelta
import json

fake = Faker('ko_KR')

data_list = []
start_date = datetime(2024, 3, 1,0,0,0)
end_date = datetime(2024, 3, 14,0,0,0)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

for _ in range(136):
    phone_num = "010-" + ''.join(random.choices(string.digits, k=4)) + '-' + ''.join(random.choices(string.digits, k=4))

    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y%m%d")
    postcode = ''.join(random.choices(string.digits, k=5))
    address = fake.address().split('\n')[0]  # 주소 (동까지)
    detailed_address = "호수 " + fake.building_number()  # 상세 주소 대체 생성 방법
    sex = random.choice(['남자', '여자'])
    path = random.choice(["SNS", "인터넷검색", "기타", "커뮤니티", "카탈로그"])
    user_type = random.choice(["환자", "보호자", "관련종사자", "기타"])
    related_diseases = random.choice(["선택1", "선택2", "선택3", "선택4"])
    hope_info = random.choice(["관련 법 사항", "관련 정책 사항", "관련 뉴스", "관련 학술정보", "프로그램 참여", "커뮤니티 소통"])
    
    random_number_of_days = random.randrange(days_between_dates + 1)
    random_date = start_date + timedelta(days=random_number_of_days)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    formatted_date_no_micro = random_date.isoformat() + "+00:00"
    join_date = (random_date + timedelta(hours=random_hour, minutes=random_minute, seconds=random_second)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-4] + "+00:00"  # 마이크로초 포함하되, 마지막 3자리(마이크로초의 천분의 1초 부분)를 제외


    user_data = {
        "user_ID": ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
        "user_pswd": ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
        "user_email": ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@gmail.com",
        "user_name": fake.name()[:3],    
        "user_phone": phone_num,
        "user_birth": birth_date,
        "user_postcode": postcode,
        "user_address": address,
        "user_detailed_address": detailed_address,
        "user_sex": sex,
        "path_select": path,
        "user_who": user_type,
        "ralated_diseases":related_diseases,
        "hope_info": hope_info,
        "join_date": join_date
    }
    data_list.append(user_data)

print(data_list)
json_data = json.dumps(data_list, ensure_ascii=False, indent=4)

# JSON 데이터를 파일로 저장
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

print("JSON 파일이 성공적으로 생성되었습니다.")