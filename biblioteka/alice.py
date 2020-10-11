class Alice:
	def alice_wonder(self):
		filename = 'alice_wonderland.txt'

		try:
			with open(filename) as f_obj:
				contents = f_obj.read()
		except FileNotFoundError:
			msg = ('ERROR' + filename)
		else:
			#count words
			words = contents.split() #dzieli slowa na osobne stringi
			num_words = len(words)
			print(" file " + filename + ' has ' + str(num_words) + ' words.')
			
	def count_words(filename): # liczy slowa
		try:
			with open(filename) as f_obj:
				contents = f_obj.read()
		except FileNotFoundError:
			msg = ('ERROR' + filename)
		else:
			#count words
			words = contents.split() #dzieli slowa na osobne stringi
			num_words = len(words)
			print(" file " + filename + ' has ' + str(num_words) + ' words.')

	def countALL(self):
		filenames = ['alice_wonderland.txt', 'Moby_Dick.txt', 'Sherlock_Holmes.txt']
		for filename in filenames:
			Alice.count_words(filename)


if __name__ == '__main__':
	start = Alice()
	start.countALL()
	#start.alice_wonder()