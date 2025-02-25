



def sort(list):
    count = 0
    for i in range(1, 4):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            count +=1
            j -= 1
        list[j + 1] = key
    return list


list = [12, 11, 13, 5, 6]
print(sort(list))