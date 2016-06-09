# RPI_ADC0832
A python library to use the ADC0832 analog to digital converter with a Raspberry Pi

## Installation

To install the library from source (recommended) run the following commands on a Raspberry Pi or other Debian-based OS system:

    sudo apt-get install git build-essential python-dev
    cd ~
    git clone https://github.com/sahithyen/RPI_ADC0832.git
    cd RPI_ADC0832
    sudo python setup.py install

## Usage

Here is a sample code which prints the current value of channel 0 and the difference between channel 0 and channel 1

    import time
    import RPI_ADC0832

    # Create an ADC0832 instance
    adc = RPI_ADC0832.ADC0832()

    # Specify which GPIO pins will be used
    adc.csPin = 17 # Default pin: 17
    adc.clkPin = 27 # Default pin: 27
    adc.doPin = 22 # Default pin: 23
    adc.diPin = 22 # Default pin: 24

    # Print the current value of channel 0
    print('Value of channel 0: ' +  adc.read_adc(0))

    # Print the difference of both channel. You have to give which channel has the bigger value
    print('Difference: ' +  adc.read_adc(0))

You can use the digital input and output pin connected to the same GPIO pin.
