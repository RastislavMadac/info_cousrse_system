from classes.pupil import Pupil
from classes.print_data import Print
import constants.phase_constants

def pupil_phase():
    """get user input"""
    print_obj=Print("Pupil")
    name =print_obj.print_name()
    surname =print_obj.print_surname()
    
    adress=print_obj.print_adress()
    town=print_obj.print_town()
    course=print_obj.print_course_name()

    """Create a teatcher instance with user-provided data"""
    pupil = Pupil(name=name, surname=surname,adress=adress, town=town, course=course)

    """save teacher data to JSON"""
    data_pupil=pupil.add_pupil()

    if data_pupil:
        print("Saved teacher data", data_pupil)
    else:
        print("Failed to save pupil data.")

    def results():
        print_obj.print_person_info_results(name,surname)

    results()

    return constants.phase_constants.INTRO