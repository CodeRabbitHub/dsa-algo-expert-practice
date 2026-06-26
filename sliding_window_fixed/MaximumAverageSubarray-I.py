def find_max_average(nums, k):
    # Calculate the sum of first k elements
    current_sum = sum(nums[0:k])
    max_sum = current_sum
    # Sliding Window
    for left in range(1, len(nums) - k + 1):
        current_sum += nums[left + k - 1] - nums[left - 1]
        if current_sum > max_sum:
            max_sum = current_sum
    # Return the average
    return max_sum / k
