from tensorflow import keras 
from tensorflow.keras.models import load_model
import cv2     
import numpy as np
import random 
import time


model = load_model('/Users/macbook/Downloads/converted_keras-2/keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) 
choices = ['rock', 'paper', 'scissors']
possible_predictions = choices + ['nothing']
bot_choice = random.choice(choices)
print(bot_choice)


def put_text_to_frame(frame, text, x_y = (50, 50), fontscale = 1, thickness = 2):
    return cv2.putText(
        frame, 
        text, 
        x_y, 
        cv2.FONT_HERSHEY_SIMPLEX, 
        fontscale,
        (255, 0, 0), 
        thickness,
        cv2.LINE_AA
    )
  


def user_choose_an_option(index):
    return index != 3

beats = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

def choose_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return 'TIE', 0, 0
    if beats[player_choice] == bot_choice:
        return 'The bot beats', 0, 1
    elif beats[bot_choice] == player_choice:
        return 'You beat the bot', 1, 0
    else:
        raise ValueError('Something is not right')

waittime = 3
user_ready = False
start_time = None
user_num_wins = 0
bot_num_wins = 0



while (user_num_wins < 3) and (bot_num_wins < 3): 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) 
    
   
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image, -1 le 1 arasina sikistiriyor
    data[0] = normalized_image
    prediction = model.predict(data) #tas kagit makasi predict ediyor
    index = np.argmax(prediction) # kameradaki goruntuye gore most probable sonucu veriyor
    if not user_ready:
        frame = put_text_to_frame(frame, 'press c if you are ready')
        frame = put_text_to_frame(frame, f'{user_num_wins} - {bot_num_wins}', (1100, 50))
    else:
        time_passed = min(3, int(time.time() - start_time)) 
        countdown = waittime - time_passed
        if  (countdown == 0) and user_choose_an_option(index):
            result, user_win, bot_win = choose_winner(possible_predictions[index], bot_choice)
            user_num_wins += user_win 
            bot_num_wins += bot_win          
            user_ready = False    
            start = time.time()
            while (3 - (time.time() - start)) > 0:     
                ret, frame = cap.read()
                frame = put_text_to_frame(frame, result) 
                frame = put_text_to_frame(frame, f'{user_num_wins} - {bot_num_wins}', (1100, 50))
                cv2.imshow('frame', frame)
                cv2.waitKey(1)
        else:
            frame = put_text_to_frame(frame, 'Please show a rock, paper or a pair of scissors to your camera')
            frame = put_text_to_frame(frame, str(countdown), (600, 400), 8, 5)
            frame = put_text_to_frame(frame, f'{user_num_wins} - {bot_num_wins}', (1100, 50))

      


    cv2.imshow('frame', frame)
    # Press q to close the window
    # print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        user_ready = True 
        start_time = time.time()
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

