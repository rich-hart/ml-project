import unittest

import retro


class TestAcademy(unittest.TestCase):
    def test_minimum_execution(self):
        env = retro.make(game='Airstriker-Genesis')
        obs = env.reset()
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        env.close()
