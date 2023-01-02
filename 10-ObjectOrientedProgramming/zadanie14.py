class ebook():
    def __init__(self, u_title, u_author, u_no_of_pages):
        self.author = u_author
        self.title = u_title
        self.no_of_pages = u_no_of_pages
        self.current_page = 1
        self.is_open = False
    def open_book(self):
        if self.is_open == False:
            self.is_open = True
    def close_book(self):
        if self.is_open:
            self.is_open = False
    def next_page(self):
        if self.is_open and self.current_page < self.no_of_pages:
            self.current_page += 1
        else:
            print("otworz ksiazke!")
    def previous_page(self):
        if self.is_open and self.current_page > 1:
            self.current_page -= 1
        else:
            print("otworz ksiazke!")
    def book_status(self):
        if self.is_open:
            print(f"autor: {self.author}, Tytul: {self.title}, strona: {self.current_page}")
        else:
            print("otworz ksiazke!")            


    

Harry_Potter = ebook("Harry Potter", "J.K Rowling", 500)
Harry_Potter.open_book()
Harry_Potter.book_status()
Harry_Potter.next_page()
Harry_Potter.next_page()
Harry_Potter.next_page()
Harry_Potter.next_page()
Harry_Potter.book_status()
Harry_Potter.close_book()
Harry_Potter.previous_page()

