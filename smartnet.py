import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)

time.sleep(0.1)

print "Starting Measurement.."


while True:
	GPIO.output(TRIG,1)
	time.sleep(0.00001)
	GPIO.output(TRIG,0)

	while GPIO.input(ECHO) == 0:
		pass
	start = time.time()

	while GPIO.input(ECHO) == 1:
		pass
	stop = time.time()

	print (stop - start) * 17000
	time.sleep(0.6 - ((time.time() - start) % 0.6))
	if (stop-start ) * 17000 < 10.0:
		print "Nice Shot"
		os.system('mpg321 niceshot.mp3 &')
GPIO.cleanup()
