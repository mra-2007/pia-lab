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


vars = ['X', 'Y', 'Z']
domains = {v: [1, 2, 3, 4] for v in vars}

constraints = {
    'X': [
        lambda v, val, a: 'Y' not in a or val < a['Y']
    ],
    'Y': [
        lambda v, val, a: 'X' not in a or a['X'] < val,
        lambda v, val, a: 'Z' not in a or val < a['Z']
    ],
    'Z': [
        lambda v, val, a: 'Y' not in a or a['Y'] < val,
        lambda v, val, a: not ('X' in a and 'Y' in a and a['X'] + a['Y'] == val)
    ]
}

csp = CSP(vars, domains, constraints)
solution = csp.backtrack()

print("Solution found:" if solution else "No solution found.")
if solution:
    for k, v in solution.items():
        print(k, ":", v)
