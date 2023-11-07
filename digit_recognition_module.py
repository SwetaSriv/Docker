import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the model (make sure to provide the correct path to your model file)
model = load_model('path_to_your_model.h5')

def predict_digit(img_path):
    # Load an image file and resize it to the size your model was trained on, e.g., 28x28 pixels for MNIST
    img = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    
    # Convert the image to a numpy array
    img_array = image.img_to_array(img)
    
    # Scale image pixels by 255 (or use the same scaling your model was trained with)
    img_array /= 255
    
    # Flatten the image array and add an extra dimension for batch_size (required by keras)
    img_array = img_array.reshape(1, 28, 28, 1)
    
    # Make a prediction
    predictions = model.predict(img_array)
    
    # Get the digit with the highest probability
    predicted_digit = np.argmax(predictions)
    
    return predicted_digit