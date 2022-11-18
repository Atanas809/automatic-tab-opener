

        if course not in my_dict.keys():
            my_dict[course] = list()

        my_dict[course].append(name)

        command = input().split(" : ")

    output(my_dict)

softuni_courses()
