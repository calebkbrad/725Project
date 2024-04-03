#!/usr/bin/python3

import os

def main():
    with open('data/pedfatalitiesbytype.csv', 'w') as final_csv:
        final_csv.write('Year, Vehicle Type, Number of Fatalities\n')
        for file in os.listdir('data/processed'):
            with open(f'data/processed/{file}') as input:
                passenger_fatalities = input.readline().split()[12]
                final_csv.write(f'{file.split(".")[0]}, Car, {passenger_fatalities}\n')
                truck_fatalities = input.readline().split()[12]
                final_csv.write(f'{file.split(".")[0]}, Truck, {truck_fatalities}\n')

if __name__ == "__main__":
    main()