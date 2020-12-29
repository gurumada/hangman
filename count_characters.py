from collections import defaultdict
from collections import Counter


def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    print(count_dict)


count_characters("Dynasty")


def count_characters2(string):
    count_dict = defaultdict(int)
    for c in string:
        count_dict[c] += 1

    print(count_dict)


count_characters2("Dynasty")

print(Counter("Dynasty"))
