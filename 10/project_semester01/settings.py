

class Settings:

	def __init__(self):
		self.active = False

		self.products_location = "data/products.json"
		self.users_location = "data/users.json"

		self.products = None 
		self.users = None 

		self.menu = """
**********************************
 -AQUAMART WAREHOUSE INFORMATION-
**********************************
1. VIEW ALL PRODUCTS
2. FIND PRODUCT BY CODE
3. ADD NEW PRODUCT
4. UPDATE PRODUCTS INFO
5. REMOVE PRODUCTS
Q. EXIT
		"""