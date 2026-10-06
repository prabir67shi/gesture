import cv2, mediapipe as mp, numpy as np
from pycaw.pycaw import AudioUtilities,  IAudioEndpointVolume
import screen_brightness_control as sbc

Hands = mp.solutions.hands
hands = Hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils
TH, IX = Hands.Handlandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP

try:
    dev= AudioUtilities.GetDefaultOutput() if hasattr(AudioUtilities, "GetDefaultOutputDevice") else AudioUtilities.GetSpeakers()
    volctl = dev.ENDpointVolume.QueryInterface(IAudioEndpointVolume)
    minv, maxv = volctl.GetVolumeRange()[:2]
except Exception as e:
    print(f"Pycaw error: {e}"); exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened(): print('Error: webcam not accesible.'); exit()

WIN = "Hand Gesture Control"; cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

while True:
    ok, img = cap.read()
    if not ok: break
    img = cv2.flip(img, 1); h, w = img.shape[:2]
    res=hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks and res.multi_handedness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)
            lm= hand.landmark
            tp= (int(lm[TH].x*w), int(lm[TH].y*h)); ip= int(lm[IX].x*w), int(lm[IX].y*h)
            