
""" 
Nadia Aly, April 1, 2015, CSCI 241, Lab 5: Stack-Based Tools
This lab uses the stack abstract data structure to make a prefix and 
postfix expression evaluator. Prefix and postfix
expression are used to take care of the order of operations and compute 
values of expressions that typically use parenthesize to show that an
operation is performed before another. The order of the operations in this 
lab are: are espectively; Multiplication, Division, Addition, Subtraction.
The stack is used to input an integer value and store to type string. 
A computer does not automatically no what order to perform operations in so 
the structure of the prefix or postfix expression accounts for this along
with our algorithm.
"""


from lstack import Stack
#import or Stack Abstract Data Structure from module

def mystr(anInteger):
    '''Accepts an input integer, negative or positive and converts to a string. The algorithim works by using a loop

    as long as the absolute value of our remainder (absolute value is used to take care of negative cases) finds the

    remainder of the value divided by 10 (module finds remainder) and pushes the remainder on to the top of the stack,

    the newValue variable is then used to store the next loop which takes the original value/ 10 (less remainder-

    int takes care of this).

    '''
    myStack = Stack()
    #initialize stack
    aString = ''
    #Initialize string
    value = int(anInteger)
    if value < 0:
        '''Checks to see if the input is negative, if this is negative stores a boolean value of True for variable

        negative, take the absolute value of the integer if it negative for the while loop condition (greater than 0)

        to iterate. the Boolean value is then checked later and a (-) is added to the string.
        '''
        negative = True
        value = abs(value)
    else:
        negative = False

    if value == 0:
        #0 is a special condition because 0 mod 10 will never be greater than 0. Add 48 to get string storage of
        # character 0.
        digit = chr(48)
        aString = digit
    else:
        while value > 0:
            newValue = value % 10
            value = int(value / 10)
            myStack.push(newValue)

        while not myStack.isEmpty():
            '''Takes the stack after it has stored all of the remainders. Pops the remainder off the top to iterate to

            the next remainder and adds 48 to the integer value to store as a character in string. Coincentrates remainder

            to the previous remainder's string.

            '''
            item = myStack.pop()
            digit = chr(item + 48)
            aString = aString + digit

    if negative is True:
        #if negative true coincintrate (-) to the string
        aString = '-' + aString

    else:
        aString = aString


    return aString


def evalPostFix(postfixExpression):
    '''The evalPostFix operation takes a postfix Expression and computers the value of the expression.

     Essentially PostFix works by initializes an empty stack and stores tokens until they are needed.

    The operands are pushed onto the stack first, once we encounter an operator, the top two operands are popped off

    the stack and return the result to top of the stack. In postfix, the top value is the right hand operand while

    the next to top value is the left operand. (This is important when order matters.) if there is another operand

    (and operator) - pop them off of the stack and evaluate the expression again  return the value to the stack

     repeat until there is only one operand token left on stack.
    '''

    myStack = Stack()
    postList = postfixExpression.split()
    for token in postList:
        '''The string is split, which places each token separated by a white space into a list. Iterates over the list

        containing the tokens from the string, we are assuming only real numbers and the only operations entered are

        addition, subtraction, division, and multiplication.

        Precondition for operations: Assert that the stack has at least two elements on before popping off two operands.

            If this is not done, then we would encounter an error from the Stack ADT because you can not pop from an

            empty list. If the list is empty, this is one of the possible errors in which there are two few operands

            or user has input an invalid postfix expression.

            The for loops just tells what we have, and identifies the operator, perform that operation.
        '''
        if token not in "+*/-":
            '''
            We are assuming only real numbers and the only operators: multiplication, division, subtraction, and

            addition are entered. This checks and if  token is not an operator, appends or pushes to operand stack.
            '''
            item = float(token)
            myStack.push(item)

        elif token == "+":
            '''Identifies what operator we have, if it is a plus, pop two operands off the stack and add these together.

            Order of operation does not matter, but first token popped off is set as RHS operand and second item is LHS.
            '''
            assert len(myStack) >= 2
            right = myStack.pop()
            left = myStack.pop()
            result = right + left
            myStack.push(result)

        elif token == "*":
            '''Identifies what operator we have, if it is a * (multiplication sign), pop two operands off the stack

            and add these together. Order of operation does not matter for multiplication, but we set the first token from

            the stack  as the RHS and the second token as the LHS operand. pre-condition explained earlier.
            '''
            assert len(myStack) >= 2, 'Too few operands on stack'
            right = myStack.pop()
            left = myStack.pop()
            result = right * left
            myStack.push(result)


        elif token == "/":
            '''Identifies what operator we have, if it is a / (division sign), pop two operands off the stack the order of

            operation does matter for division, so we set the first token popped off as the right hand operator and

            the second token is the LHS operator, then divide left by right. Ex: 8 3 / is then RHS=3  LHS=8.
            '''
            assert len(myStack) >= 2
            right = myStack.pop()
            left = myStack.pop()

            if left == 0:
                #Make sure that we are not dividing by 0 because we cannot divide a determinate form function or value
                # by 0, Raise value error and stop iteration
                raise ValueError
                return None
            else:
                result = left / right
                myStack.push(result)

        else:
            '''Identifies what operator we have, this is else, so by now we have identified all other operand and operator

            values, so -, subtraction sign is automatically classified. pop two operands off the stack. the order of

            operation does matter for subtraction, so we set the first token popped off as the right hand operator and

            the second token is the LHS operator, then subtract left from right. Ex: 8 3 - is then RHS=8  LHS=3
            '''
            assert len(myStack) >= 2
            right = myStack.pop()
            left = myStack.pop()
            result = left - right
            myStack.push(result)

    myStack.pop()
    if myStack.isEmpty():
        '''After the entire expression is evaluated, this  checks to make sure the stack is empty after we pop off our

        result. The condition is used to make sure that a valid expression has been provided and we have not been

        given too many operands.

        '''

        print(result)
        return result
    else:
        return None


evalPostFix(input('Enter a postfix expression: '))


def evalPrefix(prefixExpression):
    '''The evalPreFix operation takes a prefix Expression and computers the value of the expression.

    Prefix evaluator is similar to postfix. The order of the string is reversed. Initializes an empty stack and stores

    operands until they are needed. The operands are pushed onto the stack first, once we encounter an operator,

    the top two operands are popped off the stack and return the result to top of the stack.

    In prefix, because the order is reversed, the top value is the left hand operand while the next to top value is the

    right-hand operand. (This is important when order matters.) if there is another operand

    (and operator) - pop them off of the stack and evaluate the expression again  return the value to the stack

     repeat until there is only one operand token left on stack.

        '''

    aString = prefixExpression.split()
    myStack = Stack()
    newString = aString[::-1]
    #Python function to reverse the order of a string, could have done this with myStr, but this is easier and probably
    #more efficient
    for token in newString:

        if token not in "+*/-":
            ''' Once again, We are assuming only real numbers and the only operators: multiplication, division, subtraction, and

            addition are entered. This checks and if  token is not an operator, appends or pushes to operand stack. uses

            a float in case a decimal is entered or if an operation stores a value that is not integer, but is real.
            '''
            item = float(token)
            myStack.push(item)

        elif token == "+":
            '''Identifies what operator we have, if it is a plus, pop two operands off the stack and add these together.

            Order of operation does not matter, but first token popped off is set as LHS operand and second item is RHS.
            '''
            assert len(myStack) >= 2
            left = myStack.pop()
            right = myStack.pop()
            result = left + right
            myStack.push(result)

        elif token == "*":
            '''Identifies what operator we have, if it is a * (multiplication sign), pop two operands off the stack

            and add these together. Order of operation does not matter for multiplication, but we set the first token from

            the stack  as the LHS and the second token as the RHS operand. pre-condition explained earlier.
            '''
            assert len(myStack) >= 2, 'Too few operands or Invalid expression'
            left = myStack.pop()
            right = myStack.pop()
            result = left * right
            myStack.push(result)


        elif token == "/":
            '''Identifies what operator we have, if it is a / (division sign), pop two operands off the stack the order of

            operation does matter for division, so we set the first token popped off as the Left hand operator and

            the second token is the RHS operator, then divide right by left. Ex: /8 3  is then RHS=8  LHS=3.
            '''
            assert len(myStack) >= 2
            left = myStack.pop()
            right = myStack.pop()

            if right == 0:
                #Make sure that we are not dividing by 0 because we cannot divide a determinate form function or value
                # by 0, Raise value error and stop iteration
                raise ValueError
            else:
                result = left / right
                myStack.push(result)

        else:
            '''Identifies what operator we have, this is else, so by now we have identified all other operand and operator

        values, so -, subtraction sign is automatically classified. pop two operands off the stack. the order of

        operation does matter for subtraction, so we set the first token popped off as the left hand operator and

        the second token is the RHS operator, then subtract the right operand from the left.

        Ex: - 8 3  is then RHS=3  LHS=s
        '''
            assert len(myStack) >= 2
            left = myStack.pop()
            right = myStack.pop()
            result = left - right
            myStack.push(result)


    myStack.pop()
    if myStack.isEmpty():
        '''After the entire expression is evaluated, this  checks to make sure the stack is empty after we pop off our

        result. The condition is used to make sure that a valid expression has been provided and we have not been

        given too many operands.

        '''
        print(result)
        return result
    else:
       
        return none




evalPrefix(input('Enter a prefix expression: '))
