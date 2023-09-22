# Iris Flower Identification
 This project is a demonstration of the skills I acquired in the CS50AI course offered by HarvardX, with a focus on TensorFlow technology. It uses a database to describe the length and width of three species of iris (Iris Setosa, Iris Virginica, and Iris Versicolor), which are mainly found in the United States.
  
![1_YYiQed4kj_EZ2qfg_imDWA](https://github.com/Superjoa10/iris_identif-GUI/assets/108309932/aa1d8587-576a-496f-9e04-af66c74e9789)

![sign_18_6_26_fig-2](https://github.com/Superjoa10/iris_identif-GUI/assets/108309932/80163573-6ad6-47c6-a563-d7bcba590b94)

* For more info about the database used for the model creation, visit the link below:
* Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.


# Tutorial 
The app is a user interface that offers two options for predicting instances of the flower based on the width and length of the petal and sepal. You can either predict a single instance or use a file, which can be in either Excel or .data format, similar to the one found in the training database. The file should be formatted as follows:

   1. sepal length in cm	
   2. sepal width in cm	
   3. petal length in cm	
   4. petal width in cm	
   5. class: Any or None

![sepals_and_petals_600w](https://github.com/Superjoa10/iris_identif-GUI/assets/108309932/e18f4ec1-f69b-4379-a075-f37a735b6525)

* If you use a .data file, make sure it is separated by commas.


To make predictions, check the configuration section in the app and ensure the location of the model presented on the page. The app comes with the .h5 file needed to use it, correctly referenced as a relative path. However, to confirm if the app can read it correctly, click the apply button and wait for a confirmation message to pop up before starting predictions.

# Model information (TensorFlow)

If you wish to create your own .h5 models for this database, you can reference them in the options menu under the 'model' section and check if they are usable by applying the change. To see the settings I used for defining the model, refer to line 15 in the "get_model" function in the model_functions.py file. Running it directly will create a new .h5 file saved to the model directory in the app's root directory.

![Captura de tela 2023-09-21 2310055555](https://github.com/Superjoa10/iris_identif-GUI/assets/108309932/ae20aa41-0f43-47fb-b3d1-9d3639263deb)

* Alternatively, you can modify the values referenced in the get_model function to obtain a better model or experiment with its definition.

This project is not meant for professional use; it serves as a demonstration of my abilities in TensorFlow, model definition for predictions, as well as the visualization of the idea and the creation of a user interface that can be easily used and understood by non-programmers.
