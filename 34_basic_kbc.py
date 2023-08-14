'''
This game is not 100% current bcoz many more changes can be done in future. 
'''
questions = [["Which of the following corresponds to ‘ek bataa do’?","Pura", "Sawa", "Adha", "Pauna","None",3],
["In the game of ludo the discs or tokens are of how many colours?","Four", "One", "Two", "Three","None",1],
["Which of these terms can only be used for women?","Dirghaayu", "Suhagan", "Chiranjeevi", "Sushil","None",2],
["Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving two girls from drowning?","Anandiben Patel", "Vasundhara Raje Scindia", "Uma Bharti", "Mamata Banerjee","None",1],
["Where was the BRICS summit held in 2014?","Brazil", "India", "Russia", "China","None",1],
["Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?","P.B. Shelley", "Alfred Tennyson", "W.B. Yeats", "T.S. Elliot","None",3],
["Which of these sports requires you to shout out a word loudly during play?","Ludo", "Kho-kho", "Playing cards", "Chess","None",2],
["Which of these spices is the smallest in size?","Ajwain", "Jeera", "Saunf", "Methi Seeds","None",1],
["In which of these two sports is the term ‘free hit’ used?","Football, Squash", " Badminton, Tennis", " Badminton, Cricket", "Hockey, Cricket","None",4],
["Which of these medical conditions is most likely to cause dehydration?","Malaria", "Tetanus", "Diarrhoea", " Beriberi","None",3],
["Which of these countries is larger than India in territorial space?","Australia", "Argentina", "Kazakhstan", "UAE","None",1],
["Which of these battles didn’t involve the Mughal army?","Battle of Buxar", "Battle of Haldighati", "Second battle of Panipath", "Third battle of Panipath","None",4],
["About whom did the poet write,” Lakshmi thi yaa Durga thi woh swayam veerta ki avatar, dekh marathe pulkit hote uski talwaaroke ke waar?”","Rani Durgavati", "Jhansi ki rani", "Rani Ahilyabai Holkar", " Rani Padmavati","None",2],
["Which queen did Draupadi,the wife of five pandavas, serve in the guise of Sairandhri for one year?","Sanjana", "Satyavati", "Satyabhama", "Sudeshna","None",4]]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000,1250000,25000000,5000000,10000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"(A) {question[1]}   (B) {question[2]} ")
  print(f"(C) {question[3]}   (D) {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    if (i >= 4):
      money = 0
      break
    else:
      money = levels[i-1]
      break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")