
t = []

while True:
    c = input("Введите команду (add, remove, list, exit): ")
    
    if c.startswith("add "):
        t.append(c[4:])
        print("Задача добавлена.")
    
    elif c.startswith("remove "):
        try:
            i = int(c[7:])
            r = t.pop(i)
            print(f"Задача '{r}' удалена.")
        except IndexError:
            print("Ошибка: Задача с таким индексом не существует.")
        except ValueError:
            print("Ошибка: Введите корректный номер задачи.")
    
    elif c == 'list':
        if not t:
            print("Список задач пуст.")
        else:
            for j, task in enumerate(t):
                print(f"{j}: {task}")
    
    elif c == 'exit':
        print("Выход из программы.")
        break
    
    else:
        print("Ошибка: Неизвестная команда. Используйте add, remove, list или exit.")