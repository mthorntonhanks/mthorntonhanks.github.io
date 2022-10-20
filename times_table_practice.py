'''
To do
-----
Research best/latest string format method
Research best random integer method (randint?)
'''

import random

#Start off by asking just one question instead of 5

correct_score = 0
print('Welcome to the times table practice')

for question_number in range(1, 6):
    #Could ask user if they want easy or difficult mode (lower or higher numbers)
    a = random.randrange(13)
    b = random.randrange(13)

    print(f'Question {question_number} - what is {a} x {b}?')
    user_answer = input()

    if int(user_answer) == (a * b):
        #Could change the scores so that you get 10 points for a correct answer
        correct_score += 1
        print('Correct! :)')
    else:
        #Could tell the user the correct answer
        #Could change scores so you get points deducted for wrong answer
        print('Wrong! :(')

print(f'You scored {correct_score} out of 5')
if correct_score <= 1:
    print('Don''t give up the day job!')
elif correct_score <= 3:
    #Could change this to score == 1 or score == 2
    print('Could do better!')
elif correct_score == 4:
    print('Pretty good!')
elif correct_score == 5:
    #Could change this to 'else'
    print('Full marks!')

#Could ask user if they want to play again
#Could keep track of the highest score (and name)
