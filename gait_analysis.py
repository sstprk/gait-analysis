from load_mvnx import load_mvnx
import matplotlib.pyplot as plt

#A class for lists
class lists:
    foot_contacts = []
    left_heel_strikes = []
    right_heel_strikes = []
    right_joint = []
    left_joint = []
    xleft_gait_cycles = []
    yleft_gait_cycles = []
    zleft_gait_cycles = []
    xright_gait_cycles = []
    yright_gait_cycles = []
    zright_gait_cycles = []

#Importing the walking data
data = load_mvnx(r"C:\Users\stcr3\Desktop\Data\baran_walking-001.mvnx")
frame_count = data.frame_count
temp = []

for idx in range(frame_count):
    temp.append(data.get_foot_contacts(frame=idx))
    lists.foot_contacts.append(temp[idx][0])

#Determinating the heel strikes for each foot
i = 1
for i in range(frame_count):
    if lists.foot_contacts[i-1][0] - lists.foot_contacts[i][0] == -1:
        lists.left_heel_strikes.append(i)

ix = 1
for ix in range(frame_count):
    if lists.foot_contacts[ix-1][3] - lists.foot_contacts[ix][3] == -1:
        lists.right_heel_strikes.append(ix)

#A function for reading the joint data
def get_joint(RjointIndex, LjointIndex, rList, lList):
    for i in range(frame_count):
        rList.append(data.get_joint_angle(RjointIndex)[i])
        lList.append(data.get_joint_angle(LjointIndex)[i])

#Seperating each axis of cycles with a function 
def organise_joint(rList, lList):
    j = 1
    for j in range(len(lists.left_heel_strikes)):
        ltempListx = []
        ltempListy = []
        ltempListz = []
        for x in range(lists.left_heel_strikes[j-1], lists.left_heel_strikes[j]):
            if lists.left_heel_strikes[j] == 0:
                continue
            ltempListx.append(lList[x][0])
            ltempListy.append(lList[x][1])
            ltempListz.append(lList[x][2])
        lists.xleft_gait_cycles.append(ltempListx)
        lists.yleft_gait_cycles.append(ltempListy)
        lists.zleft_gait_cycles.append(ltempListz)

    k = 1
    for k in range(len(lists.right_heel_strikes)):
        rtempListx = []
        rtempListy = []
        rtempListz = []
        for y in range(lists.right_heel_strikes[k-1], lists.right_heel_strikes[k]):
            if lists.right_heel_strikes[k] == 0:
                continue
            rtempListx.append(rList[y][0])
            rtempListy.append(rList[y][1])
            rtempListz.append(rList[y][2])
        lists.xright_gait_cycles.append(rtempListx)
        lists.yright_gait_cycles.append(rtempListy)
        lists.zright_gait_cycles.append(rtempListz)

get_joint(16, 20, lists.right_joint, lists.left_joint)
organise_joint(lists.right_joint, lists.left_joint)

#Plotting the final data   
fig = plt.figure()
for i in range(len(lists.left_heel_strikes)): 
    plt.autumn()
    plt.subplot(3,2,1)
    plt.plot(lists.xleft_gait_cycles[i])

for i in range(len(lists.right_heel_strikes)):
    plt.subplot(3,2,2)
    plt.plot(lists.xright_gait_cycles[i])

for i in range(len(lists.left_heel_strikes)):
    plt.subplot(3,2,3)
    plt.plot(lists.yleft_gait_cycles[i])

for i in range(len(lists.right_heel_strikes)):
    plt.subplot(3,2,4)
    plt.plot(lists.yright_gait_cycles[i])

for i in range(len(lists.left_heel_strikes)):
    plt.subplot(3,2,5)
    plt.plot(lists.zleft_gait_cycles[i])

for i in range(len(lists.right_heel_strikes)):
    plt.subplot(3,2,6)
    plt.plot(lists.zright_gait_cycles[i])
plt.suptitle("Knee Flexion/Extension")
plt.show()
