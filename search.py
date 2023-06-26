import json
import random
import math
import numpy as np
class User():
    def __init__(self, usrname, subs, grd, profs, dta):
        self.name = usrname
        self.subjects = subs
        self.grade_level = grd
        self.proficiencies = profs
        self.users = dta
        self.dists = {}
        self.nearestcentroid = ''
    def dist_finder(self, user):
        dta_grade = user.grade_level
        dta_subjects = user.subjects
        dta_profs = user.proficiencies
        dis_g, dis_s, dis_p = 0, 0, 0
        dis_g += float(self.grade_level - dta_grade)**2
        for i in range(len(dta_subjects)):
            dis_s += 5*(float(self.subjects[i]-dta_subjects[i])**2)
            dis_p += (float(self.proficiencies[i]- dta_profs[i])**2)/4
        return dis_g + dis_s - dis_p
class Centroid(User):
    def __init__(self, usrname, subs, grd, profs,dta):
        super().__init__(usrname, subs, grd, profs,dta)
        self.name = usrname
        self.subjects = subs
        self.grade_level = grd
        self.proficiencies = profs
        self.users = dta
        self.dists = {}
        self.cluster = []
    def new_cluster():
        pass
class System():
    def __init__(self, dta_users):
        self.K = math.ceil(float(len(data_users)/5))
        self.K_centroids = {}
        self.users = dta_users
    def cluster_picker(self):
        searching = True
        index =0
        centroid_users = []
        while searching:
            picked = self.users[random.randint(0,len(self.users)-1)]
            if picked['username'] not in centroid_users:
                centroid_users.append(picked['username'])
                self.K_centroids[picked['username']] = Centroid(picked['username'], picked['subjects'], picked['grade'], picked['subjects proficiency'], self.users)
                index += 1
            else:
                print('hey')
            if index >= self.K:
                searching = False
    def cluster_definer(self):
        self.cluster_picker()
        user_objects = []
        for user in self.users:
            usr_object = User(user['username'],user['subjects'], user['grade'], user['subjects proficiency'], self.users)
            user_objects.append(usr_object)
            print(usr_object.dists)

            for key in self.K_centroids:
                usr_object.dists[key] = usr_object.dist_finder(self.K_centroids[key])
            min = 1000000000000000
            for key in usr_object.dists:
                if usr_object.dists[key] <= min:
                    min = usr_object.dists[key]
                    closest = key
                usr_object.
            print(usr_object.name, usr_object.dists)
        
        

            
           



d = open('database.json', 'r')
data = json.load(d)    
data_users = data['users']

Search = System(data_users)
Search.cluster_definer()