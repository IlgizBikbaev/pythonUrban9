def all_variants(text):
  word_line = len(text)
  word_list = [text[k:j+1] for k in range(word_line) for j in range(k, word_line)]
  word_list.sort(key=lambda item:(len(item), item))
  for word in word_list:
      yield word


a = all_variants("abс")
for i in a:
  print(i)
