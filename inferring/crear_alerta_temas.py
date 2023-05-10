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

# Determinar si en un texto están presentes los temas de la lista

story = """
In a recent survey conducted by the government, 
public sector employees were asked to rate their level 
of satisfaction with the department they work at. 
The results revealed that NASA was the most popular 
department with a satisfaction rating of 95%.

One NASA employee, John Smith, commented on the findings, 
stating, "I'm not surprised that NASA came out on top. 
It's a great place to work with amazing people and 
incredible opportunities. I'm proud to be a part of 
such an innovative organization."

The results were also welcomed by NASA's management team, 
with Director Tom Johnson stating, "We are thrilled to 
hear that our employees are satisfied with their work at NASA. 
We have a talented and dedicated team who work tirelessly 
to achieve our goals, and it's fantastic to see that their 
hard work is paying off."

The survey also revealed that the 
Social Security Administration had the lowest satisfaction 
rating, with only 45% of employees indicating they were 
satisfied with their job. The government has pledged to 
address the concerns raised by employees in the survey and 
work towards improving job satisfaction across all departments.
"""

topic_list = [
    "nasa", "local government", "engineering",
    "employee satisfaction", "federal government"
]

prompt = f"""
Determine whether each item in the following list of \
topics is a topic in the text below, which
is delimited with triple backticks.

Give your answer as list with 0 or 1 for each topic.\

List of topics: {", ".join(topic_list)}  

Text sample: '''{story}'''
"""
response = get_completion(prompt)
print(response)
print(response.split(sep='\n'))
# Crear un diccionario con la lista de temas
topic_dict = {i.split(': ')[0]: int(i.split(': ')[1]) for i in response.split(sep='\n')} #como la respuesta la dio con saltos de linea, creo una lista en que cada item se identifica cuando hay salto de linea
# con i.split(': ')[0] identifico el primer item (indice 0) que resulta de hacer split en el primer item de la lista, lo separo con ':' para que quede como diccionario y como value identifico el segundo item y lo convierto a entero con: int(i.split(': ')[1] estoy
if topic_dict['nasa'] == 1:     #mostrar alerta si el tema esta presente
    print("ALERT: New NASA story!")
print(topic_dict)

#repasar split crear un diccionario con split

# intentar modificar el prompt para obtener la respuesta en formato json