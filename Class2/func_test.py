def run1():
    print("Hello From My Function!")

    
def run2():
    return "Hello"

  
def run3(name):
    print(name)

 
def run4(name):
    return "Hello " + name

  
  
run1()
my_word = run2()
run3('daniel')
my_word = run4('daniel')

# empty return
def r():
if 1 > 0:
    print(1)
    return
if 1 > 0: # will never run!
    print(2)

    
# pass
def still_developing():
    pass
  
  
# yield  
def simple_fun():
    yield 1
    yield 2

for value in simple_fun():
    print(value > 1) 

