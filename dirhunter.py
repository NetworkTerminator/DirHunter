import requests
import sys

def directory_bruteforce(url, wordlist_file):
    # Read the wordlist file
    with open(wordlist_file, 'r') as file:
        wordlist = file.read().splitlines()

    for word in wordlist:
        # Construct the URL with the word from the wordlist
        test_url = f"{url}/{word}"
        
        # Send a GET request
        response = requests.get(test_url)
        
        # Check if the response status code indicates success
        if response.status_code == 200:
            print(f"Found: {test_url}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bruteforce.py <url> <wordlist_file>")
        sys.exit(1)
    
    target_url = sys.argv[1]
    wordlist_file = sys.argv[2]
    
    directory_bruteforce(target_url, wordlist_file)
