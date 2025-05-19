from selenium.webdriver.common.by import By


class MainPageLocators:
    # Блок FAQ
    FAQ_HEADERS = (By.XPATH, "//div[@data-accordion-component='AccordionItemHeading']")  # Заголовки вопросов
    FAQ_ITEMS = (By.XPATH, "//div[@data-accordion-component='AccordionItem']")  # Блоки вопросов
    FAQ_ANSWER = (By.XPATH, ".//div[@data-accordion-component='AccordionItemPanel']")  # Текст ответа

    # Кнопки заказа
    ORDER_BUTTON_TOP = ( By.XPATH, "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g']")  # Верхняя кнопка заказа
    ORDER_BUTTON_BOTTOM = (By.XPATH,"//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g Button_UltraBig__UU3Lp']")  # Нижняя кнопка заказа

    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Логотип Самоката
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")  # Логотип Яндекса