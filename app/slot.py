import random
import sys
import time
import os

print('Welcome to Leo\'s Casino!')
time.sleep(1)
print('Let\'s start with your first bet.')
time.sleep(1)

money = int(input('How much money did you bring today? $'))
odds1 = str(random.randint(82,98))
odds2 = str(random.randint(82,98))
odds3 = str(random.randint(82,98))

print(f'\nOkay, you bring ${money} dollars. Let\'s see how your bet goes...')
time.sleep(2)
    
flag = 'True'
while flag == 'True':
  go = input('Ready? (Type "y")\n')
  go = go.upper()
  
  if go == 'Y':
    #os.system('cls')
    print('\nTime to choose your machine')
    time.sleep(1)
    print('-Caça Níquel 1 - Odds', odds1 + '%')
    print('-Caça Níquel 2 - Odds', odds2 + '%')
    print('-Caça Níquel 3 - Odds', odds3 + '%')
    slot = int(input('Which Caça Níquel do you want to use? (1, 2, 3) '))
    if slot == 1:
      #os.system('clear')
      print('\nThis machine has 3 numbers. You win if match all 3. \nIf you match 2 numbers, don\'t lose any money. If you don\'t match any numbers, money goes to $0!')
      time.sleep(2)
      bet1 = int(input('\nHow much was your bet? $'))

#Slot 1 - 3numbers     
      if bet1 > money or bet1 < 0:
        sys.exit()    
      money = money - bet1
      num1 = str(random.randint(1,3))
      num2 = str(random.randint(1,3))
      num3 = str(random.randint(1,3))
      

      print('\nRolling!')
      time.sleep(2)
      print(f' -----\t-----\t-----\n'
            f' | {num1} |\t| {num2} |\t| {num3} |\n'
            f' ----- \t----- \t-----')
      time.sleep(1)
      

      if all(x == num1 for x in [num2, num3]):
        print('Congrats! 3 times your bet! $$$')
        win = bet1 * 3
        money = money + win
        print(f'\nNew balance:', money)
        if money == '0':
          sys.exit()

#Se pelo menos 2 números são iguais, faça algo
      elif sum(x == y for x, y in [(num1, num2), (num1, num3), (num2, num3),]) >= 2:
        print('Woah! Close One! You have been refunded!')
        win = bet1
        money = money + win
        print(f'\nNew balance:', money)
        if money == '0':
          sys.exit()
      else:
        print('Aww man! You lost!')
        print(f'\nNew balance:', money)
        if money == 0:
          sys.exit()

#Slot 2 - 4numbers
    elif slot == 2:
      #os.system('clear')
      print('\nThis slot machine has only 4 numbers. \nTo win you have to match all 4 numbers. \nIf you match 3 numbers, you don\'t lose any money. If you don\'t match any numbers, you lose all money!')
      time.sleep(2)
      bet2 = int(input('\nHow much was your bet? $'))

      if bet2 > money or bet2 < 0:
        sys.exit()
      money = money - bet2
      num1 = str(random.randint(1,4))
      num2 = str(random.randint(1,4))
      num3 = str(random.randint(1,4))
      num4 = str(random.randint(1,4))

      print('\nRolling!')
      time.sleep(2)
      print(f' -----\t-----\t-----\t-----\n'
            f' | {num1} |\t| {num2} |\t| {num3} |\t| {num4} |\n'
            f' ----- \t----- \t----- \t-----')
      time.sleep(1)

      if all(x == num1 for x in [num2, num3, num4]):
        print('Congrats! 4 times your bet! $$$')
        win = bet2 * 4
        money = money + win
        print(f'\nNew balance:', money)
        if money == '0':
          sys.exit()

# Se pelo menos três números são iguais, faça alguma coisa
      elif sum(x == y for x, y in [(num1, num2), (num1, num3), (num1, num4), (num2, num3), (num2, num4), (num3, num4)]) >= 3:
        print('Woah! Close One! You have been refunded!')
        win = bet2
        money = money + win
        print(f'\nNew balance:', money)
        if money == '0':
          sys.exit()
      else:
        print('Aww man! You lost!\n')
        print(f'\nNew balance:', money)
        if money == 0:
          sys.exit()


#Slot 3 - 5 numbers
    elif slot == 3:
      #os.system('clear')
      print('\nThis slot machine has only 5 numbers. \nTo win you have to match all 5 numbers. \nIf you match 4 numbers, you don\'t lose any money. If you don\'t match any numbers, you lose all money!')
      time.sleep(2)
      bet3 = int(input('\nHow much was your bet? $'))

      if bet3 > money or bet3 < 0:
       sys.exit()
      money = money - bet3
      num1 = str(random.randint(1,5))
      num2 = str(random.randint(1,5))
      num3 = str(random.randint(1,5))
      num4 = str(random.randint(1,5))
      num5 = str(random.randint(1,5))

      print('\nRolling!')
      time.sleep(2)
      print(f' -----\t-----\t-----\t-----\t-----\n'
            f' | {num1} |\t| {num2} |\t| {num3} |\t| {num4} |\t| {num5} |\n'
            f' ----- \t----- \t----- \t----- \t-----')
      time.sleep(1)
    
    if all(x == num1 for x in [num2, num3, num4, num5]):
        print('Congrats! 5 times your bet! $$$')
        win = bet3 * 5
        money = money + win
        print(f'\nNew balance:', money)
        if money == '0':
          sys.exit()

# Se pelo menos quatro números são iguais, faça alguma coisa
    elif sum(x == y for x, y in [(num1, num2), (num1, num3), (num1, num4), (num1, num5), (num2, num3), (num2, num4), (num2, num5), (num3, num4), (num3, num5), (num4, num5)]) >= 4:
      print('Woah! Close One! You have been refunded!')
      win = bet3
      money = money + win
      print(f'\nNew balance:', money)
      if money == '0':
        sys.exit()
    else:
      print('Aww man! You lost!\n')
      print(f'\nNew balance:', money)
      if money == 0:
        sys.exit()