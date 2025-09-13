s = input()
search_word = input()

max_idx = len(s)-len(search_word)+1
i = 0
res = 0
while i < max_idx:
    if s[i:i+len(search_word)] == search_word:
        i += len(search_word)
        res += 1
        continue
    i += 1

print(res)