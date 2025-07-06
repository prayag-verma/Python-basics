
def find_and_sort_intervals(intervals):
    
    # Step 1: Firstly, map each start point to its corresponding interval
    interval_map = {start: (start, end) for start, end in intervals}

    # Step 2: Then, identifying all end points from the intervals
    end_points = {end for _, end in intervals}

    # Step 3: Next, finding out the actual starting point (not present in any end)
    start_point = None
    for start, _ in intervals:
        if start not in end_points:
            start_point = start
            break

    if start_point is None:
        raise ValueError("No unique starting point found in the interval list.")

    # Step 4: Now, following the loop of intervals in order
    sorted_intervals = []
    while start_point in interval_map:
        current = interval_map[start_point]
        sorted_intervals.append(current)
        start_point = current[1]

    return sorted_intervals


# Finally, let's call the function 'find_and_sort_intervals' and run the code:
if __name__ == "__main__":
    intervals_input = [(5, 7), (15, 29), (7, 9), (1, 5), (12, 15), (29, 34), (9, 12)]
    result = find_and_sort_intervals(intervals_input)
    print(f"Output: {result}")


