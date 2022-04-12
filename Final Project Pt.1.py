# Bruk Thomas Tewelde
# PSID:1834504
# FINAL PROJECT PT.1


import csv
import string
import itertools

Fullroster = {
}
dict_StudentMajorlist = {
}
dict_GPAList = {
}
dict_GraduationDatesList = {
}
with open('StudentsMajorsList.csv', mode='r') as StudentMajorlist_file:
    s = 0
    for i in StudentMajorlist_file:
        a, b, c, d, e = i.rstrip('\n').split(',')
        dict_StudentMajorlist[s] = {"ID": a, "last": b, "first": c, "major": d, "displinary": e}
        s += 1
with open('GPAList.csv', mode='r') as GPA_file:
    s = 0
    for i in GPA_file:
        a, b = i.rstrip('\n').split(',')
        dict_GPAList[s] = {"ID": a, "GPA": b}
        s += 1
with open('GraduationDatesList.csv', mode='r') as GraduationDatesList_file:
    s = 0
    for i in GraduationDatesList_file:
        a, b = i.rstrip('\n').split(',')
        dict_GraduationDatesList[s] = {"ID": a, "Date": b}
        s += 1
g = ""
d = ""
o = 0
for x in dict_StudentMajorlist:
    for y in dict_GPAList:
        if dict_StudentMajorlist[x]["ID"] == dict_GPAList[y]["ID"]:
            g = dict_GPAList[y]["GPA"]
    for z in dict_GraduationDatesList:
        if dict_StudentMajorlist[x]["ID"] == dict_GraduationDatesList[z]["ID"]:
            d = dict_GraduationDatesList[y]["Date"]
    Fullroster[o] = {"ID": dict_StudentMajorlist[x]["ID"], "major": dict_StudentMajorlist[x]["major"],
                     "first": dict_StudentMajorlist[x]["first"],
                     "last": dict_StudentMajorlist[x]["last"], "GPA": g, "Date": d,
                     "displinary": dict_StudentMajorlist[x]["displinary"]}
    o += 1
print(Fullroster)
for i in Fullroster.keys():
    if i < 6:
        j = i + 1
    while j <= 6:
        if Fullroster[i]["last"][0] > Fullroster[j]["last"][0]:
            Fullroster[i], Fullroster[j] = Fullroster[j], Fullroster[i]
        j = j + 1

print(Fullroster)
fields = {'ID', 'major', 'first', 'last', 'GPA', 'Date', 'displinary'}
with open("FullRoster.csv", "w") as f:
    w = csv.DictWriter(f, fields)
    w.writeheader()
    for k in Fullroster:
        w.writerow({field: Fullroster[k].get(field) or k for field in fields})
computer = {}
l = 0
with open("ComputerScience.csv", "w") as f:
    for k in Fullroster:
        if Fullroster[k]["major"] == 'Computer Science':
            computer[l] = {"ID": Fullroster[k]["ID"], "first": Fullroster[k]["first"],
                           "last": Fullroster[k]["last"], "GPA": Fullroster[k]["GPA"], "Date": Fullroster[k]["Date"],
                           "displinary": Fullroster[k]["displinary"]}
        l += 1
fields1 = {'ID', 'first', 'last', 'GPA', 'Date', 'displinary'}
with open("ComputerScience.csv", "w") as f:
    w = csv.DictWriter(f, fields1)
    w.writeheader()
    for k in computer:
        w.writerow({field: computer[k].get(field) or k for field in fields1})

electrical = {}
l = 0
for k in Fullroster:
    if Fullroster[k]["major"] == 'Electrical Engineering':
        electrical[l] = {"ID": Fullroster[k]["ID"], "first": Fullroster[k]["first"],
                         "last": Fullroster[k]["last"], "GPA": Fullroster[k]["GPA"], "Date": Fullroster[k]["Date"],
                         "displinary": Fullroster[k]["displinary"]}
    l += 1

fields2 = {'ID', 'first', 'last', 'GPA', 'Date', 'displinary'}
with open("ElectricalEngineeringStudents.csv", "w") as f:
    w = csv.DictWriter(f, fields2)
    w.writeheader()
    for k in electrical:
        w.writerow({field: electrical[k].get(field) or k for field in fields2})

ComputerInformationSystems = {}
l = 0
for k in Fullroster:
    if Fullroster[k]["major"] == 'Computer Information Systems':
        ComputerInformationSystems[l] = {"ID": Fullroster[k]["ID"], "first": Fullroster[k]["first"],
                                         "last": Fullroster[k]["last"], "GPA": Fullroster[k]["GPA"],
                                         "Date": Fullroster[k]["Date"], "displinary": Fullroster[k]["displinary"]}
    l += 1
fields3 = {'ID', 'first', 'last', 'GPA', 'Date', 'displinary'}
with open("ComputerInformationSystems.csv", "w") as f:
    w = csv.DictWriter(f, fields3)
    w.writeheader()
    for k in ComputerInformationSystems:
        w.writerow({field: ComputerInformationSystems[k].get(field) or k for field in fields3})

for i in Fullroster.keys():
    if i < 6:
        j = i + 1
    while j <= 6:
        if Fullroster[i]["GPA"][0] < Fullroster[j]["GPA"][0]:
            Fullroster[i], Fullroster[j] = Fullroster[j], Fullroster[i]
        j = j + 1
print(Fullroster)
scholar = {}
l = 0
for k in Fullroster:
    if Fullroster[k]["GPA"] > '3.8' and Fullroster[k]["displinary"] != 'Y':
        scholar[l] = {"ID": Fullroster[k]["ID"], "first": Fullroster[k]["first"],
                      "last": Fullroster[k]["last"], "major": Fullroster[k]["major"], "GPA": Fullroster[k]["GPA"]}
        l += 1
fields4 = {'ID', 'first', 'last', 'major', 'Date'}
with open("ScholarshipCandidates.csv", "w") as f:
    w = csv.DictWriter(f, fields4)
    w.writeheader()
    for k in scholar:
        w.writerow({field: scholar[k].get(field) or k for field in fields4})
for i in Fullroster.keys():
    if i < 6:
        j = i + 1
    while j <= 6:
        if Fullroster[i]["Date"][0] < Fullroster[j]["Date"][0]:
            Fullroster[i], Fullroster[j] = Fullroster[j], Fullroster[i]
        j = j + 1
displinary = {}
l = 0
for k in Fullroster:
    if Fullroster[k]["displinary"] != 'Y':
        displinary[l] = {"ID": Fullroster[k]["ID"],
                         "last": Fullroster[k]["last"], "first": Fullroster[k]["first"], "Date": Fullroster[k]["Date"]}
    l += 1
fields5 = {'ID', 'first', 'last', 'Date'}
with open("DisciplinedStudents.csv", "w") as f:
    w = csv.DictWriter(f, fields5)
    w.writeheader()
    for k in displinary:
        w.writerow({field: displinary[k].get(field) or k for field in fields5})
