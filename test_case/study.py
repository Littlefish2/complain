#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：study.py
# @IDE：PyCharm 
# @Date：2021/3/3 16:56 
# @Author: zhangy
'''
fo = open("test9.txt","r+")
str = fo.read(3)
print("读取到的字符串是："+str)

position = fo.tell()
#p = str(position)
print(position)

class gxd(object):     #新式类    多继承方式改变
    def __init__(self,name,age,address,score):
        self.name = name
        self.age = age
        self.address = address
        self.__score = score
    def mingzi(self):
        print("你的名字是",self.name,"年龄：",self.age)
    def simple(self):
        print("分数为：",self.__score)  #私有属性    私有方法类似
    # def __del__(self):
    #     print("程序结束（析构函数)",self.name)
    # del __del__
r1 =gxd('gxd','22','henan','100')
r1.mingzi()
r1.simple()
class xxx(object):
    def playwith(self,obj):
        print("%s is play with %s"%(self.name,obj.name))
class ggg(gxd,xxx):             #继承
    ####### 多继承默认从左到右   python3 都是是广度优先来继承    python2经典类是深度优先来继承      新式类也是广度优先来继承（加object）
    def __init__(self,name,age,address,score,intresting):     #重构子类属性
        # gxd.__init__(self,name,age,address,score)
        super(ggg,self).__init__(name,age,address,score)      #同上    新式类写法
        self.intresting = intresting
                # @classmethod    类方法  只能访问类变量，不能访问实例变量
        # @staticmethod     静态方法  名义上归类管理，实际上跟类没啥关系
        # @property      属性方法  把一个方法变成一个静态属性    平常不能传参数
        # 如果要传参数   要写一个同名字的方法，在方法上边@方法名.setter    删除的话 @方法名.deleter 同上
    def play(self):
        print("%s   is playing DOTA2"% self.name)
    def simple(self):                     #调用（重构）父类方法
        gxd.simple(self)
# m = ggg("ggg","22","henan","99")
m = ggg("gxd","22","henan","99","DOTA2")
m.play()
m.simple()
m.playwith(r1)
'''
'''
class people:
    def say(self,a,b,c):
        self.name = a
        self.age = b
        self.__weight = c
        print("%s说：我%s岁,我%s千克" %(self.name,self.age,self.__weight))
#p = people()
people().say("zhangyu",18,50)
'''
'''
list1 =[1,2,3,4]
list2 =[]
count=0
for i in range (len(list1)):
    x=str(list1.pop(i))
    #print(x)
    for j in range(len(list1)):
        y=str(list1.pop(j))
        #print(y)
        for k in range(len(list1)):
            z=str(list1[k])
            #print(z)
            m = x + y + z
            print(m, end=" ")
            count=count+1
            list2.append(m)
        list1.insert(j,int(y))
        print(list1)
    list1.insert(i,int(x))
    print(list1)
    print("")
print("一共%s个" %count)
print(list2)



s="nihao: tester "
a=s.split(":")[1].rstrip()
print(a)

'''
a = [1,2,3,4,5]
a.pop(3)
print(a)