import random

print("🎯 Гра: Вгадай число від 1 до 10!")

number = random.randint(1, 10)  # загадуємо число

while True:
    guess = int(input("Введи своє число: "))

    if guess == number:
        print("✅ Вітаю, ти вгадав число!")
        break  # вихід із циклу
    else:
        print("❌ Невірно, спробуй ще раз!")

print("Дякую за гру 😊")
