import requests
from bs4 import BeautifulSoup
from colorama import Style, Fore, init

init(autoreset=True)

URL = "https://www.bbc.com/news"

def scrape_headlines():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # headlines = soup.select('h3[class*="heading"]')
        # headlines = soup.select('[class*="title"]')
        headlines = soup.select('h1, h2, h3')
        clean_headlines = []
        for hl in headlines:
            text = hl.get_text().strip()
            if text and len(text) > 10:
                clean_headlines.append(text)
        return clean_headlines
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching content: {e}")
        return []
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        return []
    
def main():
    print(Fore.CYAN + Style.BRIGHT + "\n=== LATEST NEWS HEADLINES ===")
    print(Fore.YELLOW + f"Source: {URL}\n")

    headlines = scrape_headlines()

    if headlines:
        for idx, headline in enumerate(headlines[:10], 1):
            print(Fore.GREEN + f"{idx}. {headline}")
    else:
        print(Fore.RED + "No headlines found. Check website structure.")

if __name__ == "__main__":
    main()
