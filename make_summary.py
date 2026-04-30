from functions.summaries_from_sheet import summaries_from_sheet
 
csv_path = "data/expats_page.csv"
output_path = "data/expats_page.txt"

summaries_from_sheet(csv_path, output_path, "anthropic")
