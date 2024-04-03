#!/usr/bin/python3

import os

def main():
    for file in os.listdir('data/raw'):
        with open(f'data/raw/{file}', 'r') as input:
            with open(f'data/processed/{file}', 'w') as output:
                for line in input.readlines():
                    if 'Passenger Car' in line or 'Light Truck' in line:
                        output.write(line)

if __name__ == "__main__":
    main()