def func(lists):
    count = 0
    for i in range(len(lists) - 1):
        for j in range(len(lists[i])):
            for k in range(len(lists[i + 1])):
                if lists[i][j] == lists[i + 1][k]:
                    count += 1
    return count
