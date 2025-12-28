BASE_CODES = {
    "Moon ball": "LMA2005MA",
    "Helium shouts": "LMA2005MB",
    "Bass shouts": "LMA2005MC",
    "Healing hands": "LMA2005A",
    "No more money worries": "LMA2005B",
}
ALL_EFFECTS = [
    (0x00, "It always snows at matches"),
    (0x01, "It is always sunny at matches"),
    (0x02, "It always rains at matches"),
    (0x03, "Rainbow trails"),
    (0x05, "Toon sounds"),
    (0x08, "Card free zone"),
    (0x09, "Chariots of fire"),
    (0x0A, "Creme de la creme"),
    (0x0B, "Defying time"),
    (0x0D, "Do you want to be in my gang?"),
    (0x0E, "Rome wasn't built in a day"),
    (0x0F, "Armchair selection"),
    (0x10, "Full to the brim"),
    (0x12, "All bonuses"),
]


def to_char(val):
    return chr((val % 26) + 0x41)


def generate_code(unique_id, index):
    d, m = divmod(unique_id, 100)
    exp_1 = pow(0x39, m ^ index, 0x44A5)
    exp_2 = pow(0x39, d ^ index, 0x44A5)

    u_low = to_char(exp_2)
    u_mid = to_char(exp_2 // 26)
    u_high = to_char(exp_2 // 676)
    l_low = to_char(exp_1)
    l_mid = to_char(exp_1 // 26)
    l_high = to_char(exp_1 // 676)

    return f"LMA2005{u_low}{l_mid}{u_mid}{l_high}{l_low}{u_high}"


def get_all_codes(unique_id):
    ret = BASE_CODES.copy()
    for i, effect in ALL_EFFECTS:
        ret[effect] = generate_code(unique_id, i)

    return ret


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        prog="lma_manager_2005",
        description="Generate bonus codes for LMA Manager 2005",
    )
    parser.add_argument("unqiue_id", type=int, help="The Unique ID for your game")
    parsed_args = parser.parse_args()

    all_codes = get_all_codes(parsed_args.unqiue_id)
    for effect, code in all_codes.items():
        print(f"{effect}: {code}")
