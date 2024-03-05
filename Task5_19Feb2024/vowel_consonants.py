def count_vowel_consonants(S1):
    vowel_count = 0
    consonant_count = 0
    for i in S1:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
    return vowel_count, consonant_count


S1 = str(input("Enter a String"))
Count = count_vowel_consonants(S1)
print("Vowels count in given string is: ", Count[0])
print("Consonants count in given string is: ", Count[1])
