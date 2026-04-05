from student import Student
from file_manager import save_students, load_students

def add_student(students):
    student_id = input("ID: ")
    name = input("Имя: ")
    age = input("Возраст: ")
    grade = input("Оценка: ")

    student = Student(student_id, name, age, grade)
    students.append(student)
    print(" Студент добавлен")

def show_students(students):
    if not students:
        print(" Список пуст")
        return

    for student in students:
        print(student)

def delete_student(students):
    student_id = input("Введите ID для удаления: ")
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("🗑️ Удалено")
            return
    print(" Студент не найден")

def main():
    students = load_students()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить студента")
        print("2. Показать всех")
        print("3. Удалить студента")
        print("4. Сохранить")
        print("5. Выход")

        choice = input("Выберите: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            save_students(students)
            print(" Сохранено")
        elif choice == "5":
            save_students(students)
            print("Выход")
            break
        else:
            print(" Неверный выбор")

if __name__ == "__main__":
    main()