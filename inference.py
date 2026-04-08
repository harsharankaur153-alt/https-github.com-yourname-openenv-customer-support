import os
from openai import OpenAI
from env import CustomerSupportEnv
from models import Action

# ENV VARIABLES (IMPORTANT)
API_BASE = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    api_key=HF_TOKEN,
    base_url=API_BASE
)

def run_inference():
    env = CustomerSupportEnv()
    obs = env.reset()

    print("START STEP")

    prompt = f"User query: {obs.query}\nGenerate a helpful support response."

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response.choices[0].message.content

    action = Action(response=reply)

    obs, reward, done, info = env.step(action)

    print("END STEP")
    print("Model Response:", reply)
    print("Reward:", reward)

if __name__ == "__main__":
    run_inference()