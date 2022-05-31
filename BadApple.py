import cv2
import numpy as np
import sys
import os
from time import sleep, process_time

def main():
	name: str = "BadApple.mkv"
	if len(sys.argv) >= 2:
		name = sys.argv[1]
	else:
		print(f"Warning: Using Default Name \"%s\"" % name)
		sleep(1)

	print(f"Name Selected: %s" % name)

	raw = cv2.VideoCapture(name)

	result, frame = raw.read()

	height = int(frame.shape[0] / 20)
	width = int(frame.shape[1] / 20)
	
	# Load sorted frames into a list for ease of access
	img_dirs = os.listdir("SortedFrames")
	image_count = len(img_dirs)
	sorted_frames = [None] * image_count
	for path in img_dirs:
		sorted_frames[int(os.path.splitext(path)[0])] = cv2.imread(f"SortedFrames/%s" % path)

	pixel_height = sorted_frames[0].shape[0]
	pixel_width = sorted_frames[0].shape[1]

	writer = cv2.VideoWriter()
	writer.open("Output.avi", cv2.VideoWriter_fourcc(*'MJPG'), raw.get(cv2.CAP_PROP_FPS), (width * pixel_width, height * pixel_height))

	image_count -= 1
	finished_frames = 0

	conversion_factor = image_count/255
	while result:
		frame = cv2.resize(conversion_factor * frame, None, fx = 0.05, fy = 0.05).astype(np.uint8)

		collage = None
		col = None

		first = True
		for row in frame:
			first_row = True
			for pixel in row:
				val = pixel[0]
				if first_row:
					col = [sorted_frames[val]]
					first_row = False
				else:
					col.append(sorted_frames[val])
			if first:
				collage = [np.hstack(col)]
				first = False
			else:
				collage.append(np.hstack(col))

		collage = np.vstack(collage)

		#cv2.imwrite("test.png", collage)
		writer.write(collage)
		result, frame = raw.read(frame)

		if finished_frames % 100 == 99:
			finished_frames += 1
			print(f"finished %s frames so far" % finished_frames)
		else:
			finished_frames += 1
	writer.release()

if __name__ == "__main__":
	start = process_time()
	main()
	end = process_time()

	print(f"\nScript finished in %s seconds" % (end - start))