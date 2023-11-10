
import threading
import cv2
from deffcode import Sourcer
import os
import PIL
import matplotlib.pyplot as plt
from os import path
import time
# Class for acquiring and processing images for machine vision class FrankaCamera:
def __init__(self, cam_name="Intel"):
    self.cap = None
    self.cam_name = cam_name
    self.processor = ImageProcessor()
    self.frames_folder = "/home/samsung/data/realsense/frames/"
    found_source= False
    for j in range (20):
        try:
            sourcer = Sourcer ("%d" % j).probe_stream()
            found_source= True
            break
        except Exception as err:
            print("Cannot open source %d" % j)
            continue
        if found_source== False:
            cam_num = None
            else:=
            for src in sourcer.enumerate_devices.keys():
                entry = sourcer.enumerate_devices [src]
                for key in entry.keys():
                    print(key, entry [key])
                    if entry [key][0] == cam_name:
                        cam_num= int(key.split("video") [-1])
                        break
                    self.cam_num = cam_num
   
    # Connects to the camera def initialize(self):
        def initialize(self):
            print("Initializing camera")
            if self.cam_num:
                print("Cam num = %d" % self.cam_num)
                self.cap = cv2.VideoCapture(self.cam_num)
                self.cap.set(cv2.CAP_PROP_AUTO EXPOSURE, 3) # MAKES SURE AUTO EXPOSURE IS TURNED ON
                self.cap.set(cv2.CAP_PROP_AUTO_WB, 1)
                self.lock
                threading.Lock()
                self.t threading. Thread (target=self.reader)
                self.t.daemon = True
                self.t.start()
                self.initialized = True
                else:
                    print("No camera detected")
     
        def close_camera (self):
            self.cap.release()
    #Grabs frames as soon as they are available
        def reader(self):
            while True:
                with self.lock:
                    ret = self.cap.grab()
                    if not ret:
                        break
    # retrieve latest frame
        def get_frame (self, savename=None, skip_frames=0):
            if not self.initialized:
                self.initialize()
                with self.lock:
                    ret, frame = self.cap.retrieve()
                    if ret:
                        if savename:
                            savepath = self.frames_folder+savename + ".
                            else:
                                frame_number = 1
                                savename = "frame_%d" % frame_number
                                savepath = self.frames_folder + savename + ".png"
                                self.cap.release()
    #Grabs frames as soon as they are available
    def reader(self):
        while True:
            with self.lock:
                ret = self.cap.grab()
                if not ret:
                    break
    # retrieve latest frame
    def get_frame(self, savename=None, skip_frames=0):
        if not self.initialized:
            self.initialize()
            with self.lock:
                ret, frame = self.cap.retrieve()
                if ret:
                    if savename:
                        savepath = self.frames_folder + savename + ".png"
                        else:
                            frame_number = 1
                            savename = "frame_%d" % frame_number
                            savepath = self.frames_folder+ savename + ".png" 
                            while path.exists(savepath):
                                frame_number += 1
                                savename = "frame_%d" % 
                                savepath = self.frames_folder + savename + ".png"
                                print("Image collected, saving at %s" % savepath) cv2.imwrite(savepath, frame)
                else:
                    print("No frame collected")
                    return
                filename = 'Webcam'
                filepath = self.frames_folder + filename + ".png"
                cv2.imwrite(filepath, frame)
                return frame
     def load_frame(self, savename):
         savepath = self.frames_folder + savename + ".png"
         frame = cv2.imread(savepath)
         return frame
     def show_frame(self, savename):
         savepath = self.frames_folder + savename + ".png"
         img= PIL.Image.open(savepath)
         plt.figure(num=savename)
         plt.title(savename)
         plt.imshow(img)
     def set brightness(self, value):
         self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)
         
     def get_brightness(self):
         return self.cap.get(cv2.CAP_PROP_BRIGHTNESS)
     
     def set_exposure (self, value):
     self.cap.set(cv2.CAP_PROP_EXPOSURE, value)
     # Class for image processing functions
     class Image Processor:
         def __init__(self, frames_folder="/home/samsung/data/real sense/frames/"):
             self.frames_folder= frames_folder
         def load_frame (self, savename):
             savepath = self.frames_folder + savename + ".png"
             frame = cv2.imread(savepath)
             return frame
             
     # Determines if Flacktek insert alignment is correct by detecting red tape in picture 
     # Returns
         def detect_red (self, savename="red_tape_alignment"):
             #readimagesavedframesfolder
             image_path='/home/samsung/data/realsense/frames/Webcam.png'
             image = cv2.imread(image_path)
             cv2.normalize(image, image, 55, 345, cv2.NORM_MINMAX) # ADJUSTS BRIGHTNESS AND CONTRAST LEVEL
             image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
             # Lower mask (0-10)
             mask1= cv2.inRange (image_hsv, (0, 50, 20), (5, 255, 255)) # upper mask (170-180)
             mask2= cv2.inRange(image_hsv, (175, 50, 20), (180, 255, 255)) # Binary mask with pixels matching the color threshold in white mask = cv2.bitwise_or(mask1, mask2)
             maskname = 'mask'
             maskpath = self.frames_folder maskname + ".png" cv2.imwrite(maskpath, mask)
             redcolor= cv2.bitwise and (image, image, mask=mask) maskcrop = mask [300:380, 518:562]
             # if franka.camera.detect_red_tape():
             if cv2.countNonZero (maskcrop) > 0:
                 return True
             else:
                 return False
                 
