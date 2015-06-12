#-*-coding:utf-8-*-
print '欢迎使用校验身份证号码真伪系统'
print '------------------------------'
print '    1.测试身份证的检验码      '
print '    2.测试身份证的真伪        '
print '    3.显示制作人员信息        '
print '    4.退出                    '
print '------------------------------'
cz=input('请输入想要进行的操作:')
def hanshu(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q):
    
    sum=7*a+9*b+10*c+5*d+8*e+4*f+2*g+1*h+6*i+3*j+7*k+9*l+10*m+5*n+8*o+4*p+2*q#定义公式，计算各位数字乘以系数之和
    #求余数
    y = sum%11
    return y
    #根据余数求其校验码
def hanshu2(y):
    z=0
    if y==1:
        z=0
    elif y==2:
        z='x'
    elif y==3:
        z=9
    elif y==4:
        z=8
    elif y==5:
        z=7
    elif y==6:
        z=6
    elif y==7:
        z=5
    elif y==8:
        z=4
    elif y==9:
        z=3
    elif y==10:
        z=2
    else:
        z=1
    return z

for s in range(10000):
#输入身份证信息的前17位数字
    if cz==1:
        a=input('请输入第一位数字：')
        b=input('请输入第二位数字：')
        c=input('请输入第三位数字：')
        d=input('请输入第四位数字：')
        e=input('请输入第五位数字：')
        f=input('请输入第六位数字：')
        g=input('请输入第七位数字：')
        h=input('请输入第八位数字：')
        i=input('请输入第九位数字：')
        j=input('请输入第十位数字：')
        k=input('请输入第十一位数字：')
        l=input('请输入第十二位数字：')
        m=input('请输入第十三位数字：')
        n=input('请输入第十四位数字：')
        o=input('请输入第十五位数字：')
        p=input('请输入第十六位数字：')
        q=input('请输入第十七位数字：')
        z=hanshu(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q)
        print '校验码为',z
        cz=input('请输入想要进行的操作:')
    if cz==2:
        a=input('请输入第一位数字：')
        b=input('请输入第二位数字：')
        c=input('请输入第三位数字：')
        d=input('请输入第四位数字：')
        e=input('请输入第五位数字：')
        f=input('请输入第六位数字：')
        g=input('请输入第七位数字：')
        h=input('请输入第八位数字：')
        i=input('请输入第九位数字：')
        j=input('请输入第十位数字：')
        k=input('请输入第十一位数字：')
        l=input('请输入第十二位数字：')
        m=input('请输入第十三位数字：')
        n=input('请输入第十四位数字：')
        o=input('请输入第十五位数字：')
        p=input('请输入第十六位数字：')
        q=input('请输入第十七位数字：')
        y=hanshu(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q)
        s8=input('请输入第十八位数字：')
        z=hanshu2(y)
        if s8==z:
            print 'True'
        else:
            print 'False'
        cz=input('请输入想要进行的操作:')
    if cz==3:
        print '制作人员及其名单：：'
        print '收集数据，设计及编写代码：齐佳民'
        print '撰写报告及答辩：王大勇'
        cz=input('请输入想要进行的操作:')
    else:
        break



