import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open('dict.txt', 'r') as file:
    word_list = [line.strip() for line in file if line.strip()]

word_list = [word.lower() for word in word_list]

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

unique_word_list = list(dict.fromkeys(word_list))
deduped_word_list = remove_duplicates(word_list)

first_letter_count = {}
for letter in alphabet:
    first_letter_count[letter] = sum(1 for word in word_list if word.startswith(letter))

print(alphabet)
time.sleep(2)
print(word_list)
time.sleep(2)
print(unique_word_list)
time.sleep(2)
print(deduped_word_list)
# print(first_letter_count)