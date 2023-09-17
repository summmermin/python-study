money = eval(input('지금 가지고 계신 현금이 얼마인가요>>>'))

if money >= 20000:
    print('오늘은 회를 드세요!')
elif money >= 10000:
    print('떡볶이를 추천드립니다')
else:
    print('오늘은 간단히 드세요!')
