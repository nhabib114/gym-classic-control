
# coding: utf-8

# In[1]:

import gym
import agents
import numpy as np
import random

env = gym.make('Taxi-v2')
agent = agents.SarsaAgent(actions = env.action_space.n )#alpha, gamma = #gamma, ...)

state = env.reset()
done = False
episodes = 100#episodes
steps = 0
totalSteps = 0

for episode in range(episodes):

    while not done:
        if np.random.rand() < agent.epsilon:
            action = env.action_space.sample()
        else:
            action = agent.act(state) #do this for next action
        next_state, reward, done, info = env.step(action)
        agent.learn(state, action, reward, next_state          )               #next_action)
        state = next_state

        #put in next_action

        steps += 1
        print(steps)

    totalSteps += steps


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



