import matplotlib.pyplot as plt
import csv

# Creating empty list to store star data
star_data_rows = []

# storing star data in the list
with open("star_data_with_gravity.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        star_data_rows.append(row)

star_data_rows.pop(0)  # Removing the headers from the list

# print(star_data)

# Creating lists to store different parameters of stars
radiuses = []
masses = []
gravity = []

for star_data in star_data_rows:
    masses.append(star_data[3])
    radiuses.append(star_data[4])
    gravity.append(star_data[5])

radiuses.sort()
masses.sort()
gravity.sort()

plt.plot(radiuses, masses)
plt.xlabel("radius")
plt.ylabel("mass")
plt.show()

plt.plot(gravity, masses)
plt.xlabel("gravity")
plt.ylabel("mass")
plt.show()