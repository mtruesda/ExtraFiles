# this I've actually seen in leetcode and answered before

def countUniqueCharacters(stri):
    seen = set()
    counter = 0
    for i in stri:
        if i not in seen:
            seen.add(i)
            counter += 1
    return counter

# unit test would've been more proper but this works
def main():
    print(countUniqueCharacters("hi there")) # almost thought this broke it, space counts as a char.
    print(countUniqueCharacters("hello"))
    print(countUniqueCharacters("xyzzy"))
    print(countUniqueCharacters("abcdefffffffaaaaabbbbccccdddd"))

main()