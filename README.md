
# Analog-Clock

The Analog Clock: Each group must build an analog clock that tells the time (creativity is a must). The clock can be built from anything (cardboard, laser cut pieces, 3D printed, etc.) however, you must use at least one servo.

## Demo

https://user-images.githubusercontent.com/57788768/140411186-4c6056f9-7a67-407a-9bf7-f6a002e7d996.mp4

Watch on [Youtube](https://www.youtube.com/watch?v=XxoPbqSJhxU&list=PL8x_oaw7WPIKmYdH6yHr6_GRv5VZokT7q&index=9)

## Design

### Mechanical Design

Our CAD design is three “Barrels” one for hours, one for minutes and another for seconds. 

<img src="../../blob/main/media/cadModelISO.png" width="750">

<img src="../../blob/main/media/fabricatedModel.png" width="750">

We also had to design parts to holds the servo in the middle of the barrel with screwable clips.

<img src="../../blob/main/media/servomotorStand.png" width="200">

### Electronics Design 

#### Servo Motors 

* Servo HAT Allows for:
  * External libraries which simplifies communication with multiple servo motors without leaning on PWM
    *  Simplifies control to i2c where we only need
  *  Flexible Power Supply (Battery or Wall)
*  Use of Smaller Servo Motors allows for more compact design

#### Getting the Time 

* time.time()
  * Returns the number of seconds since EPOCH (1/1/1970)
* time.localtime(t)
  * Takes an input in seconds
  * Returns the Date and Time of that input as a struct containing hours, minutes, seconds, current month, year, and more
* Data converted to 12 hour clock format
* Time Multiplier:
  * Subtract current time and initial time, multiply by facto

### Software Design 

#### Robot Control (Clock Class)

* Stores previous servo positions (prevent twitch)
* Holds Lookup Tables
* Sets servo positions based on processed system time

#### Open Source

*Adafruit-circuitpython-servokit*

* Setups register-level configuration of servos
* i2c comms
* PWM communication for position control
* Easy API to access / control servos

## Run Locally

Clone the project

```bash
  git clone https://github.com/paccionesawyer/Analog-Clock.git
```

Go to the project directory

```bash
  cd Analog-Clock
```

Run the program

```bash
  python3 2Axis-LidarScanner.py
```


## Acknowledgements

 - [Readme.so](https://readme.so/editor)

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@paccionesawyer](https://github.com/paccionesawyer)

