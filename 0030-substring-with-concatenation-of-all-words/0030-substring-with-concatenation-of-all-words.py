class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:


        if not s or not words:
            return []

        # 1. Compute basic lengths and counts
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        # 2. Build a frequency map word_count from the words array
        word_count = Counter(words)
        
        # 3. Initialize an empty result list
        result = []
        
        # 4. Iterate over each starting offset i from 0 to word_len - 1
        for i in range(word_len):
            # 5. Set left, right, and create an empty counter seen
            left = i
            right = i
            seen = Counter()
            
            # 6. While right + word_len does not exceed the length of s
            while right + word_len <= len(s):
                # Extract the word and advance right
                word = s[right:right + word_len]
                right += word_len
                
                # 7. If the extracted word exists in word_count
                if word in word_count:
                    seen[word] += 1
                    
                    # Advance left repeatedly until the overcount is resolved
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        
                # 8. If the extracted word does not exist in word_count
                else:
                    seen.clear()
                    left = right
                    
                # 9. Check if right - left equals total_len
                if right - left == total_len:
                    result.append(left)
                    
        # 10. After all offsets are processed, return the result list
        return result


            
            