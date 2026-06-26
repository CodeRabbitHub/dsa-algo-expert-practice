def maximum_subarray_sum(nums: list[int], k: int) -> int:
    """
    Find the maximum subarray sum of all subarrays of nums of length k with distinct elements.
    
    Time Complexity: O(len(nums))
    Space Complexity: O(k) since the dictionary holds at most k elements.
    """
    if len(nums) < k:
        return 0
        
    element_counts = {}
    current_sum = 0
    max_sum = 0
    
    # Initialize the first window of size k
    for i in range(k):
        val = nums[i]
        element_counts[val] = element_counts.get(val, 0) + 1
        current_sum += val
        
    if len(element_counts) == k:
        max_sum = current_sum
        
    # Slide the window
    for left in range(1, len(nums) - k + 1):
        # Remove the outgoing element at nums[left - 1]
        outgoing_val = nums[left - 1]
        element_counts[outgoing_val] -= 1
        if element_counts[outgoing_val] == 0:
            del element_counts[outgoing_val]
        current_sum -= outgoing_val
        
        # Add the incoming element at nums[left + k - 1]
        incoming_val = nums[left + k - 1]
        element_counts[incoming_val] = element_counts.get(incoming_val, 0) + 1
        current_sum += incoming_val
        
        # Check if all elements in current window are distinct
        if len(element_counts) == k:
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum

if __name__ == '__main__':
    # Test cases
    print("Running tests for Maximum Sum of Distinct Subarrays With Length K...")
    
    # Example 1
    assert maximum_subarray_sum([1, 5, 4, 2, 9, 9, 9], 3) == 15, "Failed Example 1"
    
    # Example 2
    assert maximum_subarray_sum([4, 4, 4], 3) == 0, "Failed Example 2"
    
    # Custom test cases
    assert maximum_subarray_sum([1, 2, 3, 4, 5], 3) == 12, "Failed Custom 1: all distinct array"
    assert maximum_subarray_sum([1, 1, 1, 2, 3, 1], 3) == 6, "Failed Custom 2: duplicates before distinct subarray"
    assert maximum_subarray_sum([1, 2, 2, 3, 4], 3) == 9, "Failed Custom 3: duplicates in middle"
    assert maximum_subarray_sum([1, 2], 3) == 0, "Failed Custom 4: nums length less than k"
    
    print("All tests passed successfully!")
