import pandas as pd

from functions.llms.prompt_claude import prompt_claude
from functions.llms.prompt_ollama import prompt_ollama

def summaries_from_sheet(csv_path, output_path, provider="ollama"):
    posts_dataframe = pd.read_csv(csv_path)
    posts = "\n\n".join(posts_dataframe["post_text"].dropna().tolist())

    prompt = """
        Onderstaand krijg je een lijst posts te zien uit een expat-groep in Brussel. Vat voor me samen waar deze posts over gaan in enkele zinnen, probeer gemeenschappelijke thema's te destilleren. Houd de posts over aangeboden vastgoed uit de data waar mogelijk.
    """

    summary = ""

    if provider == "ollama":
        summary = prompt_ollama(prompt, posts)

    if provider == "anthropic":
        summary = prompt_claude(prompt, posts)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"Samenvatting opgeslagen als {output_path}")
    return summary
