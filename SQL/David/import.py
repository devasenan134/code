import csv


with open("data.tsv", "r") as titles:
    reader = csv.DictReader(titles, delimiter = "\t")
    with open("shows1.csv", "w") as shows:
        writer = csv.writer(shows)
        writer.writerow(["tconst", "primaryTtile", "startYear", "genres"])  # writing headers
        for row in reader:
            if row["startYear"] != "\\N" :
                continue

            year = int(row["startYear"])
            if year >= 1970 :
                continue
            
            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":
                writer.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])
				