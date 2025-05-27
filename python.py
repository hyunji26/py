#1) 리스트 과제
#학생들의 이름과 점수 정보를 리스트로 관리하는 코드 구현
list1 = []

def add_student(list1):
    name = input("이름:")
    score = input("점수:")

    list_student = [name,score]
    list1.append(list_student)
    print(f"학생 이름과 점수가 추가되었습니다.")

def delete_student(list1):
    name = input("이름:")

    for student in list1:
        if student[0] == name:
            list1.remove(student)
            print(f"{name} 학생 정보가 삭제되었습니다.")
            return
    print("학생을 찾을 수 없습니다.")

def modify_student(list1):
    name = input("name:")

    for student in list1:
        if student[0] == name:
            student[1] = input("수정할 score:")
            print(f"{name}학생의 점수가 수정되었습니다.")
            return
        
def all_student_list(list1):
    for student in list1:
        print(f"{student[0]}님의 점수는 {student[1]}입니다.")

def calculate_student_list(list1):
    max_score = int(list1[0][1])
    min_score = int(list1[0][1])
    total_score = 0
    count = 0

    for student in list1:
        score = student[1]

        if max_score < score:
            max_score = score
        if min_score > score:
            min_score = score

        total_score += score
        count += 1

    average = total_score / count
    return max_score, min_score, average

add_student(list1)
add_student(list1)
add_student(list1)
delete_student(list1)
modify_student(list1)
all_student_list(list1)

max_score,min_score,average = calculate_student_list(list1)
print(f"최고 점수:{max_score} 최저 점수:{min_score} 평균 점수:{average}")

#2)튜플 quiz 01
t1 = (1,2,3)
t2 = (4,5,6)
result = t1 + t2
print(result[2:5])
#답 : (3,4,5)

#튜플 Quiz 2
person = ('홍길동',30,'서울')
name,age,city = person
age += 1
person[1] = age
print(f"{name}은 {age}세이고 {city}에 살고 있습니다.")
# 답안 : 튜플은 수정할 수 없다

#튜플 Quiz 3
def get_values():
    return 1,2,3

x, *y = get_values()
print(x)
print(y)
#답 : 1  \n [2,3]

#과제
# 데이터: (연도, 분기, 제품, 가격, 판매량, 지역)
sales_data = [
    (2020, 1, "노트북", 1200, 100, "서울"),
    (2020, 1, "스마트폰", 800, 200, "부산"),
    (2020, 2, "노트북", 1200, 150, "서울"),
    (2020, 2, "스마트폰", 800, 250, "대구"),
    (2020, 3, "노트북", 1300, 120, "인천"),
    (2020, 3, "스마트폰", 850, 300, "서울"),
    (2020, 4, "노트북", 1400, 140, "부산"),
    (2020, 4, "스마트폰", 900, 350, "서울"),
    (2021, 1, "노트북", 1400, 110, "서울"),
    (2021, 1, "스마트폰", 900, 220, "대전"),
    (2021, 2, "노트북", 1300, 160, "인천"),
    (2021, 2, "스마트폰", 900, 270, "부산"),
    (2021, 3, "노트북", 1500, 130, "서울"),
    (2021, 3, "스마트폰", 950, 320, "대구"),
    (2021, 4, "노트북", 1500, 140, "부산"),
    (2021, 4, "스마트폰", 950, 370, "서울"),
]

def sales(sales_data):
    twenty = 0
    twentyOne = 0
    for sale in sales_data:
        if sale[0] == 2020:
            twenty += sale[4]
        else:
            twentyOne += sale[4]
    return twenty, twentyOne

twenty, twentyOne = sales(sales_data)
print("2020년 총 판매량:", twenty)
print("2021년 총 판매량:", twentyOne)

#3)딕셔너리
#Quiz 01
student = {"name": "홍길동", "scores": [85, 90, 78]}
print(student.get("age", "나이 정보 없음"))
student["scores"][1] = 95
print(student["scores"])

#2
inventory = {"사과": 10, "바나나": 5, "오렌지": 8}
total = 0

for item, count in inventory.items():
    if count > 7:
        total += count

print(total)
#답: 18

#과제:딕셔너리 활용하여 간단한 주소록 프로그램 작성
#1) 연락처 이름을 키로 하고 전화번호,이메일,주소 값 
#2)각 연락처 여러 정보 저장
#3) 연락처 추가,삭제,검색,수정,모든 연락처 보기 기능 구현
address = {"임현지" : {
    "전화번호" : "010-4932-2222",
    "이메일" : "dlaguswlsl@naver.com",
    "주소" : "서울 강남구 청담동"
}}

def add_address(address):
    name = input("이름:")

    if name in address:
        print(f"이미 존재하는 이름입니다.")
        return
    
    phone = input("전화번호:")
    email = input("이메일:")
    add = input("주소:")

    address[name] = {
        "전화번호" : phone,
        "이메일" : email,
        "주소" : add
    }
    print(f"{name}의 연락처가 추가되었습니다.")

def delete_address(address):
    name = input("이름:")

    if name in address:
        del address[name]

def search_address(address):
    name = input("이름:")

    if name in address:
        print(f"{name}님의 연락처가 존재합니다.")
    else:
        print(f"{name}님의 연락처가 존재하지 않습니다.")

def search_all_address(address):
    for name, info in address.items():
        print(f"\n이름: {name}")
        print(f"전화번호: {info['전화번호']}")
        print(f"이메일: {info['이메일']}")
        print(f"주소: {info['주소']}")

add_address(address)
add_address(address)
delete_address(address)
search_all_address(address)

#4) 집합(set)
#quiz 1
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {1, 2}

print(set3.issubset(set1))    # set3이 set1의 부분집합인지 확인
print(set3 < set1)            # set3이 set1의 진부분집합인지 확인
print(set1.isdisjoint(set2))  # set1과 set2가 서로소인지 확인 (공통 원소 없음?)
print(set1 ^ set2)            # set1과 set2의 대칭 차집합 (둘 중 한 쪽에만 있는 원소들)
#답
# True
# True
# False
# {1, 2, 6, 7}

#quiz 2
def process_data(data):
    unique = set()
    result = []
    for item in data:
        if isinstance(item, list):
            item = tuple(item)
        if item not in unique:
            unique.add(item)
            result.append(item)
    return result

data = [1, 2, 2, [3, 4], [3, 4], 5]
print(process_data(data))
#답: [1,2,(3,4),5]

#과제
#소셜 네트워크에서 사용자 간의 관계와 추천 시스템을 구현하는 프로그램 작성
# 공통 관심사를 갖는 친구 응답
# 공통 관심사가 없는 친구 응답
hobbies = {
    "Alice": ["음악", "영화", "독서"],
    "Bob": ["스포츠", "여행", "음악"],
    "Charlie": ["프로그래밍", "게임", "영화"],
    "David": ["요리", "여행", "사진"],
    "Eve": ["프로그래밍", "독서", "음악"],
    "Frank": ["스포츠", "게임", "요리"],
    "Grace": ["영화", "여행", "독서"]
}
def hob(hobbies):
    positive_list = []
    negative_list = []

    my_name = input("name:")

    my_hobby = set(hobbies[my_name])

    for other_name,other_hobbies in hobbies.items():
        if other_name == my_name:
            continue
        if my_hobby & set(other_hobbies):
            positive_list.append(other_name)
        else:
            negative_list.append(other_name)

    return positive_list,negative_list

positive_friend, negative_friend = hob(hobbies)

print(f"공통 관심사를 갖는 친구: {positive_friend}")
print(f"공통 관심사가 없는는 친구: {negative_friend}")

# 5)반복문
#quiz 01
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end="")
    print()

#Quiz 2
sum_value = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue
    sum_value += i
    if sum_value > 10:
        break

print(sum_value)

#과제
#여러 개의 숫자를 입력받아 합계를 계산하는 함수 작성
#사용자가 'q'를 입력하면 입력을 중단하고 지금까지 입력한 숫자의 합을 출력'
def calculate_sum():
    total = 0

    while 1:
        new_num = input("number:")

        if new_num == 'q':
            return total
        else:
            value = int(new_num)
            total += value
            
    return total

print(f"{calculate_sum()}")




    
                




