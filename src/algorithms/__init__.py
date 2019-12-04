class Language:
    pass

class Problem:
    pass

class Entropy:
    def __call__(self, *args, **kwargs):
        pass

class Force:
    def __call__(self, *args, **kwargs):
        pass

class Macrostate:
    env = None
    t_0 = None
    x_0 = None

    def __init__(self, env=None, x_0=None, t_0=None):
        pass



class Temperature:
    def __mul__(self, other):
        pass

class System:
    # thermodynamic / probability
    def __init__(self, *args, **kwargs):
        pass

class Microstate:
    pass

class Base:
    pass    

class Algorithm:
    # _input = None
    # _output = None
    
    # initialization
    # maintainace 
    # termination
    #@property
    #def input(self):
    #     pass
    #@property
    #def output(self):
    #     pass
    #def main(self):
    #     pass
    def __init__(self, *args,**kwargs):
        pass
  
    @staticmethod
    def solve(problem):
        pass

class CausalPathEntropy(Entropy):
    def __call__(self, macrostate, tau, *args, **kwargs):
        pass

class CausalEntropicForce(Force):
    def __call__(self, macrostate_0, tau=None, *args, **kwargs):
        pass
    

class ForceComponent(CausalEntropicForce):
    j = None

    def __init__(self, j):
        self.j = j
    
    def __call__(self, macrostate_0, tau=None, *args, **kwargs):
        pass

#u_t system input
    
def system_output(t, x_t, u_t):
    pass

def state_vector_first_derivative(t_0, t, x_t, x_0, u_t):
    pass

class MaximizeCausalForce(Algorithm):
    def solve(F, X_0, *args, **kwargs):
        pass



