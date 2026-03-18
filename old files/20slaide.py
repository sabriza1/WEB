library_books = {
    "B001": {"title": "Основы Python", "borrower": "Алиса", "due_date": -5, "fine_rate": 0.5},
    "B002": {"title": "Наука о данных", "borrower": "Боб", "due_date": 3, "fine_rate": 0.75},
    "B003": {"title": "Введение в ИИ", "borrower": None, "due_date": 0, "fine_rate": 0.25},
    "B004": {"title": "Алгоритмы", "borrower": "Алиса", "due_date": 2, "fine_rate": 1.0}
}

def check_books(books):
    fines = {}  

    for book_id, info in books.items():
        borrower = info["borrower"]  
        days = info["due_date"]     
        rate = info["fine_rate"]     
        if borrower is None:
            print(book_id, "Доступна", 0)

        elif days < 0:
            fine = abs(days) * rate  
            print(book_id, "Просрочена", fine)
            fines[borrower] = fines.get(borrower, 0) + fine

        else:
            print(book_id, "В срок", 0)
            fines[borrower] = fines.get(borrower, 0)  

    if fines:  
        max_name = max(fines, key=fines.get)
        print("Больше всех должен:", max_name, fines[max_name])
    else:
        print("Штрафов нет.")

check_books(library_books)
