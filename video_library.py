from library_item import LibraryItem


library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
library["03"] = LibraryItem("Casablanca", "Casablanca", 2)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)
library["06"] = LibraryItem("The Godfather", "Francis Ford Coppola", 5)
library["07"] = LibraryItem("Pulp Fiction", "Quentin Tarantino", 4)
library["08"] = LibraryItem("The Shawshank Redemption", "Frank Darabont", 5)
library["09"] = LibraryItem("The Dark Knight", "Christopher Nolan", 5)
library["10"] = LibraryItem("Schindler's List", "Steven Spielberg", 5)
library["11"] = LibraryItem("Fight Club", "David Fincher", 4)
library["12"] = LibraryItem("Forrest Gump", "Robert Zemeckis", 4)
library["13"] = LibraryItem("Inception", "Christopher Nolan", 4)
library["14"] = LibraryItem("The Matrix", "The Wachowskis", 5)
library["15"] = LibraryItem("Goodfellas", "Martin Scorsese", 4)
library["16"] = LibraryItem("The Silence of the Lambs", "Jonathan Demme", 5)
library["17"] = LibraryItem("Se7en", "David Fincher", 4)
library["18"] = LibraryItem("The Green Mile", "Frank Darabont", 5)
library["19"] = LibraryItem("Interstellar", "Christopher Nolan", 5)
library["20"] = LibraryItem("Gladiator", "Ridley Scott", 4)
library["21"] = LibraryItem("The Prestige", "Christopher Nolan", 4)
library["22"] = LibraryItem("Memento", "Christopher Nolan", 4)
library["23"] = LibraryItem("Braveheart", "Mel Gibson", 5)
library["24"] = LibraryItem("The Departed", "Martin Scorsese", 4)
library["25"] = LibraryItem("Django Unchained", "Quentin Tarantino", 4)
library["26"] = LibraryItem("Whiplash", "Damien Chazelle", 5)
library["27"] = LibraryItem("The Lion King", "Roger Allers & Rob Minkoff", 5)
library["28"] = LibraryItem("WALL-E", "Andrew Stanton", 5)
library["29"] = LibraryItem("Up", "Pete Docter", 5)
library["30"] = LibraryItem("Toy Story", "John Lasseter", 5)
library["31"] = LibraryItem("Finding Nemo", "Andrew Stanton", 5)
library["32"] = LibraryItem("Inside Out", "Pete Docter", 5)
library["33"] = LibraryItem("Coco", "Lee Unkrich & Adrian Molina", 5)
library["34"] = LibraryItem("Ratatouille", "Brad Bird", 5)
library["35"] = LibraryItem("The Incredibles", "Brad Bird", 5)
library["36"] = LibraryItem("Spider-Man: Into the Spider-Verse", "Bob Persichetti, Peter Ramsey & Rodney Rothman", 5)
library["37"] = LibraryItem("Zootopia", "Byron Howard & Rich Moore", 5)
library["38"] = LibraryItem("Shrek", "Andrew Adamson & Vicky Jenson", 4)
library["39"] = LibraryItem("Kung Fu Panda", "Mark Osborne & John Stevenson", 4)
library["40"] = LibraryItem("Madagascar", "Eric Darnell & Tom McGrath", 4)
library["41"] = LibraryItem("Ice Age", "Chris Wedge & Carlos Saldanha", 4)
library["42"] = LibraryItem("Despicable Me", "Pierre Coffin & Chris Renaud", 4)
library["43"] = LibraryItem("The Secret Life of Pets", "Chris Renaud", 4)
library["44"] = LibraryItem("Minions", "Kyle Balda & Pierre Coffin", 4)
library["45"] = LibraryItem("Monsters, Inc.", "Pete Docter", 5)
library["46"] = LibraryItem("A Bug's Life", "John Lasseter & Andrew Stanton", 4)
library["47"] = LibraryItem("Brave", "Mark Andrews & Brenda Chapman", 4)
library["48"] = LibraryItem("Cars", "John Lasseter & Joe Ranft", 4)
library["49"] = LibraryItem("Big Hero 6", "Don Hall & Chris Williams", 5)
library["50"] = LibraryItem("Frozen", "Chris Buck & Jennifer Lee", 5)
library["51"] = LibraryItem("Frozen", "Chris Buck & Jennifer Lee", 5)

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1
    
def set_play_count(key, count):
    if key in library:
        library[key]['play_count'] = count


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
