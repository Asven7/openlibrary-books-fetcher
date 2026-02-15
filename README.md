# Open Library Books Fetcher 📚

This project is a simple Python script that fetches book data from the Open Library API,
filters books published after the year 2000, sorts them by publication year (ascending),
and saves the results into a CSV file.

---

## ✨ Features
- Fetches book data from Open Library API
- Filters books published after 2000
- Sorts books by publication year (oldest to newest)
- Exports data to a CSV file
- Clean, readable, and PEP8-compliant code

---

## 🛠 Technologies Used
- Python 3
- requests
- csv (Python Standard Library)

---

## 📦 Requirements
Make sure Python 3 is installed on your system.

Install dependencies:
bash
pip install -r requirements.txt


---

## ▶️ How to Run
bash
python main.py


After execution, the following file will be created:
text
books_after_2000.csv


---

## 📄 CSV Output Structure
The generated CSV file contains the following columns:
- title
- author
- first_publish_year
- edition_count

Books are sorted by first_publish_year in ascending order (oldest first).

---

## 📁 Project Structure
```text
openlibrary-books-fetcher/
│
├── main.py
├── requirements.txt
├── books_after_2000.csv
└── README.md
```

---

## 🚀 Possible Improvements
- Accept search query as a command-line argument
- Fetch multiple pages to guarantee exactly 50 results
- Add logging and error handling
- Convert the script into a CLI tool

---

## 📌 Data Source
Data is fetched from the Open Library API:
https://openlibrary.org/developers/api

---

## 👤 Author
Ali Ayouman