import re


your_text = """В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку."""

cleaned_text = re.sub(r'[^\w\s]', '', your_text.lower())
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_common_words = []
for _ in range(10):
    if word_counts:
        max_word = max(word_counts, key=word_counts.get)
        most_common_words.append((max_word, word_counts[max_word]))
        del word_counts[max_word]
    else:
        break

print(most_common_words)
