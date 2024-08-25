def save_documentation(doc_text, output_file="documentation.md"):
    with open(output_file, "w") as f:
        f.write(doc_text)
