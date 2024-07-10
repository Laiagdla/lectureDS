import requests

# url = 'https://api.github.com/users/ssaunier'
# response = requests.get(url)

def book_info(isbn):
    url = 'https://openlibrary.org/api/books'
    params = {
        'bibkeys' : isbn,
        'format' : 'json'
    }
    response = requests.get(url, params=params).json()
    return response

if __name__ == "__main__":
    isbn = "ISBN:9780747532699"
    book = book_info(isbn)
    print(book[isbn]['info_url'])
