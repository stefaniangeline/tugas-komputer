import os
import json
from getpass import getpass

from settings import Settings
from user import User
from product import Product

class Warehouse:

	def __init__(self):
		self.settings = Settings()
		self.login_attempts = 0
		self.user = None

	def clear_screen(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

	def load_data(self):
		try:
			with open(self.settings.users_location, 'r') as file:
				self.settings.users = json.load(file)

		except:
			self.settings.users = {}

		try:
			with open(self.settings.products_location, 'r') as file:
				self.settings.products = json.load(file)
		except:
			self.settings.products = {}

	def save_data(self):
		with open(self.settings.products_location, 'w') as file:
			json.dump(self.settings.products, file)

	def logger(self): 
		self.clear_screen()
		while self.login_attempts < 3:
			print("\nPlease login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.settings.users:
				if self.settings.users[username]['password'] == password:
					self.user = User(
								username,
								first=self.settings.users[username]['first'],
								last=self.settings.users[username]['last'],
								password=self.settings.users[username]['password']
								)	
					return True
			else:
				print("Login Failed. ")
				self.login_attempts += 1

		return False

	def show_menus(self):
		self.clear_screen()
		print("Welcome ..", self.user.first.title(), self.user.last.title())
		print(self.settings.menu)

	def find_product(self, code):
		products = self.settings.products
		if code in products:
			print("The Product has been found!")
			print(f"Code	: {code}")
			print(f"Name 	: {products[code]['name'].title()}")
			print(f"Expired	: {products[code]['expired']}")
			print(f"Quantity: {products[code]['qty']}")
			return True

		
		print("Sorry, The Product wasn't found..")
		return False

	def check_user_option(self, choice):
		if choice == "q":
			self.settings.active = False

		elif choice == "1":
			self.clear_screen()
			products = self.settings.products 
			print("Code\t\tName\t\tExpired\t\tQuantity")

			for code, product in products.items():
				print(f"{code}\t\t{product['name'].title()}\t\t{product['expired']}\t{product['qty']}")

			input("Press ENTER to return to menu.")

		elif choice == "2":
			self.clear_screen()
			code = input("Enter code : ")

			self.find_product(code)

			input("Press ENTER to return to menu.")

		elif choice == "3":
			self.clear_screen()
			code = input("Code	: ")
			name = input("Name	: ")
			expired = input("Expired	: ")
			qty = input("Quantity  : ")
			product = Product(code, name, expired, qty)
			self.settings.products[code] = {

				"name" : name,
				"expired" : expired,
				"qty" : qty
			}
			self.save_data()
			print("Product has been saved!")
			input("Press ENTER to return to menu.")

		elif choice == "4":
			self.clear_screen()
			code = input("Code	: ")

			if self.find_product(code):
				print("Edit\n1.Code, 2.Name, 3.Expired, 4.Quantity")
				option = input("Which data do you want to edit / update ? (1/2/3/4)  ")
				if option == "1":
					old_product = self.settings.products[code]
					new_code = input("New code : ")

					self.settings.products[new_code] = {

						"name" : old_product["name"],
						"expired" : old_product["expired"],
						"qty" : old_product["qty"]

					}

					del self.settings.products[code]
					self.save_data()
					print("New product's code has been saved.")
					input("Press ENTER to return to menu.")

				elif option == "2":
					new_name = input("New Name : ")
					self.settings.products[code]["name"] = new_name
					self.save_data()
					print("New name has been saved.")
					input("Press ENTER to return to menu.")

				elif option == "3":
					new_expired = input("New Expired : ")
					self.settings.products[code]["expired"] = new_expired
					self.save_data()
					print("New Expired date has been saved.")
					input("Press ENTER to return to menu.")

				elif option == "4":
					new_qty = input("New Quantity : ")
					self.settings.products[code]["qty"] = new_qty
					self.save_data()
					print("New Quantity of product has been saved.")
					input("Press ENTER to return to menu.")

		elif choice == "5":
			self.clear_screen()
			code = input("Code : ")

			if self.find_product(code):
				confirm = input("Are you sure want to delete this product ? (y/n)  ")
				if confirm.lower() == "y":

					del self.settings.products[code]

					self.save_data()
					print("The Product has been deleted.")

			input("Press ENTER to return to menu.")


	def run(self):
		self.load_data()
		if self.logger():
			self.settings.active = True

		while self.settings.active:
			self.show_menus()
			self.check_user_option(input("Option : ").lower())


if __name__ == '__main__':
	app = Warehouse()
	app.run()


