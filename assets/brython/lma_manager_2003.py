BASE_CODES = {
    "Sell Out": "LMA2003MA",
    "Anytime, Any Place": "LMA2003MB",
    "That's All Folks": "LMA2003MC",
    "Loadza Money": "LMA2003A",
    "Low Gravity Ball": "LMA2003B",
}
ALL_EFFECTS = [
    "Too Much Coffee",
    "Rainbow Trails",
    "Win, Win, Win",
    "Pyscho Team",
    "Selective Sight",
    "Medicine Man",
    "Instant Stadium",
    "Dream Team",
    "Super Team",
    "Sit Back And Relax",
    "Winter Sport",
    "You Are My Sunshine",
    "Rain God",
    "Forever Young",
    "Super Coach",
    "Don't Worry, Be Happy",
    "Teamwork",
    "Pinky and Perky",
    "Lucifer",
    "Go Now",
]


def get_digits(val):
    low = val % 26
    mid = (val // 26) % 26
    high = (val // 676) % 26
    return (chr(low + 0x41), chr(mid + 0x41), chr(high + 0x41))


def generate_code(unique_id, index):
    d, m = divmod(unique_id, 100)
    exp_1 = pow(0x39, m ^ index, 0x44A5)
    exp_2 = pow(0x39, d ^ index, 0x44A5)
    c_0, c_1, c_2, c_3, c_4, c_5 = get_digits(exp_1) + get_digits(exp_2)

    return f"LMA3{c_0}{c_2}{c_1}{c_4}{c_5}{c_3}"


def get_all_codes(unique_id):
    ret = BASE_CODES.copy()
    for i, effect in enumerate(ALL_EFFECTS):
        ret[effect] = generate_code(unique_id, i)

    return ret


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        prog="lma_manager_2003",
        description="Generate bonus codes for LMA Manager 2003",
    )
    parser.add_argument("unqiue_id", type=int, help="The Unique ID for your game")
    parsed_args = parser.parse_args()

    all_codes = get_all_codes(parsed_args.unqiue_id)
    for effect, code in all_codes.items():
        print(f"{effect}: {code}")
