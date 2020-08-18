import cv2, os
from mylib.TesseractPython import tesseract_class
from mylib.LogData import logger_class
from mylib.SpellChecker import correct_sentence
from mylib.Pre import preproc

#===============================================================================
""" CONFIG v1: RANGE OF ARCHITECTURE FEATURES BELOW
     -you can enable or disable them- """
#===============================================================================
# To correct text sentences
Correct = False
# To save extracted text in a simple log
Log = True
# Text translation from foreign lang. to english
Translate = True
# Image processing to get better output
ImProc = False
#===============================================================================
#===============================================================================


class LiveOCR(object):
    def __init__(self):
        ##To test on webcam
        self.capture = cv2.VideoCapture(0)
        ##To test on video file. NOTE: the result may vary.
        #self.capture = cv2.VideoCapture('tests/test.mp4')

        self.image_coordinates = []
        self.extract = False
        self.selected_ROI = False
        self.update()

    def update(self):
        while True:
            if self.capture.isOpened():
                # Read frame
                (self.status, self.frame) = self.capture.read()
                cv2.imshow('Test_Window', self.frame)
                x,y,w,h = 0,0,270,60
                # Add background
                cv2.rectangle(self.frame, (x, x), (x + w, y + h), (255, 255, 255), 1)
                # Add text
                cv2.putText(self.frame, "c=crop, r=resume, q=quit", (x + int(w/10),y + int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                key = cv2.waitKey(2)

                # Crop image
                if key == ord('c'):
                    self.clone = self.frame.copy()
                    cv2.namedWindow('Test_Window')
                    cv2.setMouseCallback('Test_Window', self.extract_coordinates)
                    while True:
                        key = cv2.waitKey(2)
                        cv2.imshow('Test_Window', self.clone)

                        # Crop and display cropped image
                        if key == ord('c'):
                            self.crop_ROI()
                            self.show_output()

                        # Resume video
                        if key == ord('r'):
                            break

                if key == ord('q'):
                    cv2.destroyAllWindows()
                    exit(1)
            else:
                pass
    ##Extracting static ROI has been modified from this source:
    #https://stackoverflow.com/questions/56467902/select-a-static-roi-on-webcam-video-on-python-opencv
    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x,y)]
            self.extract = True

        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x,y))
            self.extract = False
            self.selected_ROI = True
            # Draw rectangle around ROI with desired color
            cv2.rectangle(self.clone, self.image_coordinates[0], self.image_coordinates[1], (255, 255, 255), 2)

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.frame.copy()
            self.selected_ROI = False

    def crop_ROI(self):
        if self.selected_ROI:
            self.cropped_image = self.frame.copy()
            x1 = self.image_coordinates[0][0]
            y1 = self.image_coordinates[0][1]
            x2 = self.image_coordinates[1][0]
            y2 = self.image_coordinates[1][1]
            self.cropped_image = self.cropped_image[y1:y2, x1:x2]
            #print('Cropped image: {} {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
        else:
            print('Select ROI before cropping')

    def show_output(self):
        cv2.imshow('cropped image', self.cropped_image)
        # Save cropped image to data folder in the system
        if not os.path.exists('data'):
            os.makedirs('data')
        cv2.imwrite('data/cropped image.png', self.cropped_image)
        output = tesseract_class.extract_ocr('data/cropped image.png')

        # To correct sentences
        if Correct:
            print("")
            print("With text correction:", correct_sentence(output))
            print("")
            print("Without text correction:", output)

        else:
            print("")
            print('Without img. processing:', output)
            if Log:
                logger_class.save_log(output)
            if ImProc:
                preproc.contrast(self.cropped_image)
                proc_out = tesseract_class.extract_ocr('data/processed image.png')
                print("")
                print("========================")
                print("")
                print('After img. processing:', proc_out)

        # To translate different languages
        if Translate:
            output = tesseract_class.translate_ocr('data/cropped image.png')
            if Log:
                logger_class.save_log_trans(output)



if __name__ == '__main__':
    Live_OCR = LiveOCR()
