## Milestone 1
- I created an image project model on Teachable-Machine consisting of four classes: Rock, Paper, Scissors, Nothing and trained the model.  
- Teachable-Machine is a tool to create fast and easy machine learning models, these models can be based on images, sounds or videos.
- I downloaded the model I trained (tensorflow-keras model) to upload into my code later. I received a keras.h5 file alongside a text file containing the labels of my classes.
> ![Screenshot 2022-04-28 at 18 45 45](https://user-images.githubusercontent.com/102605064/165815299-5099a4ce-2ebb-489b-88d6-fc17205d4250.png)

## Milestone 2
- I installed the dependencies (tensorflow, opencv, ipykernel) after creating a virtual environment called myenvironment. 
- To do this I simply typed in the terminal the following:
```python
pip install tensorflow
pip install opencv-python
```
- I had a few issues when I tried to import keras and cv2 into my environment. Python did not recognise tensorflow (or its packages like keras) or opencv. 
- I uninstalled tensorflow and opencv, then reinstalled. Since I am using Python 3.10.4, I made sure that I am using the latest version of tensorflow (2.8). Python 3.10 requires at least tensorflow 2.8 or later. 
- This didn't work either, so I changed the beginning of the code that AI core provided a little bit. Instead of importing cv2 first, I imported keras from tensorflow, and then imported load_model next. I imported the load_model from tensorflow.keras.models instead of keras.models.

>![Screenshot 2022-04-28 at 19 03 15](https://user-images.githubusercontent.com/102605064/165818066-4df9fd8d-1b28-4e0d-87f7-4a7209f7478d.png)

- This seemed to work fine when I ran the code in the terminal. 
- When I analysed this code, I saw that I have 3 main variables. Model, which is the keras.h5 model I downloaded previously; cap, which uses opencv (a huge open-source library for computer vision and machine learning) to read videos and accesses the webcam; and data, which defines an initial size for the camera using arrays for its shape.
- In the code, the image from the images from the webcam are processed using ret and frame. Frame, an image array vector, will obtain the next image from the camera and ret will return the data obtained from the camera frame (true or false). 
- Then, the image is resized using .resize() function. Next, the image is normalised between 1 and -1 using the .astype() function.
- According to the new image size arrangements, 'rock, paper, or scissors' is predicted by using the data from the model, using the .predict() function. 

## Milestone 3
-
