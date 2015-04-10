# -*- coding:utf-8 -*-
#########学生基本信息############
#姓名:齐佳民
#学号:1403050116
#班级：通风14-1班
##############题目###############
#12.8
############代码#################
import math
p,k,T=1.013e5,1.38e-23,300.15
n=p/(k*T)
print 'n=',n
M,NA=32e-3,6.022e23
n=M/NA
print 'n=',n
n,m=2.45e25,5.31e-26
rho=n*m
print 'rho=',rho
R=8.31
v=math.sqrt(3*R*T/M)
print 'math.sqrt(v**2)=',math.sqrt(v**2)
epsilonk=3/2*k*T
print 'epsilonk=',epsilonk
epsilon=m/M*5/2*R*T
print 'epsilon=',epsilon