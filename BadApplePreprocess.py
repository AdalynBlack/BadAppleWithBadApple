import cv2
import sys
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

	height = frame.shape[0]
	width = frame.shape[1]

	crop_adj = int((width-height)/2)
	crop_left = crop_adj
	crop_right = crop_adj + height

	values = [-1] * 100
	distances = [999] * 100

	count = 0
	print("Processing Frames...")
	while result:
		frame = frame[0:height, crop_left:crop_right]
		frame = cv2.resize(frame, None, fx=0.05, fy=0.05)

		mean = 99*(cv2.mean(frame)[0]/255)
		dist = abs(int(mean) - mean)

		if distances[int(mean)] > dist:
			values[int(mean)] = count
			distances[int(mean)] = dist

		result, frame = raw.read()
		count += 1

	print("Writing Best Candidates...")
	count = 0
	for value in values:
		if value != -1:
			raw.set(cv2.CAP_PROP_POS_FRAMES, value)
			_, image = raw.read()
			image = image[0:height, crop_left:crop_right]
			image = cv2.resize(image, None, fx=0.05, fy=0.05)
			cv2.imwrite((f"SortedFrames/%s.png" % count), image)
			count += 1


if __name__ == "__main__":
	start = process_time()
	main()
	end = process_time()

	print(f"Script finished in %s seconds" % (end - start))