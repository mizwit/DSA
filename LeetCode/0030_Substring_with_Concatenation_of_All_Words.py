class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        str_len, word_count, word_len = len(s), len(words), len(words[0])
        if str_len < word_count * word_len: return []

        full_map = {}
        for word in words: full_map[word] = full_map.get(word, 0) + 1

        res = []
        for i in range(word_len):
            cur_map = {"counter": 0}
            start, end = i, i
            while end < str_len:
                word = s[end: end + word_len]
                
                # if word in full_map, keep moving from end and incrementing counter
                if full_map.get(word, None):
                    cur_map[word] = cur_map.get(word, 0) + 1
                    cur_map["counter"] += 1
                    end += word_len

                    # if word occurs more than full_map, keep shrinking from start till it does not
                    while cur_map[word] > full_map[word]:
                        cur_map[s[start: start + word_len]] -= 1
                        cur_map["counter"] -= 1
                        start += word_len
                    
                    # if word count in cur_map same as full_map, save the start index
                    if cur_map["counter"] == word_count: res.append(start)

                # if word not in full_map, reset the whole window  
                else:
                    cur_map = {"counter": 0}
                    end += word_len
                    start = end
        return res