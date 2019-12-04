import ipdb
import unittest

import retro
import gym 

from scipy.constants import Boltzmann
from scipy.stats import norm
import time
from agents import Agent, Observation, Action
from algorithms import MaximizeCausalForce, CausalEntropicForce, Macrostate

#GYM_GAME_LIST = [e.id for e in list(gym.envs.registry.all())]

class TestEntropicForce(unittest.TestCase):
    def setUp(self):
        self.env = gym.make('CartPole-v1')

    def tearDown(self):
        self.env.close()

    def test(self):
        import ipdb; ipdb.set_trace()
        obs = self.env.reset()
        F = CausalEntropicForce()
        X_0 = Macrostate(env=self.env, x_0=obs)
        agent = Agent('test')
        obs = Observation(obs,agent)
        MaximizeCausalForce(F, X_0)


