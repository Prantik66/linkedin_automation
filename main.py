import os

print("Running Scraper")
os.system("python scraper.py")

print("Running data cleaner...")
os.system("python data_cleaner.py")

print("Sending emails...")
os.system("python smtp_sender.py")