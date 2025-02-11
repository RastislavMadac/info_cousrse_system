

from classes.teatcher import Teatcher
import json

class Pupil(Teatcher):
    def __init__(self, name:str, surname:str, adress:str =None, town:str=None, course:str=""):
        # Pupils don’t need a title, so we pass an empty string
        super().__init__(name, surname, "", adress, town,course)
       
        
    def add_pupil(self, file_name="pupil.json", course_file="courses.json"):

        return self.add_teatcher(file_name, course_file)