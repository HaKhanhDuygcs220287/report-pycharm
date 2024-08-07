# Example usage
search_results = search_by_name("godfather")
for result in search_results:
    print(result.info())

search_results = search_by_director("tarantino")
for result in search_results:
    print(result.info())
