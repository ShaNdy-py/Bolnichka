class Person(): # ага - да
	
	def __init__(self, name, family, patron, number):
		self.name = name
		self.family_name = family
		self.patronymic = patron
		self.phone_number = number

	def set_name(self, name):
		self.name = name