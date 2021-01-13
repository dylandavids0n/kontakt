from googlesearch import search

def get_urls(term, n):
    return search(term, num_results=n)

if __name__ == "__main__":

    for i in get_urls("plastic injection manufacturing philly", 10):
        print(i)

