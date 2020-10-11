import json

class Json1:
	def Main(self):
		print("start")
		numbers = [1,2,3,4,5]
		filename = 'numbers.json'
		with open(filename, 'w') as xxx:
			json.dump(numbers, xxx)




if __name__ == '__main__':
	start = Json1()
	start.Main()