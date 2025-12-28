BASE_CODES = {
    'Rainbow trails': 'LMA2004MC',
    'Toon sounds': 'LMA2004MB',
    'Chariots of fire': 'LMA2004B',
    'Defying time': 'LMA2004A',
    'Full to the brim': 'LMA2004MA',
}
ALL_EFFECTS = [
    (0x00, 'It always snows at matches'),
    (0x01, 'It is always sunny at matches'),
    (0x02, 'It always rains at matches'),
    (0x04, 'Moon ball'),
    (0x06, 'Helium shouts'),
    (0x07, 'Bass shouts'),
    (0x08, 'Card free zone'),
    (0x0a, 'Creme de la creme'),
    (0x0c, 'Healing hands'),
    (0x0d, 'Do you want to be in my gang?'),
    (0x0e, "Rome wasn't built in a day"),
    (0x0f, 'Armchair selection'),
    (0x11, 'No more money worries'),
    (0x12, 'All bonuses'),
]


def to_char(val):
    return chr((val % 26) + 0x41)


def generate_code(unique_id, index):
    d, m = divmod(unique_id, 100)
    exp_1 = pow(0x39, m ^ index, 0x44A5)
    exp_2 = pow(0x39, d ^ index, 0x44A5)

    c_0 = to_char(exp_2 // 26)
    c_1 = to_char(exp_1 // 676)
    c_2 = to_char(exp_1 // 26)
    c_3 = to_char(exp_2)
    c_4 = to_char(exp_2 // 676)
    c_5 = to_char(exp_1)

    return f"LMA2004{c_0}{c_1}{c_2}{c_3}{c_4}{c_5}"


def get_all_codes(unique_id):
    ret = BASE_CODES.copy()
    for i, effect in ALL_EFFECTS:
        ret[effect] = generate_code(unique_id, i)

    return ret


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        prog="lma_manager_2004",
        description="Generate bonus codes for LMA Manager 2004",
    )
    parser.add_argument("unqiue_id", type=int, help="The Unique ID for your game")
    parsed_args = parser.parse_args()

    all_codes = get_all_codes(parsed_args.unqiue_id)
    for effect, code in all_codes.items():
        print(f"{effect}: {code}")
