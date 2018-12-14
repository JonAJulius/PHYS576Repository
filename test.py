from pyuvdata import UVData
from SSINS import SS
from SSINS import Catalog_Plot as cp
from SSINS import plot_lib
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

outpath = '/Users/jonj/Test_Folder/lwa'
obs = 'LWA_First_Test_without_Autocorelate'
read_kwargs = {'ant_str':'cross'}
bad_time_indices = [0,-1,-2,-3]

UV1 = UVData()
UV2 = UVData()
UV3 = UVData()
UV4 = UVData()
UV5 = UVData()
UV6 = UVData()
UV7 = UVData()
UV8 = UVData()
UV = UVData()

UV1.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp2_0_00300673800807520000_58342_05_00_14.ms', ant_str = 'cross')
#UV2.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp2_0_00300673800807520000_58342_05_00_24.ms', ant_str = 'cross')
#UV3.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp2_0_00300673800807520000_58342_05_00_34.ms', ant_str = 'cross')
#UV4.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp3_0_00300673800807520000_58342_05_00_14.ms', ant_str = 'cross')
#UV5.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp3_0_00300673800807520000_58342_05_00_24.ms', ant_str = 'cross')
#UV6.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp3_0_00300673800807520000_58342_05_00_34.ms', ant_str = 'cross')
#UV7.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp6_0_00300673800807520000_58342_05_00_14.ms')
#UV8.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp1_0_00300674099096000000_58342_05_39_26.ms')

#UV1.object_name = 'same'
#UV1.unphase_to_drift()
#UV1.phase(5.03706309897,.598912483314)

#UV2.object_name = 'same'
#UV2.unphase_to_drift()
#UV2.phase(5.03706309897, .598912483314)

#UV3.object_name = 'same'
#UV3.unphase_to_drift()
#UV3.phase(5.03706309897,.598912483314)

print UV1.freq_array


#UV = UV1 + UV2 + UV3

#ss = SS(obs=obs, outpath=outpath, UV = UV, diff= True)
#print(ss.UV.data_array.mean(axis=1).shape)


#ss.INS_prepare()
#ss.VDH_prepare()
#print 'Marker 2'
#ss.INS.save()
#ss.VDH.save()

#cp.INS_plot(ss.INS, ms_vmax=5, ms_vmin=-5)
#print 'Marker 3'
#cp.VDH_plot(ss.VDH, xscale = 'linear')
#print 'Marker 4'
#fig, ax = plt.subplots(nrows = 2)
#ss.INS.outpath = '/Users/jonj/Test_Folder/lwa'




