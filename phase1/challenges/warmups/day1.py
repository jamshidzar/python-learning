temps = [-3, -7, -1, -5]


temps = [-3, -7, -1, -5]

warmest_temp = temps[0]
warmest_day = 1

for day, temp in enumerate(temps, start=1):
    if temp > warmest_temp:
        warmest_temp = temp
        warmest_day = day

print(f"Warmest: Day {warmest_day} ({warmest_temp}°)")
