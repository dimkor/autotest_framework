import requests
import allure

class BoardApi:
    
    base_url = 'https://api.trello.com/1'
    api_key = '9a4c098cfc8b126b70975af522e016cf'
    api_token = 'ATTA84feb27d467f7cefcc9ac45012deec4c4fc476e62b6f578c3393cfc5a881a508A8B85F15'
    
    @allure.step("URL: {base_url}, ключ api {api_key}, токен авторизации {api_token}")
    def __init__(self, base_url: str, api_key: str, api_token: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.api_token = api_token
        
    @allure.step("Создать доску {boardname}")
    def create_board(self, boardname: str) -> dict:
        """
        Создание доски с указанным именем
        Args:
            boardname (str): название доски

        Returns:
            dict: ответ сервера в json c id и другой информацией
        """
        path = f'{self.base_url}/boards/?name={boardname}&key={self.api_key}&token={self.api_token}'
        resp = requests.post(path)

        return(resp.json())
    
    @allure.step("Удалить доску {board_id}")    
    def delete_board_by_id(self, board_id: str) -> dict:
        """
        Удаляем доску по её id
        Args:
            board_id (str): id доски

        Returns:
            dict: ответ сервера в json с информацией
        """
        path = f'{self.base_url}/boards/{board_id}?key={self.api_key}&token={self.api_token}'
        resp = requests.delete(path)

        return(resp.json())

    @allure.step("Создать список на доске")
    def create_list_on_board(self, board_id: str, list_name: str) -> dict:
        """
        Создаём список на доске
        
        Args:
            board_id (str): id доски, в которой создаётся список
            list_name (str): имя списка

        Returns:
            dict: ответ сервера
        """
        path = f'{self.base_url}/boards/{board_id}/lists?name={list_name}&key={self.api_key}&token={self.api_token}'
        
        resp = requests.post(path)
        return( resp.json() )
    
    @allure.step("Редактирование карточки")
    def update_card(self, card_id: str, new_name: str) -> dict:
        
        path = f'{self.base_url}/cards/{card_id}?key={self.api_key}&token={self.api_token}&name={new_name}'
        
        resp = requests.put(path)
        
        return( resp.json() )
    
    @allure.step("Удаление карточки")
    def delete_card(self, card_id: str) -> dict:
        
        path = f'{self.base_url}/cards/{card_id}?key={self.api_key}&token={self.api_token}'
        resp = requests.delete(path)
        
        return( resp.json() )
    
    @allure.step("Перемещение карточки в другой список")
    def move_card(self, card_id: str, new_list_id: str) -> dict:
        
        path = f'{self.base_url}/cards/{card_id}?key={self.api_token}&token={self.api_token}&idList={new_list_id}'
        resp = requests.put(path)
        
        return resp.json()

    @allure.step("Получить список всех досок")
    def get_all_boards(self) -> dict:

        path = f'{self.base_url}/members/me/boards?key={self.api_key}&token={self.api_token}'
        resp = requests.get(path)

        return(resp.json())

    @allure.step("Создать карточку внутри списка")
    def create_card_in_list(self, list_id: str, card_name: str) -> dict:
        
        path = f'{self.base_url}/cards?idList={list_id}&key={self.api_key}&token={self.api_token}&name={card_name}'
        resp = requests.post(path)
        return(resp.json())
    
    @allure.step("Получить список, в котором лежит карточка")
    def get_list_of_a_card(self, card_id: str) -> dict:
        """
        Получить список, в котором лежит карточка
        
        Args:
            card_id (str): id карточки
        Returns:
            dict: json с id листа, в котором лежит карточка
        """
        path = f'/cards/{card_id}/list?key={self.api_key}&token={self.api_token}'
        resp = requests.get(path)
        
        return( resp.json() )
    
    @allure.step("Получить список карточек в листе")
    def get_cards_in_list(self, card_id: str) -> dict:
        
        path = f'{self.base_url}/lists/{card_id}/cards?key={self.api_key}&token={self.api_token}'
        resp = requests.get(path)
        return( resp.json() )