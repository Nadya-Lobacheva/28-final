valid_email = "nado555@mail.ru"
valid_pass = "Lalafa11"

invalid_email = 'nado5555@gmail.com'
invalid_pass = 'vavaR123'

name = 'Надежда'
surname = 'Лобачева'
region = 'Москва г'
email = 'likoffka13@gmail.com'
password = 'Zxc12345'

false_email = '123456'
false_mobile_max = '89275678911'
false_mobile_mini = '892756789'
false_name_mini = 'Н'
name_two_letters = "Он"
thirty_letters = 'гагариняваслюбила-лалалалалал'
thirty_one_letters = 'гагариняваслюбила-лалалалалала'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
