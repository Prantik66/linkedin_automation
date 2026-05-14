import pandas as pd
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# sender email
EMAIL = "email@gmail.com"

# cc emails
CC_EMAILS = [
    "quinn@jpitstaffing.com",
    "kim@jpitstaffing.com"
]

# load cleaned data
df = pd.read_csv("cleaned_leads.csv")

print("Emails loaded:", len(df))

# create folder for drafts
os.makedirs("draft_outputs", exist_ok=True)

# loop through each recruiter
for i, row in df.iterrows():

    to_email = row["email"]
    jd = row["text"]
    link = row["link"]

    subject = "Application for Opportunity"

    body = f"""
Hi,

I came across your job post.

Job Description:
{jd}

Post Link:
{link}

Please find my resume attached.

Regards,
Prantik
"""

    # creating email
    msg = MIMEMultipart()

    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Cc"] = ", ".join(CC_EMAILS)
    msg["Subject"] = subject

    # add body
    msg.attach(MIMEText(body, "plain"))

    # attach resume
    with open("assets/resume.pdf", "rb") as file:

        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        "attachment; filename=resume.pdf"
    )

    msg.attach(part)

    # preview draft
    print("\n====================")
    print("DRAFT EMAIL")
    print("====================")
    print("TO:", to_email)
    print("CC:", CC_EMAILS)
    print("SUBJECT:", subject)
    print(body[:300])
    print("====================\n")

    # save draft
    with open(f"draft_outputs/email_{i+1}.txt", "w", encoding="utf-8") as f:

        f.write(f"TO: {to_email}\n")
        f.write(f"CC: {CC_EMAILS}\n")
        f.write(f"SUBJECT: {subject}\n\n")
        f.write(body)

print("ALL DRAFT EMAILS GENERATED")