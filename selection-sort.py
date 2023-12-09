def sort (list):
    for i in range (len(list) - 1):
        min_idx = i
        min_val = list[i]

        j = i + 1
        while j < len(list):
            if list[j] < min_val:
                min_val = list[j]
                min_idx = j
            j += 1

        # swap
        temp = list[i]
        list[i] = min_val
        list[min_idx] = temp

    print(f"sorted list: {list}")

sort([20, 12, 10, 15, 2])        
