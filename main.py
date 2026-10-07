import cv2, time, pyautogui
import mediapipe as mp

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing= mp.solutions.drawing_utils

SCROLL_SPPED=300
SCROLL_DELAY=1
CAM_WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness):
    fingers=[]
    tips=[mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hand.MIDDLE_FINGER_TIP, mp_hands.HandLandmark]