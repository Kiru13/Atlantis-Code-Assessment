from itertools import combinations


def search_vowel(s):
    """
    Searches vowel in string and length of consonants.
    Args:
        s (str) : input string
    Returns:
        tuple : tuple of vowel exists as boolean and length of consonants
    """
    vowels = 'aeiouAEIOU'
    consonants = 0
    result = False
    for ch in s:
        if ch in vowels:
            result = True
        else:
            consonants = consonants + 1
    return result, consonants


def pronuncible(string_combs):
    """
    Perform operation on string combinations and find pronuncible string
    Args:
        string_combs (list) : string combinations
    Returns:
        list : pronuncible string
    """
    pronuncible_str = []
    for i in range(len(string_combs)):
        is_vowel, consonants = search_vowel(string_combs[i])
        if is_vowel and consonants >= 2:
            pronuncible_str.append(string_combs[i])
    return pronuncible_str


if __name__ == '__main__':
    test_str = input("Enter string : ")
    string_combinations = [test_str[x:y] for x, y in combinations(
        range(len(test_str) + 1), r=2)]
    print(f'Output : {pronuncible(string_combinations)}')
