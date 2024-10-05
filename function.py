name = input("Enter your name: ")
course = input("Enter your course: ")

match course:
    case "BSIT":
        print(f"BS in Information Technology")
    case "BSCS":
        print(f"BS in Computer Science")
    case _:
        print(f"You don't belong in this department.")
