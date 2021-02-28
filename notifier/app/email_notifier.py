from notifier import UserGetter, Sender, FormatterBuilder, Factory


class EmailUserGetter(UserGetter):
    """Получить почтовый адрес пользователя"""

    def __init__(self, id):
        super().__init__(id)

    def get_address(self):
        # todo: получить из storage API адрес
        return "user@example.com"


class EmailSender(Sender):
    """Отправление сообщения пользователю по электронной почте"""

    def __init__(self, address):
        super().__init__(address)

    def send(self, message):
        # todo: Отправить сообщение на e-mail
        print(f"send {message} to {self._address}")


class EmailFormatterBuilder(FormatterBuilder):

    def __init__(self):
        super().__init__()
        self._format = "Hello, {name}! You wanted to know if {currency} will go {event} and bypass value {watch}. Its value is now {value}."


class EmailFactory(Factory):

    def __init__(self):
        super().__init__()
        self._formatter_builder = EmailFormatterBuilder
        self._sender = EmailSender
        self._address_getter = EmailUserGetter
