import time

def countdown_timer(seconds):
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer = f"{minutes:02d}:{secs:02d}"
        print(timer, end="\r")  # Выводим на одной строке
        time.sleep(1)  # Ждём 1 секунду
        seconds -= 1

    print("Время вышло!")


if __name__ == "__main__":
    print("Добро пожаловать в программу обратного отсчёта!")
    user_input = int(input("Введите время для обратного отсчёта в секундах: "))
    #countdown_timer(user_input)