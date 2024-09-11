from urllib3.util import parse_url

if __name__ == '__main__':
    url = parse_url("https://hwv430.blogspot.com/search?updated-max=2024-09-12T03:07:00%2B08:00&max-results=50")
    print(url.query)

