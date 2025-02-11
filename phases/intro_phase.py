from classes.print_data import Print
import constants.phase_constants
intro_text=("Welcome in our info school sistem")
from phases.teacher_intro import teacher_phase
from phases.pupil_intro import pupil_phase
from phases.course_intro import course_phase

def intro_phase():
    while True:
        Print.print_choices()
        print()
        intro_choice=Print.choice_input()
        
        
        if intro_choice not in ["0","1", "2", "3"]:
            Print.wrong_choice()
            continue

        if intro_choice=="0":
            return constants.phase_constants.END
        
        if intro_choice=="1":
            teacher_phase()
        
        if intro_choice=="2":
            pupil_phase()
        
        if intro_choice=="3":
            course_phase()

            


