def subset_sum(nums, target):
    n = len(nums)
    # Initialize a table of size (n+1) x (target+1) with False
    # row 0 represents no items, col 0 represents sum of 0
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    # Base case: A sum of 0 is always possible (empty set)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the table
    for i in range(1, n + 1):
        current_val = nums[i-1]
        for j in range(1, target + 1):
            if j < current_val:
                # If current number is greater than the capacity, exclude it
                dp[i][j] = dp[i-1][j]
            else:
                # Use the recurrence: exclude OR include the item
                dp[i][j] = dp[i-1][j] or dp[i-1][j - current_val]

    # Result is in the bottom-right cell
    found = dp[n][target]
    
    # Backtracking to find the subset elements
    subset = []
    if found:
        curr_i, curr_j = n, target
        while curr_i > 0 and curr_j > 0:
            # If value came from the previous row, item wasn't used
            if dp[curr_i][curr_j] != dp[curr_i-1][curr_j]:
                subset.append(nums[curr_i-1])
                curr_j -= nums[curr_i-1]
            curr_i -= 1
            
    return found, subset

# Example usage from your slides:
numbers = [3, 2, 7, 1]
goal = 6
is_possible, result_set = subset_sum(numbers, goal)

print(f"Is sum {goal} possible? {is_possible}")
if is_possible:
    print(f"Subset: {result_set}")