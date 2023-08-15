import allure
from api.BoardApi import BoardApi

@allure.step('Cоздание новой доски')
def test_create_board():

    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    api = BoardApi(base_url, api_key, api_token)
   
    after = len(api.get_all_boards())

    test_board = api.create_board('my_board')
    
    before = len(api.get_all_boards())

    assert after < before

    api.delete_board_by_id(test_board['id'])

@allure.step('Удаление существующей доски')
def test_delete_board():

    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    api = BoardApi(base_url, api_key, api_token)
   
    test_board = api.create_board('my_board')
    
    after = len(api.get_all_boards())

    api.delete_board_by_id(test_board['id'])

    before = len(api.get_all_boards())

    assert after > before

    

@allure.step('Добавление карточки на доску')
def test_add_card_to_board():
    
    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'

    api = BoardApi(base_url, api_key, api_token)
   
    test_board = api.create_board('my_board')
    
    after = len(api.get_all_boards())

    api.delete_board_by_id(test_board['id'])

    before = len(api.get_all_boards())

    assert after > before

@allure.step('Редактирование карточки')
def test_edit_card():
    return

@allure.step('Удаление карточки')
def test_delete_card():
    return

@allure.step('Перемещение карточки в другую колонку')
def test_move_card():
    return
