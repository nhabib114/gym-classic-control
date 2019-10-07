#td template
import gym
import numpy as np

alpha = None
gamma = None
epsilon = None

V = np.zeros([env.observation_space.n, env.action_space.n]) #initialize your value function

state = env.reset()

while not done:
  if np.random.rand() < epsilon:
    action = env.action_space.sample() #select a random action
  else:
 #   action = np.argmax(V[state]) # choose an action according to your custom method
    action = select_action(V[state])
 
next_state, reward, done, info = env.step(action) #get the next state and reward
 
# V(state) = V(state) + alpha * (reward + gamma * V(next_state) - V(state)) # update your value function
 
state = next_state # set the next state
