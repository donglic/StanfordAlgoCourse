# Python program to Count Inversions in an array using merge sort

# This function merges two sorted subarrays arr[l..m] and arr[m+1..r]
# and also counts inversions in the whole subarray arr[l..r]
def merge_and_count(left, right):
    i = j = inv_count = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged += left[i:]
    merged += right[j:]
    return merged, inv_count

def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort_and_count(arr[:mid])
    right, inv_right = merge_sort_and_count(arr[mid:])
    merged, inv_split = merge_and_count(left, right)

    return merged, inv_left + inv_right + inv_split

def read_input_file(filepath):
    with open(filepath, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

if __name__ == "__main__":
    filepath = "array_data.txt"
    data = read_input_file(filepath)
    _, inversion_count = merge_sort_and_count(data)
    print(inversion_count)
