import math

def main():
    print("hello, my name is {} and I like {}.".format("Timber", math.pi))
    print("hello, my name is {} and I like {:.3}.".format("Timber", math.pi))
    print("hello, my name is {} and I like {:.3f}.".format("Timber", math.pi))
    print("hello, my name is {} and I like {:.2f}.".format("Timber", math.pi))
    print("hello, my name is {:.3s} and I like {:.2f}.".format("Timber", math.pi))
    print("hello, my name is {:^20} and I like {:.2f}.".format("Timber", math.pi))
    print("hello, my name is {} and I like {:>14.2f}.".format("Timber", math.pi))
    print("hello, my name is {} and I like {:.3}.".format("Timber", 147.58))
    print("hello, my name is {} and I like {:.3}.".format("Timber", 147.16))
    print("hello, my name is {} and I like {:.3f}.".format("Timber", 147.58))

    print()
    
    #name = "Justin"
    #age = 39
    #t_name = "Timber"
    #t_age = 24
    #s_name = "Shandell"
    #s_age = 35
    #c_name = "Case"
    #c_age = 24

    #print("{:<10}{:^5}".format("name", "age"))
    #print("{:<10}{:^5}".format(name, age))
    #print("{:<10}{:^5}".format(t_name, t_age))
    #print("{:<10}{:^5}".format(s_name, s_age))
    #print("{:<10}{:^5}".format(c_name, c_age))

    people = [
        {"name": "Justin", "age":40, "sport":"track"},
        {"name": "Timber", "age":24, "sport":"softball"},
        {"name": "Shandell", "age":35, "sport":"boxing"},
        {"name": "Case", "age":24, "sport":"basketball"},
    ]

    print("{:<10}{:<10}{:<10}".format("name", "age", "sport"))
    for person in people:
        print("{:<10}{:<10}{:<10}".format(person["name"], person["age"], person["sport"]))

    print()

    records = [
        {"title" : "Title 1", "release_year": 1000, "genre" : "rock"},
        {"title" : "Title 2", "release_year": 2000, "genre" : "rock"},
        {"title" : "Title 3", "release_year": 3000, "genre" : "rock"},
        {"title" : "Title 4", "release_year": 4000, "genre" : "rock"},
        {"title" : "Title 5", "release_year": 5000, "genre" : "rock"},
        {"title" : "Title 6", "release_year": 6000, "genre" : "rock"},
        {"title" : "Title 7", "release_year": 7000, "genre" : "rock"},
    ]

    print("{:<10}{:<10}{:<10}".format("title", "release", "genre"))
    for record in records:
        print("{:<10}{:<10}{:<10}".format(record["title"], record["release_year"], record["genre"]))

if __name__ == "__main__":
    main()