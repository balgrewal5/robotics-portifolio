// HC-SR04 basic distance test
const int trigPin = 9;
const int echoPin = 8;

void setup() {
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  digitalWrite(trigPin, LOW); // keep TRIG low to start
}

void loop() {
  // 1) Trigger pulse: LOW -> HIGH for 10 microseconds -> LOW
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  // 2) Measure echo pulse length (microseconds)
  long duration = pulseIn(echoPin, HIGH, 30000); // timeout 30ms (~5m max)

  // 3) Convert to distance (cm)
  // speed of sound ~343 m/s => 0.0343 cm/us
  // distance = (duration * 0.0343) / 2
  float distance_cm = (duration * 0.0343) / 2.0;

  // If timeout happened, duration will be 0
  if (duration == 0) {
    Serial.println(-1);
  } else {
    Serial.println(distance_cm);
  }

  delay(100);
}
