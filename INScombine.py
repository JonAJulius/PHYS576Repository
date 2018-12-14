from SSINS import util, INS, INS_helpers, plot_lib, MF
from SSINS import Catalog_Plot as cp
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

basedir = '/Users/jonj/Test_folder/lwa'
obs =['LWA_50to51', 'LWA_51to52', 'LWA_52to53', 'LWA_53to54', 'LWA_54to55','LWA_55to56', 'LWA_56to57', 'LWA_57to58', 'LWA_58to59', 'LWA_59to60'] 
outpath = '%s/test_combines' % basedir
insarray = []
for x in obs:
	read_paths = util.read_paths_construct(basedir, 'None', x, 'INS')
	insarray.append(INS(obs = x, outpath = outpath, read_paths = read_paths, flag_choice = 'orginal'))
inscombined = INS_helpers.INS_concat(insarray,axis = 0)
inscombined.obs = 'LWA_50to60'
inscombined.outpath = outpath
inscombined.vis_units = insarray[0].vis_units
inscombined.pols = insarray[0].pols
inscombined.save()

cp.INS_plot(inscombined, vmax = .05, ms_vmax = 5, ms_vmin = -5)


shape_dict = {'44MHZ':[44e6,45e6],'40.6MHZ':[40.4e6,40.7e6]}
sig_thresh = 4.35

mf = MF(inscombined, shape_dict=shape_dict, sig_thresh=sig_thresh,point = False,streak = False)

mf.apply_match_test()

cp.MF_plot(mf, ms_vmin = -mf.sig_thresh, ms_vmax = mf.sig_thresh)


