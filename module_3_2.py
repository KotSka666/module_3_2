
def send_email(message="", recipient="", *, sender="university.help@gmail.com"):
    position = [".com", ".ru", ".net"]
    if "@" not in sender:
        return print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif any(i in sender[-len(i):] for i in position):
        pass
    else:
        return print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if "@" not in recipient:
        return print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif any(i in recipient[-len(i):] for i in position):
        pass
    else:
        return print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if sender == recipient:
        return print("Нельзя отправить письмо самому себе!")
    if sender == "university.help@gmail.com":
        return print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        return print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



# Примеры использования
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')