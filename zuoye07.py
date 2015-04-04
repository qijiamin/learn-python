#-*-coding:utf-8-*-
import math
a=3
#dx=0.1
f1=(math.pow(3+0.1,a)-math.pow(3,a))/0.1
print 'f1=',f1
#dx=0.01
f2=(math.pow(3+0.01,a)-math.pow(3,a))/0.01
print 'f1=',f1,'f2=',f2
#dx=0.001
f3=(math.pow(3+0.001,a)-math.pow(3,a))/0.001
print 'f1=',f1,'f2=',f2,'f3=',f3
#dx=0.0001
f4=(math.pow(3+0.0001,a)-math.pow(3,a))/0.0001
print 'f1=',f1,'f2=',f2,'f3=',f3,'f4=',f4
import math
a=3
#dx=0.1
f1=(math.pow(3*a+0.1*a,a-1)-math.pow(3*a,a-1))/0.1
print 'f1',f1
#dx=0.01
f2=(math.pow(3*a+0.01*a,a-1)-math.pow(3*a,a-1))/0.01
print 'f1=',f1,'f2=',f2
#dx=0.001
f3=(math.pow(3*a+0.001*a,a-1)-math.pow(3*a,a-1))/0.001
print 'f1=',f1,'f2=',f2,'f3=',f3
#dx=0.0001
f4=(math.pow(3*a+0.0001*a,a-1)-math.pow(3*a,a-1))/0.0001
print 'f1=',f1,'f2=',f2,'f3=',f3,'f4=',f4