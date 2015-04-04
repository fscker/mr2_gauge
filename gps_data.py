import gps

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
	report = session.next()
	if report['class'] == 'TPV':
		if hasattr(report, 'speed'):
			print int(report.speed * gps.MPS_TO_MPH)

