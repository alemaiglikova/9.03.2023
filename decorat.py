def check_decorator(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        if password == "my_password":
            return func(*args, **kwargs)
        else:
            return "Доступ запрещен!"
    return wrapper


def function(arg1, arg2):
    pass