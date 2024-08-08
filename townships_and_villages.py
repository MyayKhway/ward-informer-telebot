import pandas as pd


def wards_LUT_key_search(township, ward_index_input):
    df = pd.read_csv("Wards and Villages.csv")

    wards_LUT = {}
    township_index = 'A'
    for column in df.columns:
        ward_index = 0
        township_index = chr(ord(township_index) + 1)
        wards = []
        wards_in_township = {}
        for ward in df[column]:
            if not pd.isna(ward):
                wards.append(ward)
                wards_in_township[ward] = ward_index
                ward_index += 1
            wards_LUT[column] = wards_in_township
    for key, value in wards_LUT.get(township, {}).items():
        if int(value) == int(ward_index_input):
            return key
    return "No key found"
