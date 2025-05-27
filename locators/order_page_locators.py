from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле ввода имени
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле ввода фамилии
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле ввода адреса
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")  # Поле выбора метро
    METRO_STATION = (By.XPATH, "//div[text()='{}']")  # Станция метро в списке
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле ввода телефона
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")  # Кнопка "Далее"

    # Форма "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле выбора даты
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-root')]")  # Поле выбора срока аренды
    PERIOD_OPTION = (By.XPATH, "//div[text()='{}']")  # Вариант срока аренды
    COLOR_BLACK = (By.XPATH, "//label[@for='black']")  # Лейбл для черного
    COLOR_GREY = (By.XPATH, "//label[@for='grey']")  # Лейбл для серого
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Поле комментария
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(text(), 'Заказать') and ./preceding-sibling::button[text()='Назад']]")  # Кнопка "Заказать"
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")  # Кнопка подтверждения
    DATE_PICKER_HEADER = (By.CLASS_NAME, "Order_Header__BZXOb")  # Для клика вне календаря
    # Модальное окно
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")  # Заголовок модального окна