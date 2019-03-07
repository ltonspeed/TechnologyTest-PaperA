'''
采用numpy.random函数随机生成M*N带权矩阵作为地图，然后采用动态规划的方法求出左上角到右下角路
径最长的路径，与英雄生命进行对比，在有剩余血量的英雄中挑选出攻击力最高的英雄输出。
'''
import numpy as np
#Hero类记录英雄基本信息
class Hero(object):
    def __init__(self,hp,atk,name):
        self.hp = hp
        self.atk = atk
        self.name = name

class Solution(object):#求解左上角到右下角的最大权值之和
    def pathMinSum(self,nums):
        row_count = len(nums)
        col_count = len(nums[0])
        #计算在列边界走的步数
        for i in range(1,row_count):
            nums[i][0] += nums[i-1][0]
        #计算在行边界走的步数
        for j in range(1,col_count):
            nums[0][j] += nums[0][j-1]
        #选择步数最长的，攻击力高的英雄血量低，最大即为走过棋盘途中所受伤害最小
        for i in range(1,row_count):
            for j in range(1,col_count):
                nums[i][j] += max(nums[i-1][j],nums[i][j-1])
        return nums[-1][1]

#---------------自行设置随机地图-----------------#
L=[]
#M*N的地图
m=10
n=12
#棋盘内随机数取值范围[x,y]
x=-2000
y=1000
for i in range(m*n):
   L.append(np.random.randint(x,y))#
Map = np.array(L).reshape(m,n)
print(Map)
#---------------自行设置随机地图-----------------#

#展示随机生成的地图
x=Solution()
Mindamage = x.pathMinSum(Map)
print("该随机地图对英雄造成的最小伤害：",Mindamage)

#英雄基础信息，分别为血量、攻击力、姓名
Hero = [[10000,100,'梦琪'],[5000,200,'程咬金'],[2000,500,'亚瑟'],[1000,1000,'铠'],[100,2000,'狄仁杰']]
print("英雄信息：",Hero)

#排除掉无法获胜的英雄
for i in Hero:
    temp = i[0] + Mindamage
    if temp >= 0:
        continue
    else:
        i[1] = 0
print(Hero)

#找出可以通关的英雄的中攻击力最高的英雄
l=[]
for j in Hero:
    if j[1] != 0:
        l.append(j[1])
for k in Hero:
    if max(l) == k[1]:
        print('可以通关的英雄中攻击力最高的是:',k[2])