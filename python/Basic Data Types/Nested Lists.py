def order_list(unordered_list, unordered_names):
    ordered = True
    for i in range(0, len(unordered_list)-1, 1):
        if unordered_list[i] > unordered_list[i+1]:
            temp = unordered_list[i]
            unordered_list[i] = unordered_list[i+1]
            unordered_list[i+1] = temp
            temp = unordered_names[i]
            unordered_names[i] = unordered_names[i+1]
            unordered_names[i+1] = temp
            ordered = False
    if ordered == False:
        order_list(unordered_list, unordered_names)
    else:
        return unordered_list, unordered_names

def sort_alphabet(alphabet):
    ordered = True
    for i in range(0, len(alphabet)-1, 1):
        if alphabet[i] > alphabet[i+1]:
            temp = alphabet[i]
            alphabet[i] = alphabet[i+1]
            alphabet[i+1] = temp
            ordered = False
    if ordered == False:
        sort_alphabet(alphabet)
    else:
        for i in range(0, len(alphabet), 1):
            print(alphabet[i])

def get_lists():
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)
    return name_list, score_list

if __name__ == '__main__':
    name_list, score_list = get_lists()
    order_list(score_list, name_list)
    second_list = []
    alphabet = []
    min_score = min(score_list)
    for i in range(1, len(score_list), 1):
        if score_list[i] > min_score:
            second_list.append(score_list[i])
    second = min(second_list)
    for i in range(1, len(score_list), 1):
        if score_list[i] == second:
            alphabet.append(name_list[i])

    alphabet = sort_alphabet(alphabet)

