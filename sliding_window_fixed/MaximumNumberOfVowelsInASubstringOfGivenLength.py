def max_vowels(s: str, k: int) -> int:
    """
    Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

    Time Complexity: O(len(s))
    Space Complexity: O(1) since the set of vowels is of constant size (5 vowels).
    """
    vowels = {"a", "e", "i", "o", "u"}

    # Calculate vowels in the first window of size k
    current_vowels = sum(1 for i in range(k) if s[i] in vowels)
    max_vowels_count = current_vowels

    # If the first window already has the maximum possible vowels, we can return early
    if max_vowels_count == k:
        return k

    # Slide the window
    for left in range(1, len(s) - k + 1):
        # Remove outgoing character at s[left - 1]
        if s[left - 1] in vowels:
            current_vowels -= 1

        # Add incoming character at s[left + k - 1]
        if s[left + k - 1] in vowels:
            current_vowels += 1

        if current_vowels > max_vowels_count:
            max_vowels_count = current_vowels
            # Optimization check: cannot have more than k vowels
            if max_vowels_count == k:
                return k

    return max_vowels_count


if __name__ == "__main__":
    # Test cases
    print(
        "Running tests for Maximum Number of Vowels in a Substring of Given Length..."
    )

    # Example 1
    assert max_vowels("abciiidef", 3) == 3, "Failed Example 1"

    # Example 2
    assert max_vowels("aeiou", 2) == 2, "Failed Example 2"

    # Example 3
    assert max_vowels("leetcode", 3) == 2, "Failed Example 3"

    # Custom test cases
    assert max_vowels("bcdfg", 2) == 0, "Failed Custom 1: all consonants"
    assert max_vowels("aeiouaeiou", 5) == 5, "Failed Custom 2: all vowels matching k"
    assert max_vowels("work", 4) == 1, "Failed Custom 3: exact match with k"

    print("All tests passed successfully!")
