ALL_EFFECTS = [
    "It always snows at matches",
    "It is always sunny at matches",
    "It always rains at matches",
    "Rainbow trails",
    "Moon ball",
    "Toon sounds",
    "Helium shouts",
    "Bass shouts",
    "Card free zone",
    "Chariots of Fire",
    "Crème de la crème",
    "Defying time",
    "Healing hands",
    "Do you want to be in my gang?",
    "Rome wasn't built in a day",
    "Armchair selection",
    "Full to the brim",
    "No more money worries",
    "Youth Stars",
    "Transfer Free-For-All",
    "Training Boost",
    "Super Staff",
    "Happy Talky Talky",
    "Job for Life",
    "Permanent Vote of Confidence",
    "Transfer Market Shutdown",
    "Fantasy Team in the Money",
    "All bonuses",
]
ALPHABET = "0123456789ABCDEFGHJKLMNPQRTUVWXY"
XOR_MASK = 0xCC0DE3A54E7550F4
PUBLIC_EXPONENT = 65537
PRIVATE_EXPONENT = 0xB4DF15C731EF8A39
MODULUS = 0x0102B112A82EE4F459


def decode_string(code):
    ret = 0
    for char in reversed(code):
        c = ord(char.upper())
        val = c - 0x30

        if c > ord("9"):
            val -= 0x07
        if c > ord("H"):
            val -= 0x01
        if c > ord("O"):
            val -= 0x01
        if c > ord("R"):
            val -= 0x01
        if c > ord("Y"):
            val = -1
        if (val < 0) or (val > 31):
            raise ValueError(f"Invalid character: {char}")
        ret = (ret << 5) | val
    return ret


def encode_integer(val, length=13):
    ret = []
    for _ in range(length):
        ret.append(ALPHABET[val & 0x1F])
        val >>= 5

    return "".join(ret)


def get_target_value(unique_id, index):
    x = (index << 8) & 0xFFFF
    y = unique_id & 0xFFFF
    z = MODULUS & 0xFFFF
    return x | (y << 16) | (z << 32)


def check_code(unique_id, index, code):
    try:
        s_val = decode_string(code)
    except ValueError:
        return False

    rsa_res = pow(s_val, PUBLIC_EXPONENT, MODULUS)
    check_val = rsa_res ^ XOR_MASK
    target = get_target_value(unique_id, index)
    return check_val == target


def generate_code(unique_id, index):
    target = get_target_value(unique_id, index)
    required_rsa_val = target ^ XOR_MASK
    s_val = pow(required_rsa_val, PRIVATE_EXPONENT, MODULUS)
    return encode_integer(s_val)


def get_all_codes(unique_id):
    ret = {}
    for i, effect in enumerate(ALL_EFFECTS):
        code = generate_code(unique_id, i)
        check_code(unique_id, i, code)
        ret[effect] = code

    return ret


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        prog="lma_manager_2006",
        description="Generate bonus codes for LMA Manager 2006",
    )
    parser.add_argument("unqiue_id", type=int, help="The Unique ID for your game")
    parsed_args = parser.parse_args()

    all_codes = get_all_codes(parsed_args.unqiue_id)
    for effect, code in all_codes.items():
        print(f"{effect}: {code}")
