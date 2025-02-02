import pygame

# Eventually I want to implement ICD codes to be comprehensive
# in our simulation. But for now I just want to implement
# a few items.
# https://jackwasey.github.io/icd/
# This ICD package is for R and covers ICD-9 and ICD-10
# https://icd.who.int/dev11/downloads/
# This is the WHO downlaod site 
# https://icd.who.int/icdapi
# ICD API from WHO
# https://icd.who.int/icdapi/docs/ICD-schema.html
# Schema of the ICD API

class MedicalIssue ():
    def __init__ (self, name, impact, communicability = 0,
                  mutability = 0, incubation = 0,
                  mortality = 0):
        self.name = name
        self.impact = impact
        self.communicability = communicability
        self.mutability = mutability
        self.incubation = incubation
        self.mortality = mortality




