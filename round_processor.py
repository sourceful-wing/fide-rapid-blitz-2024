import round_to_json
import jsonround_to_player_json

ROUND_NUMBER = 10


def main():
    round_to_json.round_to_json(ROUND_NUMBER)
    jsonround_to_player_json.jsonround_to_player_json(ROUND_NUMBER)


if __name__ == "__main__":
    main()
