import listItem

#Stress Testing Remaining 
class List(object):

	def __init__(self, name="Nameless List"):
		#Constructor

		self.list_name = name 
		self.items = list()
		self.item_count = 0

	def change_name(self, new_name):
		if not isinstance(new_name, str):
			print("Error: value is not a string. Listname not updated") 
			return False 
		
		self.list_name = new_name
		return True 

	def add_item(self, item, prior=0, urgent=True):

		if isinstance(item, listItem.ListItem):
			self.items.append(item)
		elif item == None:
			print("Error: NoneType object passed. Expecting string.")
			return False 
		else:
			self.items.append(listItem.ListItem(str(item), prior, urgent))

		self.item_count += 1 
		return True

	def remove_item(self, item_number):

		if not isinstance(item_number, int):
			print("Error: Item no. should be integer.")
			return False

		if item_number > self.item_count or item_number < 1:
			print("Error: Invalid item no. Valid numbers from 1 - " + str(self.item_count) + ".")
			return False 
		
		ret_val = self.items.pop(item_number - 1)
		self.item_count -= 1 
		return ret_val

	def update_item_name(self, item_number, new_name):
		
		if not isinstance(item_number, int):
			print("Error: Item no. should be integer.")
			return False

		if item_number <= self.item_count and item_number >= 1:
			mod_val = self.items[item_number - 1]
			mod_val.update_item(str(new_name))
			return True
		else:
			print("Error: Invalid item no. Valid numbers from 1 - " + str(self.item_count) + ".")
			return False 

	def update_item_priority(self, item_number, p):
		
		if not isinstance(item_number, int):
			print("Error: Item no. should be integer.")
			return False

		if not isinstance(p, int):
			print("Error: Expected Integer got " + str(type(p)) + ".")
			return False

		if p < 0:
			print("Error: Highest priority is 0.")
			return False 

		if item_number <= self.item_count and item_number >= 1:
			mod_val = self.items[item_number - 1]
			mod_val.set_priority(p)
			return True
		else:
			print("Error: Invalid item no. Valid numbers from 1 - " + str(self.item_count) + ".")
			return False

	def update_item_urgency(self, item_number, u):

		if not isinstance(item_number, int):
			print("Error: Item no. should be integer.")
			return False

		if not isinstance(u, bool):
			print("Error: Expected Boolean got " + str(type(u)) + ".")
			return False

		if item_number <= self.item_count and item_number >= 1:
			mod_val = self.items[item_number - 1]
			mod_val.urgent = u
			return True
		else:
			print("Error: Invalid item no. Valid numbers from 1 - " + str(self.item_count) + ".")
			return False

	def check_item(self, item_number):
		
		if not isinstance(item_number, int):
			print("Error: Item no. should be integer.")
			return False

		if item_number <= self.item_count and item_number >= 1:
			mod_val = self.items[item_number - 1]
			mod_val.check()
			return True
		else:
			print("Error: Invalid item no. Valid numbers from 1 - " + str(self.item_count) + ".")
			return False

	def uncheck_item(self, item_number):
		
		if not isinstance(item_number, int):
			print("Error: Item no. should be integer.")
			return False 

		if item_number <= self.item_count and item_number >= 1:
			mod_val = self.items[item_number - 1]
			mod_val.uncheck()
			return True
		else:
			print("Error: Invalid item no. Valid numbers from 1 - " + str(self.item_count) + ".")
			return False

	def show(self):
		print(" \t\t\t" + self.list_name + "\t\t\t|")
		count = 1
		for i in self.items:
			print(str(count) + ".", i)
			count += 1
		print(" \t\t\t" + self.list_name + "\t\t\t|")