import round_to_json
import jsonround_to_player_json

ROUND_NUMBER = 11


def main():
    for round_number in range(1, ROUND_NUMBER + 1):
        round_to_json.round_to_json(round_number)
        jsonround_to_player_json.jsonround_to_player_json(round_number)


if __name__ == "__main__":
    main()
