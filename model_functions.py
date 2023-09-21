import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from configparser import ConfigParser
import os
from tkinter import *
from tkinter import filedialog, messagebox
from helper_functions import restore_special_char

# Model functions
def get_model(input_shape):
    """
    Returns a compiled neural network model.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=input_shape),  # Input layer
        tf.keras.layers.Dense(16, activation="tanh"),
        tf.keras.layers.Dense(200, activation="relu"),
        tf.keras.layers.Dense(300, activation="relu"),
        tf.keras.layers.Dense(200, activation="relu"),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.Dense(num_classes, activation="softmax")  # Output layer
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model

def train_model(EPOCHS, dir, save, name):
    """Data must be in a .data file formated as ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
This functions trains the data, creates the model and returns it"""
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
    data = pd.read_csv(dir, names=column_names, sep=",")

    # Map class labels to numerical values
    class_mapping = {
        "Iris-setosa": 0,
        "Iris-versicolor": 1,
        "Iris-virginica": 2
    }
    data["class"] = data["class"].map(class_mapping)

    x = data.drop("class", axis=1)
    y = data["class"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    global num_classes
    num_classes = len(data["class"].unique())

    y_train = tf.keras.utils.to_categorical(y_train, num_classes=num_classes)
    y_test = tf.keras.utils.to_categorical(y_test, num_classes=num_classes)

    input_shape = ((x_train.shape[1]),)
    
    model = get_model(input_shape)

    model.fit(x_train, y_train, epochs=EPOCHS)

    model.evaluate(x_test,  y_test, verbose=2)

    if save == True:
        model_dir = f'C:/Users/João/Projects/Resume.atempts/iris_identif/models/model_{name}.h5'
        model.save(model_dir)
        print(f"Model saved to {model_dir}.")

    return model

def predict_one(data_str, model_dir):
    """Data_str is a str formated as the following: ({s_len},{s_wid},{p_len},{p_wid}, Predict)
S- Sepal; P- Petal
model_dir is a str containing the location of the model
    """
    model = tf.keras.models.load_model(model_dir)
    new_data = [float(value) if i < 4 else value for i, value in enumerate(data_str.split(','))]
    new_data_features = new_data[:-1]

    predicted_probabilities = model.predict([new_data_features])
    predicted_class = tf.argmax(predicted_probabilities, axis=1)
    return predicted_class

def return_result(predicted_class):
    """Given a number, ir returns the name of the iris flower corresponding to the result
    0 = Iris-setosa
    1 = Iris-versicolor 
    2 = Iris-virginica """
    
    if predicted_class.numpy()[0] == 0:
        return 'Iris-setosa'
    
    elif predicted_class.numpy()[0] == 1:
        return 'Iris-versicolor' 
        
    elif predicted_class.numpy()[0] == 2:
        return 'Iris-virginica' 

def test_real(model):#TODO delete
    new_data = "7.9,4.4,6.9,2.5, which?"  # Replace with your actual new data
    new_data = [float(value) if i < 4 else value for i, value in enumerate(new_data.split(','))]
    new_data_features = new_data[:-1]

    predicted_probabilities = model.predict([new_data_features])
    predicted_class = tf.argmax(predicted_probabilities, axis=1)


    # Print the results
    print("Predicted Class:", return_result(predicted_class))
    print("Predicted Probabilities:", predicted_probabilities[0])

    return return_result(predicted_class)

def read_data_file(file_path):
    if file_path.endswith(".data"):
        df = pd.read_csv(file_path, header=None, names=["s_len", "s_wid", "p_len", "p_wid", "Predict"])
        file_type = 'csv'
        
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path, header=None, names=["s_len", "s_wid", "p_len", "p_wid", "Predict"])
        file_type = 'excel'

    else:
        raise ValueError("Unsupported file format. Supported formats: .data, .xlsx")
    
    return df, file_type

def predict_and_add_class(df, model_dir):
    model = tf.keras.models.load_model(model_dir)
    def predict_row(row):
        slice = [row['s_len'], row['s_wid'], row['p_len'], row['p_wid']]
        predicted_probabilities = model.predict([slice])
        predicted_class = tf.argmax(predicted_probabilities, axis=1)
        return return_result(predicted_class)

    df["Predicted_Class"] = df.apply(predict_row, axis=1)
    return df
    
def predict_and_save_results():
    parser = ConfigParser()
    parser.read("C:/Users/João/Projects/Resume.atempts/iris_identif/iris_ops.ini")
    model_dir = restore_special_char(str(parser.get('file_local', 'model')))

    file_path = filedialog.askopenfilename()
    df, file_type = read_data_file(file_path)
    df = predict_and_add_class(df, model_dir)
    output_directory = filedialog.askdirectory()

    filename = os.path.basename(file_path)
    file_name_without_extension = os.path.splitext(filename)[0]

    output_file = str(output_directory + f"/prediction_{file_name_without_extension}.xlsx")
    df.to_excel(output_file, index=False)
    messagebox.showinfo("Success", f"Predictions saved to {output_directory}")


if __name__ == "__main__": #Test the creation and testing of a model
    parser = ConfigParser()
    parser.read("C:/Users/João/Projects/Resume.atempts/iris_identif/iris_ops.ini")

    epochs = int(parser.get('train_config', 'epochs'))
    iris_data_dir = restore_special_char(str(parser.get('file_local', 'train')))

    model = train_model(epochs, iris_data_dir, save=True, name= 'NEW')
    test_real(model)