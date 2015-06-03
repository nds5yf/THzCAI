device=rf.N('sapphire.s1p')
caled=cal.apply_cal(device)
freq=caled[0].frequency
air50 =rf.media.Freespace(frequency =freq, z0 = 50)
air377 =rf.media.Freespace(frequency =freq, ep_r=1)
saphire = rf.media.Freespace(frequency = freq, ep_r= 10)
substrate_thickness = 430e-6
# re-embed sample 
for k in caled:
    caled[k]= air50.line(substrate_thickness)**caled[k]
    caled[k].name = k

if write_caled_duts:
    [caled[k].write_touchstone(dir = join(dir,'caled_duts')) for k in caled]
    
    
def plot_stuff():
    caled_ns = rf.NS([caled[k] for k in caled if name in k])
    
    figure()
    title('%s, Phase'%title_name)
    [caled[k].plot_s_deg_unwrap() for k in caled if name in k]
    
    
    figure()
    title('%s, Phase With Bounds'%title_name)
    caled_ns.plot_minmax_bounds_s_deg_unwrap(label='Measured')
    
    figure()
    title('%s, Magnitude'%title_name)
    [caled[k].plot_s_db() for k in caled if name in k]
    ylim(ybounds)
    
    figure()
    title('%s, Magnitude  With Bounds'%title_name)
    caled_ns.plot_minmax_bounds_s_db(label='Measured')
    ylim(ybounds)
    