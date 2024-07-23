import requests

def load_wordlist(wordlist_path):
    """Load the wordlist from a file."""
    with open(wordlist_path, 'r') as file:
        return [line.strip() for line in file]

def brute_force(base_url, wordlist):
    """Brute force directories on the given base URL."""
    found_directories = []
    for word in wordlist:
        url = f"{base_url.rstrip('/')}/{word.lstrip('/')}"
        print(f"Scanning: {url}")  # Debugging statement
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Found: {url}")
                found_directories.append(url)
            elif response.status_code == 403:
                print(f"Forbidden: {url}")
            elif response.status_code == 404:
                continue  # Not found, move to the next word
        except requests.RequestException as e:
            print(f"Request failed for {url}: {e}")
    return found_directories

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Directory Bruteforce Tool")
    parser.add_argument('url', help="Base URL to scan")
    parser.add_argument('wordlist', help="Path to wordlist file")
    args = parser.parse_args()

    base_url = args.url
    wordlist_path = args.wordlist

    wordlist = load_wordlist(wordlist_path)
    brute_force(base_url, wordlist)

if __name__ == "__main__":
    main()
