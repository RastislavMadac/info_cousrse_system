import constants.phase_constants
from phases.intro_phase import intro_phase
from classes.print_data import Print




current_phase=constants.phase_constants.INTRO

should_continue= True
while should_continue:
    if current_phase==constants.phase_constants.INTRO:
        current_phase=intro_phase()
    
    if current_phase==constants.phase_constants.END:
        Print.print_end_program()
        should_continue=False


