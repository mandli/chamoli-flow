#!/usr/bin/env python

import numpy
import matplotlib.pyplot as plt

import clawpack.geoclaw.topotools as tt

path = "./ch_new_elev.nc"

topo = tt.Topography(path=path, topo_type=4)
topo.read(nc_params={"x_var":"x", "y_var":"y", "z_var":"Band1"})
topo.write(path="./ch_new_elev_converted.nc", topo_type=4)
