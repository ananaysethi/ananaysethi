#!/usr/bin/env python
# coding: utf-8

# In[1]:


# SPIN 2021 Exercise II for Roland Haas' project - Improving speed of characterizing numerical relativity waveforms
# Solution by Ananay Sethi
# UID: ananays2


# In[2]:


import scipy.optimize
import numpy

omega0 = 1.2
phi0 = -1.3


# In[3]:


def fun(pars, times):
    # get trial parameters
    omega, phi = pars
    return numpy.sin(omega*times - phi) - numpy.sin(omega0*times - phi0)

times = numpy.linspace(0, 2., 100)

omega_start = 1.
phi0_start = 0.

x0 = numpy.array([omega_start, phi0_start])

res = scipy.optimize.least_squares(fun, x0, args = (times, ))# use scipy.optimize.least_squares to solve find parameters

# NOTE BY ANANAY - the line above was edited from the Example given in the documentation page - 
# "solving a curve fitting problem using robust loss function to take care of outliers in the data".
# specific line -- "res_lsq = least_squares(fun, x0, args=(t_train, y_train))".

print("success:", res.success, "pars:", res.x)

