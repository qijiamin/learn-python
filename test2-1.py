# -*- coding:utf-8 -*-
#########学生基本信息############
#姓名:齐佳民
#学号:1403050116
#班级：通风14-1班
##############题目###############
#12.8
############代码#################
import math
p,k,T,M,NA,n,m,R=1.013e5,1.38e-23,300.15,32e-3,6.022e23,2.45e25,5.31e-26,8.31
n=p/(k*T)
print 'n=p/(k*T)=',n
n=M/NA
print 'n=M/NA=',n
rho=n*m
print 'rho=n*m=',rho
v=math.sqrt(3*R*T/M)
print 'v=math.sqrt(3*R*T/M)=',math.sqrt(v**2)
epsilonk=3/2*k*T
print 'epsilonk=3/2*k*T=',epsilonk
epsilon=m/M*5/2*R*T
print 'epsilon=m/M*5/2*R*T=',epsilon