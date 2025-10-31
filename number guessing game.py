#numberguessinggame

import random
class guessinggame:
    def __init__(self,min_num=1,max_num=100,max_attempts=5):
        self.min_num=min_num
        self.max_num=max_num
        self.max_attempts=max_attempts 
        self.secret_number=random.randint(self.min_num,self.max_num) 
    def play(self):
        print(f'Welcome to the Guessing Game!🔢 You have {self.max_attempts} attempts to guess the number') 
    def get_user_guess(self):
        for value in range(0,self.max_attempts):
            guess=int(input(f'guess a number between {self.min_num} and {self.max_num} :'))
            if guess==self.secret_number:
                print(f'Congrats!🎉 You Guessed Correctly')
                break
            elif guess<self.secret_number:
                print("too low!📉")
            else:
                print("too high!📈")
        else:
            print(f'You have used all attempts ☹. The number was {self.secret_number} ')

    def run(self):
        while True:
            
            again =input("Play again? (YES/NO):   ")
            if again !="YES":
                print("thanks for playing!😊")
            break


gamer=guessinggame()
while True:
    q=input("Do you wanna play? \nYes/No:")
    if q=="Yes":
        gamer.play()
        gamer.get_user_guess()
        gamer.run()
            
            
    