import 分数依赖
def 减法(nb1,nb2) :
    nnb = int(nb1) - int(nb2)
    return nnb

def 分数相减(a1,a2,b1,b2) :
    o2 = 分数依赖.最小公倍数(a2,b2)
    na1 = o2 / a2 * a1
    nb1 = o2 / b2 * b1
    o1 = na1 - nb1
    return str(int(o2)) + "分之" + str(int(o1))