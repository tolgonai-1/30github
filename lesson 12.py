from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Задайте ваши учетные данные
USERNAME = 'your_username'
PASSWORD = 'your_password'
URL = 'https://example.com/login'  # Замените на URL вашей страницы входа

# Инициализируем драйвер (например, Chrome)
driver = webdriver.Chrome()

try:
    # Открываем страницу входа
    driver.get(URL)

    # Находим элементы формы для ввода логина и пароля
    username_input = driver.find_element(By.NAME, 'username')  # Замените на правильное имя поля
    password_input = driver.find_element(By.NAME, 'password')  # Замените на правильное имя поля

    # Вводим учетные данные
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    # Находим и нажимаем кнопку входа
    login_button = driver.find_element(By.NAME, 'login')  # Замените на правильное имя кнопки
    login_button.click()

    # Ждем немного, чтобы страница загрузилась
    time.sleep(5)

    # Проверяем, произошел ли вход (например, ищем элемент, который отображается только после успешного входа)
    # Это может быть заголовок, приветствие пользователя или какой-то элемент на главной странице
    assert "Welcome" in driver.page_source
    print("Авторизация прошла успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
