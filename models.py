import openai


models = openai.Model.list()
for model in models['data']:
    print(model['id'])
