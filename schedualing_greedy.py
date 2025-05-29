def read_jobs(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    n = int(lines[0])  # number of jobs
    jobs = []
    for line in lines[1:]:
        weight, length = map(int, line.strip().split())
        jobs.append((weight, length))
    return jobs

def compute_weighted_sum_by_difference(jobs):
    # Sort by (weight - length), break ties by weight
    jobs.sort(key=lambda x: (x[0] - x[1], x[0]), reverse=True)
    total_time = 0
    weighted_sum = 0
    for weight, length in jobs:
        total_time += length
        weighted_sum += weight * total_time
    return weighted_sum

def compute_weighted_sum_by_ratio(jobs):
    # Sort by (weight / length), ties handled arbitrarily
    jobs.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_time = 0
    weighted_sum = 0
    for weight, length in jobs:
        total_time += length
        weighted_sum += weight * total_time
    return weighted_sum

if __name__ == "__main__":
    filepath = "jobs.txt"
    jobs = read_jobs(filepath)

    # Strategy 1: Difference
    jobs_copy1 = jobs.copy()
    result_difference = compute_weighted_sum_by_difference(jobs_copy1)

    # Strategy 2: Ratio
    jobs_copy2 = jobs.copy()
    result_ratio = compute_weighted_sum_by_ratio(jobs_copy2)

    # Print results with comma separation
    print(f"Weighted sum by difference: {result_difference:,}")
    print(f"Weighted sum by ratio: {result_ratio:,}")
