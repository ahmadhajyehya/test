# try-except specific except
try:
    f = open("C:\\Users\dgotl\\testfile.txt", "r")
    f.write('123')
except IOError:
    print("Error: can't find file or read data")


# try-except bare-excpet
try:
    f = open("C:\\Users\dgotl\\testfile.txt", "r")
except:
    print('All kind of errors will be handled')

# try-except-finally
try:
    f = open("C:\\Users\dgotl\\testfile.txt", "r")
except IOError:
    print('Fatal error…')
finally:
    print('this will run anyway')

# try-finally
try:
    f = open("C:\\Users\dgotl\\testfile.txt", "r")
finally:
    print('this will run anyway')

    
    
# using with statement 
with open('file_path', 'w') as file: 
    file.write('hello world !') 
