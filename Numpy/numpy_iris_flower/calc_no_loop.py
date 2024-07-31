# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    new_points_reshaped=new_points[:,np.newaxis,:]
    points_reshaped=points[np.newaxis,:,:]
    d=np.sum(np.square(new_points_reshaped-points_reshaped),axis=2)
    return d # TO-DO
