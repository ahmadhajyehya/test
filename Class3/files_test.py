# read from file 
my_file = open('C:/Python33/README.txt', 'r')
content = my_file.read()
print(content)

# write to file 
my_file = open('C:/Python33/README.txt', 'r+')
my_file.write('text to add')

# use encoding
my_file = open('C:/Python33/README.txt', 'r' , encoding='utf-8')

# close file
my_file.close()
