from my_autodoc.parser import parse_project, save_summary
from my_autodoc.gpt_interface import request_gpt
from my_autodoc.doc_generator import save_documentation

# Шаг 1: Парсинг проекта
project_dir ="C:\\Users\\User\\PycharmProjects\\automotized-restoraunt-api"

project_data = parse_project(project_dir)

# Шаг 2: Сохранение краткого содержания проекта в файл
summary_file = "project_summary.txt"
save_summary(project_data, summary_file)

# Шаг 3: Отправка запроса к GPT для генерации документации
api_key = "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"
documentation_text = request_gpt(api_key, summary_file)

# Шаг 4: Сохранение сгенерированной документации в файл
documentation_file = "generated_documentation.md"
save_documentation(documentation_text, documentation_file)

print(f"Документация успешно сгенерирована и сохранена в {documentation_file}")
