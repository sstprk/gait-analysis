from load_mvnx import load_mvnx
import matplotlib.pyplot as plt

class lists:
    foot_contacts = []
    left_heel_strikes = []
    right_heel_strikes = []
    right_knee = []
    left_knee = []
    left_gait_cycles = []
    right_gait_cycles = []

data = load_mvnx(r"C:\Users\stcr3\Desktop\Data\baran_walking-001.mvnx")
frame_count = data.frame_count
temp = []

for idx in range(frame_count):
    temp.append(data.get_foot_contacts(frame=idx))
    lists.foot_contacts.append(temp[idx][0])

i = 1
for i in range(frame_count):
    if lists.foot_contacts[i-1][0] - lists.foot_contacts[i][0] == -1:
        lists.left_heel_strikes.append(i)

ix = 1
for ix in range(frame_count):
    if lists.foot_contacts[ix-1][3] - lists.foot_contacts[ix][3] == -1:
        lists.right_heel_strikes.append(ix)

def get_joint(RjointIndex, LjointIndex, rList, lList):
    for i in range(len(lists.right_heel_strikes)):
        rList.append(data.get_joint_angle(RjointIndex)[lists.right_heel_strikes[i]])
    for i in range(len(lists.left_heel_strikes)):
        lList.append(data.get_joint_angle(LjointIndex)[lists.left_heel_strikes[i]])

get_joint(15, 19, lists.right_knee, lists.left_knee)

j = 1
for j in range(len(lists.left_heel_strikes)):
    diff = lists.left_knee[j] - lists.left_knee[j-1]
    lists.left_gait_cycles.append(diff)

k = 1
for k in range(len(lists.right_heel_strikes)):
    diff = lists.right_knee[k] - lists.right_knee[k-1] 
    lists.right_gait_cycles.append(diff)

#Plotting   
for i in range(len(lists.left_heel_strikes)): 
    plt.subplot(1,2,1)
    plt.title("Left Knee Flexion/Extension")
    plt.plot(lists.left_gait_cycles[i])

for i in range(len(lists.right_heel_strikes)):
    plt.subplot(1,2,2)
    plt.title("Right Knee Flexion/Extension")
    plt.plot(lists.right_gait_cycles[i])

plt.show()