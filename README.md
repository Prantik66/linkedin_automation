# LinkedIn Recruiter Automation System

## Project Overview

This project automates the process of extracting recruiter leads from LinkedIn posts and generating recruiter-specific email drafts automatically.

The system performs:

* LinkedIn keyword-based post scraping
* Recruiter email extraction
* CSV data storage
* Data cleaning and filtering
* Automated email draft generation
* Resume attachment preparation
* CC email handling

The project was built as an automation workflow prototype focused on backend automation and process orchestration.

---

# Tech Stack

* Python
* Playwright
* Pandas
* SMTP (Draft Mode)
* CSV Processing

---

# Project Workflow

```text
scraper.py
→ linkedin_results.csv
→ data_cleaner.py
→ cleaned_leads.csv
→ smtp_sender.py
→ draft email generation
```

---

# Features

* Automated LinkedIn post scraping
* Multiple keyword support
* Recruiter email extraction using regex
* Duplicate lead removal
* Automated email body generation
* Resume attachment support
* CC handling
* Safe draft mode (no real email sending)

---

# Keywords Used

* JAVA DEVELOPER C2C
* BUSINESS ANALYST C2C
* PROJECT MANAGER C2C
* DATA ANALYST C2C

---

# Folder Structure

```text
linkedin_automation_project/
│
├── scraper.py
├── data_cleaner.py
├── smtp_sender.py
├── main.py
│
├── linkedin_results.csv
├── cleaned_leads.csv
│
├── assets/
│   └── resume.pdf
│
├── draft_outputs/
│
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-link>
cd linkedin_automation_project
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

# Run Project

```bash
python main.py
```

---

# Important Note

SMTP email sending was intentionally disabled during demo/testing to prevent accidental outbound emails to real recruiters.

The current implementation generates local draft previews instead of sending emails directly.

---

# Future Improvements

* Flask/FastAPI dashboard
* Resume tailoring
* NLP-based job matching
* HTML email templates
* Real SMTP production mode
* Database integration
* Analytics dashboard

---

# Disclaimer

This project was created for educational and automation workflow demonstration purposes only.
