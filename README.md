# Iris Flower Identification
  This project is a demonstration of the skills I acquired in the CS50AI course offered by HarvardX,  with a focus on TensorFlow technology. It uses a database to describe the length and         width of three species of iris (Iris Setosa, Iris Virginica and Iris Versicolor)  which are found mainly in the United States.
  
![1_YYiQed4kj_EZ2qfg_imDWA](https://github.com/Superjoa10/iris_identif-GUI/assets/108309932/aa1d8587-576a-496f-9e04-af66c74e9789)

![sign_18_6_26_fig-2](https://github.com/Superjoa10/iris_identif-GUI/assets/108309932/80163573-6ad6-47c6-a563-d7bcba590b94)

* for more info about the database used for the model creation, visit the link below:
* Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.


# Tutorial 
The App is a user interface, that gives 2 options on how to predict the instances of the flower given the width and length of the petal and sepal, can either predict one instance, or a file, either a excel or a .data file like the one found on the database used for training. This file should be formated as: 
   1. sepal length in cm	
   2. sepal width in cm	
   3. petal length in cm	
   4. petal width in cm	
   5. class: Any or None
![sepals_and_petals_600w](https://github.com/Superjoa10/iris_identif-GUI/assets/108309932/e18f4ec1-f69b-4379-a075-f37a735b6525)

* If  .data file should be separeted with ","


In order to make any prediction, you should first check the config section on the app, and the location of the model presented in the page, the app comes with the .h5 file needed to use it, and already refereced correctly on the settings as a relative path, but even thou, to check if the app can read it correcly, click the apply button, and wait or a confirmation message to pop up in order to confirm if you can start doing the predictions. Or if you wish to make your own .h5 model, you can reference it on this section on the option menu and check if its usable. In order to se the settings i use for the definition of the model, refer to the line . function . on the model_functions.py file, in which if you run it directly it'll create a new .h5 file saved to the model directory on the apps root directory

# Model information (TensorFlow)


* This project is not ment for professional use, it serves as a demonstration of my abilities in tensorflow, model definition for predictions, as well as a visualization of the idea, creation of the user interface in a way a user/non programer could easealy visualize and use.
