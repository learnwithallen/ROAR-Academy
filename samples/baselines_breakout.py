## This is course material for Introduction to Modern Artificial Intelligence
## Example code: baselines_breakout.py
## Author: Allen Y. Yang
##
## (c) Copyright 2023-2024. Intelligent Racing Inc. Not permitted for commercial use

import os
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3 import A2C

# There already exists an environment generator that will make and wrap atari environments correctly.
# We use 8 parallel processes
env = make_atari_env('Breakout-v4', n_envs=8, seed=0)
# Stack 4 frames
env = VecFrameStack(env, n_stack=4)

# A2C is primarily meant to be run on the CPU
model = A2C('CnnPolicy', env, verbose=1, device='cpu')

path = os.path.dirname(os.path.abspath(__file__))
model_file_name = path + '/breakout_a2c'
LOAD_PRETRAINED = False
TRAIN_TIMESTEPS = int(1e5)
if LOAD_PRETRAINED:
    # Load saved model
    model = A2C.load(model_file_name)
else:
  model.learn(total_timesteps=TRAIN_TIMESTEPS)
  model.save(model_file_name)

# Evaluate the agent
episode_reward = 0
obs = env.reset()
for _ in range(1000):
  action, _ = model.predict(obs)
  obs, reward, done, info = env.step(action)
  env.render("human")
  episode_reward += reward
  if sum(done):
    print("Reward:", episode_reward)
    episode_reward = 0.0
    obs = env.reset()