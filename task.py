
# First Solution

original_text = input("Enter the sentence: ")
word_to_replace = input("Enter the word you want to replace: ")
replacement = input("Enter the word you want to add: ")

new_sentence= original_text.replace(word_to_replace, replacement)
print(new_sentence)


#---------------------second solution-------------------------------

# original_text = input("Enter the sentence: ")
# word_to_replace = input("Enter the word you want to replace: ")
# replacement = input("Enter the replacement word: ")

# def replace_word_in_sentence(sentence, word_to_replace, replacement):
#     modified_sentence = sentence.replace(word_to_replace, replacement)
#     return modified_sentence


# modified_result = replace_word_in_sentence(original_text, word_to_replace, replacement)
# print("Modified text:", modified_result)




sentence = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."

new_sentence = sentence.replace("dog", "cat")

print(f"Output: {new_sentence}")




