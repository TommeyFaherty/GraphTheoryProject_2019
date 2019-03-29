#Shunting

def shunt(infix):

    specails = {'*': 50, '.': 40, '|': 30, '+': 50, '?': 50}

    pofix = ""
    stack = ""

    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                pofix,stack = pofix + stack[-1],stack[:-1]
                # would be stack = stack[:-1] if two lines
            stack = stack[:-1]
        elif c in specails:
            while stack and specails.get(c,0) <= specails.get(stack[-1],0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix, stack = pofix + stack[-1],stack[:-1]

    #print("postfix: "+pofix)
    return pofix


