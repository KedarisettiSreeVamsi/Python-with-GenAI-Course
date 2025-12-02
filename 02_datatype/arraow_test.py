import arrow

currentTime = arrow.utcnow()
currentTime.to("Europe/Amsterdam")
print(currentTime)