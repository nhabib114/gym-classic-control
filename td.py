#td template

V = np.zeros([env.observation_space.n, env.action_space.n]) #initialize your value function

state = env.reset()

while reward != 20
  if np.random.rand() < epsilon:
    action = env.action_space.sample() #select a random action
  else:
    action = np.argmax(Q[state]) # choose an action according to your custom method
 
next_state, reward, done, info = env.step(action) #get the next state and reward
 
# V(state) = V(state) + alpha * (reward + gamma * V(next_state) - V(state)) # update your value/utility function
 
state = next_state # set the next state
