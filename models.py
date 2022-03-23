class Authors():
    # this class define the characteristics of authors
    def __init__(self,name: str):
        self.name = name

    def donothing(self):
        pass

class Document():
    # this class define the characteristics of a document
    def __init__(self,id, title,number_of_pages,category, authors : str):
        self.id = id
        self.title = title
        self.number_of_pages = number_of_pages
        self.category = category
        self.authors = authors

    def donothing(self):
        pass