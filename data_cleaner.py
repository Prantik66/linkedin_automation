import pandas as pd
import re

# LOAD + CLEANING DATA
df = pd.read_csv("linkedin_results.csv")

# remove empty rows
df = df.dropna(subset=["text", "link"])

# extract email safely
def extract_email(text):
    matches = re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        str(text)
    )
    return matches[0] if matches else None

df["email"] = df["text"].apply(extract_email)

# keep only valid emails
df = df.dropna(subset=["email"])

# remove duplicates
df = df.drop_duplicates(subset=["link"])

print("Final usable rows:", len(df))

# SAVE CLEAN DATA (IMPORTANT)
df.to_csv("cleaned_leads.csv", index=False)

print("Cleaned data saved to cleaned_leads.csv")