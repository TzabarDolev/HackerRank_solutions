def split_and_join(line):
    line.split(' ')
    newline = ""
    for i in line:
        if i==" ":
            newline += '-'
        else:
            newline += i
    return newline

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

