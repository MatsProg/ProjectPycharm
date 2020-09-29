class WriteFile:
	def file_write(self):
		print('START')
		plik = '_milion.txt'
		with open(plik, 'a') as plik_obj: # 'w' - clean+Write     'r' - read      'a' - append        'r+' - read and write       | without is readonly
			plik_obj.write("LOVE\n")
			plik_obj.write("CLEAN\n")


if __name__ == '__main__':
	run = WriteFile()
	run.file_write()