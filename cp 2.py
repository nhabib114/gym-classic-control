#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gym

env = gym.make('MountainCar-v0')
env.reset()


# In[4]:


env.observation_space.high


# In[29]:


env.observation_space.sample()


# In[30]:


env.observation_space


# In[42]:


obs = env.reset()


# In[32]:


obs[0]


# In[34]:


obs[1]


# In[35]:


obs


# In[37]:


import numpy as np

obs = (obs - env.observation_space.low)*np.array([10, 100])


# In[38]:


obs


# In[45]:


obs = obs*np.array([10, 100])


# In[46]:


obs


# In[41]:


env.observation_space.low


# In[43]:


obs


# In[44]:


obs - env.observation_space.low


# In[47]:


num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])
num_states = np.round(num_states, 0).astype(int) + 1
num_states


# In[48]:


19*15


# In[49]:


env = gym.make('CartPole-v1')
env.reset()


# In[50]:


num_states = (env.observation_space.high - env.observation_space.low)*np.array([100, 100, 100, 100])
num_states = np.round(num_states, 0).astype(int) + 1
num_states


# In[58]:


env.observation_space.low


# In[54]:


env.observation_space.high - env.observation_space.low


# In[56]:


env = gym.make('MountainCar-v0')
env.reset()


# In[2]:


env.observation_space.high - env.observation_space.low


# In[59]:


env.observation_space.low


# In[60]:


env.observation_space.high


# In[63]:


num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])


# In[64]:


num_states = np.round(num_states, 0).astype(int) + 1


# In[65]:


num_states


# In[ ]:


num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])

