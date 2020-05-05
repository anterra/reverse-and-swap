
def reverse_words_order_and_swap_cases(sentence):
    original_list = sentence.split()
    new_order_list = original_list[::-1]
    swapped_list = []
    for word in new_order_list:
        for letter in word:
            if letter.islower():
                new_letter = letter.upper()
                new_word = word.replace(letter, new_letter)
                word = new_word
                print(word)
            elif letter.isupper():
                new_letter = letter.lower()
                new_word = word.replace(letter, new_letter)
                word = new_word
                print(word)
        swapped_list.append(new_word)
    empty_string = " "
    result_string = empty_string.join(swapped_list)
    return result_string


sentence = input("write something ")
result = reverse_words_order_and_swap_cases(sentence)
print(result)

