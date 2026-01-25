// Week 4 Day 4 — HC-SR04 distance reading

const int trigPin = 9;
const int echoPin = 8;

void setup() {
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Make sure TRIG starts LOW
  digitalWrite(trigPin, LOW);
}

void loop() {
  // 1) Send a 10 microsecond trigger pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  // 2) Measure how long the ECHO pin stays HIGH (in microseconds)
  long duration_us = pulseIn(echoPin, HIGH, 30000); // timeout 30ms

  // 3) Convert time to distance
  // Speed of sound ≈ 343 m/s = 0.0343 cm/us
  // Distance = (duration * speed_of_sound) / 2   (divide by 2 for round trip)
  float distance_cm = (duration_us * 0.0343) / 2.0;

  // 4) Print result
  Serial.print("duration_us=");
  Serial.print(duration_us);
  Serial.print("  distance_cm=");
  Serial.println(distance_cm, 1);

  delay(100);
}
