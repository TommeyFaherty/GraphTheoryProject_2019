#Thompson's construction

class state:
    label = None
    edge1 = None
    edge2 = None

class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    nfastack = []

    for c in pofix:
        if c == '.':
            # Pop two NFA'S off the stack
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Connect first NFA'S accept state to the second's initial
            nfa1.accept.edge1 = nfa2.initial
            # Push NFA to the stack
            nfastack.append(nfa(nfa1.initial,nfa2.accept))
        elif c == '|':
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Create a new initial state, connect it to initial states
            # of the two NFA'S popped from the stack
            initial = state()
            initial.edge1,initial.edge2 = nfa1.initial, nfa2.initial
            # Create a new accept state,connecting the accept states
            # of the two NFA'S pooped from the stack, to the new state
            accept = state()
            nfa1.accept.edge1, nfa2.accept.edge1 = accept, accept
            nfastack.append(nfa(initial, accept))
        elif c == '*':
            nfa1 = nfastack.pop()
            initial, accept = state(), state()
            # Join the new initial state to nfa's initial state and the new accept state
            initial.edge1, initial.edge2 = nfa1.initial, accept
            # Join the old accept state to the new accept state and nfa's initial state
            nfa1.accept.edge1, nfa1.accept.edge2 = nfa1.initial, accept
            nfastack.append(nfa(initial, accept))
        elif c == '+':
            nfa1 = nfastack.pop()
            initial, accept = state(), state()
            # Join the new initial state tot he nfa's initial state
            initial.edge1 = nfa1.initial
            # Join the old accept state to the new accept state and the nfa's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            nfastack.append(nfa(initial, accept))
        elif c == '?':
            nfa1 = nfastack.pop()
            accept, initial = state(), state()
            # new initial
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # new accept
            nfa1.accept.edge1 = accept
            nfastack.append(nfa(initial,accept))
        else:
            # Create new initial and accept states
            initial, accept = state(), state()
            # Join the initial state the accept state using an arrow labelled c
            initial.label,initial.edge1 = c, accept
            nfastack.append(nfa(initial, accept))

    # nfastack should only have a single nfa on it at this point
    return nfastack.pop()
