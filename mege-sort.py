def sort(list):
    # Base case
    if (len(list) < 2):
         return list
    
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    left = sort(left)
    right = sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result += left[left_idx:]
    result += right[right_idx:]
    return result

print(f"sorted list: {sort([38, 27, 43, 3, 9, 82, 10])}")
print(f"sorted list: {sort([5.3, 27, 4.3, 31, 9.9, 8.2, 10])}")