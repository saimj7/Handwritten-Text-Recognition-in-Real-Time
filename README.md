# Handwritten-Text-Recognition-in-Real-Time
> Testing out HTR-OCR-Text translation with Google's Tesseract engine using live video stream (webcam) in OpenCV. Version 1.

OCR & Text translation             |  HTR after simple image processing
:-------------------------:|:-------------------------:
![](https://imgur.com/uIhjCeR.png)  |  ![](https://imgur.com/cgXQJzJ.png)

- As we can see from the gif.1 above, Tesseract does a great job in recognizing standard OCR, translating different languages.
- Coming to the handwriting recognition in gif.2, Tesseract is not accurate. The original image is 'handwritten.png' in the folder tests:

```
Before img. processing: This is a handwrdten example wrde os 3009{ as you can.
```

- However, it certainly got better with simple image processing.
```
After img. processing: This is a handwriten example wrile as 3ood as you can.
```

- With simple text correction feature (ref. [Features](#features)), notice that '3ood' turned into 'good':
```
After correction: This is a handwriten example wrile as good as you can.
```
- Note that the model isn't trained on any handwritten data, only optimised with simple image processing.

<p>&nbsp;</p>

> The basic idea here is to extract the image from live video stream first and then do the processing. But why?

- A few reasons: Extracting a single frame is computationally less expensive. Use case: scanners, mobile phones etc.
- Better stability, leading to accurate output.
- Moreover, we can define our own region of interests in the image.
- Boring? Let's dig into the pipeline now:

--- 

## Table of Contents
* [Installing Tesseract](#installing-tesseract)
* [Running Inference](#running-inference)
* [Features](#features)
* [References](#references)
* [Next Steps](#next-steps)


## Installing Tesseract
- Detailed installation of Tesseract on Windows, Ubuntu, Mac can be found [**here**](https://github.com/tesseract-ocr/tesseract/wiki#installation).
- Python libraries and dependencies required can be installed via pip:
```
pip install -r requirements.txt
```

## Running Inference
- To run the demo on webcam, set ``` Webcam = True ``` in the config. options at 'mylib/Config.py'.
- Head into the directory/use the command: 

```
python run.py
```
- The live stream should pop up. Press 'c' on your keyboard and use your mouse to drag and select the region of interest (ROI).
- Press 'c' again and it should crop the image. 'r' to resume and 'q' to quit.
- The cropped image then gets processed by Tesseract and output is displayed.
- If you would like to test on a video file, set ``` Webcam = False ``` and place your file in the 'tests' folder.
- Then run with the command: ``` python run.py -i tests/test.mp4 ```; by simply implying the path to your file.


## Features
> Note: below are just for fun. Better versions should come up in the future.

***Simple log:***
- The output data can be logged in a simple .txt file. 
- All the features can be easily enabled/disabled in the config. options. For example:


Config. options / Features            |  Simple log
:-------------------------:|:-------------------------:
![](https://imgur.com/Xn2hNEM.png)  |  ![](https://imgur.com/ce31z8p.png)


***Image processing:***
- Background noise reduction, increasing text thickness/width can increase the accuracy on bad/low light/distored images.
- Demonstrated in the gif.2 above.

***Text correction:***
- Added a simple text corrector which tries to autocorrect the spelling mistakes.

<div align="left">
<img src="https://imgur.com/urlShd6.png" width=400>
</div>

***Text/language translation:***
- The source language (other than English) can be transated into the English text.
- Enable the translate option in the config. and run it. 
- After cropping, the command window asks for the source language code. For example, we enter 'deu for German' and 'swe for Swedish' (refer gif.1).
- Language codes supported [**here**](https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#languages-and-scripts) should work.


## References

***Main:***

- Tesseract: https://github.com/tesseract-ocr
- OpenCV Image Processing: https://docs.opencv.org/master/d7/dbd/group__imgproc.html
- Tesseract Language Codes: https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#languages-and-scripts

***Optional:***

- https://www.pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/
- https://pypi.org/project/pyspellchecker/



## Next steps
- Train Tesseract on handwritten data.
- Experiment with text localisation and benchmark the results on less expensive embedded hardware. 

<p>&nbsp;</p>

---

## Thanks for the read & have fun!

> To get started/contribute quickly (optional) ...

- **Option 1**
    - 🍴 Fork this repo and pull request!

- **Option 2**
    - 👯 Clone this repo:
    ```
    $ git clone https://github.com/saimj7/Handwritten-Text-Recognition-in-Real-Time.git  
    ```

- **Roll it!**

---

saimj7/ 18-08-2020 © <a href="http://saimj7.github.io" target="_blank">Sai_Mj</a>.
