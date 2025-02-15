from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Учетные данные и URL
login = "tolgonai.mamytova.ch@gmail.com"
password = "alisultan3"
URL = "https://koton-crm.geekstudio.kg/api/auth/v1/signin/"

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открываем страницу входа
    driver.get(URL)

    # Явное ожидание для поля ввода email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    email_input.send_keys(login)

    # Явное ожидание для поля ввода пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys(password)

    # Явное ожидание для кнопки входа и нажатие на нее
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))  # Обязательно укажите правильный селектор
    )
    login_button.click()

    # Дополнительное ожидание для проверки успешной авторизации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome')]"))  # Замените на правильный текст
    )

    print("Авторизация прошла успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
