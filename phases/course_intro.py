from classes.courses import Courses
from classes.print_data import Print
import constants.phase_constants

def course_phase():
    """get user input"""
    print_obj=Print("Course")
    name_of_course=print_obj.print_enter_name_of_course()

    """Create a course instance(objekt) wit user data"""
    course=Courses(name_of_course=name_of_course)

    """save course data to json"""

    data_course=course.add_of_course()

    print("Saved course data", data_course)

    def results():
        print_obj.print_course_info_results(name_of_course)

    results()

    return constants.phase_constants.INTRO
    