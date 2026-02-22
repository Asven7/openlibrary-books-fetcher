import csv
from dataclasses import dataclass
from typing import Final, TypedDict, Sequence, Any
import requests


# ==============================
# Constants
# ==============================

API_URL: Final[str] = "https://openlibrary.org/search.json"
QUERY: Final[str] = "python"
MAX_BOOKS: Final[int] = 50
YEAR_LIMIT: Final[int] = 2000
OUTPUT_FILE: Final[str] = "Type Hint & Simple Web Page/books_after_2000.csv"
REQUEST_TIMEOUT: Final[int] = 10


# ==============================
# API Response Models
# ==============================

class RawBook(TypedDict, total=False):
    title: str
    author_name: list[str]
    first_publish_year: int
    edition_count: int


class OpenLibraryResponse(TypedDict):
    docs: list[RawBook]


# ==============================
# Domain Model
# ==============================

@dataclass(slots=True)
class Book:
    title: str
    author: str
    first_publish_year: int
    edition_count: int


# ==============================
# Core Logic
# ==============================

def fetch_books() -> list[RawBook]:
    """Fetch raw book data from Open Library API."""
    params: dict[str, str | int] = {
        "q": QUERY,
        "limit": 100,
    }

    try:
        response = requests.get(API_URL, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError("Failed to fetch data from Open Library API") from exc

    data: OpenLibraryResponse = response.json()
    return data.get("docs", [])


def filter_books(books: Sequence[RawBook]) -> list[Book]:
    """Filter books published after YEAR_LIMIT."""
    filtered: list[Book] = []

    for book in books:
        publish_year: int | None = book.get("first_publish_year")

        if publish_year is None:
            continue

        if publish_year <= YEAR_LIMIT:
            continue

        title: str = book.get("title", "N/A")
        authors: list[str] = book.get("author_name", ["N/A"])
        edition_count: int = book.get("edition_count", 0)

        filtered.append(
            Book(
                title=title,
                author=", ".join(authors),
                first_publish_year=publish_year,
                edition_count=edition_count,
            )
        )

        if len(filtered) >= MAX_BOOKS:
            break

    filtered.sort(key=lambda book: book.first_publish_year)
    return filtered


def save_to_csv(books: Sequence[Book]) -> None:
    """Save filtered books to a CSV file."""
    fieldnames: list[str] = [
        "title",
        "author",
        "first_publish_year",
        "edition_count",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for book in books:
            writer.writerow(
                {
                    "title": book.title,
                    "author": book.author,
                    "first_publish_year": book.first_publish_year,
                    "edition_count": book.edition_count,
                }
            )


def main() -> None:
    raw_books: list[RawBook] = fetch_books()
    filtered_books: list[Book] = filter_books(raw_books)
    save_to_csv(filtered_books)

    print(f"{len(filtered_books)} books saved successfully.")


if __name__ == "__main__":
    main()