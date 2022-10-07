# Write your code here :-)
import random
import time
import urllib.request
word_list = []
url = "https://raw.githubusercontent.com/Kinkelin/WordleCompetition/main/data/official/shuffled_real_wordles.txt"
file = urllib.request.urlopen(url)
next(file)
for line in file:
	decoded_line = line.decode("utf-8")
	word_list.append(decoded_line)
selected_word = random.choice(word_list)
guess_list = []
url = "https://raw.githubusercontent.com/Kinkelin/WordleCompetition/main/data/official/combined_wordlist.txt"
file = urllib.request.urlopen(url)
for guess_lines in file:
  decode_line = guess_lines.decode("utf-8")
  guess_list.append(decode_line)
guesses = 6
count = 0
for i in range(guesses): 
  print("Guess",i+1)
  word = input("Word: ")
  word = word.lower()
  while len(word) != 5:
    word = input("Please re-enter word again: ")
  while (word+"\n") not in guess_list:
    print("Not in word list")
    word = input("Please re-enter word again: ")
  for letters in word:
    if letters == selected_word[count]: 
      print("🟩 ",end="")
    elif letters in selected_word: 
      print("🟨 ",end="")
    else: 
      print("🟥 ",end="")
    count += 1
  print()
  count = 0
  if word in selected_word:
    print("\nBrilliant!")
    
    break
  else:
    print()
print("The word is:",selected_word)
