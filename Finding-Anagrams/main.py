# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word) != len(anagram):
        return False
    else:
        for a in word:
            if a not in anagram:
                return False

    return True


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
print(find_anagram("listen", "silent"))
