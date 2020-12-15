import time 

class ListItem(object):
	def __init__(self, item="", prior=0, urgent=True):
		self.item = item #string always 
		self.is_checked = False
		self.priority = prior #lower is higher 
		self.urgent = urgent 
		self.time_of_add = time.time()

	def update_item(self, item):
		
		if not isinstance(item, str):
			print("Error: Value is not a string. Item not updated") 
			return False 
		else: 
			self.item = item
			return True 

	def check(self):
		if not self.is_checked:
			self.is_checked = True
		else:
			return False 
	
	def uncheck(self):
		if self.is_checked:
			self.is_checked = False
		else:
			return False  

	def __str__(self):
		ret_val = ""
		
		if self.is_checked:
			ret_val += "[x] "
		else:
			ret_val += "[ ] "

		ret_val += self.item 
		ret_val += " | p = " + str(self.priority)
		ret_val += " | u = " + str(self.urgent) 
		
		return ret_val

	def set_priority(self, priority_p):
		if priority_p < 0:
			print("Error: Invalid Priority Value")
			return False 
		else:
			self.priority = priority_p
			return True 

	def get_time_of_add(self):
		ret_val = time.asctime( time.localtime( time.time() ) )
		print(ret_val)
		return ret_val

