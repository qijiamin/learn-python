#-*-coding:utf-8-*-
#嵌套词典
import math
xueshengmingdan={
'车永杰':{'学号':'1403050101','性别':'男','年龄':19,'成绩信息':80},
'陈晓军':{'学号':'1403050102','性别':'男','年龄':19,'成绩信息':76},
'程太阳':{'学号':'1403050103','性别':'男','年龄':19,'成绩信息':77},
'单宇轩':{'学号':'1403050104','性别':'男','年龄':19,'成绩信息':68},
'耿峰':{'学号':'1403050105','性别':'男','年龄':19,'成绩信息':72},
'顾生权':{'学号':'1403050106','性别':'男','年龄':20,'成绩信息':76},
'黄靖宇':{'学号':'1403050107','性别':'男','年龄':19,'成绩信息':74},
'刘天威':{'学号':'1403050108','性别':'男','年龄':19,'成绩信息':76},
'刘增富':{'学号':'1403050109','性别':'男','年龄':19,'成绩信息':56},
'刘凯元':{'学号':'1403050110','性别':'男','年龄':19,'成绩信息':68},
'鲁肖丰':{'学号':'1403050111','性别':'男','年龄':19,'成绩信息':76},
'路琦':{'学号':'1403050112','性别':'男','年龄':19,'成绩信息':76},
'聂朝刚':{'学号':'1403050113','性别':'男','年龄':19,'成绩信息':78},
'戚志鹏':{'学号':'1403050114','性别':'男','年龄':19,'成绩信息':76.5},
'齐佳民':{'学号':'1403050115','性别':'男','年龄':19,'成绩信息':100},
'司建伟':{'学号':'1403050116','性别':'男','年龄':19,'成绩信息':77},
'宋健':{'学号':'1403050117','性别':'男','年龄':19,'成绩信息':82},
'隋文武':{'学号':'1403050118','性别':'男','年龄':19,'成绩信息':86},
'王本松':{'学号':'1403050119','性别':'男','年龄':19,'成绩信息':46},
'王大勇':{'学号':'1403050120','性别':'男','年龄':19,'成绩信息':72},
'王哲':{'学号':'1403050121','性别':'男','年龄':19,'成绩信息':98},
'吴文祥':{'学号':'1403050122','性别':'男','年龄':19,'成绩信息':45},
'杨强':{'学号':'1403050123','性别':'男','年龄':23,'成绩信息':32},
'杨文杰':{'学号':'1403050124','性别':'男','年龄':19,'成绩信息':75},
'杨智宇':{'学号':'1403050125','性别':'男','年龄':19,'成绩信息':86},
'朱诗豪':{'学号':'1403050126','性别':'男','年龄':19,'成绩信息':66}
}
grade=[
['车永杰',80],
['陈晓军',76],
['程太阳',77],
['单宇轩',68],
['耿峰',72],
['顾生权',76],
['黄靖宇',74],
['刘天威',76],
['刘增富',56],
['刘凯元',68],
['鲁肖丰',76],
['路琦',76],
['聂朝刚',78],
['戚志鹏',76.5],
['齐佳民',100],
['司建伟',77],
['宋健',82],
['隋文武',86],
['王本松',46],
['王大勇',72],
['王哲',98],
['吴文祥',45],
['杨强',32],
['杨文杰',75],
['杨智宇',86],
['朱诗豪',66]]
ages=[]
grades=[]


#打印所有学生的姓名，学号，性别，年龄，成绩信息
names = xueshengmingdan.keys()
for name in names:
    print '姓名:',name,'学号:',xueshengmingdan[name]['学号'],'性别:',xueshengmingdan[name]['性别'],'年龄',xueshengmingdan[name]['年龄'],'成绩信息',xueshengmingdan[name]['成绩信息']
for name in names:
    ages.append(xueshengmingdan[name]['年龄'])                         
    grades.append(xueshengmingdan[name]['成绩信息'])
def two_cmp(x1,x2):
    return cmp(x1[1],x2[1])
b=sorted(grade,two_cmp)
print b                                                     #按成绩排序


print '---------------------------------------------------------------------'
print '全班人数',len(names)                                 #全班人数
print '最大年龄',max(ages)                                  #最大年龄
print '最小年龄',min(ages)                                  #最小年龄
print '平均年龄',(1.0*sum(ages)/len(ages))                  #平均年龄
print '最高成绩',max(grades)                                #最高成绩
print '最低成绩',min(grades)                                #最低成绩
print '平均成绩',1.0*sum(grades)/len(grades)                #平均成绩
'''
如果要增加学生                 请输入
a={}
a=['xxx']={
'学号':'xxxxxx',
'性别':'x'
'年龄':'xx'
'成绩信息'：'xx'}
如果要删除某学生               请输入        del a['xx']
     例如       print xueshengmingdan['朱诗豪']
如果想要修改某个学生的信息     请输入        xueshengmingdan['name']['修改的信息']='xxxx'
     例如       xueshengmingdan['朱诗豪']['学号']=1403050127
如果想查找学生的某个信息       请输入        print xueshengmingdan['name']['查找的信息']
     例如       print xueshengmingdan['黄靖宇']['学号']


                                  制作人员信息
                              编码及测试人员：齐佳民
                              收集数据：隋文武
                              撰写报告：刘增富
                              答辩演讲：王大勇
'''









