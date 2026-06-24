import random
import os
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
while True:
    clear_screen()

    password_components = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    unique_components = "!@#$%^&*"
    
    print("======ГЕНЕРАТОР ПАРОЛЕЙ======")
    print("Для генерации нужно выбрать длину пароля")
    
    try:
        password_lenght = int(input("Введите длину пароля: "))
    except ValueError:
        input("Ошибка. Вводите Числа. Нажмите Enter......")
        continue
    
    clear_screen()
    
    unique_simvols = input("Использовать специальные символы? ").lower()
    
    if unique_simvols not in("да", "нет"):
        input("Ошибка. Вводите только Да или Нет. Нажмите Enter для продолжения")
    
    password = ""
    
    if unique_simvols == "да":
        for i in range(password_lenght):
            password += random.choice(password_components) + random.choice(unique_components)
    elif unique_simvols == "нет":
        for i in range(password_lenght):
            password += random.choice(password_components)
    
    clear_screen()
    
    print(f"Ваш пароль: {password}")
    
    input("Нажмите Enter для продолжения....")