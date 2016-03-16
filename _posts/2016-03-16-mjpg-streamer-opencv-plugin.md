---
layout: post
title: mjpg-streamer for RoboRIO 2016.3.0 released with OpenCV input plugin
---

I'm happy to announce the release of an OpenCV input plugin for mjpg-streamer, which allows you to write simple little filter plugins that can process the image from a webcam, and change what is streamed out via HTTP. You can install the mjpg-streamer-cv or mjpg-streamer-py packages [using the instructions on our github repo](https://github.com/robotpy/roborio-packages). Here's an example filter plugin:

    import cv2
    import numpy as np

    class MyFilter:
        
        def process(self, img):
            '''
                :param img: A numpy array representing the input image
                :returns: A numpy array to send to the mjpg-streamer
                          output plugin
            '''
            
            # silly routine that overlays a really large crosshair over the image
            h = img.shape[0]
            w = img.shape[1]
            
            w2 = int(w/2)
            h2 = int(h/2)
            
            cv2.line(img, (int(w/4), h2), (int(3*(w/4)), h2), (0xff, 0, 0), thickness=3)
            cv2.line(img, (w2, int(h/4)), (w2, int(3*(h/4))), (0xff, 0, 0), thickness=3)
            
            return img
            
    def init_filter():
        '''
            This function is called after the filter module is imported.
            It MUST return a callable object (such as a function or
            bound method). 
        '''
        f = MyFilter()
        return f.process


If you scp'ed this to the roborio, you could use the following command line to run it:

    mjpg_streamer -i 'input_opencv.so -r 320x240 --fps 15 --quality 30 --filter /usr/local/lib/mjpg-streamer/cvfilter_py.so --fargs /home/admin/example_filter.py'

Our team used the OpenCV plugin on our robot this weekend with a python script to do image processing and NetworkTables operations (Lifecam 3000, 320x240, 15fps, 30 quality), and it seemed to be about 20% CPU usage. Not too shabby. In theory, you could use this on a RPi or other platform too, as I've pushed the changes (plus some significant build system improvements) to [mjpg-streamer upstream](https://github.com/mjpg-streamer/mjpg-streamer).
