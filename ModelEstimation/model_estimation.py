# Copyright Ryo Tamura
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. 

# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
# GNU General Public License for more details. 

# You should have received a copy of the GNU General Public License 
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
#-------------------------------------------------------------

#In
import numpy as np
import cPickle as pickle
import scipy
import combo
import os
import urllib
import matplotlib.pyplot as plt

#In

import hphi_io as hphi

hphi_cond = {}
#For sekirei
#hphi_cond["mpi_command"] = "mpijob"
hphi_cond["path_hphi"] = "./HPhi"
hphi_cond["path_input_file"] = "stan.in"
HPhi_calc = hphi.calc_mag(hphi_cond)


#In
#Create candidate
window_num=20

J1_lower=0.0
J1_upper=2.0

J2_lower=0.0
J2_upper=2.0

J3_lower=0.0
J3_upper=2.0

X=[]

for i in range(window_num+1):
    for j in range(window_num+1):
       for k in range(window_num+1):

          X.append([round(J1_lower+(J1_upper-J1_lower)/window_num*i,3),
          round(J2_lower+(J2_upper-J2_lower)/window_num*j,3),
          round(J3_lower+(J3_upper-J3_lower)/window_num*k,3)])


X=np.array(X)



#In

#target magnetization
input_dict = {}
input_dict["J0"] = 1.0
input_dict["J0'"] = 0.5
input_dict["J0''"] = 0.3
energy_list = HPhi_calc.get_energy_by_hphi(input_dict)

magnetic_field=[0.01*num for num in range(300)]

target=[]

for H in magnetic_field:
    target.append(HPhi_calc.get_mag(energy_list, H))

#fig = plt.figure(figsize=(10, 6))
#plt.plot(magnetic_field,target,'.',label="target")
#plt.xlabel("Magnetic field")
#plt.ylabel("Magnetization")
#plt.legend(loc='lower right')
#plt.savefig('Target.png', dpi=150)





#In
# Load the data.
# X is the N x d dimensional matrix. Each row of X denotes the d-dimensional feature vector of search candidate.
# t is the N-dimensional vector that represents the corresponding negative energy of search candidates.
# ( It is of course unknown in practice. )


# Normalize the mean and standard deviation along the each column of X to 0 and 1, respectively
X_normalized = combo.misc.centering( X )



#In
# Declare the class for calling the simulator.
# In this tutorial, we simply refer to the value of t.
# If you want to apply combo to other problems, you have to customize this class.
class simulator:

    def __init__( self ):

        pass

    def __call__( self, action ):
    
        input_dict = {}
        input_dict["J0"] = X[action][0][0]
        input_dict["J0'"] = X[action][0][1]
        input_dict["J0''"] = X[action][0][2]
        energy_list = HPhi_calc.get_energy_by_hphi(input_dict)


        delta_m=0.0

        for num in range(300):
            delta_m=delta_m+(HPhi_calc.get_mag(energy_list, magnetic_field[num])-target[num])**2

        delta_m_list.append(delta_m)
        J1_list.append(X[action][0][0])
        J2_list.append(X[action][0][1])
        J3_list.append(X[action][0][2])


        print "*********************"
        print "Present optimum interactions"

        print "J1=",J1_list[np.argmin(np.array(delta_m_list))]
        print "J2=",J2_list[np.argmin(np.array(delta_m_list))]
        print "J3=",J3_list[np.argmin(np.array(delta_m_list))]

        print ""


        return -delta_m


delta_m_list=[]
J1_list=[]
J2_list=[]
J3_list=[]

#In
# Design of policy

# Declaring the policy by
policy = combo.search.discrete.policy(test_X=X_normalized)
# test_X is the set of candidates which is represented by numpy.array.
# Each row vector represents the feature vector of the corresponding candidate

# set the seed parameter
policy.set_seed( 111 )



#In[]

# If you want to perform the initial random search before starting the Bayesian optimization,
# the random sampling is performed by

res = policy.random_search(max_num_probes=20, simulator=simulator())

# Input:
# max_num_probes: number of random search
# simulator = simulator
# output: combo.search.discreate.results (class)


# single query Bayesian search
# The single query version of COMBO is performed by
res = policy.bayes_search(max_num_probes=80, simulator=simulator(), score='TS',
                                                  interval=20, num_rand_basis=5000)


# Input
# max_num_probes: number of searching by Bayesian optimization
# simulator: the class of simulator which is defined above
# score: the type of aquision funciton. TS, EI and PI are available
# interval: the timing for learning the hyper parameter.
#               In this case, the hyper parameter is learned at each 20 steps
#               If you set the negative value to interval, the hyper parameter learning is not performed
#               If you set zero to interval, the hyper parameter learning is performed only at the first step
# num_rand_basis: the number of basis function. If you choose 0,  ordinary Gaussian process runs



#In

best_fx, best_action = res.export_all_sequence_best_fx()

#estimated magnetization
input_dict = {}
input_dict["J0"] = X[int(best_action[-1])][0]
input_dict["J0'"] = X[int(best_action[-1])][1]
input_dict["J0''"] = X[int(best_action[-1])][2]
energy_list = HPhi_calc.get_energy_by_hphi(input_dict)

estimated=[]

for H in magnetic_field:
    estimated.append(HPhi_calc.get_mag(energy_list, H))


#fig = plt.figure(figsize=(10, 6))
#plt.plot(magnetic_field,target,'.',label="target")
#plt.plot(magnetic_field,estimated,'.',label="estimated")
#plt.xlabel("Magnetic field")
#plt.ylabel("Magnetization")
#plt.legend(loc='lower right')
#plt.savefig('Estimation_result.png', dpi=150)


print "*********************"
print ''
print 'Estimated model parameter'
print 'J1=',X[int(best_action[-1])][0]
print 'J2=',X[int(best_action[-1])][1]
print 'J3=',X[int(best_action[-1])][2]
print ''
print ''



#In

# The result of searching is summarized in the class combo.search.discrete.results.history()
# res.fx: observed negative energy at each step
# res.chosed_actions: history of choosed actions
# fbest, best_action= res.export_all_sequence_best_fx(): current best fx and current best action
#                                                                                                   that has been observed until each step
# res.total_num_search: total number of search
print 'f(x)='
fx_list = res.fx[0:res.total_num_search]
print fx_list

print 'history of chosed actions='
action_list = res.chosed_actions[0:res.total_num_search]
print action_list

print 'current best'
print best_fx

print 'current best action='
print best_action
        
#Save results to dat file
with open("combo_res.dat", "w") as f:
    for _fx, _action, _best_fx, _best_action in zip(fx_list, action_list, best_fx, best_action):
        f.write("{} {} {} {}\n".format(_fx, _action, _best_fx, _best_action))
