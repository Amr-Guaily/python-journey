import random

def sort(list):
    # Base case
    if (len(list) < 2): return list

    pivot = random.choice(list)

    less = [x for x in list if x < pivot]
    greater = [x for x in list if x > pivot]

    print(f"less: {less}")
    print(f"greater: {greater}")

    return sort(less) + [pivot] + sort(greater)

print(f"sorted list: {sort([10, 5, 2, 3])}")    