import json


def round_to_json(ROUND_NUMBER):

    # Load player information from JSON file and convert to dictionary
    with open("rapid_open_players.json", "r") as file:
        players_list = json.load(file)
        sno_to_player = {player["rank"]: player for player in players_list}

    # Read the round data from the file
    with open(f"rapid_open_round_{ROUND_NUMBER}.txt", "r") as file:
        text_data = file.read()

    # Process the text data
    lines = text_data.strip().split("\n")
    result = []

    for line in lines:
        parts = line.split("\t")
        print(parts)
        player1_sno = int(parts[1].strip())
        player2_sno = int(parts[-1].strip())
        result_text = parts[7].strip()

        player1_info = sno_to_player.get(player1_sno, {})
        player2_info = sno_to_player.get(player2_sno, {})

        match = {
            "Player1": {
                "Name": player1_info.get("player", "Unknown"),
                "Title": player1_info.get("title", "Unknown"),
                "Country": player1_info.get("country", "Unknown"),
            },
            "Player2": {
                "Name": player2_info.get("player", "Unknown"),
                "Title": player2_info.get("title", "Unknown"),
                "Country": player2_info.get("country", "Unknown"),
            },
            "Result": result_text,
        }
        result.append(match)

    # Convert to JSON
    json_output = json.dumps(result, indent=2)

    # Convert to JSON and write to file
    with open(f"rapid_open_round_{ROUND_NUMBER}.json", "w") as output_file:
        json.dump(result, output_file, indent=2)
