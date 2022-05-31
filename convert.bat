@echo off

if [%1]==[] (
	echo Please input a video file.
	goto exit
)

move %1 %1.old
ffmpeg -i "%1.old" -vcodec libx264 "%1"

:exit