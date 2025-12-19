# PID controller
class PID:
    def __init__(self, kp, ki, kd):    # Defining A PID controller must be created with 3 no.s/ inputs kp, ki, kd
        self.kp= kp                    # self stores gain so the controller "remembers" them
        self.ki= ki
        self.kd= kd
    
        self.integral= 0.0              # Integral needs memory: it accumalets error over time
        self.last_error= 0.0            # Derivative needs the previous error to compute the rate of change
    
    def update( self, error, dt):       # Every timestep in a loop, the controller is updated with the current error & dt
        self.integral= self.integral + error*dt   # error*dt adds the area under error curve for this timestep
        derivative= (error- self.last_error)/dt   # error- self.last_error gives how much error has changed, /dt = rate of change
        
        output= (                      # Combine P + I + D terms into an output
            self.kp*error
            + self.ki * self.integral
            + self.kd * derivative
        )                              # PID formula: output is sum of 3 terms & is a control signal: velocity, accel, motor command
        self.last_error= error         # Update last_error for next timestep, after derivative is computed
        return output                  # Returning output lets simulation use the control signal