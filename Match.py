from Shunting import shunt
from Thompson import compile

def followes(state):
    #Return set of states that can be reached from the arrows
    states = set()
    states.add(state)

    # Check if state has arrows labelled e from it
    if state.label is None:
        #Check if edge1 is a state
        if state.edge1 is not None:
            # |= means union
            states |= followes(state.edge1)
        if state.edge2 is not None:
            states |= followes(state.edge2)

    return states

def match(infix, string):
    pofix = shunt(infix)
    nfa = compile(pofix)
    #print("Postfix: "+pofix)

    # Current set of states and the next set of states
    current = set()
    next = set()

    # Check if that state is labelled s
    current |= followes(nfa.initial)

    # Loop through each character in the string
    for s in string:
        for c in current:
            # Check if state is labelled s
            if c.label == s:
                # Add the edge1 state to the next set
                next |= followes(c.edge1)
        # set current to next abd clear out next
        current = next
        next = set()

    return (nfa.accept in current)
string = {"ab","ac","abc","a","acc","abb"}
#infixes = {"a.(b|c*)",

for s in string:
    print(s,match("a.(b|c+)",s))