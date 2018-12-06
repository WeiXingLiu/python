import time
def getResult():
    listObject = []
    value = ''
    try:
        value = listObject[1]
    except Exception as e:
        print('e', e)
        value = 'error'
        f = open('data.txt', 'a+')
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.close()
    # finally:
    #     value = '结果'
    return value
print('getResult', getResult())