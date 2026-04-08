class Endpoints:

    create_user = 'https://stellarburgers.education-services.ru/api/auth/register'
    login_user = 'https://stellarburgers.education-services.ru/api/auth/login'
    data_user = 'https://stellarburgers.education-services.ru/auth/user'
    create_order = 'https://stellarburgers.education-services.ru/api/orders'
    logout = 'https://stellarburgers.education-services.ru/api/auth/logout'
class UserData:
    no_name = {"email": "jermaine1989@yandex.ru",
                     "password": "12345"}

    no_email = {"password": "12345",
                     "name": "eugene"}

    no_password = {"email": "jermaine1989@yandex.ru",
                     "name": "eugene"}
             


    bad_login =  {"email": "olololo@yandex.ru",
                     "password": "olololo"}                


class Ingredients:

    beef_meteor = '61c0c5a71d1f82001bdaaa70'
    protostomia = '61c0c5a71d1f82001bdaaa6f'
    krator_bun = '61c0c5a71d1f82001bdaaa6c'
    flu_bun = '61c0c5a71d1f82001bdaaa6d'
    spicy_sauce = '61c0c5a71d1f82001bdaaa72'
    traditional_sauce = '61c0c5a71d1f82001bdaaa74'
    burger = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6c",
            "61c0c5a71d1f82001bdaaa70",
            "61c0c5a71d1f82001bdaaa72",
            "61c0c5a71d1f82001bdaaa74"
        ]
    }

    burger_empty = {
    }

    burger_wrong_hash = {
        "ingredients": [
            "12345",
            "12345",
            "12345",
            "12345"
        ]
    }