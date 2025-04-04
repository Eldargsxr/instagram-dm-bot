
from instagrapi import Client
import time
import random

# Настройки сообщений
messages = [
    "Hey! Love your tattoo taste. Maybe you'd like mine? Check @your_account",
    "Hi! I'm a tattoo artist — let's connect: @your_account",
    "Tattoo ideas? Take a look at my work: @your_account",
    "Looking for ink inspiration? You might like what I do — @your_account",
    "Hallo! Ich bin ein Tätowierer aus Berlin. Schau mal meine Arbeiten an: @your_account",
    "Magst du Tattoos? Dann schau dir meine Kunst an: @your_account",
    "Ich teile meine neuesten Tattoos auf @your_account – vielleicht gefällt dir was!"
]

print("=== Instagram DM Bot ===")
username = input("Введите логин Instagram: ")
password = input("Введите пароль Instagram: ")

print("\nВыберите режим:")
print("1 - Рассылка по списку пользователей")
print("2 - Сбор подписчиков конкурента и рассылка")
mode = input("Ваш выбор (1/2): ")

# Логин в аккаунт
cl = Client()
try:
    cl.login(username, password)
    print("Успешный вход в аккаунт!")
except Exception as e:
    print(f"Ошибка входа: {e}")
    exit()

if mode == "1":
    try:
        user_list = input("Введите usernames через запятую (пример: user1,user2,user3): ")
        usernames = [u.strip() for u in user_list.split(",")]

        for name in usernames:
            try:
                user_id = cl.user_id_from_username(name)
                msg = random.choice(messages)
                cl.direct_send(msg, [user_id])
                print(f"Сообщение отправлено: {name}")
                time.sleep(random.randint(15, 30))
            except Exception as e:
                print(f"Ошибка при отправке {name}: {e}")

        print("Рассылка завершена.")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cl.logout()

elif mode == "2":
    try:
        competitor_username = input("Введите username конкурента: ")
        amount = int(input("Сколько подписчиков собрать (например, 20): "))
        competitor_id = cl.user_id_from_username(competitor_username)
        followers = cl.user_followers(competitor_id, amount=amount)

        print(f"Собрано {len(followers)} подписчиков. Начинаем рассылку...")

        for user_id, user_info in followers.items():
            try:
                msg = random.choice(messages)
                cl.direct_send(msg, [user_id])
                print(f"Сообщение отправлено: {user_info.username}")
                time.sleep(random.randint(15, 30))
            except Exception as e:
                print(f"Ошибка при отправке {user_info.username}: {e}")

        print("Готово. Рассылка завершена.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cl.logout()

else:
    print("Неверный выбор. Выход.")
