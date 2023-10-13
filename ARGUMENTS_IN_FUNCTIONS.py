#Required Arguments
def display(a,b):
    print(a,b)
display(20,10)

#Keyword Arguments
def display(a,b):
    print(a,b)
display(b=20,a=10)

#Default Arguments
def display(name,course='B-Tech'):
    print(name)
    print(course)
display('Prem')
display('chand','M-Tech')

#Variable Length Arguments
def display(*courses,):
    for i in courses:
        print(i)
display('b-tech','inter','10')

