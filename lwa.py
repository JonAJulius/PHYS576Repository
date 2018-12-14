from pyuvdata import UVData
from SSINS import SS
from SSINS import Catalog_Plot as cp
from SSINS import plot_lib
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt


UV2 = UVData()
UV3 = UVData()
UV4 = UVData()
UV5 = UVData()
UV6 = UVData()
UV = UVData()

outpath = '/Users/jonj/Test_Folder/lwa'
obs = 'LWA_59to60'
read_kwargs = {'ant_str':'cross'}
bad_time_indices = [0,-1,-2,-3]



second = ['04','14','24','34','44','54']

inpath1 = []
inpath2 = []
inpath3 = []
inpath4 = []
inpath5 = []


for y in range(59,60):
    for z in second:
	if y < 10:
        	inpath1.append('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp2_0_00300673800807520000_58342_05_0%s_%s.ms' % (y,z))
	else :
		inpath1.append('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp2_0_00300673800807520000_58342_05_%s_%s.ms' % (y,z))

for y in range(59,60):
    for z in second:
        inpath2.append('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp3_0_00300673800807520000_58342_05_%s_%s.ms' % (y,z))

for y in range(59,60):
    for z in second:
        inpath3.append('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp4_0_00300673800807520000_58342_05_%s_%s.ms' % (y,z))

for y in range(59,60):
    for z in second:
        inpath4.append('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp5_0_00300673800807520000_58342_05_%s_%s.ms' % (y,z))

for y in range(59,60):
	for z in second:
		inpath5.append('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp6_0_00300673800807520000_58342_05_%s_%s.ms' % (y,z))



#inpath1.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp2_0_00300673800807520000_58342_05_00_04.ms')
#inpath2.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp3_0_00300673800807520000_58342_05_00_04.ms')
#inpath3.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp4_0_00300673800807520000_58342_05_00_04.ms')
#inpath4.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp5_0_00300673800807520000_58342_05_00_04.ms')
#inpath5.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp6_0_00300673800807520000_58342_05_00_04.ms')

UVtemp = UVData()


UV2.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp2_0_00300673800807520000_58342_05_59_04.ms',ant_str = 'cross')
inpath1.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp2_0_00300673800807520000_58342_05_59_04.ms')
UV2.object_name = 'same'
UV2.unphase_to_drift()
UV2.phase(5.03706309897, .598912483314)


for x in inpath1:
	UVtemp.read(x, ant_str = 'cross')
	UVtemp.object_name = 'same'
        UVtemp.unphase_to_drift()
        UVtemp.phase(5.03706309897,.598912483314)
    	UV2 = UV2 + UVtemp
	print UV2.Nbls
	print UV2.Ntimes
	print UV2.Nblts

UV3.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp3_0_00300673800807520000_58342_05_59_04.ms', ant_str = 'cross')
inpath2.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp3_0_00300673800807520000_58342_05_59_04.ms')
UV3.object_name = 'same'
UV3.unphase_to_drift()
UV3.phase(5.03706309897, .598912483314)

for x in inpath2:
	UVtemp.read(x, ant_str = 'cross')
    	UVtemp.object_name = 'same'
    	if not UVtemp.phase_center_dec == .598912483314 or not UVtemp.phase_center_ra == 5.03706309897:
        	UVtemp.unphase_to_drift()
        	UVtemp.phase(5.03706309897,.598912483314)
    	UV3 = UV3 + UVtemp

UV4.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp4_0_00300673800807520000_58342_05_59_04.ms', ant_str = 'cross')
inpath3.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp4_0_00300673800807520000_58342_05_59_04.ms')
UV4.object_name = 'same'
UV4.unphase_to_drift()
UV4.phase(5.03706309897, .598912483314)


for x in inpath3:
    	UVtemp.read(x, ant_str = 'cross')
    	UVtemp.object_name = 'same'
    	if not UVtemp.phase_center_dec == .598912483314 or not UVtemp.phase_center_ra == 5.03706309897:
        	UVtemp.unphase_to_drift()
		UVtemp.phase(5.03706309897,.598912483314)
	UV4 = UV4 + UVtemp

UV5.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp5_0_00300673800807520000_58342_05_59_04.ms', ant_str = 'cross')
inpath4.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp5_0_00300673800807520000_58342_05_59_04.ms')
UV5.object_name = 'same'
UV5.unphase_to_drift()
UV5.phase(5.03706309897, .598912483314)


for x in inpath4:
    	UVtemp.read(x, ant_str = 'cross')
    	UVtemp.object_name = 'same'
    	if not UVtemp.phase_center_dec == .598912483314 or not UVtemp.phase_center_ra == 5.03706309897:
        	UVtemp.unphase_to_drift()
        	UVtemp.phase(5.03706309897,.598912483314)
    	UV5 = UV5 + UVtemp

UV6.read('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp6_0_00300673800807520000_58342_05_59_04.ms', ant_str = 'cross')
inpath5.remove('/Volumes/Faramir/uvfits/fornax.phys.unm.edu/lwa/data/LWA-SV/Wideband/test_adp6_0_00300673800807520000_58342_05_59_04.ms')
UV6.object_name = 'same'
UV6.unphase_to_drift()
UV6.phase(5.03706309897,.598912483314)

for x in inpath5:
    	UVtemp.read(x, ant_str = 'cross')
    	UVtemp.object_name = 'same'
    	if not UVtemp.phase_center_dec == .598912483314 or not UVtemp.phase_center_ra == 5.03706309897:
        	UVtemp.unphase_to_drift()
        	UVtemp.phase(5.03706309897,.598912483314)
    	UV6 = UV6 + UVtemp

UV = UV2 + UV3 + UV4 + UV5 + UV6

print UV.Nbls
print UV.Ntimes
print UV.Nblts
print 'the buck stop here'

ss = SS(obs=obs, outpath=outpath, UV = UV, diff= True)

ss.INS_prepare()
print 'Marker 1'
ss.VDH_prepare()
print 'Marker 2'
ss.INS.save()
ss.VDH.save()

cp.INS_plot(ss.INS, ms_vmax=5, ms_vmin=-5)
print 'Marker 3'
cp.VDH_plot(ss.VDH, xscale = 'linear')

