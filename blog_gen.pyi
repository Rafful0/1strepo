import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config['API_KEY']

def generate_blog(topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + topic,
    max_tokens = 400,
    temperature = 0.3
)

  blog = response.choices[0].text

  return blog

a = input('What do you want to write a blog about? ')

print(generate_blog(a))

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    p_topic = input('What should this paragraph talk about? ')
    print(generate_blog(p_topic))
  else:
    keep_writing = False

