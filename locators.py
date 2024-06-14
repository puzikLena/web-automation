from selenium.webdriver.common.by import By


class CommonLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_HELLO_TEXT = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    LOCATOR_CREATE_POST_BTN = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_TITLE_INPUT = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label')
    LOCATOR_DESCRIPTION_INPUT = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label')
    LOCATOR_CONTENT_INPUT = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label')
    LOCATOR_ATTACH_IMAGE = (By.XPATH, '//*[@id="create-item"]/div/div/div[6]/div/div/label/input')
    LOCATOR_SAVE_POST_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    LOCATOR_POST_IMAGE = (By.TAG_NAME, 'img')
    LOCATOR_POST_TITLE = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_MENU = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    LOCATOR_LOGOUT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/div/ul/li[3]/span[1]')
    LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')


class ContactPageLocators:
    LOCATOR_CONTACT_NAME_INPUT = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_CONTACT_EMAIL_INPUT = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTACT_CONTENT_INPUT = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACT_SUBMIT_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/span')
