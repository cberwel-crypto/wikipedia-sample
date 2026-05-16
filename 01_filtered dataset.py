import pandas as pd
import glob

keywords = ["Amber Heard", "Brad Pitt", "Jesus", "Christian views on poverty and wealth", "Curtis Yarvin", "Elon Musk", "Margaret Thatcher", "The Bible and homosexuality", "LGBTQ people and Islam", "Elizabeth II", "Squatting", "Eviction", "Coming out", "Democracy", "Dictatorship", "Dictatorship of the proletariat", "Collective farming", "Definition of terrorism", "Hezbollah", "Thomas Sankara", "September 11 attacks", "United States and state-sponsored terrorism", "Holodomor", "The Diary of a Young Girl", "Havana syndrome", "Mary Jane Kelly", "Communism and LGBTQ rights"]
pattern = "|".join(keywords)

csv_files = sorted(glob.glob('wikipedia_batch_*.csv'))

output_file = "filtered_dataset.csv"
first_write = True
match_count = 0

for file in csv_files:
    df = pd.read_csv(file)
    mask = df["title"].isin(keywords)
    matches = df[mask]
    
    if not matches.empty:
        matches.to_csv(output_file, mode="a", header=first_write, index=False)
        first_write = False
        match_count += len(matches)

print(f"Guardados {match_count} artículos en {output_file}.")