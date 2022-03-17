# -*- coding: utf-8 -*- 
import 分数依赖

def 乘法(nb1,nb2) :
    nnb = int(nb1) * int(nb2)
    return nnb

def 分数相乘(a1,a2,b1,b2) :
    #1是分子，2是分母
    o1 = 乘法(a1,b1)
    o2 = 乘法(a2,b2)
    nd = 分数依赖.最大公因数(o1,o2)
    n1 = o1 / nd
    n2 = o2 / nd
    return str(int(n2)) + "分之" + str(int(n1))
