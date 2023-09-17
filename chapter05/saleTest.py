# 사용자에게 가방, 옷의 가격을 받는다.

bag = eval(input('구매하실 가방은 얼마인가요?>>>'))
clothes = eval(input('구매하실 옷은 얼마인가요?>>>'))
total = bag+clothes
if total >= 100000:
    print('총 금액은 30% 할인되셔서', total*0.7)
elif total >= 50000:
    print('총 금액은 20% 할인되셔서', total*0.8)
else:
    print('총 금액은', total)
