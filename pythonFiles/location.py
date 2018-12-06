location = ''
current = 0
while current < 4:
    inputContent = input('请输入路径')
    location += '/' + inputContent
    current += 1
print(location)


inputStr = input('输入需要处理的字符串')
valueList = []
countList = []
for i in inputStr:
    valueIndex = -1
    for index,value in enumerate(valueList):
        if value == i:
            valueIndex = index
            break
    if valueIndex != -1:
        countList[valueIndex] += 1
    else:
        valueList.append(i)
        countList.append(1)

result = ''
for index,value in enumerate(valueList):
    result += value + str(countList[index]) + ' '
print(result)