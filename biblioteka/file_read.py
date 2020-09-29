class ReadFile:
	def start_read(self):
		with open('_reader1.txt') as file_object: #open file
			contents = file_object.read()
			print(contents)
			#or
			#print(contents.rstrip())
	#wejscie do folderu
		with open('1st/_reader2.txt') as file_object1: #open file from folder
			contents2 = file_object1.read()
			print(contents2)
	# absolute path
		#file_path ='C:\\Users\\MatsProg\\Documents\\GitHub\\read3.txt'
		#or
		file_path = 'C:/Users/MatsProg/Documents/GitHub/read3.txt'  #open file from path
		with open(file_path) as file_object3:
			contents3 = file_object3.read()
			print(contents3)

		filename = '_filename1.txt'
		with open(filename) as file_object4: #print file in for loop
			for line in file_object4:
				print(line.rstrip().title())

		#edit file
		with open(filename) as file_object5: #edycja read file
			lines = file_object5.readlines()
		for line in lines:
			print(line.rstrip())

		edit = ''
		for line in lines:
			edit += line.rstrip().strip() #obcina spacje z prawej R i z lewej STRIP
		print(edit + ' STORED IN LIST')
		print(str(len(edit)) + ' QTY CHAR')

		filenameM = '_milion.txt'
		with open(filenameM) as file_object6:
			lines = file_object6.readlines()
		edit1 = ''
		for line in lines:
			edit1 += line.strip().rstrip()
		print(edit1[:10] + "...") #print pierwsze 10
		print(len(edit1)) #char length

		birthday = input("Enter birthday mmddyy \n")
		print("you typed " + birthday)
		if birthday in edit1:
			print("You birthday is in \n")
		else:
			print("Your birthday isn't \n")




start = ReadFile()
start.start_read()

if __name__ == '__main__':
	pass