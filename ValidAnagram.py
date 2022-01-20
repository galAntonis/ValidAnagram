#Valid anagram problem
#Time Complexity: O(n)
#Space Complexity: O(n)


def anagrams(s1,s2):
    # We make two hash tables to store the frequence of characters in our strings
    # This is dump, we can use Counter from collection to solve this problem but why not use a hash table

    if len(s1) != len(s2):
        return False
    frequence1 = {}
    frequence2 = {}
    for ch in s1:
        if ch in frequence1:
            frequence1[ch]+=1
        else:
            frequence1[ch]=1
    for ch in s2:
        if ch in frequence2:
            frequence2[ch]+=1
        else:
            frequence2[ch]=1
    for key in frequence1:
        if key not in frequence2 or frequence1[key]!=frequence2[key]:
            return False
    return True

def main():
    # We use only lowercase strings to avoid confusion
    s1 = input("Enter a string: ")
    s1 = s1.lower()
    s2 = input("Enter an anagram of this string: ")
    s2 = s2.lower()
    
    if anagrams(s1,s2):
        print("The second word is a valid anagram of the first one")
    else:
        print("The second word is NOT a valid anagram of the first one")

main()

