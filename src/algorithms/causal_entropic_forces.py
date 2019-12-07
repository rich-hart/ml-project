#!/usr/bin/env python
# coding: utf-8

# In[5]:


from . import Algorithm


# $\textbf{F} \equiv \textrm{the entropic force associated with a macrostate partition}$

# $\textbf{X} \equiv \textrm{macrostate}$

# $\textbf{\{X\}} \equiv \textrm{macrostate partition}$

# $\textbf{X}_{0} \equiv \textrm{the present (current) macrostate}$

# $S(\textbf{X}) \equiv \textrm{is the entropy associated with a macrostate $\textbf{X}$}$

# $T \equiv \textrm{the reservoir temperature}$

# $\textbf{F}(\textbf{X}_{0})=T\nabla_\textbf{X}S(\textbf{X})|_{\textbf{X}_{0}}$ 

# <cite data-cite="Wissner2013">(Cite:Wissner2013)</cite>

# NOTE: Figure out how to switch between unsupervised and supervised learning. 

# In[2]:


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

class CausalEntropicForce(Force):
    def __call__(self, macrostate_0, tau=None, *args, **kwargs):
        pass
    

class ForceComponent(CausalEntropicForce):
    j = None

    def __init__(self, j):
        self.j = j
    
    def __call__(self, macrostate_0, tau=None, *args, **kwargs):
        pass


# In[4]:


def system_output(t, x_t, u_t):
    pass

def state_vector_first_derivative(t_0, t, x_t, x_0, u_t):
    pass

class MaximizeCausalForce(Algorithm):
    def solve(F, X_0, *args, **kwargs):
        pass


# In[ ]:





# In[ ]:




