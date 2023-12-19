def count_vowels_consonants_spaces(s):
    vowels = 0
    consonants = 0
    spaces = 0
    s = s.lower()

    for char in s:
        if char in "aeiou":
            vowels += 1
        elif 'a' <= char <= 'z':
            consonants += 1
        elif char == " ":
            spaces += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("White spaces:", spaces)


# Test cases
string1 = "Take u forward is Awesome"
count_vowels_consonants_spaces(string1)

string2 = "India won the cricket match"
count_vowels_consonants_spaces(string2)
