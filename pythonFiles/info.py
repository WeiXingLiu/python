info = []

def insertInfo(name, age, *values):
    if values:
        for value in values:
            print(value)

insertInfo(1, 2, 3, 3, 4, 5)

value = 100
def globalFunc():
    # global value
    # print(value)
    value = 10
    print(value)
    value= 20
    print(value)
globalFunc()
print(value)