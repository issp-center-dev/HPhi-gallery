# Copyright ISSP, The University of Tokyo 
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

import subprocess
import os

class calc_mag:
    def __init__(self, hphi_cond):
        self.input_param = {}
        self.mpi_command = hphi_cond["mpi_command"] if "mpi_command" in hphi_cond else ""
        self.path_hphi = hphi_cond["path_hphi"] 
        self.input_path = hphi_cond["path_input_file"]
        self.input_param["model"] = "Spin"
        self.input_param["method"] = "CG"
        self.input_param["lattice"] = "chain"
        self.input_param["L"] = 12
        self.input_param["J0"] = 1.0
        self.input_param["J0'"] = 0.5
        self.input_param["J0''"] = 0.25
        self.input_param["exct"] = 2
        self.input_param["2Sz"] = 0
        self.energy_list = []

    def _make_input_file(self):
        with open(self.input_path, "w") as f:
            for key, item in self.input_param.items():
                f.write("{} = {}\n".format(key, item))

    def _change_input(self, input_dict):
        #input_dict = {J0: 1.0, J0': 0.5, J0'': 0.25)
        for key, value in input_dict.items():
            self.input_param[key] = value

    def _get_energy_from_hphi(self):
        energy_list = []
        if os.path.exists("./output/zvo_energy.dat"):
            str_output = "./output/zvo_energy.dat"
            with open(str_output, "r") as f:
                lines = f.readlines()
            for line in lines:
                line1 = line.split()
                if (line.find("Energy") != -1):
                    energy_list.append(float(line1[1]))
        else:
            print("Energy file does not exist.")
            return None
        return energy_list

    def get_energy_by_hphi(self, input_dict):
        self._change_input(input_dict)
        #update 2Sz
        L = self.input_param["L"]
        energy_list = []
        for sz in range(L//2 + 1):
            self.input_param["2Sz"] = 2*sz
            self._make_input_file()

            cmd = "{} {} -s {} > std.log".format(self.mpi_command, self.path_hphi, self.input_path)
            subprocess.call(cmd, shell=True)
    
            energy = self._get_energy_from_hphi()
            if energy is None:
                exit(0)
            energy_list.append((sz, energy[0]))
            self.energy_list = energy_list
            subprocess.call("rm *.def", shell=True)
            subprocess.call("rm lattice.gp", shell=True)
            subprocess.call("rm geometry.dat", shell=True)
        return energy_list

    def get_mag(self, sz_energy_list, H):
        energy_mag = []
        for sz_energy in sz_energy_list:
            energy_mag.append(sz_energy[1]-sz_energy[0]*H)
        min_index = energy_mag.index(min(energy_mag))
        return sz_energy_list[min_index][0]
