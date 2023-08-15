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
    
    @allure.step("Добавить карточку на доску {name}")
    def add_card(self, board_id: str) -> dict:    
        return
    
    @allure.step("Редактирование карточки")
    def edit_card(self, boardname: str) -> dict:
        return
    
    @allure.step("Удаление карточки")
    def add_card(self, boardname: str) -> dict:
        return
    
    @allure.step("Перемещение карточки в другую колонку")
    def move_card(self, boardname: str) -> dict:
        return 

    @allure.step("Получить список всех досок")
    def get_all_boards(self) -> dict:

        path = f'{self.base_url}/members/me/boards?key={self.api_key}&token={self.api_token}'
        resp = requests.get(path)

        return(resp.json())