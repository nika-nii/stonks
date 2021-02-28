class UserGetter:

    def __init__(self, id):
        self._id = id
        self._user = None

    def get_data(self):
        # todo: get actual data from Users
        self._user = {
            'username': 'vasya',
            'first_name': 'Вася',
            'last_name': 'Курочкин',
            'email': 'vasya@example.com'
        }

    def get_address(self):
        if self._user is None:
            self.get_data()
        pass

    def get_name(self):
        if self._user is None:
            self.get_data()
        return f'{self._user["first_name"]} {self._user["last_name"]}'


class Sender:

    def __init__(self, address):
        self._address = address

    def send(self, message):
        pass


class Formatter:

    def __init__(self, format_msg, name, event, watch, value, time, currency):
        self._format = format_msg
        self.name = name
        self.event = event
        self.watch = watch
        self.value = value
        self.time = time
        self.currency = currency

    def render(self):
        return self._format.format(**vars(self))


class FormatterBuilder:

    def __init__(self):
        self._name = None
        self._event = None
        self._watch = None
        self._value = None
        self._time = None
        self._currency = None
        self._format = None

    def set_name(self, name):
        self._name = name

    def set_event(self, event):
        if event not in ('up', 'down'):
            raise ValueError
        self._event = event

    def set_watch(self, watch):
        self._watch = watch

    def set_value(self, value):
        self._value = value

    def set_time(self, time):
        self._time = time

    def set_currency(self, currency):
        self._currency = currency

    def get_formatter(self):
        return Formatter(
            format_msg=self._format,
            name=self._name,
            event=self._event,
            watch=self._watch,
            value=self._value,
            time=self._time,
            currency=self._currency
        )


class Factory:
    def __init__(self):
        self._formatter = Formatter
        self._formatter_builder = FormatterBuilder
        self._sender = Sender
        self._user_getter = UserGetter

    @property
    def formatter(self):
        return self._formatter

    @property
    def formatter_builder(self):
        return self._formatter_builder

    @property
    def sender(self):
        return self._sender

    @property
    def user_getter(self):
        return self._user_getter
