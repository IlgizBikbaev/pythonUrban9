def all_variants(text):
  word_line = len(text)
  for k in range(word_line):
      for j in range(k, word_line):
          yield text[k:j+1]


a = all_variants("abс")
for i in a:
  print(i)
