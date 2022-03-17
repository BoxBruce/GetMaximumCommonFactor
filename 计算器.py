# -*- coding: utf-8 -*- 
import 加
import 减
import 乘
import 除
print("BBS软件提供")
print("BoxBruceSoft(c) 2021~2022")
print("作者邮箱:BoxBruce@outlook.com")
print("加请输入1 减请输入2 乘请输入3 除请输入4")
shuZe = input()

if shuZe == "1" :
    shuZe1 = input("普通请输入1 分数请输入2")
    if shuZe1 == "1":
        a = input("第一个数")
        b = input("第二个数")
        with open("得数.txt",'w') as file:
            oN = 加.加法(int(a),int(b))
            file.write(str(oN))

    elif shuZe1 == "2":
        a1 = input("第一个数分子")
        a2 = input("第一个数分母")
        b1 = input("第二个数分子")
        b2 = input("第一个数分母")
        with open("得数.txt",'w') as file:
            oN = 加.分数相加(int(a1),int(a2),int(b1),int(b2))
            file.write(str(oN))

    else :
        with open("得数.txt",'w') as file:
            file.write("error")

elif shuZe == "2" :
    shuZe1 = input("普通请输入1 分数请输入2")
    if shuZe1 == "1":
        a = input("第一个数")
        b = input("第二个数")
        with open("得数.txt",'w') as file:
            oN = 减.减法(int(a),int(b))
            file.write(str(oN))

    elif shuZe1 == "2":
        a1 = input("第一个数分子")
        a2 = input("第一个数分母")
        b1 = input("第二个数分子")
        b2 = input("第一个数分母")
        with open("得数.txt",'w') as file:
            oN = 减.分数相减(int(a1),int(a2),int(b1),int(b2))
            file.write(str(oN))

    else :
        with open("得数.txt",'w') as file:
            file.write("error")

elif shuZe == "3" :
    shuZe1 = input("普通请输入1 分数请输入2")
    if shuZe1 == "1":
        a = input("第一个数")
        b = input("第二个数")
        with open("得数.txt",'w') as file:
            oN = 乘.乘法(int(a),int(b))
            file.write(str(oN))

    elif shuZe1 == "2":
        a1 = input("第一个数分子")
        a2 = input("第一个数分母")
        b1 = input("第二个数分子")
        b2 = input("第一个数分母")
        with open("得数.txt",'w') as file:
            oN = 乘.分数相乘(int(a1),int(a2),int(b1),int(b2))
            file.write(str(oN))
    
    else :
        with open("得数.txt",'w') as file:
            file.write("error")
    
elif shuZe == "4" :
    shuZe1 = input("普通请输入1 分数请输入2")
    if shuZe1 == "1":
        a = input("第一个数")
        b = input("第二个数")
        try : 
            with open("得数.txt",'w') as file:
                oN = 除.除法(int(a),int(b))
                file.write(str(oN))
        except ZeroDivisionError :
                print("error")
                with open("得数.txt",'w') as file:
                    file.write("error")

    elif shuZe1 == "2":
        a1 = input("第一个数分子")
        a2 = input("第一个数分母")
        b1 = input("第二个数分子")
        b2 = input("第一个数分母")
        with open("得数.txt",'w') as file:
            oN = 除.分数相除(int(a1),int(a2),int(b1),int(b2))
            file.write(str(oN))
    else :
        with open("得数.txt",'w') as file:
            file.write("error")
else :
    with open("得数.txt",'w') as file:
        file.write("error")