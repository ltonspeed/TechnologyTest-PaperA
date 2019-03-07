'''*定义Countchar函数来计算字符串中各个字符出现的次数，返回一个字典，字典的value值即为字符出现的个数，
对A和B字符串调用Countchar函数，比较字典中字符出现的次数，如果符合要求则输出A是B的超集，如果不符合则输出不是。*'''

def Countchar(str): #计算字符串中各个字符出现的次数，最后返回一个字典
    result = {} #创建一个空字典
    for i in set(str):
        result[i] = str.count(i) #将单个字符的出现次数作为value存入字典中
    return result

A = input("请输入字符串A:")
B = input("请输入字符串B:")

for i in set(B):
    if Countchar(A)[i] < Countchar(B)[i]:#一旦发现B中字符个数大于A对应字符的个数，判断A不是B的超集
        print('A不是B的超集')
        break
else:#所有字符判断结束，可以判断A为B的超集
    print('A是B的超集')

#时间复杂度为O(n),空间复杂度为n