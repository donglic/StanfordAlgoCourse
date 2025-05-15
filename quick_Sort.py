def choose_pivot(A, l, r, rule):
    if rule == "first":
        return l
    elif rule == "last":
        return r
    elif rule == "median-of-three":
        mid = l + (r - l) // 2
        trio = [(A[l], l), (A[mid], mid), (A[r], r)]
        trio.sort(key=lambda x: x[0])
        return trio[1][1]  # Return the index of the median value
    else:
        raise ValueError("Unknown pivot rule: choose 'first', 'last', or 'median-of-three'")

def partition(A, l, r, rule):
    pivot_index = choose_pivot(A, l, r, rule)
    A[l], A[pivot_index] = A[pivot_index], A[l]  # Move pivot to front

    p = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1  # Final pivot index

def quicksort(A, l, r, rule):
    if l >= r:
        return 0

    comparisons = r - l
    pivot_index = partition(A, l, r, rule)
    comparisons += quicksort(A, l, pivot_index - 1, rule)
    comparisons += quicksort(A, pivot_index + 1, r, rule)

    return comparisons

def quicksort_with_comparisons(A, rule="first"):
    A_copy = A.copy()
    total_comparisons = quicksort(A_copy, 0, len(A_copy) - 1, rule)
    return A_copy, total_comparisons

if __name__ == "__main__":
    # Load data from text file
    with open("quick_sort_data.txt", "r") as f:
        data = [int(line.strip()) for line in f if line.strip().isdigit()]

    # Run QuickSort with different pivot rules
    rules = ["first", "last", "median-of-three"]
    for rule in rules:
        comparisons = quicksort_with_comparisons(data, rule)
        print(f"Pivot rule: {rule:<17} --> Total comparisons: {comparisons[1]}")
