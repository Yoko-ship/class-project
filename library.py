from tkinter import *
from tkinter import ttk

class Book:
    def __init__(self,title,author,year,is_borrowed):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    
    def borrow_book(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            return self.is_borrowed
        
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            return self.is_borrowed
        

class Library:
    def __init__(self):
        self.books = []
    def add_book(self,title,author,year,is_borrowed=False):
        self.books.append({
            "title":title,
            "author":author,
            "year":year,
            "is_borrowed":is_borrowed
        })

    
    def remove_book_by_title(self,title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print("Книга успешна удалена")
                return
            
    def find_by_author(self,author):
        for book in self.books:
            if book["author"] == author:
                return book
            
    def find_by_title(self,title):
        for book in self.books:
            if book["title"] == title:
                return book

    def list_books(self):
        return self.books


book_title = None
books_author = None
books_year = None
books_isBorrowed = None
library = Library()

name_library = None
author_library = None
year_library = None
is_borrowed_library = None
def get_name():
    global book_title,books_author,books_year,books_isBorrowed
    try:


        name = book_name_entry.get()
        author = book_author_entry.get()
        year = int(book_year_entry.get())
        value  = check_value.get()
        if value == 1:
            books_isBorrowed = True
        elif value == 0:
            books_isBorrowed = False

        if name and author and year:
            book_title = name
            books_author = author
            books_year = year
            book_ex = Book(book_title,books_author,books_year,books_isBorrowed)
            success = Label(book_label,text="Вы успешно добавили книгу",background="green",foreground="white")
            success.pack(pady=5)
            error_message_first.pack_forget()
            
            return
        else:
            print("Произошла ошибка")
            error = Label(book_label,text="Пожалуста напишите все данные",background="RED",foreground="WHITE")
            error.pack()
    except ValueError:
        error_message_first.pack(pady=5)
    except Exception:
        error_mess = Label(book_label,text="Что то пошло не так,повторите ещё раз",background="red",foreground="white")
        error_mess.pack(pady=5)



def get_name_library():
    global name_library,author_library,year_library,is_borrowed_library
    
    try:
        title = name.get()
        auth = author_entry.get()
        years = int(year_entry.get())
        is_available = check_button.get()
        if is_available == 1:
            is_borrowed_library = True
        else:
            is_borrowed_library = False

        if title and auth and years:
            name_library = title
            author_library = auth
            year_library = years

        else:
            error = Label(library_label,text="Пожалуста напишите все данные",background="RED",foreground="WHITE")
            error.pack(pady=5)
        library.add_book(name_library,author_library,year_library,is_borrowed_library)
        print(library.list_books())

    except ValueError:
        error_message.pack(pady=5)

    except Exception:
        error_mess = Label(library_label,text="Что то пошло не так,повторите ещё раз",background="red",foreground="white")
        error_mess.pack(pady=5)


def show_books(listbox):
    book_listbox.pack(fill="both",expand=True,pady=5)
    all_books = library.list_books()
    listbox.delete(0,END)

    for row in all_books:
        if row["is_borrowed"] == False:
            row["is_borrowed"] = "Недоступно"
        
        elif row["is_borrowed"] == True:
            row["is_borrowed"] = "Доступно"
        row_text = f"Названия: {row['title']} \n Автор: {row['author']} \n Год: {row['year']} \n Доступность: {row['is_borrowed']}"
        listbox.insert(END,row_text)

def remove_books():
    title = remove_by_title_entry.get()
    if title:
        library.remove_book_by_title(title)
        Label(library_label,text="Книга успешно удалена",foreground="white",background="green").pack(pady=5)
    else:
        something = Label(library_label,text="Попробуйте заполнить все поля").pack(pady=5)


root = Tk()
root.title("Library")
root.geometry("800x800")

notebook = ttk.Notebook(root)
notebook.pack(pady=10,expand=True)

book_label = ttk.Frame(notebook)
notebook.add(book_label,text="Книги")

book_name = Label(book_label,text="Названия книги")
book_name.pack(pady=5)
book_name_entry = Entry(book_label)
book_name_entry.pack(pady=5)
book_author = Label(book_label,text="Автор книги")
book_author.pack(pady=5)
book_author_entry = Entry(book_label)
book_author_entry.pack(pady=5)
book_year = Label(book_label,text="Год выпуска")
book_year.pack(pady=5)
book_year_entry = Entry(book_label)
book_year_entry.pack(pady=5)



check_value = IntVar()
book_borrowed = Checkbutton(book_label,text="Доступно",variable=check_value)
book_borrowed.pack(pady=5)
book_button = Button(book_label,text="Подтвердить",command=get_name)
book_button.pack(pady=5)
error_message_first = Label(book_label,text="Год выпуска должен быть цифрой",background="red",foreground="white")

library_label = ttk.Frame(notebook)
notebook.add(library_label,text="Библиотека")

name_label = Label(library_label,text="Имя")
name_label.pack(pady=5)
name = Entry(library_label)
name.pack(pady=5)
author = Label(library_label,text="Автор")
author.pack(pady=5)
author_entry = Entry(library_label)
author_entry.pack(pady=5)
year = Label(library_label,text="Год выпуска")
year.pack(pady=5)
year_entry = Entry(library_label)
year_entry.pack(pady=5)
check_button = IntVar()
is_borrowed = Checkbutton(library_label,text="Доступно", variable=check_button)
is_borrowed.pack(pady=5)
confirm = Button(library_label,text="Добавить книгу",command=get_name_library)
confirm.pack(pady=5)
error_message = Label(library_label,text="Год должен быть в виде цифер",background="red",foreground="white")
book_listbox = Listbox(library_label,width=100,height=10)

show_list_books = Button(library_label,text="Показать список книг",command=lambda:show_books(book_listbox))
show_list_books.pack(pady=5)

remove_by_title = Label(library_label,text="Удалить книгу по названию")
remove_by_title.pack(pady=6)
remove_by_title_entry = Entry(library_label)
remove_by_title_entry.pack(pady=6)
confirm_button = Button(library_label,text="Удалить",foreground="white",background="red",command=remove_books)
confirm_button.pack(pady=5)
root.mainloop()


