import sys
import numpy as np
import pandas as pd

df = pd.read_csv(sys.argv[1])
df_new = {}

name_map = {
    0  : "Nose",
    1  : "Neck",
    2  : "RShoulder",
    3  : "RElbow",
    4  : "RWrist",
    5  : "LShoulder",
    6  : "LElbow",
    7  : "LWrist",
    8  : "MidHip",
    25 : "LPalmBase",
    26 : "LThumb1CMC",
    27 : "LThumb2Knuckles",
    28 : "LThumb3IP",
    29 : "LThumb4FingerTip",
    30 : "LIndex1Knuckles",
    31 : "LIndex2PIP",
    32 : "LIndex3DIP",
    33 : "LIndex4FingerTip",
    34 : "LMiddle1Knuckles",
    35 : "LMiddle2PIP",
    36 : "LMiddle3DIP",
    37 : "LMiddle4FingerTip",
    38 : "LRing1Knuckles",
    39 : "LRing2PIP",
    40 : "LRing3DIP",
    41 : "LRing4FingerTip",
    42 : "LPinky1Knuckles",
    43 : "LPinky2PIP",
    44 : "LPinky3DIP",
    45 : "LPinky4FingerTip",
    46 : "RPalmBase",
    47 : "RThumb1CMC",
    48 : "RThumb2Knuckles",
    49 : "RThumb3IP",
    50 : "RThumb4FingerTip",
    51 : "RIndex1Knuckles",
    52 : "RIndex2PIP",
    53 : "RIndex3DIP",
    54 : "RIndex4FingerTip",
    55 : "RMiddle1Knuckles",
    56 : "RMiddle2PIP",
    57 : "RMiddle3DIP",
    58 : "RMiddle4FingerTip",
    59 : "RRing1Knuckles",
    60 : "RRing2PIP",
    61 : "RRing3DIP",
    62 : "RRing4FingerTip",
    63 : "RPinky1Knuckles",
    64 : "RPinky2PIP",
    65 : "RPinky3DIP",
    66 : "RPinky4FingerTip"
}

# Get time
subname = '/openpose_ros/human_list/header'
secs = subname + '/stamp/secs'
nsecs = subname + '/stamp/nsecs'
time = [float(str(int(item[0])) + '.' + '0'*(9-len(str(int(item[1])))) + str(int(item[1]))) \
     for item in zip(df[secs], df[nsecs]) \
    if not np.isnan(item[0])]
time = [i-time[0] for i in time]
df_new.update({'Time' : time})

# /openpose_ros/human_list/human_list/0/body_key_points_with_prob/0/x

subname = '/openpose_ros/human_list/human_list/0/'

# Get coordinates
body_parts = {'body_key_points_with_prob/' : np.arange(1,9), 'left_hand_key_points_with_prob/' : np.arange(25,46), 'right_hand_key_points_with_prob/' : np.arange(46,67)}
coords = ['x', 'y', 'prob']
for key in body_parts.keys():
	for v in body_parts[key]:
		for coord in coords:
			# print(name_map[v])
			if key == 'body_key_points_with_prob/':
				df_new.update({str(name_map[v])+'.'+coord : df[subname+key+str(v)+'/'+coord]})
			elif key == 'left_hand_key_points_with_prob/':
				df_new.update({str(name_map[v])+'.'+coord : df[subname+key+str(v-25)+'/'+coord]})
			else:
				df_new.update({str(name_map[v])+'.'+coord : df[subname+key+str(v-46)+'/'+coord]})


df_new = pd.DataFrame(df_new)
df_new.to_csv(sys.argv[1].split('.')[0]+'_new.csv', index=False)