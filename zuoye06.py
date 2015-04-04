#_*_coding:utf-8-*-
import math
a=input('请输入a:')
b=input('请输入b:')
c=input('请输入c:')
D=b*b-4*a*c
print 'D=',D
if D<0:
    print '无法求根'
else:
    x1=(-1.0*b+math.sqrt(D))/(2*a)
    x2=(-1.0*b-math.sqrt(D))/(2*a)
    print x1,x2