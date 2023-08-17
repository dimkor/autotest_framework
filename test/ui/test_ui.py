import pytest
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

from api.BoardApi import BoardApi

from testdata.DataProvider import DataProvider

@allure.step('Авторизация')
def test_auth(driver: webdriver, test_data: DataProvider):
    
    email = test_data.get('email')
    password = test_data.get('password')
    
    loginPage = LoginPage(driver)
    loginPage.auth(email, password)
    loginPage.open_menu()
    
    assert loginPage.return_user_email() == email

@allure.step('Создание новой доски')
def test_create_board(driver: webdriver, api_client: BoardApi, test_data: DataProvider):
    
    board_name = test_data.get('boardname')
    
    main_page = MainPage(driver)

    before = len(api_client.get_all_boards())

    main_page.create_board(board_name)
    
    after = len(api_client.get_all_boards())

    boardid = main_page.get_board_id()
    
    api_client.delete_board_by_id(boardid)
    
    assert before < after

@allure.step('Удаление существующей доски')
def test_delete_board(driver: webdriver, api_client: BoardApi, test_data: DataProvider):
    
    boardname = test_data.get('boardname')
    
    test_board = api_client.create_board(boardname)
    
    before_delete = len(api_client.get_all_boards())
    
    main_page = MainPage(driver)

    main_page.delete_board(test_board)
    
    after_delete = len(api_client.get_all_boards())

    assert before_delete > after_delete

@allure.step('Добавление карточки на доску')
def test_add_card_to_board(driver: webdriver, api_client: BoardApi, test_data: DataProvider):
    
    board_name = test_data.get('boardname')
    list_name = test_data.get('listname')
    card_name = test_data.get('cardname')

    test_board = api_client.create_board(board_name)
    test_list = api_client.create_list_on_board(test_board['id'], list_name)
    
    lists = api_client.get_lists_on_board(test_board['id'])
    main_page = MainPage(driver)
    
    main_page.create_card(test_board, test_list, card_name, lists)
    
    boardid = main_page.get_board_id()

    cards = api_client.get_cards_on_board(boardid)

    assert cards[0]['name'] == card_name
    
    api_client.delete_board_by_id(boardid)
    
@allure.step('Редактирование карточки')
def test_update_card(driver: webdriver, api_client: BoardApi, test_data: DataProvider):

    board_name = test_data.get('boardname')
    list_name = test_data.get('listname')
    card_name = test_data.get('cardname')
    new_card_name = f'Изменённая {card_name}'
    
    test_board = api_client.create_board(board_name)
    
    test_list = api_client.create_list_on_board(test_board['id'], list_name)
    
    test_card = api_client.create_card_in_list(test_list['id'], card_name)
    
    main_page = MainPage(driver)

    main_page.update_card(test_card, new_card_name)
    
    boardid = main_page.get_board_id()

    assert 2 == 2
    
    api_client.delete_board_by_id(boardid)
    
@allure.step('Удаление карточки')
def test_delete_card(driver: webdriver, api_client: BoardApi, test_data: DataProvider):

    board_name = test_data.get('boardname')
    list_name = test_data.get('listname')
    card_name = test_data.get('cardname')

    test_board = api_client.create_board(board_name)
    
    test_list = api_client.create_list_on_board(test_board['id'], list_name)
    
    test_card = api_client.create_card_in_list(test_list['id'], card_name)

    count_card_before = len(api_client.get_cards_on_board(test_board['id']))

    main_page = MainPage(driver)

    main_page.delete_card(test_board, test_card)
    
    count_card_after = len(api_client.get_cards_on_board(test_board['id']))
    
    assert count_card_before > count_card_after
    
    api_client.delete_board_by_id(test_board['id'])

@allure.step('Перемещение карточки в другую колонку')
def test_move_card(driver: webdriver, api_client: BoardApi, test_data: DataProvider):
    
    board_name = test_data.get('boardname')
    list_name_1 = test_data.get('listname 1')
    list_name_2 = test_data.get('listname 2')
    card_name = test_data.get('cardname')

    test_board = api_client.create_board(board_name)
    
    test_list_2 = api_client.create_list_on_board(test_board['id'], list_name_2)
    test_list_1 = api_client.create_list_on_board(test_board['id'], list_name_1)
    
    test_card = api_client.create_card_in_list(test_list_1['id'], card_name)

    before_list_1 = len(api_client.get_cards_in_list(test_list_1['id']))
    before_list_2 = len(api_client.get_cards_in_list(test_list_2['id']))

    count_card_list = len(api_client.get_cards_on_board(test_board['id']))

    main_page = MainPage(driver)

    main_page.move_card(test_board)
    
    after_list_1 = len(api_client.get_cards_in_list(test_list_1['id']))
    after_list_2 = len(api_client.get_cards_in_list(test_list_2['id']))
    
    assert before_list_1 > after_list_1
    assert before_list_2 < after_list_2
      
    api_client.delete_board_by_id(test_board['id'])