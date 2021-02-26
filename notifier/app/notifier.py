class AddressGetter:

	def __init__(self, id):
		self._id = id

	def get_address(self):
		pass


class Sender:

	def __init__(self, address):
		self._address = address

	def send(self, message):
		pass


class Formatter:

	def __init__(self, format_msg, name, event, watch, value, time, currency):
		self._format = format_msg
		self._name = name
		self._event = event
		self._watch = watch
		self._value = value
		self._time = time
		self._currency = currency

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

	def setName(self, name):
		self._name = name

	def setEvent(self, event):
		if event not in ('up', 'down'):
			raise ValueError
		self._event = event

	def setWatch(self, watch):
		self._watch = watch

	def setValue(self, value):
		self._value = value

	def setTime(self, time):
		self._time = time

	def setCurrency(self, currency):
		self._currency = currency

	def getFormatter(self):
		return Formatter(
			format_msg=self._format,
			name = self._name,
			event = self._event,
			watch = self._watch,
			value = self._value,
			time = self._time,
			currency = self._currency
			)