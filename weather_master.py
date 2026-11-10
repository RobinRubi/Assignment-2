"""
File: weather_master.py
Name:
-----------------------
This program implements a console-based application that
asks the user to enter weather data and computes summary
statistics based on the inputs.

The program calculates the average, highest, and lowest
temperatures, as well as the number of cold days. The
output format should match the sample run shown in the
Assignment 2 handout.
"""

EXIT = -100

def main():
	print("stanCode \"Weather Master 4.0!\"")
	temperature = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
	highest_temp = temperature
	lowest_temp = temperature
	cold_days = 0
	day_counts = 0
	total_temperature = 0

	while temperature != EXIT:
		day_counts = day_counts + 1
		total_temperature = total_temperature + temperature

		if temperature > highest_temp:
			highest_temp = temperature

		if temperature < lowest_temp:
			lowest_temp = temperature

		if temperature < 16:
			cold_days = cold_days + 1

		temperature = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))

	if day_counts == 0:
		print("No temperatures were entered.")

	else:
		average_temperature = total_temperature / day_counts
		print("Highest temperature =  " + str(highest_temp))
		print("Lowest temperature =  " + str(lowest_temp))
		print("Average: " + str(average_temperature))
		print(str(cold_days) + " cold day(s)")

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
