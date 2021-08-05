class Database:
    def __init__(self):
        self.database = dict()

    def push(self, username: str, password: str, name: str):
        self.database[username] = {"password": password, "name": name}

    def contains(self, username: str) -> bool:
        return self.database.get(username) is not None

    def check_auth(self, username: str, password: str) -> bool:
        if not self.contains(username):
            return False

        return self.database[username]["password"] == password


data = Database()