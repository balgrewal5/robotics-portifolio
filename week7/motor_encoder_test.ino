
/*
 * Robotics Roadmap 1 - Week 7
 * DC Motor and Encoder Integration
 *
 * L298N motor driver + two encoder motors.
 * Tests forward/reverse rotation and encoder ticks.
 * Reconstructed from the physical robot setup.
 */

// L298N motor driver pins
const int ENA = 5;
const int IN1 = 7;
const int IN2 = 8;

const int ENB = 6;
const int IN3 = 9;
const int IN4 = 10;

// Encoder pins
const int LEFT_A = 2;
const int LEFT_B = 4;
const int RIGHT_A = 3;
const int RIGHT_B = 11;

volatile long leftTicks = 0;
volatile long rightTicks = 0;

const int motorPWM = 220;

// Encoder interrupt functions
void leftEncoderISR() {
  leftTicks += digitalRead(LEFT_B) ? 1 : -1;
}

void rightEncoderISR() {
  rightTicks += digitalRead(RIGHT_B) ? 1 : -1;
}

void stopMotors() {
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}

void driveMotors(bool forward) {
  digitalWrite(IN1, forward ? HIGH : LOW);
  digitalWrite(IN2, forward ? LOW : HIGH);

  digitalWrite(IN3, forward ? HIGH : LOW);
  digitalWrite(IN4, forward ? LOW : HIGH);

  analogWrite(ENA, motorPWM);
  analogWrite(ENB, motorPWM);
}

void printEncoderCounts() {
  noInterrupts();
  long left = leftTicks;
  long right = rightTicks;
  interrupts();

  Serial.print("Left ticks: ");
  Serial.print(left);
  Serial.print(" | Right ticks: ");
  Serial.println(right);
}

void setup() {
  Serial.begin(9600);

  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(LEFT_A, INPUT_PULLUP);
  pinMode(LEFT_B, INPUT_PULLUP);
  pinMode(RIGHT_A, INPUT_PULLUP);
  pinMode(RIGHT_B, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(LEFT_A),
                  leftEncoderISR, RISING);

  attachInterrupt(digitalPinToInterrupt(RIGHT_A),
                  rightEncoderISR, RISING);

  stopMotors();
  Serial.println("Motor and encoder test ready.");
}

void loop() {
  Serial.println("Forward test");
  driveMotors(true);
  delay(3000);

  stopMotors();
  printEncoderCounts();
  delay(1000);

  Serial.println("Reverse test");
  driveMotors(false);
  delay(3000);

  stopMotors();
  printEncoderCounts();
  delay(2000);
}
