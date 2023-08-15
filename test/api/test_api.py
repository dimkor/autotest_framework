import allure
from api.BoardApi import BoardApi

@allure.step('Cоздание новой доски')
def test_create_board():

    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    api = BoardApi(base_url, api_key, api_token)
   
    before = len(api.get_all_boards())

    test_board = api.create_board('my_board')
    
    after = len(api.get_all_boards())

    assert before < after

    api.delete_board_by_id(test_board['id'])

@allure.step('Удаление существующей доски')
def test_delete_board():

    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    api = BoardApi(base_url, api_key, api_token)
   
    test_board = api.create_board('my_board')
    
    before = len(api.get_all_boards())

    api.delete_board_by_id(test_board['id'])

    after = len(api.get_all_boards())

    assert after > before

@allure.step('Добавление карточки на доску')
def test_add_card_to_board(api_client):
    
    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    
    api = BoardApi(base_url, api_key, api_token)
   
    test_board = api.create_board('my_board')
    
    test_list = api.create_list_on_board(test_board['id'], 'Какой-то список')
    
    api.create_card_in_list(test_list['id'], 'Какая-то карточка')
    
    before = len(api.get_all_boards())

    assert 1 == 1 #after > before
    
    api.delete_board_by_id(test_board['id'])

@allure.step('Редактирование карточки')
def test_edit_card():
    
    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    api = BoardApi(base_url, api_key, api_token)
   
    test_board = api.create_board('My test board')
    
    test_list = api.create_list_on_board(test_board['id'], 'Какой-то список')
    
    test_card = api.create_card_in_list(test_list['id'], 'Какая-то карточка')

    update_card = api.update_card(test_card['id'], 'Новое имя карточки')
    
    assert test_card['name'] != update_card['name']
     
    api.delete_board_by_id(test_board['id'])


@allure.step('Удаление карточки')
def test_delete_card():
    
    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    api = BoardApi(base_url, api_key, api_token)
   
    test_board = api.create_board('My test board')
    
    test_list = api.create_list_on_board(test_board['id'], 'Какой-то список')
    
    test_card = api.create_card_in_list(test_list['id'], 'Какая-то карточка')
    
    before = len(api.get_cards_in_list(test_list['id']))
    
    api.delete_card(test_card['id'])
    
    after = len(api.get_cards_in_list(test_list['id']))
    
    assert before > after
    
    api.delete_board_by_id(test_board['id'])


@allure.step('Перемещение карточки в другую колонку')
def test_move_card():
    
    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    api = BoardApi(base_url, api_key, api_token)
   
    test_board = api.create_board('My test board')
    
    test_list_1 = api.create_list_on_board(test_board['id'], 'Откуда перемещаем')
    test_list_2 = api.create_list_on_board(test_board['id'], 'Куда перемещаем')
    
    test_card = api.create_card_in_list(test_list_1['id'], 'Карточка из списка "Откуда перемещаем"')
    
    before_list_1 = len(api.get_cards_in_list(test_list_1['id']))
    before_list_2 = len(api.get_cards_in_list(test_list_2['id']))
    
    api.move_card(test_card['id'], test_list_2['id'])
    
    after_list_1 = len(api.get_cards_in_list(test_list_1['id']))
    after_list_2 = len(api.get_cards_in_list(test_list_2['id']))
        
    assert before_list_1 > after_list_1
    assert before_list_2 < after_list_2
    
    api.delete_board_by_id(test_board['id'])