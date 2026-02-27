class CSP:
    def __init__(self, vars, domains, constraints):
        self.vars = vars
        self.domains = domains
        self.constraints = constraints

    def is_valid(self, var, val, assign):
        return all(c(var, val, assign) for c in self.constraints.get(var, []))

    def backtrack(self, assign={}):
        if len(assign) == len(self.vars):
            return assign

        var = next(v for v in self.vars if v not in assign)

        for val in self.domains[var]:
            if self.is_valid(var, val, assign):
                assign[var] = val
                result = self.backtrack(assign)
                if result:
                    return result
                assign.pop(var)
        return None
    
vars = ['A', 'B', 'C']
domains = {v: [1, 2, 3] for v in vars}

constraints = {
    'A': [lambda v, val, a: 'B' not in a or a['B'] != val],
    'B': [lambda v, val, a: 'A' not in a or a['A'] != val],
    'C': [lambda v, val, a: ('A' not in a or a['A'] != val) and
                             ('B' not in a or a['B'] != val)]
}

csp = CSP(vars, domains, constraints)
solution = csp.backtrack()

print("Solution found:" if solution else "No solution found.")
if solution:
    for k, v in solution.items():
        print(k, ":", v)
