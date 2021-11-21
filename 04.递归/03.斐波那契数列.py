"""
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
在数学上，费波那契数列是以递归的方法来定义：
                                    F0 = 0 (n=0)
                                    F1 = 1 (n=1)
                                    Fn = F[n-1]+ F[n-2](n=>2)
"""
# -*- coding=utf-8 -*-
def Fibo(n):
    if n < 2:
        return 0 if (n==0) else 1
    else:
        return Fibo(n-1) + Fibo(n - 2)

if __name__ == "__main__":
    result = Fibo(12)
    print(result)