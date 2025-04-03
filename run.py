import os
import time
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import spotipy
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials
import config
from emotion_video_classifier import emotion_testing
import cv2
import webbrowser
from tensorflow.keras.utils import load_img
import requests
import threading

root = tk.Tk()
root.withdraw()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(BASE_DIR, "images", "background.mp4") 

if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video not found: {video_path}")

client_credentials_manager = SpotifyClientCredentials(client_id=config.cid, client_secret=config.Secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

root.deiconify()
root.title('Music Recommendation System')
root.geometry("800x600")
root.configure(bg='#FFE4E1')
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
cap = cv2.VideoCapture(video_path)

def update_video():
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) 
        return

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (800, 600))
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    canvas.create_image(400, 300, image=imgtk, anchor=tk.CENTER)
    canvas.imgtk = imgtk
    root.after(20, update_video) 
update_video()

def submit():
    messagebox.showinfo("Information", "Starting Emotion Detection and Weather Analysis...")
    cap.release()
    root.destroy()

sub_btn = tk.Button(root, text='Start Emotion Detection', command=submit, bg='#ADD8E6', font=('Arial', 12, 'bold'))
sub_btn_window = canvas.create_window(400, 500, window=sub_btn)

EMOTIONS = ["happy", "sad", "angry", "surprise", "fear", "neutral"]


root.mainloop()

def get_weather():
    api_key = "e7bb8187bc004eccbd444202250703"  
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Hyderabad,Telangana"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        location = data['location']['name'] + ", " + data['location']['region']
        temperature = str(data['current']['temp_c']) + "°C"
        condition = data['current']['condition']['text']
        local_time = data['location']['localtime']
        print(f"Location: {location}")
        print(f"Temperature: {temperature}")
        print(f"Weather Condition: {condition}")
        print(f"Local Time: {local_time}")
        return condition
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return "Unknown"

def detect_emotion():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Error: Could not open webcam.")
    emotion_word = emotion_testing()
    cap.release()
    cv2.destroyAllWindows()
    if emotion_word not in EMOTIONS:
        print(f"Emotion '{emotion_word}' not recognized.")
        return None
    return emotion_word

def play_music(emotion, weather):
    print(f"Detected Emotion: {emotion}, Weather: {weather}")
    query = f"{emotion} songs" if emotion else f"{weather} songs"
    results = sp.search(q=query, type='track', limit=20)
    if not results['tracks']['items']:
        print("No songs found for this emotion and weather.")
        return
    for track in results['tracks']['items']:
        print(f"Playing: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")
        print(f"Opening in Spotify: {track['external_urls']['spotify']}")
        webbrowser.open(track['external_urls']['spotify'])

weather_condition = get_weather()
emotion_detected = detect_emotion()

if emotion_detected:
    play_music(emotion_detected, weather_condition)
else:
    print("Emotion detection or weather check failed.")