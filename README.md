This repository designed to recreate each frame of Bad Apple as a mural of other frames in Bad Apple. I mostly created this just for fun and as a way to mess around with OpenCV and python.

# Prerequisites
1. Python
2. ffmpeg
3. OpenCV

# Usage
1. Clone this project
2. Download the video using a program like youtube-dl
3. Open a command prompt in the folder you cloned this project from
4. Run `.\convert.bat VIDEO_FILE`, and replace "VIDEO_FILE" with the name of the file you downloaded. This will make sure the video is encoded in a way OpenCV can understand
5. Run `python BadApplePreprocess.py`. This will create a sorted list of frames from darkest to brightest, and store them in the `SortedFrames` folder. The default name this program checks for is `BadApple.mkv`, but you can choose a different name as a command line argument if you so choose
6. Run `python BadApple.py`. This will use the sorted frames from the previous step to generate the video file. This file is in the AVI format, and encoded in MJPEG, so compression is not good
7. Run `ffmpeg -i Output.avi -i BadApple.mkv.old -c:v libx264 -c:a copy -map 0:v:0 -map 1:a:0 Final.mp4` for better compression and better supported file formatting. This also pulls the audio from the original video file and adds it on as well. Replace `BadApple.mkv.old` with the `.old` file created in the conversion step if you used a different file name