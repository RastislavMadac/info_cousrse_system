import json
class Courses:
    def __init__(self, name_of_course:str=None):
        self.name_of_course=name_of_course
    
    def add_of_course(self, file_name="courses.json"):
        courses_data={"name_of_course":self.name_of_course}

        """read existing data or create a new list"""

        try:
            with open(file_name, "r", encoding="utf-8")as file:
                data=json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data=[]
        
        data.append(courses_data)

        """save back to json file"""
        with open (file_name, "w", encoding="utf-8") as file:
            json.dump(data,file,indent=4, ensure_ascii=False)

        return courses_data

