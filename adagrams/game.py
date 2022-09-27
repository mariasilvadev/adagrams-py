import copy

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}


def draw_letters():
    import random
    list_of_all_letter = []
    for key, value in LETTER_POOL.items():
        for i in range(value):
            list_of_all_letter.append(key)

    ten_letters = []
    for i in range(10):
        ten_letters.append(list_of_all_letter.pop(random.randrange(0, len(list_of_all_letter))))
    
    return ten_letters


def uses_available_letters(word, letter_bank):
    copy_bank = copy.deepcopy(letter_bank)
    word = word.upper()
    for char in word:
        if char in copy_bank:
            copy_bank.remove(char)
            
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
