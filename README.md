## Space-Debris-Detector
# Features of the model
 1. LSTM-Based Sequential Model

- The core of the prototype is an LSTM (Long Short-Term Memory) neural network.
- Designed to learn from time-series data, it effectively captures temporal dependencies in 
  orbital motion.
- Built using the Sequential API from TensorFlow/Keras for simplicity and flexibility.

2. Modern, Clean Architecture

- Utilizes the Input(shape=...) layer to avoid deprecated input_shape warnings.
- Ensures compliance with best practices in TensorFlow model design.
- Modular code structure for easy scaling and integration of additional layers in future.

3. Simulated Orbital Trajectory Data

- Instead of using random noise, the model trains on a synthetic sinusoidal function (sin(t)) 
  mimicking orbital debris movement.
- This creates a realistic pattern of motion, ideal for early learning by the model.
- Adds slight Gaussian noise to replicate real-world disturbances.

4. Preprocessing Pipeline

- Implements a create_dataset() function to convert a flat time series into supervised learning 
  format.
- Reshapes data for LSTM input ([samples, timesteps, features]), enabling temporal learning.

5. Model Training Loop

- Trains over 10 epochs using mean squared error (MSE) loss.
- Uses Adam optimizer for stable and adaptive learning.
- Prints loss at every epoch to monitor convergence.

6. Visual Output – Prediction Graph

- Final result is a plotted comparison of actual vs predicted debris positions.
- Uses matplotlib to visualize the learning quality and pattern prediction.
- Graph clearly shows the model’s ability to track and predict movement trends.

7. Self-Contained and Demo-Ready 

- The current version does not rely on any external dataset or internet connection.
- All data is generated inside the script, making it ideal for offline demonstration.
- Lightweight and executable on any basic machine with Python 3.10 and TensorFlow.

8. Modular Code for Easy Expansion

- Code is cleanly divided into sections: data simulation, preprocessing, model building, 
  training, and visualization.
- Ready for integration with real debris datasets (e.g., TLE from NORAD).
- Can be adapted for Streamlit dashboards, web interfaces, or advanced models with minimal changes.
   
