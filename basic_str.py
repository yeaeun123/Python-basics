# str 기초
def define_str():
    """
    함수 정의 연습
    """
    # 문자열의 정의
    # 한 줄 문자열 : 쌍따옴표("), 홑따옴표(') 모두 가능
    s1 = "Hello Python"  # 리터럴 생성
    s2 = str("Hello Python")  # 타입 함수 사용
    s3 = str(3.14159)  # 다른 타입을 변환 생성
    print(s1, type(s1))
    print(s2, type(s2))
    print(s3, type(s3))

    print("s1은 str? ", isinstance(s1, str))

    # 여러 줄 문자열 : """, '''
    s4 = """Life is too short, You need Python.
파이썬은 데이터 처리가 중요한 시대에서 
가장 널리 사용되는 언어입니다."""

    print(s4)

    # 여러 줄 문자열은 한 줄 주석만 있는 파이썬에서
    # 여러 줄 주석을 사용하고자 할 때도 사용할 수 있다.
    """여러 줄 문자열을 사용한 여러 줄 주석
    메서드 정의 바로 아래 여러 줄 주석을 추가하면 
    문서화 할 때 이용될 수 있고
    help 명령어로 해당 메서드의 주석을 볼 수 있다. 
    docstring 이라 한다."""

    # f-string : 문자열 포맷팅 방식 중 하나
    name, age = "홍길동", 28
    message = f"안녕하세요, {name}님. 당신은 {age}살 입니다."
    print(message)

    width, height = 10, 5
    message = f"사각형의 면적은 {width * height} 입니다."
    print(message)


def string_oper():
    """
    문자열 연산
    """
    str1 = "First String"
    str2 = "Second String"
    # len(), 인덱싱 가능, 슬라이싱 가능, 포함여부 판별 가능
    # 불변 자료형 (immutable), 치환 불가능 !
    print(len(str1), len(str2))  # 길이

    # 인덱싱
    print(str1[0], str1[1], str1[2], "...", str1[9], str1[10], str1[11])  # 정방향
    print(str1[-12], str1[-11], str1[-10],
          "...", str1[-3], str1[-2], str1[-1])  # 역방향

    # 문자열은 immutable -> 치환 불가
    # str1[0] = "f" # 변경 불가 error

    # 슬라이싱
    str1 = "First String"
    # [시작 경계 : 끝 경계 [:간격]]
    print(str1)
    print(str1[6:9])    # 정방향 인덱스 활용
    print(str1[-6:-3])  # 역방향 인덱스 활용

    print(str1[0:5])
    print(str1[:5])     # 시작부터 -> 0 생략 가능

    print(str1[6:len(str1)])
    print(str1[6:])     # 끝까지 -> len(str1) 생략 가능

    print(str1[::2])    # 처음부터 끝까지 간격 2
    print(str1[::-1])   # 간격 값이 음수 -> 역방향 

    # str = "문자열" # 대표적 에러
    # print(str)
    # s2 = str(3.14159)


if __name__ == "__main__":
    # define_str()
    string_oper()
