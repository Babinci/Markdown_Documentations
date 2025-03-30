#!/usr/bin/env python3
"""
Firecrawl Scraping Script for Markdown Documentation

This script uses the Firecrawl SDK to scrape websites and convert them to markdown documentation.
It loads the API key from a .env file in the root directory and supports saving the scraped content
to an output folder.
"""

import os
import json
from pathlib import Path
from typing import Dict, Any
from urllib.parse import urlparse

# Force immediate output for logs
import builtins
real_print = builtins.print
def print_and_flush(*args, **kwargs):
    kwargs.setdefault('flush', True)
    return real_print(*args, **kwargs)
builtins.print = print_and_flush

# External dependencies: Install via `pip install python-dotenv firecrawl`
from dotenv import load_dotenv
from firecrawl.firecrawl import FirecrawlApp

# Configuration variables - modify these as needed
OUTPUT_FOLDER = "pydantic_ai"
SITE_URL = "https://ai.pydantic.dev/"


def load_api_key() -> str:
    """Load the Firecrawl API key from a .env file in the project root directory."""
    root_dir = Path(__file__).resolve().parent.parent
    load_dotenv(root_dir / ".env")
    
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        raise ValueError("FIRECRAWL_API_KEY not found in .env file. Please add it to your .env file.")
    
    return api_key


def ensure_output_directory(path: str) -> Path:
    """Ensure the output directory exists and return its Path object."""
    output_path = Path(path)
    
    # If path is relative, make it relative to the project root
    if not output_path.is_absolute():
        root_dir = Path(__file__).resolve().parent.parent
        output_path = root_dir / output_path
    
    os.makedirs(output_path, exist_ok=True)
    return output_path


def save_scraped_content(output_dir: Path, content: Dict[str, Any]) -> None:
    """
    Save scraped content to files in the specified output directory.

    Args:
        output_dir (Path): The directory where files will be saved.
        content (Dict[str, Any]): The scraped content returned by Firecrawl.
    """
    for page_data in content.get("pages", []):
        url = page_data.get("url", "unknown_url")
        markdown_content = page_data.get("content", "")
        
        # Generate a filename based on the URL path
        parsed_url = urlparse(url)
        filename = parsed_url.path.strip("/").replace("/", "_") or "index"
        filename += ".md"
        
        # Save to file
        file_path = output_dir / filename
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        print(f"Saved: {file_path}")


def main():
    """Main function to scrape the website and save content."""
    try:
        # Load API key and initialize Firecrawl app
        api_key = load_api_key()
        app = FirecrawlApp(api_key=api_key)

        # Ensure output directory exists
        output_dir = ensure_output_directory(OUTPUT_FOLDER)

        # Scrape the website
        print(f"Scraping site: {SITE_URL}")
        scrape_status = app.scrape_url(SITE_URL, params={"formats": ["markdown"]})

        # Check if scraping was successful
        if scrape_status.get("status") != "success":
            print(f"Error during scraping: {scrape_status}")
            return

        # Save scraped content to files
        scraped_content = scrape_status.get("data", {})
        save_scraped_content(output_dir, scraped_content)

        print(f"Scraping completed. Files saved in: {output_dir}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
