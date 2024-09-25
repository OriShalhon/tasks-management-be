class Board:
    def __init__(self, id: int, name: str, icon: str, visibility: bool, user_id: int):
        self.id = id
        self.name = name
        self.icon = icon
        self.visibility = visibility
        self.user_id = user_id
