from lstack import Stack

def mystr(anInteger):   
    myStack = Stack()
    aString = ''
    value =  int(anInteger)
    if value <0 :
        negative = True
        value = abs(value)
    else:
        negative = False

    if value == 0:
        digit = chr(48)
        aString = digit
    else:
        while value > 0:
            newValue= value%10
            value = int(value/10)
            myStack.push(newValue)


        while not myStack.isEmpty():
            item = myStack.pop()
            digit = chr(item + 48)
            aString = aString + digit

    if negative is True:
        aString = '-' + aString
    else:
        aString = aString
        
    print(aString)
    return aString

    
def evalPostfix(postfixExpression):
    myStack=Stack()
    postList =postfixExpression.split()    
    for token in postList:
       if token not in "+*/-":
            item = float(token)
            myStack.push(item)


       elif token == "+" :
           assert len(myStack) >= 2
           left = myStack.pop()
           right = myStack.pop()
           result = left + right
           myStack.push(result)



       elif token == "*":
           assert len(myStack) >= 2, 'Too few operands on stack'
           left = myStack.pop()
           right = myStack.pop()
           result = left * right
           myStack.push(result)


       elif token == "/":
           assert len(myStack) >= 2
           right = myStack.pop()
           left = myStack.pop()

           if right == 0:
               raise ValueError
           else:
               result = left / right
               myStack.push(result)


       else:
           assert len(myStack) >= 2
           left = myStack.pop()
           right = myStack.pop()
           result = right - left
           myStack.push(result)

    print(result)
    myStack.pop()
    if len(myStack) ==0:
        return result
    
    else:
        raise AssertionError
        return None
        
evalPostfix(input('Enter a postfix expression: '))


def evalPrefix(prefixExpression):
    preList =prefixExpression.split()
    myOtherStack=Stack()
    myRealStack=Stack()
    for token in preList:
        while not preList .isEmpty():
            reverse=preList.pop()
            myRealStack.push(reverse)
            print(reverse)


evalPrefix(input('Enter a prefix expression: '))
