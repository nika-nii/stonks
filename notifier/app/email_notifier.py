from notifier import UserGetter, Sender, FormatterBuilder, Factory

import smtplib
import ssl

from email.mime.text import MIMEText

import os


class EmailUserGetter(UserGetter):
    """Получить почтовый адрес пользователя"""

    def __init__(self, id):
        super().__init__(id)
        print("EUG")

    def get_address(self):
        super().get_address()
        print(self._user)
        return self._user['email']


class EmailSender(Sender):
    """Отправление сообщения пользователю по электронной почте"""

    def __init__(self, address):
        super().__init__(address)

        # todo: сделать с этим что-нибудь
        from dotenv import load_dotenv
        load_dotenv()

        self._host = os.environ.get('EMAIL_HOST')
        self._port = os.environ.get('EMAIL_PORT')
        self._my_address = os.environ.get('EMAIL_ADDRESS')
        self._my_password = os.environ.get('EMAIL_PASSWORD')

    def send(self, message):

        frm = self._my_address
        to = self._address
        print(frm, to)
        subject = "Уведомление об изменении курса"
        host = self._host
        port = self._port
        text = message

        msg = MIMEText(text.encode('utf-8'), _charset='utf-8')

        msg['Subject'] = subject
        msg['From'] = frm
        msg['To'] = to

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(self._my_address, self._my_password)
            server.sendmail(frm, [to], msg.as_string())


class EmailFormatterBuilder(FormatterBuilder):

    def __init__(self):
        super().__init__()
        self._format = "Привет, {name}! Сообщаем, что с валютой {currency} произошло событие {event}, и она преодолела отметку в {watch}. Сейчас курс составляет {value}."


class EmailFactory(Factory):

    def __init__(self):
        super().__init__()
        self._formatter_builder = EmailFormatterBuilder
        self._sender = EmailSender
        self._user_getter = EmailUserGetter
