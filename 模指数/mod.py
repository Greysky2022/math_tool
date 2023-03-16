def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result


b = int(input("请输入底数\n"))
e = int(input("请输入指数\n"))
m = int(input("请输入模数\n"))
x = fastExpMod(b,e,m)
print(x)