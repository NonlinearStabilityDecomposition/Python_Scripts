# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:40:26 2024

@author: User
"""
from abaqus import *
from abaqusConstants import *
import regionToolset
import __main__
import section
import regionToolset
import part
import material
import assembly
import step
import interaction
import load
import mesh
import job
import sketch
import visualization
import xyPlot
import connectorBehavior
import odbAccess
from operator import add

from caeModules import *
from driverUtils import executeOnCaeStartup

import numpy as np
import matplotlib.pyplot as plt
from random import randint
import os

os.chdir(r"C:\MC_2025_Y\G21")
#a = mdb.models['Model-1'].rootAssembly
for i in range(17,71,1):
    mdb.ModelFromInputFile(name='IW1_'+str(i)+'_scaled', inputFileName='C:\MC_2025_Y\G21/IW1_'+str(i)+'_scaled.inp')


# os.chdir(r"C:\MC_2025_wt4\A12")
# #a = mdb.models['Model-1'].rootAssembly
# for i in range(17,61,1):
#     mdb.ModelFromInputFile(name='IW1_'+str(i)+'_scaled', inputFileName='C:\MC_2025_wt4\A12/IW1_'+str(i)+'_scaled.inp')

# os.chdir(r"E:\MC_2025_v2_MGI\A400_Y145")
# #a = mdb.models['Model-1'].rootAssembly
# for i in range(17,48,1):
#     mdb.ModelFromInputFile(name='IW1_'+str(i)+'_scaled', inputFileName='E:\MC_2025_v2_MGI\A400_Y145/IW1_'+str(i)+'_scaled.inp')

# os.chdir(r"C:\MC_2025_v1_MGI\A200M")
# #a = mdb.models['Model-1'].rootAssembly
# for i in range(17,61,1):
#     mdb.ModelFromInputFile(name='IW1_'+str(i)+'_scaled', inputFileName='C:\MC_2025_v1_MGI\A200M/IW1_'+str(i)+'_scaled.inp')

# os.chdir(r"F:\MC_2025_v1_MGI2\A10000")
# #os.chdir(r"D:\MC_Z\Z200 - 2")
# #a = mdb.models['Model-1'].rootAssembly
# for i in range(1,29,1):
#     mdb.ModelFromInputFile(name='Z1_'+str(i)+'_scaled', inputFileName='E:\MC_2025_v1_MGI2\A10000/Z1_'+str(i)+'_scaled.inp')