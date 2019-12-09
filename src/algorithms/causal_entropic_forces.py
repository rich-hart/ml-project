#!/usr/bin/env python
# coding: utf-8

# In[8]:


try:
    from . import Algorithm
except ImportError:
    from __init__ import Algorithm


# $\textbf{F} \equiv \textrm{the entropic force associated with a macrostate partition}$

# $\textbf{X} \equiv \textrm{macrostate}$

# $\textbf{\{X\}} \equiv \textrm{macrostate partition}$

# $\textbf{X}_{0} \equiv \textrm{the present (current) macrostate}$

# $S(\textbf{X}) \equiv \textrm{is the entropy associated with a macrostate $\textbf{X}$}$

# $T \equiv \textrm{the reservoir temperature}$

# $\textbf{F}(\textbf{X}_{0})=T\nabla_\textbf{X}S(\textbf{X})|_{\textbf{X}_{0}}$ 

# <cite data-cite="Wissner2013">(Cite:Wissner2013)</cite>

# NOTE: Figure out how to switch between unsupervised and supervised learning. 

# In[9]:


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
        self.env = env
        self.t_0 = t_0
        self.x_0 = x_0

class Temperature:
    def __mul__(self, other):
        pass

class System:
    # thermodynamic / probability
    def __init__(self, *args, **kwargs):
        pass

class Microstate:
    pass


# project plan
# 

# DEFINE AGENT DRIVER SENSOR ACUATOR CLASSES

# DEFINE GRAPH

# DEFINE PROTECTED BASE CLASS ABSTRACT / PROTECTED. FOR AI NAMESPACE (MIGHT BE OVERBOARD IN A LOT OF CASES/execpt DATABSE models for created / updated timestamps, we'll see)

# 

# start proof

# In[ ]:





# $S_{c} \equiv \textrm{causal path entropy}$

# $x \equiv \textrm{phase-space function}$

# $x(t) \textrm{  for } 0 \leq t \leq \tau \equiv \textrm{microstates}$

# In[3]:


class CausalPathEntropy(Entropy):
    def __call__(self, macrostate, tau, *args, **kwargs):
        pass


# 

# Let $X$ be a random variable,  with a probability density function $f$ whose support is a set $\chi$
# 
# Differential entropy is 
# 
# $$H(X)=-\int_{\chi}f(x)\log{f(x)}dx$$
# 
# Change variables and let $x -> x(t)$
# 
# (wikipedia, https://en.wikipedia.org/wiki/Differential_entropy)

# can be approximated by producing a histogram of the observations, and then finding the discrete entropy (https://en.wikipedia.org/wiki/Entropy_estimation)
# 
# $$H(X) = -\sum_{i=1}^{n} f(x_i)\log{ {\left( \frac{f(x_i)}{w(x_i)} \right)}}$$
# 
# of that histogram (which is itself a maximum-likelihood (ML) estimate of the discretized frequency distribution[citation needed]), where w is the width of the ith bin. 

# In[7]:


class CausalEntropicForce(Force):
    
    def __call__(self, macrostate_0, case, tau=None, T_r=1, T_c=1, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        
        
        if case=='newtonian':
            x_0 = macrostate_0.x_0
            agent = macrostate_0.observer
            
            force = -1 * 2 * (T_c/T_r) * 1  
        else:
            raise NotImplementedError("No general case defined")

class ForceComponent(CausalEntropicForce):
    j = None

    def __init__(self, j):
        self.j = j
    
    def __call__(self, macrostate_0, tau=None, *args, **kwargs):
        pass


# In[5]:


def system_output(t, x_t, u_t):
    pass

def state_vector_first_derivative(t_0, t, x_t, x_0, u_t):
    pass

class MaximizeCausalForce(Algorithm):
   # _T_c = None
  #  _T_r = None
    
    #def __init__(self, T_c, T_r):
   #     self._T_c = T_c
    #    self._T_r = T_r

    #@property
    #def T_c(self):
    #    return self._T_c
    
    #@property
    #def T_r(self):
    #    return self._T_r
    
    #def 
    @staticmethod
    def solve(F, X_0, case='newtonian', tau=None, T_r=1, T_c=1, *args, **kwargs):
        entropic_force = F(X_0, case, tau, T_r, T_c, *args, **kwargs)
        return entropic_force


# In[ ]:





# In[ ]:




