from functions.get_posts_from_html import get_posts_from_html

html_page_path = "data/expats_page.html"
csv_output_path = "data/expats_page.csv"

get_posts_from_html(html_page_path, csv_output_path)

