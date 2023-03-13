from selenium.webdriver.common.by import By


class QuestionPageLocators():
    question_about_text=(By.XPATH,"//div[text()='Вопросы о важном']")
    open_text_answer = (By.XPATH, ".//div[@role='region' and not(@hidden)]/p")
    question_1 = (By.ID, 'accordion__heading-0')
    question_2 = (By.ID, 'accordion__heading-1')
    question_3 = (By.ID, 'accordion__heading-2')
    question_4 = (By.ID, 'accordion__heading-3')
    question_5 = (By.ID, 'accordion__heading-4')
    question_6 = (By.ID, 'accordion__heading-5')
    question_7 = (By.ID, 'accordion__heading-6')
    question_8 = (By.ID, 'accordion__heading-7')
    answer_1 = (By.XPATH, "// p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    answer_2 = (By.XPATH,
                "// p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                "можете просто сделать несколько заказов — один за другим.']")
    answer_3 = (By.XPATH,
                "// p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    answer_4 = (By.XPATH, "// p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    answer_5 = (By.XPATH,
                "// p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    answer_6 = (By.XPATH,
                "// p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    answer_7 = (By.XPATH,
                "// p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    answer_8 = (By.XPATH, "// p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")




