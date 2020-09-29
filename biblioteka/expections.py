class Except:
	def excpetions(self):
		print('START')
		try:
			print(5/0)
		except:
			print('ERROR')
		print('STOP')

		while True:
			f_n = input('\n First Number' )
			if f_n == 'q':
				break
			s_n = input('\n Sec Num')
			if s_n == 'q':
				break
			try:
				solve = int(f_n) / int(s_n)
			except:
				print('\nERROR')

			else:
				print('\n  result is'+ str(solve))
				break
	def filename(self):

		filename = '_milion.txt'
		try:
			with open(filename) as f_obj:
				contents = f_obj.read()
		except FileNotFoundError:
			msg = 'sorry file   ' + filename + '    does not exist.'
			print(msg)
		else:
			print("OK")



if __name__ == '__main__':
	start = Except()
	start.filename()
	start.excpetions()