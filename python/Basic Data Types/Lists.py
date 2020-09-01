if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        x = input().split()
        action = x[0]
        if action == "insert":
            l.insert(int(x[1]), int(x[2]))
        if action == "print":
            print(l)
        if action == "append":
            l.append(int(x[1]))
        if action == "remove":
            l.remove(int(x[1]))
        if action == "sort":
            l.sort()
        if action == "pop":
            l.pop()
        if action == "reverse":
            l.reverse()

