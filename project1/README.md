In essence, "Automatic Number-Plate Recognition" (ANPR) systems are used to automatically detect and recognize number plates in images. From there, the identified license plate can be used to look up information about the car's owner. ANPR systems are mainly used for car park access control although the main use of ANPR is to fine drivers for traffic offences.

It is important to understand that there is no one size fits all ANPR solution!. Whenever we can apply a priori knowledge about the domain of the problem to be solved (whether it's computer vision, machine learning, or knitting a scarf for our grandmother), that knowledge will help us solve the problem more effectively and accurately. For this challenge we will focus on Spanish registrations. Since the last format change in license plates, these have 4 numbers followed by 3 letters

So now that we know what ANPR actually is, let's briefly review the 4 steps required to build any ANPR system. Obviously, we'll go over each of these steps in more detail in the rest of this module

Goals:

Familiarize yourself with the terms Automatic Number Plate Recognition.

The four steps to building any ANPR system:

    Acquisition of an image
    Localization/Detection
    Segmentation
    Recognition

1. Acquisition of images

The first step in any ANPR system is to acquire a photo of a car that (presumably) has a license plate that we want to detect and recognize. Most production-level ANPR systems implemented in the real world use infrared cameras so that photos of vehicles can be captured regardless of the time of day. In addition, these cameras could be part of a closed circuit system (parking), connected to a much larger network (traffic,. or connected to a mini-computer (Raspberry Pi) to control access to an urbanisation.

There are an endless variety of ways to capture our original image of a vehicle. But the point here is that we have to (1) consider our environment, (2) determine what camera/setup will work best, and (3) anticipate how we will install the camera.

An intermediate step between photo acquisition and localization is how to actually activate our camera to capture a photo of the passing vehicle. There are many methods to achieve this, the main ones being radar and motion detection. Here I include the camera shot in the photo acquisition step, but others may split it into a completely separate step.

2. Locatization/Detection

Now that we have a real image that contains a vehicle, we need to find or locate the region of the image that contains the license plate.

Again, there are a variety of methods for performing localization tasks. Perhaps surprisingly, we don't need a sophisticated machine learning algorithm to detect license plates in images (although we will introduce that in a second version). In general, we can take advantage of clever combinations of basic image processing techniques to reveal regions of an image that might contain a license plate. We call these regions candidate registrations and use additional image processing to filter out false positives. Then we take the license plate regions and pass them to the segmentation step.

3. Segmentation

Now that we have found the region of our image that contains the license plate. What we do? Well, to identify each of the characters in the license plate, we must first segment, that is to say distinguish between background and form. In general, you'll find that license plate images are too noisy to apply optical character recognition (OCR) algorithms directly, so we'll need to leverage our image processing skills. Most techniques perform some form of adaptive thresholding to "clip" the license plate characters.

4. Recognition

Finally, given each individual character (cleanly segmented) in the license plate, we apply some machine learning to recognize it. Each character is quantified using feature extraction. There are many procedures you can use to quantify each character. One possibility could be to divide each character into regions and add up which pixels belong to the number, it is a simple but effective method to characterize and quantify the license plate characters in images:

Once we have the feature vector associated with each character, it will need to be run through a machine learning model to classify and recognize each element. After recognizing each character, we will have obtained our license plate recognition.