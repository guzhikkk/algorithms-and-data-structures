word1 = input()
word2 = input()
dict1 = {}
dict2 = {}
for char in word1:
    dict1[char] = dict1.get(char, 0) + 1
for char in word2:
    dict2[char] = dict2.get(char, 0) + 1
if dict1 == dict2:
    print("YES")
else:
    print("NO")

