class UrTube:
    def __init__(self):
        self.videos = []
        self.users = {}  # Используем словарь для хранения пользователей
        self.current_user = None

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users[nickname] = new_user  # Сохраняем пользователя по никнейму
            print(f'Пользователь {nickname} добавлен')
            self.current_user = new_user
            print(f'Текущий пользователь {nickname}')

    def log_in(self, nickname, password):
        user = self.users.get(nickname)  # Получаем пользователя по никнейму
        if user:
            if user.password == hash(password):
                self.current_user = user
                print(f'Пользователь {nickname} вошел в систему')
            else:
                print(f'Неверный пароль для пользователя {nickname}')
        else:
            print(f'Пользователь {nickname} не найден')
