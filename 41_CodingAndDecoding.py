import random 
import string
def random_words(length): # using this function random letters of any length can be generated.
  return "".join(random.choice(string.ascii_lowercase) for x in range(length))
message = input("Enter the message: ")
words = message.split(" ")
choice = input("Press 1 for Coding or Press 0 for Decoding: ")
coding = True if (choice=="1") else False
print(coding)
if(coding): # coding = True. For coding purpose this if statement will be executed.
  new_words = []
  for word in words:
    if(len(word)>=3): # length of word is more or equal to 3 then the if statement will be executed or else will be
      r1 = random_words(3)
      r2 = random_words(3)
      new_message = r1 + word[1:] + word[0] + r2 # 3 random letters are added at start and at end, 1 letter of word is 
      # placed at the end of word.
      new_words.append(new_message) # this new message will be added in new words list
    else:
      new_words.append(word[::-1]) # if word's length is lesser than 3 then it is simply reversed
  print(" ".join(new_words)) # list of words in new words will be joined together

else: # coding = False. For decoding purpose this else statement will be executed.
  new_words = []
  for word in words:
    if(len(word)>=3): # length of word is more or equal to 3 then the if statement will be executed or else will be
      new_message = word[3:-3] # 3 random letters are removed from start and end of word.
      new_message = new_message[-1] + new_message[:-1] #  last letter of word is removed and it is added remaing letters.
      new_words.append(new_message)
    else:
      new_words.append(word[::-1])# if word's length is lesser than 3 then it is simply reversed
  print(" ".join(new_words)) # list of words in new words will be joined together