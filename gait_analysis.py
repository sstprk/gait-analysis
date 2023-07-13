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

for idx in range(frame_count):
    if foot_contacts[idx][0] == 1:
        continue
    left_heel_strikes.append(idx)

right_heel_strikes = []

for idx in range(frame_count):
    if foot_contacts[idx][3] == 1:
        continue
    right_heel_strikes.append(idx)
fig = plt.figure(0)
fig.subplots(1, 1, 1)
plt.plot(right_heel_strikes)
fig.subplots(1, 2, 0)
plt.plot(left_heel_strikes)
plt.show()