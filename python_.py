# 심화 day 01
# 1)함수
#Quiz 01
#문제: 다음 리스트에서 홀수만 추출하여 제곱한 결과를 반환하세요.
numbers = [1,2,3,4,5,6,7,8,9,10]

def num(numbers):
    new_numbers = []
    for n in numbers:
        if n % 2 != 0:
            new_numbers.append(n*n)
    return new_numbers

print(num(numbers))

#Quiz 02
#함수 호출 시 매개변수와 반환값을 로그로 출력하는 데코레이터를 작성하세요.
#그리고 이 데코레이터를 add 함수에 적용하세요
def log_function_call(func):
    def wrapper(a,b):
        print(f"입력값: {a} , {b}")
        result = func(a,b)
        print(f"반환값: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b
#add = log_function_Call(add)와 같은 거

add(3,5)


#과제
#CSV 파일을 읽어 딕셔너리 리스트로 변환하는 함수 작성
#학생 중 성적이 80점 이상인 학생만 필터링
#필터링된 학생들의 평균 나이 계산
#모든 함수 호출 시간을 측정하는 데코레이터 적용
import csv,time
# 데코레이터: 함수 실행 시간 측정
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print("[{}] 실행 시간: {:.6f}초".format(func.__name__, end - start))
        return result
    return wrapper

#csv 파일을 읽어 딕셔너리 리스트로 변환환
@timing_decorator
def read_csv_dict_list(filename):
    with open(filename,encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            data.append(dict(row))
        return data
    
#성적이 80점 이상인 학생만 필터링
@timing_decorator
def select_student(data):
    student = []

    for x in data:
        if int(x['score']) >=80:
            student.append(x['name'])
    return student

#평균 나이 계산
@timing_decorator
def age_average(data):
    age = 0
    count = 0

    for x in data:
        age += int(x['age'])
        count += 1

    age = age/count
    return age

#전체 실행 흐름
file_path = "students.csv"
students = read_csv_dict_list(file_path)
high_scorers = select_student(students)
avg_age = age_average(high_scorers)

print("성적 80점 이상 학생들의 평균 나이: {:.2f}세".format(avg_age))


#2)모듈과 패키지
#과제
#간단한 계산기 모듈을 만들어 보세요
#모듈에는 덧셈,뺄셈,곱셈,나눗셈 함수가 포함
import calculator

add = calculator.add(4,5)
print(f"4 더하기 5 : {add}")


subtract = calculator.subtract(10,1)
print(f"10 - 1 : {subtract}")

s = calculator.square(5)

a = s.area()
print(f"한 변의 길이 5인 정사각형 넓이: {a}")


#3)클래스와 객체지향 과제
#클래스 구현현
#'Book`: 도서 정보(제목, 저자, ISBN, 출판연도 등)를 관리
#'Library`: 도서 컬렉션을 관리하고 대출/반납 기능 제공
#'Member`: 도서관 회원 정보와 대출 목록 관리
#기능 구현
# 도서 추가/삭제
# 도서 검색(제목, 저자, ISBN으로)
# 도서 대출/반납
# 회원 등록/관리
# 회원별 대출 현황 확인
# 객체 지향 설계 원칙(SOLID)을 최소한 2가지 이상 적용하세요
# 적절한 캡슐화를 통해 데이터를 보호하세요.
class Book:
    def __init__(self, title, author, isbn, year):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__year = year
        self.__is_borrowed = False

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def year(self):
        return self.__year

    @property
    def is_borrowed(self):
        return self.__is_borrowed

    #대출
    def borrow(self):
        if self.__is_borrowed:
            raise Exception("이미 대출된 책입니다.")
        self.__is_borrowed = True

    #반납
    def return_book(self):
        self.__is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.isbn}"

class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    @property
    def name(self):
        return self.__name

    @property
    def member_id(self):
        return self.__member_id

    def borrow_book(self, book: Book):
        if book in self.__borrowed_books:
            raise Exception("이 책은 이미 이 회원이 대출했습니다.")
        book.borrow()
        self.__borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.__borrowed_books:
            raise Exception("이 회원이 이 책을 대출하지 않았습니다.")
        book.return_book()
        self.__borrowed_books.remove(book)
    #회원 대출 도서 목록 반환환
    def borrowed_books(self):
        return self.__borrowed_books
# 도서,회원 관리
# 대출/반납 및 검색 기능 제공
class Library:
    def __init__(self):
        self.__books = [] #도서 목록 저장
        self.__members = [] #회원 목록 저장장

    def add_book(self, book: Book):
        self.__books.append(book)

    def remove_book(self, isbn):
        self.__books = [book for book in self.__books if book.isbn != isbn]

    def find_books(self, keyword):
        return [
            book for book in self.__books
            if keyword.lower() in book.title.lower()
            or keyword.lower() in book.author.lower()
            or keyword in book.isbn
        ]
    #회원 등록록
    def register_member(self, member: Member):
        self.__members.append(member)
    #회원 검색
    def get_member(self, member_id):
        for member in self.__members:
            if member.member_id == member_id:
                return member
        raise Exception("회원 ID를 찾을 수 없습니다.")
    #회원 도서 대출출
    def loan_book(self, member_id, isbn):
        member = self.get_member(member_id)
        for book in self.__books:
            if book.isbn == isbn:
                member.borrow_book(book)
                return f"{member.name}님이 '{book.title}'를 대출하셨습니다."
        raise Exception("해당 ISBN의 책을 찾을 수 없습니다.")
    #회원 도서 반납
    def return_book(self, member_id, isbn):
        member = self.get_member(member_id)
        for book in self.__books:
            if book.isbn == isbn:
                member.return_book(book)
                return f"{member.name}님이 '{book.title}'를 반납하셨습니다."
        raise Exception("해당 ISBN의 책을 찾을 수 없습니다.")
    #회원의 대출 도서 목록록
    def member_loans(self, member_id):
        member = self.get_member(member_id)
        return [str(book) for book in member.borrowed_books()]

book1 = Book("Python", "hyunji", "123-456", 2025)
book2 = Book("AI", "dohyun", "789-101", 2024)

member1 = Member("Sujin", "M001")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_member(member1)

print(library.loan_book("M001", "123-456"))  # 대출
print(library.member_loans("M001"))          # 대출 현황
print(library.return_book("M001", "123-456")) # 반납

#심화 day 02
#4)예외처리 
#과제 파일 처리기 구현
#다양한 유형의 파일(텍스트, CSV, JSON, 바이너리)을 읽고 쓸 수 있어야 합니다
#파일이 존재하지 않거나, 권한이 없거나, 형식이 잘못된 경우 등 다양한 오류 상황을 적절히 처
#사용자 정의 예외 계층 구조를 설계하고 구현
#오류 발생 시 로깅을 통해 문제를 기록
#모든 파일 작업은 컨텍스트 매니저(`with` 구문)를 사용
# handler.py
# log.txt에 기록
import os
import csv
import json
import logging

# 로깅 설정
logging.basicConfig(
    filename='log.txt',
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

class FileHandler:
    def __init__(self, file_path, mode='r', file_type='text'):
        self.file_path = file_path
        self.mode = mode
        self.file_type = file_type
        self.file = None

    def __enter__(self):
        if not os.path.exists(self.file_path) and 'r' in self.mode:
            raise FileNotFoundErrorCustom(f"File not found: {self.file_path}")
        try:
            self.file = open(self.file_path, self.mode, newline='', encoding='utf-8' if 'b' not in self.mode else None)
            return self
        except PermissionError:
            raise PermissionErrorCustom(f"Permission denied: {self.file_path}")
        except Exception as e:
            logging.error(f"Unexpected error opening file: {e}")
            raise FileHandlerError(f"Unexpected error: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def read(self):
        try:
            if self.file_type == 'text':
                return self.file.read()
            elif self.file_type == 'csv':
                reader = csv.reader(self.file)
                return list(reader)
            elif self.file_type == 'json':
                return json.load(self.file)
            elif self.file_type == 'binary':
                return self.file.read()
            else:
                raise InvalidFormatError(f"Unsupported file type: {self.file_type}")
        except Exception as e:
            logging.error(f"Read error in {self.file_path}: {e}")
            raise FileHandlerError(f"Read error: {e}")

    def write(self, data):
        try:
            if self.file_type == 'text':
                self.file.write(data)
            elif self.file_type == 'csv':
                writer = csv.writer(self.file)
                writer.writerows(data)
            elif self.file_type == 'json':
                json.dump(data, self.file, indent=4)
            elif self.file_type == 'binary':
                self.file.write(data)
            else:
                raise InvalidFormatError(f"Unsupported file type: {self.file_type}")
        except Exception as e:
            logging.error(f"Write error in {self.file_path}: {e}")
            raise FileHandlerError(f"Write error: {e}")

#main.py
from handler import FileHandler, FileHandlerError

# 텍스트 파일 쓰기/읽기 예시
try:
    with FileHandler('example.txt', 'w', 'text') as handler:
        handler.write("안녕하세요. 파일 처리기 예제입니다.")

    with FileHandler('example.txt', 'r', 'text') as handler:
        content = handler.read()
        print("텍스트 파일 내용:", content)
except FileHandlerError as e:
    print("에러 발생:", e)

# JSON 파일 쓰기/읽기 예시
data = {'name': 'Alice', 'age': 30}
try:
    with FileHandler('data.json', 'w', 'json') as handler:
        handler.write(data)

    with FileHandler('data.json', 'r', 'json') as handler:
        content = handler.read()
        print("JSON 파일 내용:", content)
except FileHandlerError as e:
    print("에러 발생:", e)

# 존재하지 않는 파일 읽기 시도
try:
    with FileHandler('nofile.txt', 'r', 'text') as handler:
        content = handler.read()
except FileHandlerError as e:
    print("예외 테스트:", e)



# 심화 day 03
# 5)이터레이터와 제너레이터
# 과제 
# 로그 파일을 한 줄씩 읽는 제너레이터 함수 작성
# 특정 패턴이 포함된 줄만 필터링하는 제너레이터 작성
# 로그 파일을 한 줄씩 읽는 제너레이터
def read_log_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

# 특정 패턴이 포함된 줄만 필터링하는 제너레이터
def filter_log(lines, keywords):
    for line in lines:
        if any(keyword in line for keyword in keywords):
            yield line

# 사용 예시
if __name__ == "__main__":
    log_file_path = 'example.log'  # 로그 파일 경로

    # 모든 로그 줄 출력
    for log in read_log_file(log_file_path):
        print(log)

    print("\n[ERROR, WARNING 만 필터링한 로그]")
    # 필터링된 로그만 출력
    filtered = filter_log(read_log_file(log_file_path), ['ERROR', 'WARNING'])
    for log in filtered:
        print(log)

#6)동시성과 병렬처리
#과제
#공통 데이터
import time
import requests
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor

API_URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5"
]

#순차 처리 방식
def fetch_sequential(urls):
    results = []
    for url in urls:
        response = requests.get(url)
        results.append(response.text)
    return results

#멀티스레딩 threadpoolExecutor 사용
def fetch_single(url):
    response = requests.get(url)
    return response.text

def fetch_threadpool(urls):
    results = []
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_single, urls))
    return results

#asyncio + aiohttp 사용 (비동기 방식)
async def fetch_async(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_asyncio(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        return await asyncio.gather(*tasks)

#성능 비교 실행 코드
def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"{func.__name__} took {end - start:.2f} seconds")
    return result

def measure_time_async(async_func, *args):
    start = time.time()
    result = asyncio.run(async_func(*args))
    end = time.time()
    print(f"{async_func.__name__} took {end - start:.2f} seconds")
    return result

if __name__ == "__main__":
    print("\n 순차 처리:")
    measure_time(fetch_sequential, API_URLS)

    print("\n " \
    "ThreadPoolExecutor 사용:")
    measure_time(fetch_threadpool, API_URLS)

    print("\n asyncio + aiohttp 사용:")
    measure_time_async(fetch_asyncio, API_URLS)

