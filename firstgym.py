import gym
env = gym.make('MountainCar-v0')
env.reset()

print('State space: ', env.observation_space)

print('Action space: ', env.action_space)

print(env.observation_space.low)
print(env.observation_space.high)

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()