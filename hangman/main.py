import random
from hangman_art import logo, stage
from hangman_words import word_list


print(logo)

choosen_word = random.choice(word_list)
count = 0
lives = 6
word = []

for letter in choosen_word:
  word+="_"
while count<len(choosen_word) and lives>=0:
  guess = input("guess a letter").lower()
  flag = False
  if guess in word:
      print("word already entered")
  for position in range(len(choosen_word)): 
    letter = choosen_word[position]
    if guess == letter:
      count+=1
      word[position]=guess
      flag = True

  print(word)
  if not flag:
    print(stage[lives])
    print("letter not in word")
    lives-=1

if lives<0:  
  print("u lose")
else:
  print("u win")
