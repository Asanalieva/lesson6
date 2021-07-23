import random
try:
    def guess():
        integers = random.randint(1,50)
        user_input = int(input('Guess the number from 1 to 50 '))
        if user_input == integers:
            print('Woha, you are cool!')
        elif user_input - 1 == integers or user_input + 1 == integers:
            print('Pochti!')
        else:
            print("Sorry,you didn't guess")
    def main():
        for i in range(n):
            guess()
    n = int(input('How many rounds do you want to play? '))
    main()
except:
    print('Error') #srting etc will be error