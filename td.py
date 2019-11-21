#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[67]:


class TD:
    def __init__(self, actions, epsilon=0.1, alpha=0.2, gamma=0.9):
        self.q = {}
        self.actions = [i for i in range(actions)]

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)
    
    def updateQ(self, state, action, reward, newValue):
        currentQ = self.q.get((state, action), None)
        if currentQ is None:
            self.q[(state, action)] = reward 
        else:
            self.q[(state, action)] = currentQ + self.alpha * (newValue - currentQ)
    
    def learn(self, state1, action1, reward, state2, action2):
        pass
        
    def chooseAction(self, state):
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            q = [self.getQ(state, a) for a in self.actions] #fix this line - done
            maxQ = max(q)
            count = q.count(maxQ)
            if count > 1:
                best = [a for a in self.actions if q[a] == maxQ] #fix this line
                i = random.choice(best)
            else:
                i = q.index(maxQ)

            action = self.actions[i]
        return action


# In[68]:


class sarsa(TD):
    
    def learn(self, state1, action1, reward, state2, action2):
        nextQ = self.getQ(state2, action2)
        self.updateQ(state1, action1, reward, reward + gamma * nextQ)


# In[86]:


class qLearn(TD):
    
    def learn(self, state1, action1, reward, state2):
        maxQ = max([self.getQ(state2, a) for a in self.actions])
        self.updateQ(state1, action1, reward, reward + gamma * maxQ)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


s = '''
bBE3 bBAD
b930 b8F3
bEF1 bEBA
bE26 bDE5
b882 b862
bE91 bE4A
b9C1 b96E
b9F3 b9B8
bC63 bC0E
b8C1 b895
b937 b8FA
bCEE bCAC
bC0E bBC5
b86C b84A
b8FA b8CD
bA47 bA09
bC4B bBE5
bE24 bDE2
bA27 b9ED
b7AA b75D
b955 b91D
bA23 b9EA
bC72 bC25
bE81 bE3C
bE14 bDCB
bB8E bB21
b92F b8F1
bAF3 bAA
bBE5 bBAF
bD59 bD11
bA71 bA2C
b93F b908
bF01 bEC8
bD03 bCBA
bD13 bCC5
bD48 bD09
bAEC bAA8
bA1E b9E2
bC51 bBF2
bF24 bEE2
bE57 bE1C
bC31 bBDE
bA4A bA0B
b74C b6C5
b9B5 b959
b917 b8DD
b862 b840
bB13 bAB6
b99B b94A
bB75 bB13
b61D b5A4
bF46 bF01
bD12 bCC4
bCAF bC5A
bC70 bC22
b5C7 b4BC
bF35 bEF1
bE36 bDFC
bAB8 bA75
bE10 bDC5
bEFA bEC2
b599 b47D
bEFC bEC4
b5B0 b49E
b4ED b426
b275 b1ED
b827 b7FC
bE5C bE20
bC03 bBBB
b692 b5F0
'''


# In[ ]:





# In[ ]:





# In[ ]:




