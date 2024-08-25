import openai


def request_gpt(api_key, summary_file):
    openai.api_key = api_key

    with open(summary_file, "r", encoding="utf-8") as f:
        prompt = f.read()

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()



