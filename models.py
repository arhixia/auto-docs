import openai

# Получите список доступных моделей
models = openai.Model.list()
for model in models['data']:
    print(model['id'])
