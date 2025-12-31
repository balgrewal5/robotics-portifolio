
// LED dimmer with potentiometer
//Labels for pins
  int potPin = A0;  // Reads potentiometer middle pin voltage from A0
  int ledPin = 9;   //Makes a variable called ledPin, will control LED from pin 9 (PWM pin so can do fake analog with analogwrite)

  void setup()  {
    // put your setup code here, to run once:
    pinMode (ledPin, OUTPUT);        //Tells Arduino pin 9 is an OUTPUT pin (will send volgae out not read)
  }

void loop() {
  // put your main code here, to run in forever:
  int potValue = analogRead (potPin);     //Reads the volatge on A0, coverts to a number, 0-1023 where 5v is 1023
  int brightness= map (potValue, 0, 1023, 0, 255); // Uses 0-255 instead 
  analogWrite (ledPin, brightness); //Output PWM on pin 9, 0= LED off, 255= fully on, middle values= dimmer

}