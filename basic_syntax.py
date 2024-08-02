# Operator 연산자
# 기본적으로 하나의 python 파일은 그 자체가 모듈이다.

# 산술 연산자
def arith_oper():
    print("======== 산술 연산")
    print(7 / 3)  # 파이썬 3 -> int / int -> float
    print(7 // 3)  # 정수 나눗셈의 몫 연산자 //
    print(7 % 3)  # 정수 나눗셈의 나머지 연산자

    # 나눗셈의 몫과 나머지 동시에 구함
    print(divmod(7, 3))  # -> (2, 1) : Tuple

    print("7/3의 몫:", divmod(7, 3)[0])  # 7/3의 몫
    print("7/3의 나머지:", divmod(7, 3)[1])  # 7/3의 나머지

    print(7 ** 3)  # 지수승: 7의 3제곱
    print(pow(7, 3))  # 지수 함수 : 7의 3제곱


# 비교 연산자
def rel_oper():
    # pass # 함수 구현부 없어도 비워두면 안됩니다.
    print("======= 비교 연산자 ")
    # >, >=, <, <=, ==, !=

    s1 = "python";
    s2 = "python"
    print("문자열의 비교: ", s1 == s2)

    # 복합 관계식
    a = 6
    # a가 0~10 사이의 값인가?
    # 조건 1: a > 0
    # 조건 2: a < 10
    # 조건 1 and 조건 2
    print(0 < a and a < 10)
    print(0 < a < 10)

    # 다양한 자료 구조의 대소 비교
    print("문자열의 대소: ", "abcd" > "abd")
    print("튜플의 대소: ", (1, 2, 3) > (1, 3, 4))

    # 동질성의 비교 == , 동일성의 비교 is
    a = 10;
    b = 20;
    c = a
    print("a == b ? ", a == b)
    print("a is b ? ", a is b)
    print("a == c ? ", a == c)
    print("a is c ? ", a is c)


# 변수
import keyword  # import 키워드 -> 모듈을 불러오는 명령어


def var_ex():
    print("========== 변수")
    # 문자, 숫자, _ 의 조합
    # 숫자로 시작하면 안됨
    # 예약어는 변수명으로 사용 될 수 없다.
    # 파일명도 변수 명명 규칙에 맞춰 줘야 한다.
    print("예약어 목록: ", keyword.kwlist)
    print("예약어 갯수: ", len(keyword.kwlist))


# 변수 치환
def assignment_ex():
    print("======== 치환문")
    # 변수 선언 절차가 없다.
    print("namespace : ", dir())
    a = 2024  # 첫 번째 할당이 발생할 때 namespace에 추가
    b = a + 1
    print(a, b)
    print("namespace : ", dir())

    # 여러 변수를 한꺼번에 할당 할 수 있다.
    c, d = 3.5, 5.3
    print("c, d = ", c, d)
    # 값의 교환 (Swap)
    c, d = d, c
    print("c, d = ", c, d)

    # 같은 값을 동시 할당
    x = y = z = 10
    print(x, y, z)

    # 파이썬은 동적 타이핑 언어
    a = 2024  # 값이 할당될 때 타입이 결정 -> 타입이 뭔지 확인 필요
    print(a, "is", type(a))  # 현재 객체의 형식을 체크 -> type 함수
    a = "Hello Python"
    print(a, "is", type(a))

    # 특정 객체인지 여부를 판단하는 함수 : isinstance
    print("a는 str의 객체?", isinstance(a, str))

    # 확장 치환문 : 산술, 비트 연산자 등은 확장 치환문으로 변경 할 수 있다.
    a = 10
    a += 10  # a = a+10
    print(a)


# 논리 연산자
def bool_ex():
    print("========= bool 연습")
    # 참(True), 거짓(False)
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판정
    # 조건 분기, 흐름 제어 활용되기 때문에 중요함
    # boolean 판정
    #       논리 연산자, 비교 연산자의 결과
    #       bool 객체 함수를 통해 논리 결과를 얻을 수 있음
    print(bool(0))
    a = 2024
    print(a > 0)  # 비교 연산자를 통한 논리 값의 판정
    print(type(a))

    print(isinstance(True, bool))  # True
    print(isinstance(True, int))  # True
    # 내부적으로 boolean은 int로 처리되고 있다. 거짓=0,"",  참=0,"" 빼고 다
    print(True + True)  # 2

    # 자료의 형태에 의한 boolean 판정
    print(bool(2024), bool(0))  # True False / int 값에 의한 boolean
    print(bool(3.14), bool(0))  # True False / float 값에 의한 boolean
    print(bool("Python"), bool(""))  # True False / str 값에 의한 boolean

    print(bool([1, 2, 3]), bool([]))  # True False/ list 값에 의한 boolean
    print(bool({"key": "value"}), bool({}))  # dict 값에 의한 boolean
    print(bool(None))  # False / None -> 비어있음 -> Java null

    # 논리식의 계산 순서 : Curcuit Break
    # OR일 경우 , 첫 번째 True 연산 결과를 취한다.
    # AND일 경우, 둘 다 True면 뒤쪽 결과를 취한다.
    # AND일 경우, 전체 논리식이 거짓이라면 None을 반환한다.
    print("CB 1: ", [] or "logical")  # False or True
    print("CB 2: ", 'logical' or 'operator')  # True or True
    print("CB 2-1: ", 'logical' and 'operator')  # True and True
    print("CB 3: ", '' or 'operator')  # False or True
    print("CB 3-1: ", '' and 'operator')  # False and True
    print("CB 4: ", None and 1)  # False and True
    print("CB 5: ", None or [])  # False or False


# 타입 힌트
def type_hint():
    # 파이썬은 동적 타이핑 언어 -> 변수의 타입을 명시적으로 지정하지 않는다.
    # 3.5 버전부터 타입 힌트를 이용, 타입 체크를 진행 할 수 있다.

    def add(a: int, b: int) -> int:  # 두 개의 int 입력 받아서 int를 리턴하는 함수
        return a + b

    print(add(10, 20))  # 30

    #print(add("Python", 3.10))  # error

    def greet(name: str) -> str:  # str 입력 받아서 str를 리턴하는 함수
        return 2024
        # return "Hello, " + name

    untyped = "string"  # 타입 힌트가 적용되지 않은 변수
    print(untyped)
    untyped = 2024
    print(untyped)

    typed: str = "string"  # 타입 힌트가 적용된 변수
    print(typed)
    typed = 2024
    print(typed)


def int_ex():
    print("======= 정수형 연습")

    a = 2024  # 리터럴 선언
    b = int(2024)  # 타입 함수 사용

    print(a, "is", type(a))
    print(b, "is", type(b))

    # 2진, 8진, 16진 정수 표현 가능
    b = 0b1101  # 0b /2진수
    o = 0o23  # 0o /8진수
    x = 0xFF  # 0x /16진수

    print(b, o, x)

    # 파이썬 버전 3에서는 int와 long 구분 없음
    # long형 데이터 저장 크기 64bit 초과해서 적재할 수 있음
    i = 2 ** 2048
    print(i)
    print(i.bit_length())

    # 진법 변환 함수
    i = 48
    print(i, bin(i), oct(i), hex(i))  # 10진수를 2진수, 8진수, 16진수로 변환


def float_ex():
    print("======= 실수형 연습")
    a = 3.14159  # 리터럴로 생성
    print(a, "is", type(a))
    print(isinstance(a, float))  # a는 float 인가?

    b = float(3.0)  # type 함수로 생성
    print(b, "is", type(b))
    print(isinstance(b, float))  # b는 float 인가?
    print(a.is_integer(), b.is_integer())
    # False True (b는 소수점 자리가 0이라 int 로도 볼 수 있음)

    # 지수 표기법으로도 확인 가능
    c = 3e3  # 3 * 10 ** 3
    d = -2E-5  # -2 * 10 ** -5
    print(c, d)
    print(-2E-5 == -0.00002)  # 같은 표현


def complex_ex():
    print("======= 복소수 연습")
    # 복소수 : 실수부 + 허수부 j
    a = 4 + 5j
    print(a, "is", type(a))
    print(isinstance(a, complex))  # a 는 복소수인가?

    b = 7 - 2J
    print(a + b)  # 복소수는 산술 연산이 가능
    print(b.real, b.imag)  # 실수부, 허수부
    print(a, "의 켤레복소수는", a.conjugate())  # 켤레 복소수


if __name__ == "__main__":
    # 다른 모듈로 import 되는 경우 __name__ == "python_basics"
    # 직접 실행될 경우(최상위 모듈일 경우) __name__ == "__main__"

    # arith_oper()   # 산술 연산자 연습
    # rel_oper()   # 비교 연산자 연습
    # var_ex()    # 변수 연습
    # assignment_ex() # 변수 치환 연습
    # bool_ex()     # 논리 연산자 연습
    # type_hint()
    # int_ex()
    # float_ex()
    complex_ex()
