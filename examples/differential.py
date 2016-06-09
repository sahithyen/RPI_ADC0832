import math
import time
import atexit

# Import the ADC0832 library
import RPI_ADC0832

# Create an ADC0832 ADC instance
adc = RPI_ADC0832.ADC0832()

print('Reading the differential value on the ADC0832. Column 1 shows channel 0 subtracted by channel 1 and column 2 shows channel 1 subtracted by channel 0.')
print('Press Ctrl-C to quit...')

# Print mode column headers
print('-' * 13)
print('| {0:>3} | {1:>3} |'.format(*range(2)))
print('-' * 13)

# Main loop
while True:
    # Read all the ADC channel values in a list
    values = [0]*2

    for i in range(2):
        values[i] = adc.read_adc_difference(i)

    # Print the ADC values.
    print('| {0:>3} | {1:>3} |'.format(*values))

    time.sleep(0.5)
