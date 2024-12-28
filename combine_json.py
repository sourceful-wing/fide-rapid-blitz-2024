import json
import os


def combine_json_files(n, output_file="combined_players.json"):
    combined_data = []

    for i in range(1, n + 1):
        file_name = f"rapid_open_round_{i}_players.json"
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                data = json.load(file)
                combined_data.extend(
                    data
                )  # Assuming each file contains a list of players

    with open(output_file, "w") as outfile:
        json.dump(combined_data, outfile, indent=4)


N = 10

# Example usage
combine_json_files(N)
