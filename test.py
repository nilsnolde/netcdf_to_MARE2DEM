# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:12:57 2017

@author: nnolde
"""

import os
import numpy as np
from netCDF4 import Dataset
from emtools import BaseClasses

# In[10]:

nc_dir = r"C:\Users\nnolde\Documents\Python27\Projects\EM\MARE2DEM\Rotated"
ex_nc = None
nc_list = []
for fd, sub, files in os.walk(nc_dir):
    for f in files:
        if f.endswith('.nc'):   
            ex_nc = BaseClasses.nc(os.path.join(nc_dir, f), 'r')