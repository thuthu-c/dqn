# import gym
# env = gym.make("CartPole-v1")
# observation, info = env.reset(seed=42)

# for _ in range(1000):
#   action = env.action_space.sample()
#  observation, reward, terminated, truncated, info = env.step(action)

# if terminated or truncated:
#    observation, info = env.reset()
# env.close()

#import gym

#env = gym.make("LunarLander-v2", render_mode="human")
#observation, info = env.reset(seed=42)


#def policy(observation):
 #   pass
  #  return


#for _ in range(1000):
    #action = policy(observation)  # User-defined policy function
    #observation, reward, terminated, truncated, info = env.step(action)

    #if terminated or truncated:
        #observation, info = env.reset()
#env.close()

import gym
env = gym.make("CartPole-v1", render_mode="human")
env.action_space.seed(42)

observation, info = env.reset(seed=42)

for _ in range(1000):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

    if terminated or truncated:
        observation, info = env.reset()

env.close()

