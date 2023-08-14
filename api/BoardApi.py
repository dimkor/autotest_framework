import requests
import allure

class BoardApi:
    
    token = '64cf25acc9f789ff5ee14224/ATTSm2oaSf5kMOOSNhYOGjmZQsVAuLbFPE1FXxbtpdkZ5II9iVw0AdmEytZOApt9NHcE234E623C'
    
    @allure.step("URL: {base_url}, токен авторизации {token}")
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token
        
    @allure.step("Создать доску {name}")
    def create_board(self, name: str, default_lists=True) -> dict:
        body = {
            'defaultLists': default_lists,
            'name': name,
            'token': self.token
        }

        cookie = {"token": self.token}
        path = "{trello}/boards/".format(trello=self.base_url)
        resp = requests.post(path, json=body, cookies=cookie)

        return resp.json()
    
    @allure.step("Удалить доску {id}")    
    def delete_board_by_id(self, id: str):
        cookie = {'token': self.token}
        path = "{trello}/boards/{board_id}".format(trello=self.base_url, board_id=id)
        resp = requests.delete(path, json=cookie, cookies=cookie)

        return resp.json()