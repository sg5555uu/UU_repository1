

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    rec_3 = recipient[-3:].lower()
    rec_4 = recipient[-4:].lower()
    snd_3 = sender[-3:].lower()
    snd_4 = sender[-4:].lower()
    if ("@" not in recipient or (rec_3 != ".ru" and rec_4 != ".com" and rec_4 != ".net")
            or "@" not in sender or (snd_3 != ".ru" and snd_4 != ".com" and snd_4 != ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
