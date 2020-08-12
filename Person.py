class Person(): # ага - да
	
	def __init__(self, name, family, patron, number, policy, place, type_of_help):
		self.name = name
		self.family_name = family
		self.patronymic = patron
		self.phone_number = number
		self.policy = policy
		self.place = place
		self.type_of_help = type_of_help

	def set_name(self, name):
		self.name = name

	def set_family_name(self, family):
		self.family_name = family	

	def set_patron(self, patron):
		self.patronymic = patron
				
	def set_number(self, number):
		self.phone_number = number

	def set_policy(self, policy):
		self.policy = policy

	def set_place(self, place):
		self.place = place

	def set_type_of_help(self, type_of_help):
		self.type_of_help = type_of_help

	def get_name(self):
		return self.name

	def get_family_name(self):
		return self.family_name	

	def get_patron(self):
		return self.patronymic
				
	def get_number(self):
		return self.phone_number

	def get_policy(self):
		return self.policy

	def get_place(self):
		return self.place

	def get_type_of_help(self):
		return self.type_of_help