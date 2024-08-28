import os
import pandas as pd
from bs4 import BeautifulSoup

folders = ['btech/found','bpharma/found']

data = []

def extract_c_s(f_path):
    with open(f_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        sgpa, cgpa = 'N/A', 'N/A'

        # Search for all table rows that contain 'SGPA' or 'CGPA'
        for row in soup.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) >= 2:
                label = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True)
                if 'SGPA' in label:
                    sgpa = value
                elif 'CGPA' in label:
                    cgpa = value

        return cgpa, sgpa

# Traverse folders and scrape data
for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            f_path = os.path.join(folder, filename)
            cgpa, sgpa = extract_c_s(f_path)
            data.append({"File_name": filename, "cgpa": cgpa, "sgpa": sgpa})

# Save the data into a CSV file
df = pd.DataFrame(data)
df.to_csv('cgpa_sgpa.csv', index=False)

print("Data saved to cgpa_sgpa.csv")