# Principle 2: Give the model time to “think”
# limitacion-alucinaciones

# Model Limitations: Hallucinations
#
#     Boie is a real company, the product name is not real

import openai
openai.api_key = ""
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
response = get_completion(prompt)
print(response)

# Reducir alucinaciones:
# 1- Buscar - Encontrar información relevante
# 2- Responder la pregunta en base a la información relevante