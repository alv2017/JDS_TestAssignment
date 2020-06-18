import csv

# Data Preparation for Data Visualization

input_file = "Data/clustered_elnino.csv"
output_file = "Data/elnino_by_clusters.csv"
output_header = ["day", "group", "zone_wind", "meridian_wind", "humidity", 
                 "air_temperature", "sea_temperature"]

with open(output_file, 'w', newline='') as outf:
    fieldnames = output_header
    writer = csv.DictWriter(outf, fieldnames=fieldnames)
    writer.writeheader()

groups = ["180W", "170W", "155W", "140W", "125W", "110W", "95W", 
          "156E", "165E"]

colnames = ["buoy", "day", "latitude", "longitude", 
            "zone_wind",  "meridian_wind", "humidity",
            "air_temperature", "sea_temperature", "group"]


data = []
for group in groups:
    group_data = []
    for day in range(1, 14):
        day_data = {
            "day":day,
            "group":group,
            "zone_wind":[0,0],
            "meridian_wind":[0,0],
            "humidity":[0,0],
            "air_temperature":[0,0],
            "sea_temperature":[0,0]
            }
        

        with open(input_file, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["group"] == group and int( row["day"] ) == day:
                    if row["zone_wind"] != ".":
                        day_data["zone_wind"][0] += float( row["zone_wind"] )
                        day_data["zone_wind"][1] += 1
                    # meridian wind
                    if row["meridian_wind"] != ".":
                        day_data["meridian_wind"][0] += float( row["meridian_wind"] )
                        day_data["meridian_wind"][1] += 1
                    # humidity
                    if row["humidity"] != ".":
                        day_data["humidity"][0] += float( row["humidity"] )
                        day_data["humidity"][1] += 1
                    # air_temperature
                    if row["air_temperature"] != ".":
                        day_data["air_temperature"][0] += float( row["air_temperature"] )
                        day_data["air_temperature"][1] += 1
                    # sea_temperature
                    if row["sea_temperature"] != ".":
                        day_data["sea_temperature"][0] += float( row["sea_temperature"] )
                        day_data["sea_temperature"][1] += 1
        

        
        output_day_data = {
            "day":day_data["day"],
            "group":day_data["group"],
            "zone_wind": round(day_data["zone_wind"][0] / day_data["zone_wind"][1], 2), 
            "meridian_wind":round(day_data["meridian_wind"][0] / day_data["meridian_wind"][1], 2),
            "humidity":round(day_data["humidity"][0] / day_data["humidity"][1], 2),
            "air_temperature":round(day_data["air_temperature"][0] / day_data["air_temperature"][1], 2),
            "sea_temperature":round(day_data["sea_temperature"][0] / day_data["sea_temperature"][1], 2),
        }
                        
        with open(output_file, 'a', newline='') as outf:
            fieldnames = output_header
            writer = csv.DictWriter(outf, fieldnames=fieldnames)
            writer.writerow(output_day_data)
                        
        
                    

                