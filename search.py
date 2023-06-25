import json
import numpy as np
class User():
    def __init__(self, usrname, subs, grd, profs):
        self.name = usrname
        self.subjects = subs
        self.grade_level = grd
        self.proficiencies = profs
        self.dists = {}
        self. grp = {}
    def dist_finder(self, dta):
        self.dists[self.name] = {}
        for user in dta:
            dta_grade = user['grade']
            dta_subjects = user['subjects']
            dta_profs = user['subjects proficiency']
            dis_g, dis_s, dis_p = 0, 0, 0
            dis_g += float(self.grade_level - dta_grade)**2
            for i in range(len(dta_subjects)):
                dis_s += float(self.subjects[i]-dta_subjects[i])**2
                dis_p += float(self.proficiencies[i]- dta_profs[i])**2
            
            if self.name != user['username']:
                self.dists[self.name][user['username']]= [dis_g, dis_s, dis_p]
class System():
    def __init__(self):
        self.coeffs = [1,1,1]


d = open('database.json', 'r')
data = json.load(d)    
data_users = data['users']
K = len(data_users)/5
users_dists = {}
for user in data_users:
    usr_object = User(user['username'],user['subjects'], user['grade'], user['subjects proficiency'])
    usr_object.dist_finder(data_users)
    print(usr_object.dists)
