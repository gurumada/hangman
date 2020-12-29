def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break

    return found


numbers = range(0, 100)
print(ss(numbers, 79))
print(ss(numbers, 409))
