word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import  random
def letter_counter(text,letter):
    total = 0
    for count in text:
        if letter in text:
            total +=1
        return(total)
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
word = random.choice(word_list)
blank =''
blank_list =[]
lives = 6
for i in range(len(word)):
    blank +="_"
    blank_list.append("_")
print("Our word is ", blank)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while "_" in blank_list:
    guess = input('What is the letter in this word? >> ').lower()
    blank_ans = ''
    if guess in word:
        print ("Correct! there is/are ", letter_counter(word,guess), "letter \"", guess, "\"in the word")
        for i in range(0, len(word)):
            if guess == word[i]:
                blank_list[i] = guess
        for i in blank_list:
            blank_ans += i
        print(blank_ans)
    else:
        print ("Incorrect!")
        print(f"You have {lives-1} lives left")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            break
if lives == 0:
    print("*****Too bad, you man is now hung up T.T******")
else:
    print("*****Congrats, you saved your man******")


