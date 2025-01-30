import pygame
import random

class Person ():
    def __init__(self):
        self.sex = None
        #self.dob = None
        self.medicalHistory = []

    def set_sex(self, sex=None):
        if sex != None:
            self.sex = sex
        else:
            self.sex = random.choices(["M","F","O"],[50,50,.05])

    # set a dob

    # get the age calculated based on dob and game day

    # add item to medicalHistory
    def add_medical_issue (self, mi):
        self.medicalHistory.append(mi)

    # fun idea, simulate nutrition, weight, spo2, cardiovascular fitness, other items that get into the details of 
    # the individual, but not sure that's actually worth the overhead for a population health sim