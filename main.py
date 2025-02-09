import constants.phase_constants
from phases.teacher_intro import teacher_phase


current_phase=constants.phase_constants.INTRO
while True:
    if current_phase==constants.phase_constants.INTRO:
        current_phase==teacher_phase()


