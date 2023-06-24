import json
import numpy as np
class matcher():
    def __init__(self, usrname, subs, grd, profs):
        self.name = usrname
        self.subjects = subs
        self.grade_level = grd
        self.proficiencies = profs
    def sub_dist(self, dta):
        dists = {}
        
        for key in dta['users']:
            dta_subjects = dta['users'][key]['subjects']
            dis = 0
            for i in range(len(dta_subjects)):
                dis += (self.subjects[i]-dta_subjects[i])**2
            if self.name != key:
                dists[key] = dis
            # print(dists)
            min = 10000000
            closest = ''
        for user in dists:
            if dists[user] < min:
                min = dists[user]
        return dists
                    
        

d = open('/Users/subhashsrinivasa/Desktop/GitHub/linghacks-jsk/data/database.json', 'r')
data = json.load(d)    
testuser = 'username3'
test = data['users'][testuser]
p = matcher(testuser,test['subjects'], test['grade'], test['subjects proficiency'])
print(p.sub_dist(data))