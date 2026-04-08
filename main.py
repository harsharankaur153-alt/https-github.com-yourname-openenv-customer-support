from env import CustomerSupportEnv
from models import Action

env = CustomerSupportEnv()
obs = env.reset()

print("START STEP")
print("Query:", obs.query)

action = Action(response="Sorry, we are resolving your issue quickly")

obs, reward, done, info = env.step(action)

print("END STEP")
print("Reward:", reward)