if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = []
    for i in range(0, x+1, 1):
        for j in range(0, y+1, 1):
            for k in range(0, z+1, 1):
                if not i+j+k == n:
                    list.append([i, j, k])
    print(list)
