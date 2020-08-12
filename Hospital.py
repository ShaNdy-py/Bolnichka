class Hospital():
	
	NAMES_OF_DEPARTMENTS = []

	def __init__(self, wards):
		self.list_of_wards = wards

	def set_list_of_wards(self, wards):
		self.list_of_wards = wards

	def get_list_of_wards(self):
		return self.list_of_wards

	def check_free_wards(self):
	 	