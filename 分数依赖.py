def 最大公因数(a,b) :
    bI = max(a,b)
    sM = min(a,b)
    if bI % sM == 0 :
        return sM 
    return 最大公因数(bI % sM,sM)

def 最小公倍数(a,b) :
    oA = a*b
    oB = 最大公因数(a,b)
    return oA / oB