import pandas as pd
from bs4 import BeautifulSoup

def get_posts_from_html(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    post_elements = soup.find_all(attrs={"data-ad-rendering-role": "story_message"})
    print(f"{len(post_elements)} posts gevonden.")

    posts = [post.get_text(strip=True) for post in post_elements]

    posts_dataframe = pd.DataFrame(posts, columns=['post_text'])
    posts_dataframe.to_csv(output_path, index=False)
    print(f"Opgeslagen als {output_path}")
    return posts_dataframe
