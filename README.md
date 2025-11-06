# 8-Bit Data Transmission Using LED Visible Light Communication

This project is part of my **Measuring Techniques and Systems** class at the [University of Jyväskylä](https://www.jyu.fi/en) last December 2023 during my Erasmus Mundus [RADMEP](https://master-radmep.org/) program. This was a group project with Nico and Ale where I was mostly responsible for the _design_, _characterization_, and _signal transfer/acquisition_.

## 1. Materials
To achieve this project, the following materials were used:
- (2) Arduino UNO
- (2) 525-nm/Green LEDs
- (2) Adafruit 161 Photoresistors
- Resistors (470 Ω, 12 kΩ, 20 kΩ)
- Connector wires
- Analog Discover 2

## 2. Schematic
Below is the schematic of the transmitter (in red) and receiver (in blue) circuits, both of which contain Arduino UNO microcontrollers to handle signal transfer and acquisition. This schematic was created from this website [here](https://www.circuit-diagram.org/editor/).

<img src = "Pictures/Schematic.png">

The basic operation involves an LED turning **ON** and **OFF** whose blinking sequence depends on the selected number from 0-255. The chosen number of bits is 8, which is enough to cover the entire range.
To inform the receiver side of an incoming signal, additional LED-photoresistor pair was added.

## 3. Photoresistor Characterization
The next step was to identify which is signal is **ON** or **OFF**, and this would depend on the photoresistor response to the 525-nm LED used. Below is the schematic of the photoresistor response to LED blinking in a dark environment:

<img src = "Picture/circ.png">

<img src="Pictures/Thresholding.jpg">
