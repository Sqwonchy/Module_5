from time import sleep
#####################################################################
class User:
    all_user = []
    def __new__(cls, *args, **kwargs):
        if args[0] in User.all_user:
            return print(f"Пользователь {args[0]} уже существует")
        else:
            cls.all_user.append(args[0])
            return super().__new__(cls)
    def __init__(self, nickname= str, password= int, age= int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __eq__(self, other):
        return self.password == hash(other)
####################################################################
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.diration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def watch(self):
        for i in range(self.diration):
            print(i+1, end=" ")
            sleep(self.time_now)
        print("Конец видео")
####################################################################
class UrTube:
    users = []
    videos = []
    current_user = None
    def log_in(self, nickname,password):
        for user_ in UrTube.users:
            if user_.nickname == nickname and password == user_:
                UrTube.current_user = user_.nickname
    def register(self, nickname,password,age):
        U_1 = User(nickname,password,age)
        if U_1 != None:
            UrTube.users.append(U_1)
            UrTube.current_user = U_1.nickname
        return U_1
    def log_out(self):
        UrTube.current_user = None
    def add(self, *args):
        for videos in args:
            if isinstance(videos,Video):
                if videos not in UrTube.videos:
                    UrTube.videos.append(videos)
    def get_videos(self,search):
        result_search = []
        search_word = search.lower()
        for video_ in UrTube.videos:
            low_title = video_.title.lower()
            if search_word in low_title:
                result_search.append(video_.title)
        return result_search
    def watch_video(self, name_video):
        for user in UrTube.users:
            if UrTube.current_user == user.nickname:
                if UrTube.current_user == None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                else:
                    for video in UrTube.videos:
                        if name_video == video.title:
                            if video.adult_mode == False:
                                video.watch()
                            elif user.age >= 18:
                                video.watch()
                            else:
                                print("Вам нет 18 лет, пожалуйста покиньте страницу")
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')