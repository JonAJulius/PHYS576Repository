from pyuvdata import UVData
from SSINS import SS
from SSINS import Catalog_Plot as cp
from SSINS import plot_lib
from SSINS import MF
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

file ='1061312272'

#for x in file:
inpath = '/Volumes/Faramir/uvfits/%s.uvfits' % (file)
#outpath = '/Users/jonj/Test_Folder/post'
#obs = 'post%s' % file
#read_kwargs = {'ant_str': 'cross','freq_chans':np.arange(8)}
#bad_time_indices = [0,-1,-2,-3]
UV1 = UVData()

UV1.read(inpath)

print UV1



#ss = SS(obs=obs,outpath=outpath,inpath=inpath,read_kwargs=read_kwargs,flag_choice = 'original')
#counts, bins = np.histogram(ss.UV.data_array, bins='auto')

#ss.INS_prepare()
#ss.VDH_prepare()
#ss.INS.save()
#ss.VDH.save()

#cp.INS_plot(ss.INS, ms_vmax=5, ms_vmin=-5)
#cp.VDH_plot(ss.VDH, xscale = 'linear')

#fig, ax = plt.subplots(nrows = 2)
#ss.INS.outpath = '/Users/jonj/Test_Folder'

#for i in range(2):
#	ss.INS.mean_subtract(order=i)
#	plot_lib.image_plot(fig,ax[i],ss.INS.data_ms[:,0,:,0],cmap=cm.coolwarm,freq_array=ss.INS.freq_array[0],title='order=%i' % i,vmin=-5,vmax=5)

#fig.savefig('%s/%s_order_compare.png' % (ss.INS.outpath,ss.INS.obs))

#shape_dict = {'TV4': [1.74e8, 1.82e8],'TV5':[1.82e8, 1.9e8], 'TV6':[1.9e8, 1.98e8]}
	

#sig_thresh = 5
	
#point = False
#streak = False
	
#ss.MF_prepare(sig_thresh = sig_thresh, shape_dict = shape_dict)

#ss.MF.apply_match_test()

#cp.MF_plot(ss.MF, ms_vmin = -ss.MF.sig_thresh, ms_vmax = ss.MF.sig_thresh)




	

