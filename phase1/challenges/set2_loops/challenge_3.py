temps = [3, -2, 5, 8, -4, 1, 6]

for i, temp in enumerate(temps, start=1):
    if temp < 0:
        print(f"Day {i}: {temp}°C")

warmest_temp = temps[0]
warmest_day = 1

for day, temp in enumerate(temps, start=1):
    if temp > warmest_temp:
        warmest_day = day
        warmest_temp = temp

print(f"Warmest: Day {warmest_day} ({warmest_temp}°)")
