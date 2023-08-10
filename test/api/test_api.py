import allure
from api.BoardApi import BoardApi

# def test_create_board(api_client: BoardApi, delete_board: dict, test_data:dict):
#     org_id = test_data.get("org_id")
#     board_list_before = api_client.get_all_boards_by_org_id(org_id)
    
#     resp = api_client.create_board("New board to be deleted")
#     delete_board["board_id"] = resp.get("id")
    
#     board_list_after = api_client.get_all_boards_by_org_id(org_id)
    
#     with allure.step("Проверить, что количество досок стало больше на 1"):
#         assert len(board_list_after) - len(board_list_before) == 1