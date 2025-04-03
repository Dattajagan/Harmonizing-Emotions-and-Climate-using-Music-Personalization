# Harmonizing-Emotions-and-Climate-using-Music-Personalization

## 💥Contributors :

   * Dattajagan , github: Dattajagan

   
 
# 💥ABSTRACT :

* Harmonizing Emotions and Climate using Cloud-Powered Music Personalization

* This project presents a cloud-integrated music recommendation system that personalizes music based on  real-time emotion detection and weather analysis. By utilizing a webcam for facial emotion recognition and analyzing environmental factors, the system curates a tailored music experience. 
* Emotion classification includes happy, sad, angry, surprised, and neutral states, while weather recognition identifies conditions like sunny, rainy, or cloudy. Leveraging cloud services for scalable data processing and integrating music platforms like Spotify, the solution delivers seamless and mood-enhancing music recommendations. This innovative application aims to elevate user experiences through contextual and emotionally intelligent personalization.

# 💥DESCRIPTION :


* we first capture the user's image using a webcam with the help of the OpenCV library. The captured image is processed through a Convolutional Neural Network (CNN) combined with a Deep Neural Network (DNN) to predict the user's current emotion, detecting moods such as Happy, Sad, Angry, Surprise, Fear, or Neutral.
* Next, we apply Unsupervised Machine Learning techniques using the K-means algorithm to cluster songs into two categories — "Very Entertaining" (Class 0) and "Relaxed" (Class 1). The recommendation engine then suggests songs based on both the detected emotion and real-time weather analysis using visual input.

* If the user is sad, our system aims to uplift their mood by recommending cheerful songs. Conversely, if the user is happy, the system may suggest relaxing tracks to maintain a balanced emotional state.

* The neural network model used for emotion detection is saved as 'final_model.h5'. If any modifications are required, users can tweak the model using the code available in the 'Emotion_detector_version2' notebook. This flexible architecture ensures adaptability to specific user needs, making the system dynamic and responsive.


# 💥DATA :
 
 * This dataset contains over 160,000 songs collected using the Spotify Web API.

 * The data is well-structured and categorized by various parameters such as artist, year, genre, and popularity.
 * These attributes are essential in enhancing the accuracy of our K-means clustering algorithm to classify songs into categories like "Very Entertaining" or "Relaxed."

 * Additionally, real-time data from the webcam and weather analysis further refines the music recommendations.
 
 
# 💥LIBRARIES USED :
  * OpenCV
  * TensorFlow
  * Keras
  * Sklearn
  * LightGBM
  * Spotipy
  * Tkinter
  * Pillow
  * Numpy


# 💥HOW TO USE :

   * Run the run.py file to launch the application.A GUI will appear, prompting you to start the emotion detection.
   * The application will access your webcam and capture your image.
   * Your facial expression will be analyzed using the trained model.
   * Simultaneously, the background weather will be predicted using the image.
   * Based on the detected emotion and weather, relevant Telugu songs will be recommended.
   * The application will automatically open the selected songs on Spotify for you.
   * To exit webcam mode, press the 'q' button.
   * Enjoy a personalized music experience! 😊🎵
