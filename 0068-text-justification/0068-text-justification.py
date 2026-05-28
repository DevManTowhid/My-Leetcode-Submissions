class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        curr_line = []
        curr_length = 0 # Tracks length of characters only (no spaces)
        
        for word in words:
            # Check if adding this word + minimum required spaces exceeds maxWidth
            # len(curr_line) represents the minimum 1 space between existing words
            if curr_length + len(curr_line) + len(word) > maxWidth:
                
                # Number of gaps between words
                gaps = len(curr_line) - 1
                
                # Edge Case 1: Only one word on the line
                if gaps == 0:
                    res.append(curr_line[0] + ' ' * (maxWidth - curr_length))
                
                # Normal Case: Fully justify the line
                else:
                    total_spaces = maxWidth - curr_length
                    base_spaces = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    
                    line = ""
                    for i in range(gaps):
                        line += curr_line[i]
                        # Add base spaces + 1 extra if this gap gets a remainder space
                        line += ' ' * (base_spaces + (1 if i < extra_spaces else 0))
                        
                    # Add the very last word of the line
                    line += curr_line[-1]
                    res.append(line)
                    
                # Reset tracking variables for the new line
                curr_line = []
                curr_length = 0
                
            # Add the current word to the working line
            curr_line.append(word)
            curr_length += len(word)
            
        # Edge Case 2: The Last Line (Left justified, padded to the right)
        last_line = ' '.join(curr_line)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res