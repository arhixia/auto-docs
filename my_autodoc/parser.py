import os
import ast


def parse_project(project_dir):
    project_data = {}

    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as source_code:
                    try:
                        tree = ast.parse(source_code.read())
                        # Ваши действия с AST
                        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

                        project_data[file_path] = {
                            "Functions": functions,
                            "Classes": classes
                        }
                    except SyntaxError as e:
                        print(f"Ошибка синтаксиса в файле {file_path}: {e}")
                    except Exception as e:
                        print(f"Ошибка обработки файла {file_path}: {e}")

    return project_data

def parse_file(tree):
    data = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            data.append(f"Function: {node.name}")
        elif isinstance(node, ast.ClassDef):
            data.append(f"Class: {node.name}")
    return data

def save_summary(project_data, output_file="project_summary.txt"):
    with open(output_file, "w") as f:
        for file, elements in project_data.items():
            f.write(f"File: {file}\n")
            for element in elements:
                f.write(f"  {element}\n")
            f.write("\n")
