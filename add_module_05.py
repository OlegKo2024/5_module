class UrTube:

    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = None


    def register(self, nickname, password, age):
        if any(nickname == user.nickname for user in self.users):
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            print(f'Пользователь {nickname} добавлен')
            self.current_user = new_user
            print(f'Текущий пользователь {nickname}')

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    self.current_user = user
                    print(f'Пользователь {nickname} вошел в систему')
                    return
                else:
                    print(f'Неверный пароль для пользователя {nickname}')
                    return
            print(f'Пользователь {nickname} не найден')

    def add(self, *args):
        for video in args:
            if not any(video.title == item_video.title for item_video in self.videos):
                self.videos.append(video)
                print(f'Добавлено {video.title}')
            else:
                return

    def get_videos(self, other):
        videos_matched = []
        for video in self.videos:
            if other.lower() in video.title.lower():
                videos_matched.append(video.title)
        return videos_matched

    def watch_video(self, title):
        import time
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for second in range(1, video.duration + 1):
                    print(f'Сейчас {second} секунда просмотра...')
                    time.sleep(1)
                print('Конец видео')  # Сообщение о завершении просмотра
                video.time_now = 0  # Сбрасываем текущее время
                log_out_choice = int(input('Выберите действие: \n1 - продолжить просмотр \n2 - завершить просмотр'))
                if log_out_choice == 1:
                    print(f'Введите название видео для просмотра')
                    time.sleep(3)
                if log_out_choice == 2:
                    ur.log_out()
                    time.sleep(3)
                return

    def log_out(self):
        print(f'{self.current_user.nickname} вышел из системы. До новых встреч!')
        self.current_user = None

class Video:

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print('Проверка поиска')
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

print('Проверка на вход пользователя и возрастное ограничение')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

print('Проверка входа в другой аккаунт')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
if ur.current_user:
    print(ur.current_user.nickname)
else:
    print('Нет текущего пользователя.')

print('Попытка воспроизведения несуществующего видео')
ur.watch_video('Лучший язык программирования 2024 года!')
