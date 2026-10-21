
/*
 * Robotics Roadmap 1 - Week 5
 * Arduino Fundamentals: Analog Input and PWM
 *
 * Read a potentiometer and adjust LED brightness.
 * Demonstrates analogRead(), analogWrite(),
 * value mapping and serial communication.
 */

const int potPin = A0;
const int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Read potentiometer (0-1023)
  int potValue = analogRead(potPin);

  // Convert analog reading to PWM range (0-255)
  int pwmValue = map(potValue, 0, 1023, 0, 255);

  // Adjust LED brightness
  analogWrite(ledPin, pwmValue);

  // Monitor readings
  Serial.print("Analog: ");
  Serial.print(potValue);
  Serial.print(" | PWM: ");
  Serial.println(pwmValue);

  delay(100);
}
