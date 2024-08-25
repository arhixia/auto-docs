from my_autodoc.parser import parse_project, save_summary
from my_autodoc.gpt_interface import request_gpt
from my_autodoc.doc_generator import save_documentation


project_dir ="your_project_dir"

project_data = parse_project(project_dir)


summary_file = "project_summary.txt"
save_summary(project_data, summary_file)


api_key = "your_api_key"
documentation_text = request_gpt(api_key, summary_file)


documentation_file = "generated_documentation.md"
save_documentation(documentation_text, documentation_file)

print(f"Документация успешно сгенерирована и сохранена в {documentation_file}")
