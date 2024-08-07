class LibraryItem:
    def __init__(self, name, director, rating=0):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
        if not self.validate_name(name):
            raise ValueError(f"Invalid name: {name}")
        if not self.validate_director(director):
            raise ValueError(f"Invalid director: {director}")
        if not self.validate_rating(rating):
            raise ValueError(f"Invalid rating: {rating}")

    def validate_name(self, name):
        return isinstance(name, str) and bool(name.strip())

    def validate_director(self, director):
        return isinstance(director, str) and bool(director.strip())

    def validate_rating(self, rating):
        return isinstance(rating, int) and 0 <= rating <= 5

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
library = [
    LibraryItem("The Shawshank Redemption", "Frank Darabont", 5),
    LibraryItem("The Godfather", "Francis Ford Coppola", 4),
    LibraryItem("Inception", "Christopher Nolan", 5),
    LibraryItem("Pulp Fiction", "Quentin Tarantino", 4),
]

def search_by_name(name):
    results = []
    for item in library:
        if name.lower() in item.name.lower():
            results.append(item)
    return results

def search_by_director(director):
    results = []
    for item in library:
        if director.lower() in item.director.lower():
            results.append(item)
    return results

def search_by_director_filter(director):
    results = []
    for item in library:
        if director.lower() == item.director.lower():
            results.append(item)
    return results
# Example usage
search_results = search_by_name("godfather")
for result in search_results:
    print(result.info())

search_results = search_by_director("tarantino")
for result in search_results:
    print(result.info())

search_results = search_by_name("godfather")
for result in search_results:
    print(result.info())

search_results = search_by_director("tarantino")
for result in search_results:
    print(result.info())

filter_results = search_by_director_filter("Christopher Nolan")
for result in filter_results:
    print(result.info())

