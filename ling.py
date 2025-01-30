#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown

console = Console()

# Base URLs for Polish-English and English-Polish translations
PL_TO_EN_URL = "https://ling.pl/slownik/polsko-angielski/"
EN_TO_PL_URL = "https://ling.pl/slownik/angielsko-polski/"

def fetch_translation(word, is_english):
    """Fetch translations from Ling.pl for the given word."""
    base_url = EN_TO_PL_URL if is_english else PL_TO_EN_URL
    url = f"{base_url}{word}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error fetching data: {e}[/red]")
        return None, url

    soup = BeautifulSoup(response.text, "html.parser")

    # Find translation section inside div
    translations = []
    translation_section = soup.find("div", class_="col-lg-6 col-md-8 col-xs-12")

    if translation_section:
        for p_tag in translation_section.find_all("p"):
            text = p_tag.get_text(" ", strip=True)
            translations.append(text)

    return translations if translations else None, url

def format_translation(translations):
    """Format translations into categories and readable sections."""
    formatted_output = ""
    
    for translation in translations:
        parts = translation.split("~")  # Handle subcategories
        if len(parts) > 1:
            main_word = parts[0].strip()
            sub_translations = [p.strip() for p in parts[1:]]
            formatted_output += f"\n🔹 **{main_word}**\n"
            for sub in sub_translations:
                formatted_output += f"   - {sub}\n"
        else:
            formatted_output += f"🔹 {translation}\n"
    
    return formatted_output.strip()

def display_results(word, translations, url):
    """Format and display translation results with a clickable link."""
    
    # Display clickable link
    console.print(Panel(f"[bold cyan]🔗 [link={url}]{url}[/link][/bold cyan]", expand=False))

    # Display translations
    console.print(Panel(f"[bold cyan]Translations for '{word}'[/bold cyan]", expand=False))
    
    if translations:
        formatted_output = format_translation(translations)
        console.print(Markdown(formatted_output))
    else:
        console.print("[yellow]No translations found.[/yellow]")

def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Fetch translations from Ling.pl.")
    parser.add_argument("word", type=str, help="Word to translate")
    parser.add_argument("-a", "--angielski", action="store_true", help="Translate from English to Polish")

    args = parser.parse_args()

    translations, url = fetch_translation(args.word, args.angielski)

    if translations:
        display_results(args.word, translations, url)
    else:
        console.print(f"[red]No translations found for '{args.word}'.[/red]")

if __name__ == "__main__":
    main()
