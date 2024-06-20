import pyautogui
import time

class ScreenCapture:
    def __init__(self, left, top, height, width):
        self.left = left
        self.top = top
        self.height = height
        self.width = width

    def take_screenshot(self):
        print("Taking screenshot...")
        screenshot = pyautogui.screenshot(region=(self.left, self.top, self.width, self.height))
        return screenshot

class ObstacleDetector:
    def __init__(self, image):
        self.image = image

    def detect_obstacle(self):
        cactus_colour = (106, 143, 24)

        for x in range(self.image.width):
            for y in range(self.image.height):
                if self.image.getpixel((x, y)) == cactus_colour:
                    print("Obstacle Detected")
                    return True
        print("No obstacles")
        return False

class Dinosaur:
    def jump(self):
        print("Jumping!")
        pyautogui.press('up')

if __name__ == '__main__':
    left, top, height, width = 672, 294, 30, 120

    while True:
        screen_capture = ScreenCapture(left, top, height, width)
        image = screen_capture.take_screenshot()

        obstacle_detector = ObstacleDetector(image)
        obstacle_detected = obstacle_detector.detect_obstacle()

        if obstacle_detected:
            dinosaur = Dinosaur()
            dinosaur.jump()
