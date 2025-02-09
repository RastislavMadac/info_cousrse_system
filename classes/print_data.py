from classes.person import Person
class Print(Person):
    def __init__(self,position=str):
         self.position = position

    def print_name(self):
        """Enter name of {position}"""
        return input(f"Enter name of {self.position} ")

        
    def print_surname(self):
        """Enter surname of {self.position}"""
        return input(f"Enter surname of {self.position} ")

    def print_title(self):
        """Enter title of {self.position}"""
        return input(f"Enter title of {self.position} ")
    
    def print_adress(self):
        """Enter adress of {self.position}"""
        return input(f"Enter adress of {self.position} ")
    
    def print_town(self):
        """Enter town of {self.position}"""
        return input(f"Enter town of {self.position} ")
    
    def print_course_name(self):
        """Enter course_name of {self.position}"""
        return input(f"Enter course name of {self.position} ")
    
    def print_person_info_results(self, name, surname):
        """Name of {self.position} is {name} {surname}"""
        print(f"Name of {self.position} is {name} {surname}")
    
        
    def print_save_teatcher_data():
        """"Teatcher saved succesfully!"""
        print("Teatcher saved succesfully!")
    
    def print_enter_name_of_course(self):
        return input(f"Enter name of {self.position}")

    def print_course_info_results(self, name):
        """Name of {self.position} is {name} """
        print(f"Name of {self.position} is {name} ")