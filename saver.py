import csv
import json

class Saver:
    def save_to_csv(self, repositories, filename="open_source_games.csv"):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "description", "url"])
            writer.writeheader()
            for repo in repositories:
                writer.writerow(repo)

    def save_to_json(self, repositories, filename="open_source_games.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(repositories, file, indent=4)
