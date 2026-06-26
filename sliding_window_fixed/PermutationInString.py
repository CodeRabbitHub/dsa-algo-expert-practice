def check_inclusion(s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2, return True if s2 contains a permutation of s1,
    or False otherwise.
    
    Time Complexity: O(len(s2))
    Space Complexity: O(1) since the alphabet size is constant (26 lowercase English letters).
    """
    if len(s1) > len(s2):
        return False
        
    s1_count = {}
    s2_count = {}
    
    # Initialize the count dictionaries for s1 and the first window of s2
    for i in range(len(s1)):
        s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
        s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
    # If the first window matches, a permutation exists
    if s1_count == s2_count:
        return True
        
    # Slide the window across s2
    k = len(s1)
    for left in range(1, len(s2) - k + 1):
        # Remove the outgoing character at s2[left - 1]
        outgoing_char = s2[left - 1]
        s2_count[outgoing_char] -= 1
        if s2_count[outgoing_char] == 0:
            del s2_count[outgoing_char]
            
        # Add the incoming character at s2[left + k - 1]
        incoming_char = s2[left + k - 1]
        s2_count[incoming_char] = s2_count.get(incoming_char, 0) + 1
        
        # Check if current window's character frequencies match s1
        if s1_count == s2_count:
            return True
            
    return False

if __name__ == '__main__':
    # Test cases
    print("Running tests for Permutation in String...")
    
    # Example 1
    assert check_inclusion("ab", "eidbaooo") is True, "Failed Example 1"
    
    # Example 2
    assert check_inclusion("ab", "eidboaoo") is False, "Failed Example 2"
    
    # Custom test cases
    assert check_inclusion("adc", "dcda") is True, "Failed Custom 1: permutation with overlapping characters"
    assert check_inclusion("hello", "ooolleoooleh") is False, "Failed Custom 2: sub-anagram missing letters"
    assert check_inclusion("a", "ab") is True, "Failed Custom 3: single character match at start"
    assert check_inclusion("ab", "a") is False, "Failed Custom 4: s1 longer than s2"
    assert check_inclusion("abc", "bbbca") is True, "Failed Custom 5: permutation at the end"
    
    print("All tests passed successfully!")
