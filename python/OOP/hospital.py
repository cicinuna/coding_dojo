class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.current_patient_count = 0

    def admit(self, patient):
        if self.current_patient_count == 0:
            self.patients.append(patient)
            self.patients[0].bed_number = 1
            self.current_patient_count = len(self.patients)
            print "Admission for {} is complete. This patient has bed number: {}".format(self.patients[0].name, self.patients[0].bed_number)
            print ""
        elif self.current_patient_count > 0 and self.current_patient_count < self.capacity:
            self.patients.append(patient)
            self.patients[len(self.patients)-1].bed_number = len(self.patients)
            self.current_patient_count = len(self.patients)
            print "Admission for {} is complete. This patient has bed number: {}".format(self.patients[len(self.patients)-1].name, self.patients[len(self.patients)-1].bed_number)
            print ""
        else:
            print "The hospital is full with {} (max) patients, and cannot accept {} at this time.".format(self.current_patient_count, patient.name)
            print ""
        return self
    
    def discharge(self, patient):
        pop_index = 0
        for i in range(0, self.current_patient_count):
            if self.patients[i] == patient:
                pop_index = i
        self.patients.pop(pop_index)
        self.current_patient_count = len(self.patients)
        
        for x in range(pop_index, self.current_patient_count):
            self.patients[x].bed_number = x+1
        patient.bed_number = 0
        print "Discharge for {} is complete. There are {} space(s) left in the hospital!".format(patient.name, self.capacity-self.current_patient_count)
        print ""
        return self

    def show_patients(self):
        for i in range(0, self.current_patient_count):
            print "Current patient name is: {} and This patient is staying in bed number: {}".format(self.patients[i].name, self.patients[i].bed_number)
            print ""
        return self

class Patient(object):
    def __init__(self, id, name, allergies, address, contact):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.address = address
        self.contact = contact
        self.bed_number = 0

    def show_bed_number(self):
        print self.bed_number

# Creating a bunch of patient instances
patient1 = Patient("1", "Jason", "none", "some address", "some number")
patient2 = Patient("2", "Bosco", "none", "some address", "some number")
patient3 = Patient("3", "Nick", "none", "some address", "some number")
patient4 = Patient("4", "Steph", "none", "some address", "some number")
patient5 = Patient("5", "Nate", "none", "some address", "some number")
patient6 = Patient("6", "Patrick", "none", "some address", "some number")
patient7 = Patient("7", "Dan", "none", "some address", "some number")
patient8 = Patient("8", "Greg", "none", "some address", "some number")
patient9 = Patient("9", "Vlad", "none", "some address", "some number")

# Creating dojoHospital instance
dojoHospital = Hospital("Dojo Hospital", 5)

# Max capacity for dojoHospital is 5 patients, trying to add 6 in order to see if our conditional works
# Working as intended!
dojoHospital.admit(patient1)
dojoHospital.admit(patient2)
dojoHospital.admit(patient3)
dojoHospital.admit(patient4)
dojoHospital.admit(patient5)
dojoHospital.admit(patient6)

# Discharging patient3 and calling show_patients to see current list of patients, and to check that
# Their respective bed numbers have been arranged 
dojoHospital.discharge(patient3)
dojoHospital.show_patients()

dojoHospital.admit(patient6)

dojoHospital.discharge(patient1)
dojoHospital.discharge(patient2)
dojoHospital.show_patients()
dojoHospital.admit(patient7)

# Checking bed numbers for the discharged patients to make sure they have number 0
# Working as intended!
patient3.show_bed_number()
patient1.show_bed_number()
patient2.show_bed_number()