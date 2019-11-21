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

class sarsa(TD):
    
    def learn(self, state1, action1, reward, state2, action2):
        nextQ = self.getQ(state2, action2)
        self.updateQ(state1, action1, reward, reward + gamma * nextQ)

class qLearn(TD):
    
    def learn(self, state1, action1, reward, state2):
        maxQ = max([self.getQ(state2, a) for a in self.actions])
        self.updateQ(state1, action1, reward, reward + gamma * maxQ)
