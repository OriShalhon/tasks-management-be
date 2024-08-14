class Project:
    def __init__(self, id: int, name: str, visibility: bool, board_id: int):
        self.id = id
        self.name = name
        self.visibility = visibility
        self.board_id = board_id