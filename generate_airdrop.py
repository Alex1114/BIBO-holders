#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

holder_path  = "data/holder.txt"

holders = []
address = []
quantity = []

with open(holder_path) as f:
    for line in f.readlines():
        s = line.split("\n")
        holders.append(str(s[0]))

x = 1
for i in range(len(holders)):
    repeat = False

    if (i > 0):
        if (holders[i] == holders[i-1]):
            repeat = True
            x += 1
            quantity[-1] = x

    else:
        address.append("\'" + str(holders[i]) + "\'")
        quantity.append(x)

    if (repeat == False and i > 0):
        x = 1
        address.append("\'" + str(holders[i]) + "\'")
        quantity.append(x)

print(len(quantity))
print(len(address))

with open('data/address_1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(address[0:100])

with open('data/quantity_1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(quantity[0:100])

with open('data/address_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(address[100:200])

with open('data/quantity_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(quantity[100:200])

with open('data/address_3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(address[200:300])

with open('data/quantity_3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(quantity[200:300])

with open('data/address_4.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(address[300:400])

with open('data/quantity_4.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(quantity[300:400])

with open('data/address_5.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(address[400:])

with open('data/quantity_5.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(quantity[400:])