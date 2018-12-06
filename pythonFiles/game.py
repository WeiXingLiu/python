import random

meInput = input('请输入：剪刀(0)  石头(1)  布(2):')

meInt = int(meInput)

computer = random.randint(0, 2)

if ((meInt == 0) and (computer == 2)) or ((meInt ==1) and (computer == 0)) or ((meInt == 2) and (computer == 1)):
    print('yeah')
elif meInt == computer :
    print('平局')
else:
    print('输了')
