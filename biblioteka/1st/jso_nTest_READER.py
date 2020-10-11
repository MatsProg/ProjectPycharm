import json

class Cjson1():
	def jsonM(self):
		print('startReader')
		filename = 'numbers.json'
		with open(filename) as xxx:
			numbers = json.load(xxx)
		print(numbers)

if __name__ == '__main__':
	start = Cjson1()
	start.jsonM()