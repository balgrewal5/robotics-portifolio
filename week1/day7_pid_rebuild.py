
class PID:
    def __init__(self, kp, ki ,kd):
        self.kp= kp
        self.ki= ki
        self.kd= kd

        self.integral= 0.0
        self.last_error= 0.0

    def update(self, error, dt0):
        self.integral += error * dt
        derivative = (error - self.last_error) / dt

        output= (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        self.last_error = error
        return output
    
if __name__ == "__main__":
    pid= PID(kp=0.2, ki=0.4, kd=0.1)  #create PID controller with specific gains

    #initial states
    target= 10.0
    position= 0.0
    dt= 0.1

    #run short control loop/simulation
    for step in range(20):
        error= target- position
        u= pid.update(error, dt)
        u= pid.update(error, dt)
        position= position + u * dt  #update position based on control output
        print(f"Step {step}: Position: {position:.2f}, Control={u:.2f}")