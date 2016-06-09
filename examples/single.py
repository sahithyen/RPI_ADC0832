import time

# Import the ADC0832 library
import RPI_ADC0832

# Create an ADC0832 instance
adc = RPI_ADC0832.ADC0832()

print('Reading ADC0832 values of channel 0 and 1')
print('Press Ctrl-C to quit...')

# Print channel column headers
print('-' * 13)
print('| {0:>3} | {1:>3} |'.format(*range(2)))
print('-' * 13)

# Main loop
while True:
    # Read all the ADC channel values in a list
    values = [0]*2

    for i in range(2):
        values[i] = adc.read_adc(i)

    # Print the ADC values
    print('| {0:>3} | {1:>3} |'.format(*values))

    time.sleep(0.5)
