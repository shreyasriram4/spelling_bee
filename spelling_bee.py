from itertools import product
from english_words import get_english_words_set

def all_permutations(letters, specific_letter):
    result = list()
    letters.append(specific_letter)
    for r in range(4, 10):
        for combo in product(letters, repeat=r):
            combo_str = ''.join(combo)
            if specific_letter in combo:
                result.append(combo_str)
    return result

def get_possible_words(letters, specific_letter, eng_words=get_english_words_set(['web2'], lower=True)):
    words = []
    permutations = all_permutations(letters, specific_letter)
    for word in permutations:
        if word in eng_words:
            words.append(word)
    return words