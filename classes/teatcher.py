from classes.person import Person
from classes.print_data import Print
import json

class Teatcher(Person):
    def __init__(self,name:str, surname:str, title:str, adress:str =None, town:str=None, course:str=""):
        super().__init__(name, surname, title, adress, town) 
        self.course=course


    def load_courses(self, file_name="courses.json"):
        """load avalaible courses fro JSON file"""
        try:
            with open(file_name, "r", encoding="utf-8" ) as file:
                courses=json.load(file)
            return [course["name_of_course"] for course in courses]
        except (FileNotFoundError, json.JSONDecodeError):
            """return empty list if file is missing or corrupted"""
            return[] 
    


    def add_teatcher(self, file_name="teatcher.json", course_file="courses.json"):

        """check if the course exist before adding the teatcher"""
        avalaible_courses=self.load_courses(course_file)

        if self.course not in avalaible_courses:
            print(f"error: course {self.course} does not exist. Please add it first")
            return None

        teatcher_data={"name":self.name, "surname":self.surname, "title": self.title, "adress":self.adress, "town":self.town, "course":self.course }

        
        """read existing data or create a new list"""

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data=[]
        
        data.append(teatcher_data)

        """save back to json file"""
        with open(file_name, "w", encoding="utf-8")as file:
            json.dump(data,file, indent=4, ensure_ascii=False)
        
        Print.print_save_teatcher_data()

        return teatcher_data
    
