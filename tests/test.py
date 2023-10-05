import os
import time

from selene import browser, have, by, be


def test_otpravka_zaivki():
    browser.open('https://demoqa.com/automation-practice-form')

    #фамилия, имя, почта
    browser.element('[id="firstName"]').type('Ivan')
    browser.element('[id="lastName"]').type('Ivanov')
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
    browser.element('[id="uploadPicture"]')
    browser.element('#uploadPicture').send_keys(os.path.abspath('pic.png'))
    #вписать адрес
    browser.element('[id="currentAddress"]').type('Пушкина д.10, кв.5')
    #выбрать штат и город
    browser.element('[id="react-select-3-input"]').type('n').press_enter()
    browser.element('[id="react-select-4-input"]').type('d').press_enter()
    #нажать кнопку
    browser.element('[id="submit"]').click()
    #проверки
    browser.element('tbody').all('tr')[0].should(have.text('Ivan Ivanov'))
    browser.element('tbody').all('tr')[1].should(have.text('testovii@mail.ru'))
    browser.element('tbody').all('tr')[2].should(have.text('Male'))
    browser.element('tbody').all('tr')[3].should(have.text('8999888776'))
    browser.element('tbody').all('tr')[4].should(have.text('31 December,2023'))
    browser.element('tbody').all('tr')[5].should(have.text('Physics'))
    browser.element('tbody').all('tr')[6].should(have.text('Reading'))
    browser.element('tbody').all('tr')[7].should(have.text('pic.png'))
    browser.element('tbody').all('tr')[8].should(have.text('Пушкина д.10, кв.5'))
    browser.element('tbody').all('tr')[9].should(have.text('NCR Delhi'))
