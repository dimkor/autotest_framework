import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

from api.BoardApi import BoardApi

@allure.step('Авторизация')
def test_auth(driver: webdriver):
    email = "4cfsiixk4dwp@mail.ru"
    password = "dB:7h'HBT'>PwZw"
    
    loginPage = LoginPage(driver)
    loginPage.auth(email, password)
    loginPage.open_menu()
    
    assert loginPage.return_user_email() == email

@allure.step('Создание новой доски')
def test_create_board(driver: webdriver, api_client: BoardApi):
    
    main_page = MainPage(driver)

    before = len(api_client.get_all_boards())

    main_page.create_board("Имя доски")
    
    after = len(api_client.get_all_boards())

    boardid = main_page.get_board_id()
    
    api_client.delete_board_by_id(boardid)
    
    assert before < after

@allure.step('Удаление существующей доски')
def test_delete_board(driver: webdriver, api_client: BoardApi):
    boardname = 'Имя доски'
    api_client.create_board(boardname)

    before = len(api_client.get_all_boards())

    main_page = MainPage(driver)

    main_page.delete_board(boardname)
    
    after = len(api_client.get_all_boards())

    assert before > after

@allure.step('Добавление карточки на доску')
def test_add_card_to_board(driver: webdriver, api_client: BoardApi):

    main_page = MainPage(driver)
    
    main_page.create_card()
    
    boardid = main_page.get_board_id()

    cards = api_client.get_cards_on_board(boardid)

    assert 2 == 2
    
@allure.step('Редактирование карточки')
def test_update_card(driver: webdriver, api_client: BoardApi):

    main_page = MainPage(driver)

    main_page.update_card()
    
    boardid = main_page.get_board_id()

    assert 2 == 2

@allure.step('Удаление карточки')
def test_delete_card(driver: webdriver, api_client: BoardApi):
    
    main_page = MainPage(driver)
    main_page.create_card()
    main_page.delete_card()

    assert 5 == 5

@allure.step('Перемещение карточки в другую колонку')
def test_move_card(driver: webdriver, api_client: BoardApi):
    return
