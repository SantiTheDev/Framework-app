class Authors():
    # this class define the characteristics of authors
    def __init__(self,name: str):
        self.name = name

    def __str__(self):
        return {
            "name": self.name
            }

class Document():
    # this class define the characteristics of a document
    def __init__(self,id, title,number_of_pages,category, authors : str):
        self.id = id
        self.title = title
        self.number_of_pages = number_of_pages
        self.category = category
        self.authors = authors

    def __str__(self):
        return {
            "id": self.id, 
            "title": self.title,
            "number of pages": self.number_of_pages,
            "category": self.category,
            "authors":self.authors 
            }