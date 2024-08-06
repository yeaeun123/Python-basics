
evens = {0, 2, 4, 6, 8, 10}     # 짝수 집합
odds = {1, 3, 5, 7, 9}      # 홀수 집합
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}    # 전체 집합
mthree = {0, 3, 6, 9}   # 3의 배수 집합


def define_set():
    """
    집합 정의 연습
    SET : 순서가 없고, 중복 허용하지 않음 (인덱싱,슬라이싱 불가)
        len, in, not in 확인가능
    """

    empty = set()   # 비어 있는 set / {} 는 비어 있는 set 이 아님! dict로 인식함
    print(type(empty), type({}))  # <class 'set'> <class 'dict'>

    # 길이, 포함 여부는 확인이 가능!
    print(numbers, "LENGTH:", len(numbers))
    print(2 in numbers, 2 in evens, 2 in odds, 2 in mthree)

    # 다른 순차형으로 set 만들기
    s = "Python Programming"
    chars = set(s.upper())
    print(s, chars)

    # list 등 순차자료형의 중복 값을 제거할 때 유용하다.
    lst = "Python Programming Java Programming HTML Programming".split()
    print("lst:", lst)

    # list에서 중복 요소를 제거한 요소 갯수는?
    s = set(lst)
    print("set:", s, len(s))
        # set: {'Python', 'HTML', 'Java', 'Programming'} 4
    lst2 = list(s)  # list로 데이터 정제
    print("lst2:", lst2)


def set_methods():
    """
    set의 메서드들
    """
    print("numbers:", numbers, len(numbers))
    numbers.add(10)
    print("numbers:", numbers, len(numbers))
    numbers.add(10) # 중복을 허용하지 않는 자료형
    print("numbers:", numbers, len(numbers))

    print("evens:", evens)
    evens.add(3)    # 추가
    print("evens:", evens)
    evens.discard(3)    # 3 삭제
    print("evens:", evens)
    evens.discard(3)    # 삭제
    # discard 는 없어도 error 없이 무시
    if 3 in evens:
        evens.remove(3) # remove : 삭제할 데이터 없으면 KeyError

    evens.update({10})
    print("evens:", evens)


def set_oper():
    """
    set의 집합 연산
    """
    numbers.add(10)

    # 합집합 : | , union
    print(evens | odds == numbers)  # 짝수 집합 합집합 홀수 집합 == 전체 집합
    print(evens.union(odds) == numbers)

    # 교집합 : & , intersection
    print(evens & mthree == {0, 6})
    print(evens.intersection(mthree) == {0, 6})

    # 차집합 : - , difference
    print(numbers - odds == evens)  # 전체 집합 차집합 홀수 집합 == 짝수 집합
    print(numbers.difference(odds) == evens)

    # 판별 함수 : issuperset(모집합), issubset(부분집합)
    print(numbers.issuperset(evens), numbers.issuperset(odds))  # 부모 집합 여부 판별
    print(evens.issubset(numbers), odds.issubset(numbers))  # 부분 집합 여부 판별

def loop():
    for num in numbers:
        print(num, end="\t")
    else:
        print()



if __name__ == "__main__":
    # define_set()
    # set_methods()
    # set_oper()
    loop()