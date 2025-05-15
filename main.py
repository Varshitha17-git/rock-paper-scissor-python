import random
rock='''   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# Paper
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
# Scissors
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
game_images=[rock,paper,scissors]
user_choice=int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n"))
print("your choice:")
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print("computer choice:")
print(game_images[computer_choice])
if user_choice==0 and computer_choice==2:
  print("you win!!")
if user_choice==2 and computer_choice==0:
    print("you lose!!")
if user_choice==1 and computer_choice==2:  
    print("you lose!!")
if user_choice==2 and computer_choice==1:
    print("you win!!")
if user_choice==0 and computer_choice==1:
    print("you lose!!")
if user_choice==1 and computer_choice==0:
    print("you win!!")
if user_choice==computer_choice:
    print("its a draw!!")
