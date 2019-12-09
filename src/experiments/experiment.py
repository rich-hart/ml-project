#!/usr/bin/env python
# coding: utf-8

# In[108]:


import bayespy
import gym
from algorithms import Algorithm
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

from bayespy.nodes import (Gaussian,
                           SwitchingGaussianMarkovChain,
                           CategoricalMarkovChain,
                           Categorical,
                           Dirichlet,
                           Mixture,
                           Gamma,
                           SumMultiply,Wishart)

from bayespy.inference.vmp.vmp import VB
from bayespy.inference.vmp import transformations

import bayespy.plot as bpplt


# In[2]:


env = gym.make('CartPole-v1')


# In[3]:


env.action_space


# In[4]:


help(env.action_space)


# In[5]:


env.action_space.n


# In[6]:


env.observation_space


# In[7]:


help(env.observation_space)


# In[8]:


env.observation_space.shape


# In[9]:


env.observation_space.high


# In[10]:


env.observation_space.low


# In[11]:


len(env.observation_space.shape)


# In[12]:


observation_space_dimention = len(env.observation_space.shape)


# In[13]:


from agents import Agent, Policy, RandomPolicy, RandomAgent, Engineer, Scientist



    


# In[14]:


random_agent = RandomAgent(env=env)


# In[15]:


random_agent


# In[16]:


random_action = random_agent.policy(env.observation_space.sample())


# In[17]:


random_action


# In[18]:




class Database:
    pass

# Make context manager
class Experiment:
    description = None
    procedure = None
    database = None
    start = None
    stop = None
    
    _data = None

    def __init__(self,desciption, procedure, database, *args,**kwargs):
        self.desciption = desciption
        self.procedure = procedure
        self.database = database
        
        
    def begin(self):
        self.start = datetime.now()
    
    def end(self):
        self.stop = datetime.now()

class Trial:
    pass



class Procedure(Algorithm):
    name = None
    def __init__(self,*args,**kwargs):
        pass

class Conclusion:
    pass

class Hypothesis:
    pass


# In[19]:


class Variable:
    pass

class RandomVariable:
    pass



class Network:
    pass

class BayesNetwork(Network):
    pass

class Knowledge(BayesNetwork):
    pass



#Procedures
#class Material:
#    pass
#
#class Tool:
#    pass



# In[ ]:





# In[20]:


#Experiment agent=Random, env = 'CartPole-v1', trials = 10, desciption="question: what effect does a random agent have on the CartPole-v1 enviroment?"


# In[21]:


# state_0 --> action_0 or action_1  --> state_1 -->> action_0 or action_1 --> ... --> state_n # or state_N


# In[22]:


scientist = Scientist('scientist')


# In[ ]:





# In[23]:


class Node:
    pass

class Edge:
    pass

class Vertex(Node):
    pass
class Serializer: #SEE Django, Django RestFramework, neo4j
    pass


# In[24]:


#NOTE:An algorithm is a procedure for solving a problem in terms of the actions to be executed and the order in which those actions are to be executed. An algorithm is merely the sequence of steps taken to solve a problem. The steps are normally "sequence," "selection, " "iteration," and a case-type statement.


#NOTE: In C, "sequence statements" are imperatives. The "selection" is the "if then else" statement, and the iteration is satisfied by a number of statements, such as the "while," " do," and the "for," while the case-type statement is satisfied by the "switch" statement.


# In[25]:


####
####
# NOTE: Example Experment (Temp class definitions until I think of better ones).
####
####


# In[26]:


import pandas as pd

class ExampleScientist(Scientist):
    def execute(self, procedure, database, env, subject, *args,**kwargs):
        procedure.run(env=env,subject=subject,scientist=self,database=database, *args, **kwargs)
    
    def record(self, data, database,*tables):
        database.insert(data,*tables)
    
    def analyze(self, experiment):
        #import ipdb; ipdb.set_trace()
        conn = experiment.database.conn
        c = conn.cursor()
    
        c.execute("select * from observations")
        observations = c.fetchall()
        
        for obs in observations:
            trial, x, x_dot, phi, phi_dot, n = obs
            
        c.execute("select * from actions")
        actions = c.fetchall()

        c.execute("select * from trials")
        trials = c.fetchall()
        
        conn.close()
        
class ExampleProcedure(Procedure):
    def __init__(self, name, trials=10, steps=1000,*args,**kwargs):
        self.name = name
        self.trials = trials
        self.steps = steps

    
    def run(self, env, subject, scientist, database, *args,**kwargs):

        
        for trial in range(1,self.trials+1):
            
            #data['trial'] = trial
            obs = env.reset()
            data = {
                'trial': trial,
                'obs': obs,
                'action': -1, #reset
                'agent': scientist.name,
                'step': -1,
                'rew': None,
                'done': None,
                'info': None,
            }
            
            #data['agent'] = scientist.name
            #data['action'] = 'reset'
            #data['obs'] = obs
            
            scientist.record(data,database,'trials','observations','actions')
            for step in range(self.steps):
                action = subject.policy(obs)
                obs, rew, done, info = env.step(action)
                data['obs'] = obs
                data['agent'] = subject.name
                data['action'] = action
                data['step'] = step
                data['rew'] = rew
                data['done'] = done
                data['info'] = info
                scientist.record(data,database,'observations','actions')
                if done:
                    break
        env.close()
        
#import gym
#env = gym.make('CartPole-v0')
#env.reset()
#for _ in range(1000):
#    env.render()
#    env.step(env.action_space.sample()) # take a random action
#env.close()
class ExampleExperiment(Experiment):
    pass


# In[27]:


import sqlite3
class ExampleDatabase(Database):
    db_filename = None
    _conn = None
    def __init__(self, db_filename):
        self.db_filename = db_filename
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
        # trial has many observations
        # trial has many actions
        c.execute('''CREATE TABLE trials (number integer)''')
        c.execute('''CREATE TABLE observations (trial_id integer, cart_position real, cart_velocity real, pole_angle real, pole_velocity_at_tip real, step integer, FOREIGN KEY (trial_id) REFERENCES trials(number))''')
        c.execute('''CREATE TABLE actions (trial_id integer, agent text,action integer, step integer, FOREIGN KEY (trial_id) REFERENCES trials(number))''')
        # create tables for other data....
        conn.close()
        
    def insert(self,data, *tables):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        
        if 'trials' in tables:
            command = "INSERT INTO trials VALUES (?)"
            values = (data['trial'],)
            c.execute(command, values)
            
        if 'observations' in tables:
            command = "INSERT INTO observations VALUES (?, ?, ?, ?, ?, ?)"
            values = (
                data['trial'],
                data['obs'][0],
                data['obs'][1],
                data['obs'][2],
                data['obs'][3],
                data['step'],
            )
            c.execute(command, values)
            
        if 'actions' in tables:
            command = "INSERT INTO actions VALUES (?, ?, ?, ?)"
            values = (data['trial'], data['agent'], data['action'],data['step'])
            c.execute(command,values)
        conn.commit()
        conn.close()

    @property
    def conn(self):
        if not self._conn:
            self._conn = sqlite3.connect(self.db_filename)
        return self._conn
    


# In[28]:


env.close()


# In[ ]:





# In[31]:


database = ExampleDatabase('example.db')


# In[32]:


procedure = ExampleProcedure('example')
desciption = "question: what effect does a random agent have on the CartPole-v1 enviroment?" "We what to show that given env and random agent, 1) observation does not imply random agent action " "2) random agent action implies observation"
experiment = ExampleExperiment(desciption=desciption,procedure=procedure,database=database)
env = gym.make('CartPole-v1')
random_agent = RandomAgent(env=env, name='random_agent')
scientist = ExampleScientist('scientist')


# In[33]:


scientist.conduct(experiment,env,random_agent)


# In[ ]:





# $ Trials = \{i |i \in \mathbb{N}\text{ and } i \leq 10  \}$
# 
# 
# $ AgentActionSpace = \{0, 1\}$
# 
# $ ActionSpace = AgentActionSpace \cup \{-1\}$
# 
# $ Observations = \{(trial,x, \dot{x}, \phi, \dot{\phi},step) | trial \in Trials, step \in \mathbb{N} \text{ DEFINE  OTHER CONSTRAINTS}\}$
# 
# $ Actions = \{(trial,agent, action, step) |trial \in Trials, step \in \mathbb{N} \text{ DEFINE OTHER CONSTRAINTS }\}$
# 
# $s_{n} \equiv  $ the state of the system at step n

# $s_{n}$ is directly related to $x(t)$ 

# In[34]:


experiment.database._conn = sqlite3.connect('example.db')
scientist.analyze(experiment)


# In[35]:


# FIXME: put this in analyze
conn = sqlite3.connect('example.db')
c = conn.cursor()
    
c.execute("select * from observations")
observations = c.fetchall()
        
for obs in observations:
    trial, x, x_dot, phi, phi_dot, n = obs
            
c.execute("select * from actions")
actions = c.fetchall()

c.execute("select * from trials")
trials = c.fetchall()
        
conn.close()


# In[36]:


actions


# In[96]:


observations


# In[38]:


trials


# In[39]:


a_reset = -1
a_0 = 0
a_1 = 1


# In[40]:


current_step = -1


# In[ ]:





# In[41]:


action_space = {-1, 0, 1}


# In[42]:


observations


# In[88]:


Lambda = Wishart(2, [[1, 0], [0, 1]])
np.zeros(D)
np.identity(D)


# In[135]:


#http://www.bayespy.org/user_api/generated/generated/bayespy.nodes.SwitchingGaussianMarkovChain.html#bayespy-nodes-switchinggaussianmarkovchain
obs_nodes = {}
action_nodes = {}
O_D = int(np.prod(env.observation_space.shape)) # will only work with low dimensions.  Need filter
if isinstance(env.action_space,gym.spaces.discrete.Discrete):
    A_D = env.action_space.n
#mu = np.zeros(D)
#lambda_ = 1e-5*np.identity(D)

for obs in observations:
    trial  = obs[0]
    o_n = obs[1:O_D+1]
    n = obs[-1]
    if n in obs_nodes:
        X = obs_nodes[n]
    else:
        mu = Gaussian(np.zeros(O_D), 1e-5*np.identity(O_D))
        lambda_ =  Wishart(O_D, np.identity(O_D))
        O_n = Gaussian(mu, lambda_,name = f"O_{n}")
        obs_nodes[n] = O_n
    X.observe(o_n)

for action in actions:
    trial, agent, a_n, n = action
    if a_n < 0: #action reset
        continue
    if n in action_nodes:
        A = action_nodes[n]
    else:
        category_prob = Dirichlet(1e-3*np.ones(A_D),name='category_prob') #FIXME: Unconfirmed!
        A = Categorical(category_prob)
        action_nodes[n] = A
    A.observe(a_n)

    


# In[139]:


action_nodes[0].__dict__


# In[ ]:


Dirichlet(1e-3*np.ones(A_D))


# In[120]:


np.prod(env.action_space.shape)


# In[102]:


obs_nodes


# In[61]:


env.observation_space.shape


# In[74]:


x_n


# In[75]:


trial


# In[77]:


n


# In[81]:


nodes[0].__dict__


# In[82]:


nodes


# In[146]:


test_1 =  GaussianARD(np.zeros(O_D), 1e-5*np.identity(O_D))
test_2 =  Gamma(np.zeros(O_D), 1e-5*np.identity(O_D))
GaussianARD(test_1,test_2,plates=(2,))


# In[ ]:




