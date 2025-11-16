# Classes = blueprint
# Objects = actual thing you built
# Variables = attributes
# Functions = methods

class Movie:
    def __init__(self, title, year, seen, imdb_score):
      # Self acts as reference of current object
        self.title = title
        self.year = year
        self.seen = seen
        self.imdb_score = imdb_score

    def nice_print(self):
        print("Title: ", self.title)
        print("Year: ", self.year)
        print("Have Seen: ", self.seen)
        print("Imdb Score: ", self.imdb_score)

film1 = Movie("Dune", 2021, 2021, 8)
film2 = Movie("Dune: Part Two", 2024, 2024, 8.4)
film2.nice_print()
film1.nice_print()