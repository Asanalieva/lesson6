import random

def a_plus_b(a, b, c):
     print(a + b * c)
a_plus_b(2, 2, 2)
a_plus_b(4, 4, 4)
a_plus_b(8, 8, 8)
a_plus_b(1000, 1000, 1000)

def pojalet_temirlana():
     num1 = random.randint(1, 10)
     num2 = random.randint(1, 10)
     result = int(input(f"Guess sum of {num1}*{num2}"))
     if result == num2 * num1:
          print("Oook")
     elif result - 5 <= num2 * num1 <= result + 5:
          print('Mimo')
     else:
          print('Sorry, not your day')

def kick_player(name):
     if name == 'Temirlan':
          print("Temirlan can't get in!!!")
     else:
          print(f"{name} can!")

def  main():
     for i in range(3):
          name = input('Enter a name! ')
          kick_player(name)
          pojalet_temirlana()
main()

