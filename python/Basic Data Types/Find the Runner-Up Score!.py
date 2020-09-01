if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max_score, runner_up = [-100, -100]
    for i in range(0, n, 1):
        if arr[i] > max_score:
            runner_up = max_score
            max_score = arr[i]
        if arr[i] > runner_up and max_score > arr[i]:
            runner_up = arr[i]
    print(runner_up)

