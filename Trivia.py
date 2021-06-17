question1 = 'Enter Your question here'
question2 = 'Enter Your question here'
question3 = 'Enter Your question here'
question4 = 'Enter Your question here'
question5 = 'Enter Your question here'

ans5 = 'Enter Your answer here'
ans1 = 'Enter Your answer here' 
ans2 = 'Enter Your answer here'
ans3 = 'Enter Your answer here'
ans4 = 'Enter Your answer here'


score = 0

print(question1)
answer = input('Enter answer: ')
if answer == ans1:
        score += 1
        print('Correct! \n')

if answer != ans1:
        print('Wrong, The correct answer is',ans1, '\n')


print(question2)
answer = input('Enter answer: ')

if answer == ans2:
        score += 1
        print('Correct! \n')

if answer != ans2:
        print('Wrong, The correct answer is',ans2, '\n')


print(question3)
answer = input('Enter answer: ')

if answer == ans3:
        score += 1
        print('Correct! \n')

if answer != ans3:
        print('Wrong, The correct answer is', ans3, '\n')


print(question4)
answer = input('Enter answer: ')

if answer == ans4:
        score += 1
        print('Correct! \n')

if answer != ans4:
        print('Wrong, The correct answer is',ans4, '\n')


print(question5)
answer = input('Enter answer: ')

if answer == ans5:
        score += 1
        print('Correct! \n')

if answer != ans5:
        print('Wrong, The correct answer is',ans5, '\n')

print("You scored", score,'out of 5')