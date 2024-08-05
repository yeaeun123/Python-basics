# list는 모든 시퀀스의 시퀀스
# 시퀀스의 모든 연산 작업을 수행
def define_list():
    """
    리스트 생성 관련 샘플 코드
    """
    lst1 = list()    # 타입 함수를 이용한 생성
    print(lst1, type(lst1))
    lst2 = []   # [] -> 리스트 표기법 -> 추천하는 생성법
    lst3 = [1, 2, "Python"]     # 객체 타입을 가리지 않음
    print(lst2, lst3)

    lst4 = list("Python")
    print(lst4)     # 다른 시퀀스 자료형을 리스트로 변환 /['P', 'y', 't', 'h', 'o', 'n']

def list_oper():
    """
    리스트는 len, 인덱싱, 슬라이싱, in, not in, 내부데이터 치환 가능
    리스트 연산 연습
    """
    lst = [1, 2, "Python"]

    print(lst, "Length: ", len(lst))    # 길이의 확인 / Length: 3

    print(lst[0], lst[1], lst[2])   # 정방향 인덱싱
    print(lst[-1], lst[-2], lst[-3])    # 역방향 인덱싱

    # 슬라이스 : [시작경계:끝경계[:간격값]]
    print(lst[1:3])     # == [2, 'Python']
    print(lst[1:])      # 끝경계 생략되면 끝까지
    print(lst[0:2])  # == [1, 2]
    print(lst[:2])   # 시작경계 생략되면 처음부터

    cp = lst[:]     # 원본 전체의 copy -> 슬라이스를 활용한 전체의 복제
    print(cp)
    print(cp is lst, cp == lst)
    # False True/ 복제본이라 같은 객체아님 / 내부 데이터(내용)는 같음




if __name__ == "__main__":
    # define_list()
    list_oper()