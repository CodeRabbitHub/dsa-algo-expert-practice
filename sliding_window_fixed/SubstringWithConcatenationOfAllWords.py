def find_substring(s: str, words: list[str]) -> list[int]:
    """
    Given a string s and an array of strings words, all of the same length, return the starting
    indices of all the concatenated substrings in s.
    
    Time Complexity: O(len(s) * word_len)
    Space Complexity: O(words.length * word_len) to store the word frequencies.
    """
    if not s or not words:
        return []
        
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    
    if len(s) < total_len:
        return []
        
    # Count frequency of each word in words
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
        
    result = []
    
    # We can run word_len separate sliding windows to cover all alignments
    for i in range(word_len):
        left = i
        curr_freq = {}
        count = 0
        
        for right in range(i, len(s) - word_len + 1, word_len):
            word = s[right:right+word_len]
            if word in word_freq:
                curr_freq[word] = curr_freq.get(word, 0) + 1
                count += 1
                
                # If we have a duplicate/over-limit word, shrink the window from the left
                while curr_freq[word] > word_freq[word]:
                    left_word = s[left:left+word_len]
                    curr_freq[left_word] -= 1
                    count -= 1
                    left += word_len
                    
                # If the current window matches all requirements
                if count == word_count:
                    result.append(left)
                    # Slide the window forward by one word
                    left_word = s[left:left+word_len]
                    curr_freq[left_word] -= 1
                    count -= 1
                    left += word_len
            else:
                # Word is not in target words, reset the window
                curr_freq.clear()
                count = 0
                left = right + word_len
                
    return result

if __name__ == '__main__':
    # Test cases
    print("Running tests for Substring with Concatenation of All Words...")
    
    # Example 1
    # Sorted because results can be returned in any order
    assert sorted(find_substring("barfoothefoobarman", ["foo", "bar"])) == [0, 9], "Failed Example 1"
    
    # Example 2
    assert sorted(find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])) == [], "Failed Example 2"
    
    # Example 3
    assert sorted(find_substring("barfoofoobarthefoobarman", ["bar", "foo", "the"])) == [6, 9, 12], "Failed Example 3"
    
    # Custom test cases
    assert sorted(find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])) == [8], "Failed Custom 1"
    assert sorted(find_substring("a", ["a"])) == [0], "Failed Custom 2: single char match"
    assert sorted(find_substring("ab", ["ab", "cd"])) == [], "Failed Custom 3: s shorter than total word length"
    
    print("All tests passed successfully!")
