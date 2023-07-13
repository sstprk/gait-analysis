from load_mvnx import load_mvnx
import matplotlib.pyplot as plt

data = load_mvnx(r"C:\Users\stcr3\Desktop\Data\baran_walking-001.mvnx")
frame_count = data.frame_count
temp = []
foot_contacts = []

for idx in range(frame_count):
    temp.append(data.get_foot_contacts(frame=idx))
    foot_contacts.append(temp[idx][0])

left_heel_strikes = []
i = 1
for i in range(frame_count):
    if foot_contacts[i-1][0] - foot_contacts[i][0] == -1:
        left_heel_strikes.append(i)

right_heel_strikes = []

ix = 1
for ix in range(frame_count):
    if foot_contacts[ix-1][3] - foot_contacts[ix][3] == -1:
        right_heel_strikes.append(ix)

def get_joint(RjointIndex, LjointIndex, rList, lList):
    for i in range(frame_count):
        rList.append(data.get_joint_angle(RjointIndex)[i])
        lList.append(data.get_joint_angle(LjointIndex)[i])

right_knee = []
left_knee = []

get_joint(15, 19, right_knee, left_knee)

print(right_knee)


#Plotting 
"""plt.subplot(2,1,1)
plt.title("Left Knee Angles")
plt.plot([], label=("x", "y", "z"), marker="*")
plt.xlim(0,len(left_heel_strikes))
plt.legend()

plt.subplot(2,1,2)
plt.title("Right Knee Angles")
plt.plot([], label=("x", "y", "z"), marker="*")
plt.xlim(0, len(left_heel_strikes))
plt.legend()

plt.show()"""