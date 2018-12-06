num1 = input('请输入第一个数字:')

num2 = input('请输入第二个数字:')

while num1 < num2 :
    print('请输入小于第一个数字的数')
    num2 = input('请输入第二个数字:')

if num2 == '':
    num2 = '0'
sum = int(num1) - int(num2)
print(sum)
