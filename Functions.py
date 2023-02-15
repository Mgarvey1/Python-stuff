def hello():
    print("This is my first function")
hello()
def umbwa():
    print("we ni umbwa")
umbwa()
def calculate():
    x=10
    y=25
    print(x*y)
calculate()

#Functions buda
def majina(fname,lname):
    print(fname+" "+lname)
majina("Marcus","Garvey")
majina("Gideon","Masek")

def greetings(majina, greetings="Hello"):
    print(greetings+" "+majina)
greetings("Marcus")
greetings("alex", "niaje")

def rada(names, rada="Sema buda"):
    print(rada+" "+names)
rada("Timo")



def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(7,4,3,2,1,9)
print(result)

def minvalue(g,h,i,j,k,l,m):
    return min(g,h,i,j,k,l,m)
result=minvalue(12,43,13,76,97,42,54)
print(result)

def sort_list(list):
    return sorted(list)
answer=sort_list([39,125,94,34,443,3])
print(answer)

def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(100)



