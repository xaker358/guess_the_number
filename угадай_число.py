import random

computer = random.randint(1, 100)
#print("Добро пожаловать в игру 'угадай число' )")
#number = int(input("Загадай число: "))

def play_game():
    print("Добро пожаловать в игру 'угадай число' )")
    number = int(input("Загадай число: "))
    
    if number < computer:
        print("Ваше число меньше загаданного")
        return play_game()
        
    elif number > computer:
        print("Ваше число больше загаданного")
        return play_game()
        
    elif number == computer:
        print("Поздравляю ты выиграл")
        return play_game()
    
play_game()
        
