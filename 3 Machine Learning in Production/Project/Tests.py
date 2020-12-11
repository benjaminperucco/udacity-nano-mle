import numpy as np

word_list = [
	['apples', 'bananas', 'apples', 'tomatoes', 'tomatoes', 'tomatoes'],
	['apples', 'peaches', 'peaches', 'oranges', 'apples', 'apples', 'tomatoes'],
	['oranges', 'peaches']
]

added_word_list = []
for i in range(len(word_list)):
	added_word_list += word_list[i]

#print(added_word_list)

unique_words = sorted(set(added_word_list))
print(unique_words)

store_words = {}
for word in unique_words:
	store_words[word] = added_word_list.count(word)

print(store_words)

word_occurance = []
occurance_list = sorted(set(store_words.values()), reverse=True)
for i in occurance_list:
	for key, value in store_words.items():
		if value == i:
			word_occurance.append(key)

print(word_occurance)

dict_val = store_words.values()
dict_key = store_words.keys()

zipped_store_words = zip(dict_val, dict_key)
sorted_zipped_store_words = sorted(zipped_store_words, reverse=True)

word_occurance_2 = []
for i, j in sorted_zipped_store_words:
	word_occurance_2.append(j)

print(word_occurance_2)

word_occurance_2[:2]
