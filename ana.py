#Given two strings, return true if they are anagrams of eachother, and false otherwise.
s1 = "anagram"
t1 = "nagaram"
# Output:
# True
s2 = "rat"
t2 = "car"
#Output:
# False

# Solution in Python # 

dict = {}
dict2 ={}
def a(s1, t1):
    for letter in s1:
        if dict.get(letter):
            dict[letter] += 1
        else:
            dict[letter] = 1
    print(dict)
    for letter in t1:
        if dict2.get(letter):
            dict2[letter] += 1
        else:
            dict2[letter] = 1
    print(dict2)
    return dict == dict2
print(a(s2,t2))

