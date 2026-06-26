def find_all_anagrams_in_a_string(s: str, p: str) -> list[int]:
    """
    Given two strings s and p, return an array of all the start indices of p's anagrams in s.
    
    Time Complexity: O(len(s))
    Space Complexity: O(1) since the alphabet size is constant (26 lowercase English letters).
    """
    if len(s) < len(p):
        return []
        
    p_count = {}
    s_count = {}
    
    # Initialize the count dictionaries for p and the first window of s
    for i in range(len(p)):
        p_count[p[i]] = p_count.get(p[i], 0) + 1
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        
    result = []
    # If the first window matches, add index 0
    if p_count == s_count:
        result.append(0)
        
    # Slide the window
    k = len(p)
    for left in range(1, len(s) - k + 1):
        # Remove the outgoing character at s[left - 1]
        outgoing_char = s[left - 1]
        s_count[outgoing_char] -= 1
        if s_count[outgoing_char] == 0:
            del s_count[outgoing_char]
            
        # Add the incoming character at s[left + k - 1]
        incoming_char = s[left + k - 1]
        s_count[incoming_char] = s_count.get(incoming_char, 0) + 1
        
        # Check if the frequencies match
        if p_count == s_count:
            result.append(left)
            
    return result

if __name__ == '__main__':
    # Test cases
    print("Running tests for Find All Anagrams in a String...")
    
    # Example 1
    assert find_all_anagrams_in_a_string("cbaebabacd", "abc") == [0, 6], "Failed Example 1"
    
    # Example 2
    assert find_all_anagrams_in_a_string("abab", "ab") == [0, 1, 2], "Failed Example 2"
    
    # Custom test cases
    assert find_all_anagrams_in_a_string("a", "b") == [], "Failed Custom 1: single character mismatch"
    assert find_all_anagrams_in_a_string("a", "a") == [0], "Failed Custom 2: single character match"
    assert find_all_anagrams_in_a_string("ab", "abc") == [], "Failed Custom 3: s shorter than p"
    
    print("All tests passed successfully!")