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
        for key in dta:
            dta_grade = dta[key]['grade']
            dta_subjects = dta[key]['subjects']
            dta_profs = dta[key]['subjects proficiency']
            dis_g, dis_s, dis_p = 0, 0, 0
            dis_g += float(self.grade_level - dta_grade)**2
            for i in range(len(dta_subjects)):
                dis_s += float(self.subjects[i]-dta_subjects[i])**2
                dis_p += float(self.proficiencies[i]- dta_profs[i])**2
            if self.name != key:
                self.dists[key] = [dis_g, dis_s, dis_p]
        return self.dists
                    
        

d = open('/Users/subhashsrinivasa/Desktop/GitHub/linghacks-jsk/data/database.json', 'r')
data = json.load(d)    
data_users = data['users']
testuser = 'username1'
test = data['users'][testuser]
tst = User(testuser,test['subjects'], test['grade'], test['subjects proficiency'])
print(tst.dist_finder(data_users))