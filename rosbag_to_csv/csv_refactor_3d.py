import sys
import numpy as np
import pandas as pd

df = pd.read_csv(sys.argv[1])
df_new = {}

names_df = df.filter(regex='/name')
names = {}
for col in names_df.columns:
	key = '/'.join(col.split('/')[:4])
	names.update({key : names_df[col].iloc[0]}) #df[key+'/points/header/frame_id'].iloc[0]})

# Get time
subname = '/'.join(names_df.columns[0].split('/')[:4])
secs = subname + '/points/header/stamp/secs'
nsecs = subname + '/points/header/stamp/nsecs'
time = [float(str(int(item[0])) + '.' + '0'*(9-len(str(int(item[1])))) + str(int(item[1]))) \
     for item in zip(df[secs], df[nsecs]) \
    if not np.isnan(item[0])]
time = [i-time[0] for i in time]
df_new.update({'Time' : time})

# Get coordinates
coords = ['/points/point/x', '/points/point/y', '/points/point/z']
for k in names.keys():
	for coord in coords:
		if 'x' in coord:
			df_new.update({names[k]+'.'+coord[-1] : [i + 0.406 for i in df[k+coord] if not np.isnan(i)]})
		elif 'y' in coord:
			df_new.update({names[k]+'.'+coord[-1] : [i - 0.406 for i in df[k+coord] if not np.isnan(i)]})
		else:
			df_new.update({names[k]+'.'+coord[-1] : [i for i in df[k+coord] if not np.isnan(i)]})

df_new = pd.DataFrame(df_new)
df_new.to_csv(sys.argv[1].split('.')[0]+'_new.csv', index=False)