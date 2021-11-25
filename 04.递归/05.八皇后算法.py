def mat(n):
    place = [0 for i in range(n)] # # 表示第几行放在第几列，例如place[0] = 1, place[1] = 3
    flag = [0 for i in range(n)] # # 表示第n列被标记，比如第一列被标记 flag[1] = 1
    d1 = [0 for i in range(2*n - 1)] # 表示上对角线是否被标记，d[0+1] = 1
    d2 = [0 for i in range(2*n - 1)] # 表示下对角线是否被标记
    return place,flag,d1,d2

def print_mat(place,n):
    for i in range(n):
        for j in range(n):
            if place[i] == j:
                print("*",end=' ')
            else:
                print("-",end=' ')
        print()
    print()

def queen(row,n,place,flag,d1,d2):
    global count
    for col in range(n):
        if flag[col] == 0 and d1[row+col] == 0 and d2[row-col+n-1] == 0:
            place[row] = col
            flag[col] = 1
            d1[row+col] = 1
            d2[row-col+n-1] = 1
            if row < n - 1:
                queen(row+1,n,place,flag,d1,d2)
            else:
                count += 1
                print_mat(place,n)
            """ 这里是回溯，例如第三行不符合条件，则返回第二行，然后重新选择第二行的点 """
            flag[col] = 0
            d1[row + col] = 0
            d2[row - col + n - 1] = 0

if __name__ == "__main__":
    count = 0
    n = int(input("请输入："))
    place,flag,d1,d2 = mat(n)
    queen(0, n, place, flag, d1, d2)
    print(f"一共有{count}种可能")