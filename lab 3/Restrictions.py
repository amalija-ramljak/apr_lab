import numpy as np

class Restrictions():
    def __init__(self, lower_border=-np.inf, upper_border=np.inf, implicit_ineq=[], implicit_eq=[]):
        self.lower_border = lower_border
        self.upper_border = upper_border
        self.implicit_ineq = implicit_ineq
        self.implicit_eq = implicit_eq
    
    def get_lower(self):
        return self.lower_border

    def get_upper(self):
        return self.upper_border
    
    def get_implicit(self):
        return self.implicit_eq.extend(self.implicit_ineq)
    
    def get_inequalities(self):
        return self.implicit_ineq
    
    def get_equalities(self):
        return self.implicit_eq
    
    def check_all(self, x):
        return self.check_explicit(x) and self.check_implicit(x)
    
    def check_explicit(self, x):
        for i in range(len(x)):
            xi = x[i,0]
            if xi < self.lower_border[i,0] or xi > self.upper_border[i,0]:
                return False
        
    def check_implicit(self, x):
        return self.check_equalities(x) and self.check_inequalities(x)
    
    def check_inequalities(self, x):
        for res in self.implicit_ineq:
            if not res(x) >= 0:
                return False
        return True

    def check_equalities(self, x):
        for res in self.implicit_eq:
            if not res(x) == 0:
                return False
        return True
    
    def change_lower(self, lower_border):
        self.lower_border = lower_border
    
    def change_upper(self, upper_border):
        self.upper_border = upper_border

    def add_implicit_equality(self, new_implicit):
        self.implicit_eq.append(new_implicit)

    def add_implicit_inequality(self, new_implicit):
        self.implicit_ineq.append(new_implicit)

    def change_implicit(self, new_implicit):
        self.implicit = new_implicit