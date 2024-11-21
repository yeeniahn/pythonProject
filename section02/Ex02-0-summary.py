'''
변수 - 값을 담을 수 있는 메모리 저장 공간

변수명 = 값

변수타입(값 종류)
기본형
    1. 부울(bool) - True, False
        부울변수1 = True
        부울변수2 = False
    2. 정수(int) - 메모라 허용 음수, 0, 양수
        num1 = 1
        num2 = 2
    3. 실수(float) - 소수점 포함 숫자
        fNum1 = 3.14
        fNum2 = 2.7
    4. 문자열(str) - 문자 저장 쌍따옴표("") 또는 작은따옴표('')
        str1 = "Hello Python"
        str2 = '안녕하세요!'

컬렉션형(자료구조형)
    1. list - 순서가 있는 데이터 집합
        list1 = ['값1', '값2', '값3']
        list2 = ['값1', 10, 3.14]
    2. tuple - list 비슷하지만 수정 불가능
        tuple1 = ('값1', '값2', '값3')
        tuple2 = ('값1', 10, 3.14)
    3. set - 순서가 업고, 중복 허용하지 않는 데이터 집합
        set1 = {'값1', '값2', '값3'}
        set2 = {'값1', 10, 3.14}

변수명.메소드()
'''


'''set에다가 적기
단일추가 부분에 
fire_type.add('마그마') #중복 허용 하지 않는다'''

#4. 세트 제거 메서드
water_type = {'꼬부기', '잉어킹','라프가스'}
water_type.remove('잉어킹') # 값이 없으면 에러가 난다
'''water_type.remove('') # 값이 없으면 에러가 난다
KeyError: '''''
print('remove 후:', water_type)

water_type.discard('라프가스') #값이 없어도 에러 없음
print('discard 후:', water_type)

water_type.pop() #임의 제거
print('pop 후:', water_type)

new_type = {'메가이브이', '뮤'}
new_type.clear()   #전체 제거
print('clear 후:', new_type)

