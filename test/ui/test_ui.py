import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

from api.BoardApi import BoardApi

def test_auth(driver):
    email = "4cfsiixk4dwp@mail.ru"
    password = "dB:7h'HBT'>PwZw"
    
    loginPage = LoginPage(driver)
    loginPage.auth(email, password)
    loginPage.open_menu()
    
    assert loginPage.return_user_email() == email

# создание новой доски
def test_create_board(driver):
    
    token = '64cf25acc9f789ff5ee14224/ATTSm2oaSf5kMOOSNhYOGjmZQsVAuLbFPE1FXxbtpdkZ5II9iVw0AdmEytZOApt9NHcE234E623C'
    base_url = 'https://trello.com/1'
    
    api = BoardApi(base_url, token)
    
    loginPage = LoginPage(driver)
    loginPage.auth("4cfsiixk4dwp@mail.ru", "dB:7h'HBT'>PwZw")

    main_page = MainPage(driver)
    main_page.create_board()
    
    boardid = main_page.get_boardid()
    
    api.delete_board_by_id(boardid)
    
    assert 1 == 1

# удаление существующей доски,
def test_delete_board(driver):
    
    loginPage = LoginPage(driver)
    loginPage.auth("4cfsiixk4dwp@mail.ru", "dB:7h'HBT'>PwZw")
    # token = loginPage.get_auth_token()

    main_page = MainPage(driver)
    main_page.delete_board()
    
    assert 1 == 1

# # добавление карточки на доску
def test_add_card_board(driver):
    
    loginPage = LoginPage(driver)
    loginPage.auth("4cfsiixk4dwp@mail.ru", "dB:7h'HBT'>PwZw")
    
    main_page = MainPage(driver)
    main_page.create_card()
    
    assert 2 == 2
    
# # редактирование карточки
def test_edit_card(driver):

    loginPage = LoginPage(driver)
    loginPage.auth("4cfsiixk4dwp@mail.ru", "dB:7h'HBT'>PwZw")
    
    main_page = MainPage(driver)
    main_page.edit_card()
    
    assert 2 == 2

# # удаление карточки
def test_delete_card(driver):
    
    loginPage = LoginPage(driver)
    loginPage.auth("4cfsiixk4dwp@mail.ru", "dB:7h'HBT'>PwZw")
    
    main_page = MainPage(driver)
    main_page.create_card()
    main_page.delete_card()

    assert 5 == 5

# # перемещение карточки в другую колонку
# def test_move_card():
#     return
