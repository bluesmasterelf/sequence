"""A function which produces specified outputs on natural number inputs.
"""

from sympy import *

def sequence(*args):
    """Function takes numerical args and produces a function which outputs the nth arg on n
    I hope to add the capacity to accept inputs to replace natural n for positional inputs. 
    Using the sympy library, it can build functions using symbolic logic such as a function that is 'a' at input 1 and '2' at input 2 and 'pi' at input 3.
    """
    #sum_j frac{prod_(i!=j) x-a_i}{prod_(i!=j)(a_i-a_j)}*b_j
    #args are the b_j
    #a_i default to range(len(args))
    args2=range(len(args))

    n=Symbol('n')

    function=0
    for j in args2:
        summand=1
        numerator=1
        denominator=1

        for i in args2:
            if i != j:
                numerator=numerator*(n-i)
                denominator=denominator*(j-i)

        summand=summand*args[j]*numerator/denominator
        function=function+summand

    print(function)

    for arg in args2:
        print("The output for " + str(arg+1) + "is:"+ str(function.evalf(subs={n:arg})))



if __name__=='__main__':
    args=[]
    numTerms=input('how many terms?')
    numTerms=int(numTerms)
    for term in range(numTerms):
        temp=input('next term:')
        args.append(eval(temp))#WARNING: eval will execute user code and presents a security risk in general

    #args=(2,pi,1,-16.2)

    sequence(*args)
