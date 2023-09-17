name = ['summer', 'tom', 'harry', 'holden', 'luna']

name.append('winter')  # 데이터 마지막에 추가
del name[-1]  # 마지막 데이터 삭제

slicing = name[0:3]  # 리스트 슬라이싱
name_legth = len(name)
print('slicing>>>', slicing)
print(name)
print('name의 길이는>>>', name_legth)
name.sort()  # 오름차순으로 정렬
print(name)
name.sort(reverse=True)  # 내림차순으로 정렬
print(name)
