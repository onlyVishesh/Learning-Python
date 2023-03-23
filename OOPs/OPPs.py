def main():
    print(f"{get_student()['name']} from {get_student()['house']}")

def get_student():
    return  {"name" : input("Name :  "), "house" : input("House :  ")} #returning tuple

if __name__ == "__main__":
    main()