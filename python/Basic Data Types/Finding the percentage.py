if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    score_list = []
    sum = 0
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    for nam, scor in student_marks.items():
        if nam == query_name:
            score_list = scor
    for i in range(0, len(score_list), 1):
        sum += score_list[i]

    num = sum / len(score_list)
    formatted = "{:.2f}".format(num)
    print(formatted)

