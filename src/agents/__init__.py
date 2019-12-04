from algorithms import MaximizeCausalForce, CausalEntropicForce, Macrostate

class Brain:
    pass

class Policy:
    env = None
    name = None

    def __init__(self, env, name):
        self.name = name
        self.env = env

    def __call__(self, observation):
        return self.get_action(observation)
    
    def __eq__(self,other):
        return (self.env == other.env) and (self.name == other.name)

    @property
    def action_space(self):
        return self.env.action_space
    
    @property
    def observation_space(self):
        return self.env.observation_space
    
    def get_action(self, observation, *args, **kwargs):
        pass

class Observation:
    data = None
    observer = None

    def __init__(self, data, observer):
        data = data
        observer = observer


class Action:
    pass

class Agent:
    current_environment = None
    current_policy = None
    name = None

    def __init__(self, name, env=None, *arg, **kwargs):
        self.name = name
        self.current_environment = env

    @property
    def action_space(self):
        return self.current_environment.action_space
    
    @property
    def observation_space(self):
        return self.current_environment.observation_space
        
    def interact_with(self, env):
        self.set_environment(env)

    def set_environment(self, env):
        self.current_environment = env

    def set_policy(self, policy):
        self.current_policy = policy
    
    def policy(self, observation):
        # Return an action
        if not isinstance(observation,Observation):
            observation = Observation(observation, self)
        action = self.current_policy(observation)
        return action



class RandomPolicy(Policy):
    seed = None

    def __init__(self, env, name='random', seed=None):
        self.env = env
        self.name = name
        self.seed = seed
    
    def get_action(self, observation):
        random_action = self.action_space.sample()
        return random_action 

class RandomAgent(Agent):
    seed = None

    def __init__(self, name='random', env=None, seed=None, *args,**kwargs):
        self.seed = seed
        self.name = name
        if env:
            self.interact_with(env)
            self.set_policy()

    def set_policy(self):
        self.current_policy = RandomPolicy(env=self.current_environment,name=self.name,seed=self.seed)

        
class MaximizeCausalDecisionPaths(Policy):
    def __init__(self, env, name='maximize_causal_paths'):
        self.name = name
        self.env = env
        
    def get_action(self, observation, *args, **kwargs):
        action = None
        F = CausalEntropicForce()
        X_0 = Macrostate(env=self.env, x_0=observation)
        new_force = MaximizeCausalForce(F, X_0)
        # choose new action from new force
        return action


class Engineer(Agent):
    def create(self, *args,**kwargs):
        # new policy?
        pass
    
class Scientist(Agent):
    #????
    #def construct_hypotheses(self):
    #    pass
    def execute(self, procedure,*args,**kwargs):
        pass
    
    def conduct(self, experiment,*args,**kwargs):
        # execute has unknown parameters
        self.setUp(experiment)
        self.execute(experiment.procedure,experiment.database,*args,**kwargs)
        self.analyze(experiment)
        self.cleanUp(experiment)
    
    def record(self, data, database):
        # persist observation and actions and revant variables, constants
        pass
    # Note: don't know how i field about experiment paramenter
    def analyze(self, experiment,*args, **kwargs):
        raise NotImplementedError() 
    
    # draw conclusions ... ?? Generate bayesNetwork / Knowledge
    def deduce(self):
        pass
    
    def setUp(self, experiment):
        experiment.begin()
    
    def cleanUp(self,experiment):
        experiment.end()
