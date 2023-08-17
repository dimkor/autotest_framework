import requests
import allure

class BoardApi:
    
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

    @allure.step("Создать список {list_name} на доске")
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
    
    @allure.step("Редактирование карточки (смена названия на {new_name})")
    def update_card(self, card_id: str, new_name: str) -> dict:
        """
        Редактируем карточку

        Args:
            card_id (str): id карточки
            new_name (str): новое имя карточки

        Returns:
            dict: ответ сервера в json
        """
        path = f'{self.base_url}/cards/{card_id}?key={self.api_key}&token={self.api_token}&name={new_name}'
        
        resp = requests.put(path)
        
        return( resp.json() )
    
    @allure.step("Удаление карточки")
    def delete_card(self, card_id: str) -> dict:
        """
        Удаляем карточку

        Args:
            card_id (str): id карточки

        Returns:
            dict: ответ сервера в json
        """        
        path = f'{self.base_url}/cards/{card_id}?key={self.api_key}&token={self.api_token}'
        resp = requests.delete(path)
        
        return( resp.json() )
    
    @allure.step("Перемещение карточки в другой список")
    def move_card(self, card_id: str, target_list_id: str) -> dict:
        """
        Перемещение карточки в другой список
        
        Args:
            card_id (str): id перемещаемой карточки
            target_list_id (str): id списка назначения
        Returns:
            dict: ответ от сервера
        """
        path = f'{self.base_url}/cards/{card_id}?key={self.api_key}&token={self.api_token}&idList={target_list_id}'
        resp = requests.put(path)
        
        return resp.json()

    @allure.step("Получить список всех досок")
    def get_all_boards(self) -> dict:
        """
        Получаем список всех досок

        Returns:
            dict: ответ сервера в json
        """
        path = f'{self.base_url}/members/me/boards?key={self.api_key}&token={self.api_token}'
        resp = requests.get(path)

        return(resp.json())

    @allure.step("Создать карточку внутри списка")
    def create_card_in_list(self, list_id: str, card_name: str) -> dict:
        """
        Создать карточку внутри списка

        Args:
            list_id (str): id списка
            card_name (str): имя карточки

        Returns:
            dict: ответ сервера в json
        """        
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
    
    @allure.step("Получить список карточек из листа")
    def get_cards_in_list(self, card_id: str) -> dict:
        """
        Получить список карточек в листе
        
        Args:
            card_id (str): id карточки
        Returns:
            dict: json с id листа, в котором лежит карточка
        """        
        path = f'{self.base_url}/lists/{card_id}/cards?key={self.api_key}&token={self.api_token}'
        resp = requests.get(path)
        return( resp.json() )
    
    @allure.step("Получить список карточек на доске")
    def get_cards_on_board(self, board_id: str) -> dict:
        path = f'{self.base_url}/boards/{board_id}/cards?key={self.api_key}&token={self.api_token}'
        resp = requests.get(path)
        return(resp.json())
    
    @allure.step("Получить списки на доске")
    def get_lists_on_board(self, board_id: str) -> dict:
        path = f'{self.base_url}/boards/{board_id}/lists?key={self.api_key}&token={self.api_token}'
        resp = requests.get(path)
        return(resp.json())