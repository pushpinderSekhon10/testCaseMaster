# Importing a module random 
import importlib 

def hardcode():
    mod = importlib.import_module('samplecode')

    class_obj = getattr(mod, "Calculator")

    # Using randint function of random 
    # module as r 
    meth = getattr(class_obj, 'multiply') 
    # getattr(class name, func name)

    # calling the function and storing 
    # the value in res 
    res = meth(class_obj, 2, 9) 

    # Printing the result 
    print(res)

'''
def find_method(mod_name, class_name, method_name):
    mod = importlib.import_module(mod_name)
    class_obj = getattr(mod, class_name)
    method = getattr(class_obj, method_name)
    return method, class_obj


def myFun(*argv):
    for arg in argv:
        print(arg)


#!!!
def run_method(method, class_obj, *args):
    res = method(class_obj, *args)
    print(res)


#myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

method, classobj = find_method('samplecode', 'Calculator', 'multiply')
run_method(method, classobj, 2, 9)
'''