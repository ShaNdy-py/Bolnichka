class Person(): # ага - да
	
	def __init__(self, name, family, patron, number):
		self.name = name
		self.family_name = family
		self.patronymic = patron
		self.phone_number = number

	def set_name(self, name):
		self.name = name

	def set_family_name(self, family):
		self.family_name = family	

	def set_patron(self, patron):
		self.patronymic = patron
				
	def set_number(self, number):
		self.number = number