'''*首先定义Where函数寻找字母在矩阵中的位置并返回自定义的Location类，然后定义isAround函数来判断下一个字母在矩阵中是否与当前字母相邻，
然后通过两个for循环找出所有符合条件的单词并输出，详细请见代码旁注释。*'''
import numpy as np

class Location(object):#存储字母在矩阵中的行、列位置的类
    def __init__(self,row,col):
        self.row=row
        self.col=col

def Where(arr,m,n,x):#寻找字母x在矩阵arr中的位置，返回一个Location类
    for i in range(m):
        for j in range(n):
            if arr[i][j] == x :
                return Location(i,j)

#row为当前字母的行下标，col为当前字母的列下标，nextCh为单词中当前字母的下一个字母
def isAround(arr,m,n,row,col,nextCh):#下一个字母在矩阵中是否与当前字母相邻
    for i in range(-1,2):
        for k in range(-1,2):
            if row+i < m and col+k <n:#防止下标出界进行判断
                #row+i>=0和col+k>=0的约束保证矩阵边和角的正确处理
                if arr[row+i][col+k] == nextCh and row+i >= 0 and col+k >= 0  and not(i==0 and k==0):
                    return True
    return False

def canGenegrate(l,x,m,n):#判断单词是否可由矩阵生成，返回Bool值
    t = np.array(l).reshape(m,n)
    for i in range(len(l)):
        if l[i] == x[0]:  # 单词第一个字符匹配成功，开始进行判断
            for k in range(len(x)):
                if k == 0:
                    Next = x[1]
                    arrLoc=Where(t,m,n,x[0])#标记第一个字母在矩阵中的位置
                elif k!= 0:#
                    if k+1 < len(x):
                        Next = x[k+1]
                        arrLoc = Where(t, m, n, x[k])#标记上一次判断成功的字母的位置
                    else:#遍历到单词末尾，匹配成功
                        #print('匹配成功')
                        return True
                if isAround(t,m,n,arrLoc.row,arrLoc.col,Next):
                    continue
                else:#下一字母不在当前字母周围，返回l再次寻找首字母进行下次判断
                    break
    else:
        #print('不匹配')
        return False

#/***-----------------更改测试数据-----------------***/#

l=['A','R','E','I','P','D','E','L','P']
m=3
n=3
x=['APPLE','ARE','RED','AIR','PENPIEAPPLE','APPLEPEN','LIPS','PLEASE']

#/***-----------------更改测试数据-----------------***/#

t = np.array(l).reshape(m,n)
print(t)
print(x)
#测试
print('以下单词可以被生成:',end=' ')
for i in range(len(x)):
    if canGenegrate(l,list(x[i]),m,n) is True:
        print(x[i],end=' ')
#时间复杂度为O(n*4),空间复杂度为m*n