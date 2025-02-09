
from classes.teatcher import Teatcher
from classes.print_data import Print

def teacher_phase():
    """get user input"""
    print_obj=Print("Teatcher")
    name =print_obj.print_name()
    surname =print_obj.print_surname()
    title=print_obj.print_title()
    adress=print_obj.print_adress()
    town=print_obj.print_town()
    course=print_obj.print_course_name()

    """Create a teatcher instance with user-provided data"""
    teacher = Teatcher(name=name, surname=surname,title=title,adress=adress, town=town, course=course)

    """save teacher data to JSON"""
    data_teacher=teacher.add_teatcher()

    print("Saved teacher data", data_teacher)


    def results():
        print_obj.print_person_info_results(name,surname)

    results()