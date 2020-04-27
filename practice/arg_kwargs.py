#/bin/python3

def simpleFunction(arg):
    return('arg: ' + arg)

print(simpleFunction('argy'))



def simpleFunctionNamedArgs(arg1='Argy', arg2=2):
    return( 'I am a function, these are my named arguments: arg1=' + arg1 + ', arg2=' + str(arg2))

print(simpleFunctionNamedArgs())

def multiArguments(*args):
    return(args) #returns a tuple
print (multiArguments('one', 'two', 'three'))

def multiArguments(*args):
    for arg in args:
        print(arg + 2)
multiArguments(10, 20, 30)

def multiKeywordedArguments(**kwargs):
    return(kwargs)

print(multiKeywordedArguments(kwarg1 = 'uno', kwarg2 = 'dos', kwarg3 = 'tres'))
