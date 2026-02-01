# ============================================
# 파이썬 기본 문법 정리
# ============================================

# 1. 리스트 (List)
# ============================================
def list_basics():
    """리스트의 기본 개념과 메서드"""
    
    # 리스트 생성
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    
    # 리스트 접근 (인덱싱)
    first = fruits[0]  # "apple"
    last = fruits[-1]  # "cherry"
    
    # 리스트 슬라이싱
    slice1 = numbers[1:4]  # [2, 3, 4]
    slice2 = numbers[:3]  # [1, 2, 3]
    slice3 = numbers[2:]  # [3, 4, 5]
    slice4 = numbers[::2]  # [1, 3, 5] (2칸씩)
    slice5 = numbers[::-1]  # [5, 4, 3, 2, 1] (역순)
    
    # 리스트 메서드
    fruits.append("orange")  # 끝에 요소 추가
    fruits.insert(1, "mango")  # 특정 위치에 추가
    fruits.remove("apple")  # 특정 요소 제거
    popped = fruits.pop()  # 마지막 요소 제거 및 반환
    fruits.sort()  # 정렬 (원본 변경)
    fruits.reverse()  # 역순 정렬 (원본 변경)
    length = len(fruits)  # 리스트 길이
    count = fruits.count("banana")  # 특정 요소 개수
    index = fruits.index("cherry")  # 특정 요소의 인덱스
    
    return fruits, numbers


# 2. 딕셔너리 (Dictionary)
# ============================================
def dict_basics():
    """딕셔너리의 기본 개념과 메서드"""
    
    # 딕셔너리 생성
    person = {
        "name": "John",
        "age": 30,
        "city": "Seoul",
        "job": "Engineer"
    }
    
    # 딕셔너리 접근
    name = person["name"]  # "John"
    age = person.get("age")  # 30 (get 메서드는 안전함)
    unknown = person.get("hobby", "No hobby")  # 기본값 설정
    
    # 딕셔너리 수정
    person["age"] = 31  # 기존 키 수정
    person["hobby"] = "reading"  # 새로운 키-값 추가
    del person["job"]  # 키-값 삭제
    
    # 딕셔너리 메서드
    keys = person.keys()  # 모든 키
    values = person.values()  # 모든 값
    items = person.items()  # 키-값 쌍
    person.pop("hobby")  # 특정 키 제거 및 값 반환
    person.clear()  # 모든 요소 제거
    
    return person


# 3. 튜플 (Tuple)
# ============================================
def tuple_basics():
    """튜플의 기본 개념 (불변 시퀀스)"""
    
    # 튜플 생성
    coordinates = (10, 20)
    single = (1,)  # 단일 요소 튜플 (쉼표 필수)
    empty = ()  # 빈 튜플
    
    # 튜플 접근 (리스트와 동일)
    x = coordinates[0]  # 10
    y = coordinates[1]  # 20
    
    # 튜플 슬라이싱
    sliced = coordinates[0:1]  # (10,)
    
    # 튜플은 불변이므로 수정 불가능
    # coordinates[0] = 5  # 오류 발생
    
    return coordinates


# 4. 집합 (Set)
# ============================================
def set_basics():
    """집합의 기본 개념과 메서드"""
    
    # 집합 생성 (중복 없음, 순서 없음)
    colors = {"red", "green", "blue"}
    numbers = {1, 2, 2, 3, 3, 3}  # {1, 2, 3}
    empty_set = set()  # 빈 집합
    
    # 집합 메서드
    colors.add("yellow")  # 요소 추가
    colors.remove("red")  # 요소 제거 (없으면 오류)
    colors.discard("green")  # 요소 제거 (안전)
    
    # 집합 연산
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union = set1 | set2  # {1, 2, 3, 4, 5} (합집합)
    intersection = set1 & set2  # {3} (교집합)
    difference = set1 - set2  # {1, 2} (차집합)
    
    return colors, set1, set2


# 5. 문자열 (String)
# ============================================
def string_basics():
    """문자열의 기본 개념과 메서드"""
    
    # 문자열 생성
    text = "Hello, Python!"
    
    # 문자열 접근 (불변)
    first_char = text[0]  # "H"
    last_char = text[-1]  # "!"
    
    # 문자열 슬라이싱
    substring = text[0:5]  # "Hello"
    reversed_text = text[::-1]  # "!nohtyP ,olleH"
    
    # 문자열 메서드
    upper = text.upper()  # "HELLO, PYTHON!"
    lower = text.lower()  # "hello, python!"
    length = len(text)  # 15
    count = text.count("l")  # 3
    index = text.index("P")  # 7
    replaced = text.replace("Python", "Java")  # "Hello, Java!"
    split_text = text.split(",")  # ["Hello", " Python!"]
    stripped = "  hello  ".strip()  # "hello"
    
    return text, replaced


# 6. 반복문과 조건문
# ============================================
def loops_and_conditions():
    """반복문과 조건문의 기본 사용법"""
    
    # for 반복문 - 리스트
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        if fruit == "banana":
            print(f"Found banana: {fruit}")
    
    # for 반복문 - range
    for i in range(5):  # 0, 1, 2, 3, 4
        if i % 2 == 0:
            print(f"{i} is even")
    
    # for 반복문 - enumerate (인덱스와 값)
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    
    # for 반복문 - 딕셔너리
    person = {"name": "John", "age": 30}
    for key, value in person.items():
        print(f"{key}: {value}")
    
    # while 반복문
    count = 0
    while count < 3:
        print(f"Count: {count}")
        count += 1
    
    # List Comprehension (리스트 컴프리헨션)
    squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
    
    return squares, evens


# 7. 함수 (Function)
# ============================================
def function_basics():
    """함수의 기본 개념"""
    
    # 기본 함수
    def greet(name):
        """사용자를 인사하는 함수"""
        return f"Hello, {name}!"
    
    result1 = greet("Alice")
    
    # 기본값이 있는 함수
    def add(a, b=0):
        """두 수를 더하는 함수"""
        return a + b
    
    result2 = add(5)  # 5
    result3 = add(5, 3)  # 8
    
    # 여러 값 반환
    def get_min_max(numbers):
        """최소값과 최대값을 반환"""
        return min(numbers), max(numbers)
    
    min_val, max_val = get_min_max([1, 2, 3, 4, 5])
    
    # *args (가변 위치 인자)
    def sum_all(*args):
        """모든 인자를 더함"""
        return sum(args)
    
    result4 = sum_all(1, 2, 3, 4, 5)  # 15
    
    # **kwargs (가변 키워드 인자)
    def print_info(**kwargs):
        """키워드 인자를 출력"""
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    print_info(name="John", age=30, city="Seoul")
    
    return result1, result2, result3


# 8. 메인 함수
# ============================================
if __name__ == "__main__":
    print("=== 파이썬 기본 문법 정리 ===\n")
    
    print("1. 리스트:")
    list_data = list_basics()
    print(list_data)
    
    print("\n2. 딕셔너리:")
    dict_data = dict_basics()
    print(dict_data)
    
    print("\n3. 튜플:")
    tuple_data = tuple_basics()
    print(tuple_data)
    
    print("\n4. 집합:")
    set_data = set_basics()
    print(set_data)
    
    print("\n5. 문자열:")
    string_data = string_basics()
    print(string_data)
    
    print("\n6. 반복문과 조건문:")
    loop_data = loops_and_conditions()
    print(loop_data)
    
    print("\n7. 함수:")
    func_data = function_basics()
    print(func_data)