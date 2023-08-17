import allure
from api.BoardApi import BoardApi
from testdata.DataProvider import DataProvider

@allure.step('Cоздание новой доски')
def test_create_board(test_data: DataProvider):

    base_url = test_data.get('api_url')
    api_key = test_data.get('api_key')
    api_token = test_data.get('api_token')

    api = BoardApi(base_url, api_key, api_token)
   
    before = len(api.get_all_boards())

    test_board = api.create_board('my_board')
    
    after = len(api.get_all_boards())
    
    with allure.step('Проверка, что количество досок стало больше'):
        assert before < after

    api.delete_board_by_id(test_board['id'])

@allure.step('Удаление существующей доски')
def test_delete_board(api_client: BoardApi, test_data: DataProvider):

    board_name = test_data.get('boardname')
    
    test_board = api_client.create_board(board_name)
    
    before = len(api_client.get_all_boards())

    api_client.delete_board_by_id(test_board['id'])

    after = len(api_client.get_all_boards())
    
    with allure.step('Проверка, что количество досок стало меньше'):
        assert before > after

@allure.step('Добавление карточки на доску')
def test_add_card_to_board(api_client: BoardApi, test_data: DataProvider):
    
    board_name = test_data.get('boardname')
    list_name = test_data.get('listname')
    card_name = test_data.get('cardname')
    
    test_board = api_client.create_board(board_name)
    
    test_list = api_client.create_list_on_board(test_board['id'], list_name)
    
    after = len(api_client.get_cards_on_board(test_board['id']))
    
    api_client.create_card_in_list(test_list['id'], card_name)
    
    before = len(api_client.get_cards_on_board(test_board['id']))

    with allure.step('Проверка того, что карточек стало больше'):
        assert after < before
    
    api_client.delete_board_by_id(test_board['id'])

@allure.step('Редактирование карточки')
def test_edit_card(api_client: BoardApi, test_data: DataProvider):

    board_name = test_data.get('boardname')
    list_name = test_data.get('listname')
    card_name = test_data.get('cardname')
    new_card_name = f'Изменённая {card_name}'
    
    
    test_board = api_client.create_board(board_name)
    
    test_list = api_client.create_list_on_board(test_board['id'], list_name)
    
    test_card = api_client.create_card_in_list(test_list['id'], card_name)

    update_card = api_client.update_card(test_card['id'], new_card_name)
    
    with allure.step('Проверка того, что карточка изменила имя'):
        assert test_card['name'] != update_card['name']
     
    api_client.delete_board_by_id(test_board['id'])

@allure.step('Удаление карточки')
def test_delete_card(api_client: BoardApi, test_data: DataProvider):
    
    board_name = test_data.get('boardname')
    list_name = test_data.get('listname')
    card_name = test_data.get('cardname')
          
    test_board = api_client.create_board(board_name)
    
    test_list = api_client.create_list_on_board(test_board['id'], list_name)
    
    test_card = api_client.create_card_in_list(test_list['id'], card_name)
    
    before = len(api_client.get_cards_in_list(test_list['id']))
    
    api_client.delete_card(test_card['id'])
    
    after = len(api_client.get_cards_in_list(test_list['id']))
    
    with allure.step('Проверка того, что кол-во карточек изменилось в меньшую сторону'):
        assert before > after
    
    api_client.delete_board_by_id(test_board['id'])

@allure.step('Перемещение карточки в другую колонку')
def test_move_card(api_client: BoardApi, test_data: DataProvider):
    
    board_name = test_data.get('boardname')
    list_name_1 = test_data.get('listname 1')
    list_name_2 = test_data.get('listname 2')
    card_name = test_data.get('cardname')
    
    test_board = api_client.create_board(board_name)
    
    test_list_1 = api_client.create_list_on_board(test_board['id'], list_name_1)
    test_list_2 = api_client.create_list_on_board(test_board['id'], list_name_2)
    
    test_card = api_client.create_card_in_list(test_list_1['id'], card_name)
    
    before_list_1 = len(api_client.get_cards_in_list(test_list_1['id']))
    before_list_2 = len(api_client.get_cards_in_list(test_list_2['id']))
    
    api_client.move_card(test_card['id'], test_list_2['id'])
    
    after_list_1 = len(api_client.get_cards_in_list(test_list_1['id']))
    after_list_2 = len(api_client.get_cards_in_list(test_list_2['id']))
    
    with allure.step(f'Проверяем, что в списке /"{list_name_1}/" карточек стало меньше, чем было'):    
        assert before_list_1 > after_list_1
    with allure.step(f'Проверяем, что в списке /"{list_name_2}/" карточек стало больше, чем было'):
        assert before_list_2 < after_list_2
    
    api_client.delete_board_by_id(test_board['id'])