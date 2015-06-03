device=rf.N('Silicon.s1p')
caled=cal.apply_cal(device)
device2=rf.N('hfss_off.s1p')
device2.name='Theory dielectric=11.5'
device3=rf.N('hfss air gap.s1p')
device3.name='Theory dielectric=11.5 dembedding'

my_vna.s11.write_touchstone('AmbientAbs')
my_vna.s11.write_touchstone('MaskAbs')
my_vna.s11.write_touchstone('LightAbs')
device = rf.N('Ambient.s1p')
device2 = rf.N('MaskAbs.s1p')
device3 = rf.N('LightAbs.s1p')
device.plot_s_db()
device2.plot_s_db()
device3.plot_s_db()
device.plot_s_deg()
device2.plot_s_deg()
device3.plot_s_deg()
newDevice = device/device2
newDevice.plot_s_deg()

caled.plot_s_db()
#figure()
caled.plot_s_deg()
caled.plot_s_re()
caled.plot_s_im()
device2.plot_s_deg()
device3.plot_s_deg()
#caled.plot_s_deg()my
caled.plot_s_smith()


freq=caled.frequency
air377 =rf.media.Freespace(frequency =freq, ep_r=1)
saphire = rf.media.Freespace(frequency = freq, ep_r= 11.5)


substrate_thickness = 430e-6
model = air377.line(0)**saphire.delay_short(substrate_thickness)

model.name = 'Theory'

model.s = model.s*exp(1j*rf.degree_2_radian(30))


figure()
caled.plot_s_db()

model.plot_s_db()

title('Saphire, Phase')

difference=caled/model

figure()
difference.plot_s_deg_unwrap()
title('difference in phase: measurement vs model')


my_vna.s11.write_touchstone('sample 455')
rf.NS(cal.apply_cal(rf.lat().values())).plot_s_db()