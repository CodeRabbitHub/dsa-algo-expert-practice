def find_max_average(nums: list[int], k: int) -> float:
    """
    Find a contiguous subarray of size k that has the maximum average value, and return this value.
    
    Time Complexity: O(len(nums))
    Space Complexity: O(1)
    """
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

if __name__ == '__main__':
    # Test cases
    print("Running tests for Maximum Average Subarray I...")
    
    # Example 1
    assert abs(find_max_average([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-9, "Failed Example 1"
    
    # Example 2
    assert abs(find_max_average([5], 1) - 5.0) < 1e-9, "Failed Example 2"
    
    # Custom test cases
    assert abs(find_max_average([0, 4, 0, 3, 2], 1) - 4.0) < 1e-9, "Failed Custom 1"
    assert abs(find_max_average([-1], 1) - (-1.0)) < 1e-9, "Failed Custom 2"
    
    print("All tests passed successfully!")
