import os
import time

from selene import browser, have, by


def test_otpravka_zaivki():
    #фамилия, имя, почта
    browser.element('[id="uploadPicture"]')
    browser.element('[id="firstName"]').type('Ivanov')
    browser.element('[id="lastName"]').type('Ivan')
    browser.element('[id="userEmail"]').type('testovii@mail.ru')
    #выбор пола и телефон
    browser.element('[class ="custom-control-label"]').click()
    browser.element('[id = "userNumber"]').type('89998887766')
    #календарь
    browser.element('[id="dateOfBirthInput"]').click()   #нажал на поле календарь
    browser.element('[class="react-datepicker__navigation react-datepicker__navigation--next"]').click().click() #2 раза кликнул на стрелку в сторону (выбрал декабрь)
    browser.element('[class="react-datepicker__day react-datepicker__day--031 react-datepicker__day--weekend"]').click() #клик на 31 декабря
    #предмет
    browser.element('[id="subjectsInput"]').type('c').press_enter()
     #хобби
    browser.element("#hobbiesWrapper").element(by.text("Reading")).click() #нашли строку, где должно быть написано Reading
    #загрузка файла
    browser.element('#uploadPicture').send_keys(os.path.abspath('pic.png'))
    #вписать адрес
    browser.element('[id="currentAddress"]').type('Пушкина д.10, кв.5')
    #выбрать штат и город
    browser.element('[id="react-select-3-input"]').type('n').press_enter()
    browser.element('[id="react-select-4-input"]').type('d').press_enter()
    browser.element('[id="submit"]').click()


