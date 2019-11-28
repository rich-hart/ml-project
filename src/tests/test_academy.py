import ipdb
import unittest

import retro
import gym 

from scipy.constants import Boltzmann
from scipy.stats import norm
import time

GYM_GAME_LIST = [e.id for e in list(gym.envs.registry.all())]

class TestAcademy(unittest.TestCase):
    def setUp(self):
        self.env = None

    def target(self, game, render=False):
        if game in GYM_GAME_LIST:
            self.env = gym.make(game)
        else:
            self.env = retro.make(game=game)
        obs = self.env.reset()
        obs, rew, done, info = self.env.step(self.env.action_space.sample())
        if render:
            self.env.render()


    def tearDown(self):
        if self.env:
            self.env.close()
        self.env = None

    def test_retro_minimum_execution(self):
        self.target(game='Airstriker-Genesis')
#        env = retro.make(game='Airstriker-Genesis')
#        obs = env.reset()
#        obs, rew, done, info = env.step(env.action_space.sample())
#        env.render()
#        env.close()

    def test_gym_minimum_execution(self):
        #import ipdb; ipdb.set_trace()
        self.target(game='CartPole-v1')
#        env = gym.make('CartPole-v1')
#        obs = env.reset()
#        obs, rew, done, info = env.step(env.action_space.sample())
#        env.render()
#        env.close()

    def test_stats_norm(self):

        ipdb.set_trace()
        test_distribution = norm(0.0,1.0)
        pass
#        test_distribution = norm(0.0,1.0)
#        env = gym.make('CartPole-v1')
#        obs = env.reset()
#        obs, rew, done, info = env.step(env.action_space.sample())
#        env.render()
#        env.close()
