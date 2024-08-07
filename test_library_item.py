import pytest 
from library_item import LibraryItem  

def test_library_item_initialization():
    item = LibraryItem("The Shawshank Redemption", "Frank Darabont", 5)
    assert item.name == "The Shawshank Redemption"
    assert item.director == "Frank Darabont"
    assert item.rating == 5
    assert item.play_count == 0

def test_library_item_initialization_default_rating():
    item = LibraryItem("Pulp Fiction", "Quentin Tarantino")
    assert item.rating == 0

def test_info_method():
    item = LibraryItem("The Godfather", "Francis Ford Coppola", 4)
    assert item.info() == "The Godfather - Francis Ford Coppola ****"
    item.rating = 0
    assert item.info() == "The Godfather - Francis Ford Coppola "

def test_stars_method():
    item = LibraryItem("Inception", "Christopher Nolan")
    item.rating = 3
    assert item.stars() == "***"

    item.rating = 0
    assert item.stars() == ""
