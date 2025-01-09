import unittest
from EmotionDetection import emotion_detector

def parse_emotion(emotion):
    return emotion['dominant_emotion']

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        self.assertEqual(parse_emotion(emotion_detector("I am glad this happened")), "joy")
        self.assertEqual(parse_emotion(emotion_detector("I am really mad about this")), "anger")
        self.assertEqual(parse_emotion(emotion_detector("I feel disgusted just hearing about this")), "disgust")
        self.assertEqual(parse_emotion(emotion_detector("I am so sad about this")), "sadness")
        self.assertEqual(parse_emotion(emotion_detector("I am really afraid that this will happen")), "fear")
           