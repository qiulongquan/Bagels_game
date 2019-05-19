import random

# random.shuffle(list) 执行完后不会生成新的数组，而是写入到原来的数组里面
num = [1,2,3,4,5,6]
print(type(num))
print(num)

num1 = list(range(5))
print(type(num1))
random.shuffle(num1)
print(num1)

num2 = [1,2,3,4,5,6]
random.shuffle(num2)
print(type(num2))
print(num2)
# 每次在调用 random.shuffle() 的时候，
# 列表中的项都会打乱顺序。
random.shuffle(num2)
print(num2)

str = ['d','a','c','b']
print(str)
str.sort()
a = ','.join(str)
print(a)


str = '0 2 11 21 31 41 51 61'
list = str.split()
print(list)

str = '41'
if str in list:
    print("Sting %s's index position:%s" % (str, list.index('41')))
else:
    print("it is not exists.")

print("please press key:")
if input().lower().startswith('y'):
    print("y key have been pressed.")
else:
    print("you pressed %s." % (input().lower()))
