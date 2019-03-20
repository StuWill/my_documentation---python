# Vowel checker
def anti_vowel(text):
  vowels = "AEIOUaeiou"
  new_text = ""
  for letter in text:
    if letter not in vowels:
      new_text += letter
  return new_text

# Censor string of a word
def censor(text, word):
  texts = text.split()
  for i in range(len(texts)):
    if word == texts[i]:
      texts[i] = "*" * (len(word))
  return " ".join(texts)

# Remove duplicates
def remove_duplicates(lst):
  new_lst = []
  for i in range(len(lst)):
    if lst[i] not in new_lst:
      new_lst.append(lst[i])
  return new_lst

# lambda functions
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print (filter(lambda x: x == "Python", languages)) # prints ["Python"]
