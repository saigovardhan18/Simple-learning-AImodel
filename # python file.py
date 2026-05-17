# Simple Learning AI Model
# Predicts marks and improves weights using error correction

study = 5
revision = 2
actual_marks = 73

# Initial weights
w1 = 8
w2 = 6

learning_rate = 0.01

while True:

    # Prediction
    predicted_marks = (study * w1) + (revision * w2)

    # Calculate error
    error = actual_marks - predicted_marks

    print(f"Prediction: {predicted_marks:.2f} | Error: {error:.2f}")

    # Stop if prediction is close enough
    if abs(error) < 0.01:
        print("\nModel trained successfully!")
        print(f"Final Weights -> w1: {w1:.4f}, w2: {w2:.4f}")
        break

    # Update weights
    w1 = w1 + (error * learning_rate)
    w2 = w2 + (error * learning_rate)
    
    
