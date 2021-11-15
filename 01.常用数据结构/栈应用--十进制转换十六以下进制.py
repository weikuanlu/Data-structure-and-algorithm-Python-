from stack import Stack
"""
利用栈 先进后出的性质，进行进制间的转换，
    可以将十进制数，任意转换至十六进制以内的进制的数
"""
def baseConverter(origin_num,base):
    digitals = '0123456789ABCDEF'
    a_stack = Stack() # 创建空栈

    while origin_num > 0: # 原数大于0的情况下，进行操作
        rem = origin_num % base # 求余数，并添加到栈中
        a_stack.push(rem)
        origin_num = origin_num // base

    new_string = ''
    while not a_stack.is_empty(): # 当栈不为空的时候，一直执行
        new_string = new_string + digitals[a_stack.remove()]
    return new_string

if __name__ == "__main__":
    result = baseConverter(240,16)
    print(result)
    print(type(result)) # str