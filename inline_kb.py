from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import pandas as pd
from datetime import datetime
from pytz import timezone


class TimePicker:
    hour_text_button = InlineKeyboardButton("နာရီ", callback_data="display")
    minute_text_button = InlineKeyboardButton("မိနစ်", callback_data="display")
    hour_inc_button = InlineKeyboardButton("⬆", callback_data="hour_inc")
    minute_inc_button = InlineKeyboardButton("⬆", callback_data="minute_inc")
    hour_dec_button = InlineKeyboardButton("⬇", callback_data="hour_dec")
    minute_dec_button = InlineKeyboardButton("⬇", callback_data="minute_dec")
    ok_button = InlineKeyboardButton("OK", callback_data="submit")

    def __init__(self):
        self.current_time = datetime.now(timezone('Asia/Yangon'))
        self.hour_face = InlineKeyboardButton(str(self.current_time.hour), callback_data="hour")
        self.minute_face = InlineKeyboardButton(str(self.current_time.minute), callback_data="minute")
        self.keyboard = InlineKeyboardMarkup(
            [
                [self.hour_text_button, self.minute_text_button],
                [self.hour_inc_button, self.minute_inc_button],
                [self.hour_face, self.minute_face],
                [self.hour_dec_button, self.minute_dec_button],
                [self.ok_button]
            ]
        )

    def inc_hour(self):
        self.hour_face = InlineKeyboardButton((int(self.hour_face.text) + 1) % 24, callback_data="display")

    def dec_hour(self):
        self.hour_face = InlineKeyboardButton((int(self.hour_face.text) - 1) % 24, callback_data="display")

    def inc_minute(self):
        self.minute_face = InlineKeyboardButton((int(self.minute_face.text) + 1) % 60, callback_data="display")

    def dec_minute(self):
        self.minute_face = InlineKeyboardButton((int(self.minute_face.text) - 1) % 60, callback_data="display")

    def reset(self):
        self.hour_face = InlineKeyboardButton(str(self.current_time.hour), callback_data="display")
        self.minute_face = InlineKeyboardButton(str(self.current_time.minute), callback_data="display")


class StrengthPicker:
    small_vehicle_text_button = InlineKeyboardButton("စစ်/ရဲကားသေး", callback_data="text")
    small_vehicle_number_button = InlineKeyboardButton("0", callback_data="display")
    small_vehicle_inc_button = InlineKeyboardButton("⬆", callback_data="small_vehicle_inc")
    small_vehicle_dec_button = InlineKeyboardButton("⬇", callback_data="small_vehicle_dec")
    large_vehicle_text_button = InlineKeyboardButton("စစ်/ရဲကားကြီး", callback_data="text")
    large_vehicle_number_button = InlineKeyboardButton("0", callback_data="display")
    large_vehicle_inc_button = InlineKeyboardButton("⬆", callback_data="large_vehicle_inc")
    large_vehicle_dec_button = InlineKeyboardButton("⬇", callback_data="large_vehicle_dec")
    civ_vehicle_text_button = InlineKeyboardButton("အိမ်စီးကား", callback_data="text")
    civ_vehicle_number_button = InlineKeyboardButton("0", callback_data="display")
    civ_vehicle_inc_button = InlineKeyboardButton("⬆", callback_data="civ_vehicle_inc")
    civ_vehicle_dec_button = InlineKeyboardButton("⬇", callback_data="civ_vehicle_dec")
    motorbike_text_button = InlineKeyboardButton("ဆိုင်ကယ်", callback_data="text")
    motorbike_number_button = InlineKeyboardButton("0", callback_data="display")
    motorbike_inc_button = InlineKeyboardButton("⬆", callback_data="motorbike_inc")
    motorbike_dec_button = InlineKeyboardButton("⬇", callback_data="motorbike_dec")
    other_vehicle_text_button = InlineKeyboardButton("တခြားကား", callback_data="text")
    other_vehicle_number_button = InlineKeyboardButton("0", callback_data="display")
    other_vehicle_inc_button = InlineKeyboardButton("⬆", callback_data="other_vehicle_inc")
    other_vehicle_dec_button = InlineKeyboardButton("⬇", callback_data="other_vehicle_dec")
    uniform_text_button = InlineKeyboardButton("uniform", callback_data="text")
    uniform_number_button = InlineKeyboardButton("0", callback_data="display")
    uniform_inc_button = InlineKeyboardButton("⬆", callback_data="uniform_inc")
    uniform_dec_button = InlineKeyboardButton("⬇", callback_data="uniform_dec")
    plain_text_button = InlineKeyboardButton("အရပ်ဝတ်", callback_data="text")
    plain_number_button = InlineKeyboardButton("0", callback_data="display")
    plain_inc_button = InlineKeyboardButton("⬆", callback_data="plain_inc")
    plain_dec_button = InlineKeyboardButton("⬇", callback_data="plain_dec")
    ok_button = InlineKeyboardButton("OK", callback_data="submit")

    def __init__(self) -> None:
        self.vehicle_keyboard = InlineKeyboardMarkup(
            [
                [self.small_vehicle_text_button, self.large_vehicle_text_button],
                [self.small_vehicle_inc_button, self.large_vehicle_inc_button],
                [self.small_vehicle_number_button, self.large_vehicle_number_button],
                [self.small_vehicle_dec_button, self.large_vehicle_dec_button],
                [self.civ_vehicle_text_button, self.motorbike_text_button, self.other_vehicle_text_button],
                [self.civ_vehicle_inc_button, self.motorbike_inc_button, self.other_vehicle_inc_button],
                [self.civ_vehicle_number_button, self.motorbike_number_button, self.other_vehicle_number_button],
                [self.civ_vehicle_dec_button, self.motorbike_dec_button, self.other_vehicle_dec_button],
                [self.ok_button]
            ]
        )
        self.personnel_keyboard = InlineKeyboardMarkup(
            [
                [self.uniform_text_button, self.plain_text_button],
                [self.uniform_inc_button, self.plain_inc_button],
                [self.uniform_number_button, self.plain_number_button],
                [self.uniform_dec_button, self.plain_dec_button],
                [self.ok_button]
            ]
        )

    def inc_small(self):
        self.small_vehicle_number_button = InlineKeyboardButton((int(self.small_vehicle_number_button.text)) + 1, callback_data="display")

    def inc_large(self):
        self.large_vehicle_number_button = InlineKeyboardButton((int(self.large_vehicle_number_button.text)) + 1, callback_date="display")

    def inc_civ(self):
        self.civ_vehicle_number_button = InlineKeyboardButton((int(self.civ_vehicle_number_button.text)) + 1, callback_data="display")

    def inc_motor(self):
        self.motorbike_number_button = InlineKeyboardButton((int(self.motorbike_number_button.text)) + 1, callback_data="display")

    def inc_other(self):
        self.other_vehicle_number_button = InlineKeyboardButton((int(self.other_vehicle_number_button.text)) + 1, callback_date="display")

    def dec_small(self):
        if self.small_vehicle_number_button.text != '0':
            self.small_vehicle_number_button = InlineKeyboardButton((int(self.small_vehicle_number_button.text)) - 1, callback_date="display")

    def dec_large(self):
        if self.large_vehicle_number_button.text != '0':
            self.large_vehicle_number_button = InlineKeyboardButton((int(self.large_vehicle_number_button.text)) - 1, callback_date="display")

    def dec_civ(self):
        if self.civ_vehicle_number_button.text != '0':
            self.civ_vehicle_number_button = InlineKeyboardButton((int(self.civ_vehicle_number_button.text)) - 1, callback_date="display")

    def dec_motor(self):
        if self.motorbike_number_button.text != '0':
            self.motorbike_number_button = InlineKeyboardButton((int(self.motorbike_number_button.text)) - 1, callback_date="display")

    def dec_other(self):
        if self.other_vehicle_number_button.text != '0':
            self.other_vehicle_number_button = InlineKeyboardButton((int(self.other_vehicle_number_button.text)) - 1, callback_date="display")

    def inc_uniform(self):
        self.uniform_number_button = InlineKeyboardButton((int(self.uniform_number_button.text)) + 1, callback_date="display")

    def dec_uniform(self):
        if self.uniform_number_button.text != '0':
            self.uniform_number_button = InlineKeyboardButton((int(self.uniform_number_button.text)) - 1, callback_date="display")

    def inc_plain(self):
        self.plain_number_button = InlineKeyboardButton((int(self.plain_number_button.text)) + 1, callback_date="display")

    def dec_plain(self):
        if self.plain_number_button.text != '0':
            self.plain_number_button = InlineKeyboardButton((int(self.plain_number_button.text)) - 1, callback_data="display")

    def reset_vehicle(self):
        self.small_vehicle_number_button = InlineKeyboardButton("0", callback_date="display")
        self.large_vehicle_number_button = InlineKeyboardButton("0", callback_date="display")
        self.other_vehicle_number_button = InlineKeyboardButton("0", callback_date="display")
        self.motorbike_number_button = InlineKeyboardButton("0", callback_date="display")

    def reset_personnel(self):
        self.uniform_number_button = InlineKeyboardButton("0", callback_date="display")
        self.plain_number_button = InlineKeyboardButton("0", callback_date="display")


class WardsKeyboard:

    def __init__(self, township):
        df = pd.read_csv("Wards and Villages.csv")
        wards_LUT = {}
        for column in df.columns:
            ward_index = 0
            wards = []
            wards_in_township = {}
            for ward in df[column]:
                if not pd.isna(ward):
                    wards.append(ward)
                    wards_in_township[ward] = ward_index
                    ward_index += 1
            wards_LUT[column] = wards_in_township
        self.wards: dict = wards_LUT.get(township)
        self.wards_names: list = list(self.wards.keys())

        def lookup_ward_callback_data(ward):
            return self.wards.get(ward, 0)

        def keyboard_maker(wards):
            buttons_lst = []
            keyboard = list(zip(*[iter(wards)] * 3))
            left_buttons_num = len(wards) % 2
            for buttons in keyboard:
                button_row = list(map(lambda ward:
                                      InlineKeyboardButton(ward, callback_data=lookup_ward_callback_data(ward)),
                                      buttons))
                buttons_lst.append(button_row)
            if left_buttons_num != 0:
                left_buttons_row = list(map(lambda ward:
                                            InlineKeyboardButton(ward, callback_data=str(lookup_ward_callback_data(ward))),
                                            wards[-left_buttons_num:]))
                buttons_lst.append(left_buttons_row)

            return InlineKeyboardMarkup(buttons_lst)

        if (township == "တိုက်ကြီး"):
            self.keyboard = keyboard_maker(self.wards_names[:(len(self.wards_names) // 2)])
            self.keyboard2 = keyboard_maker(self.wards_names[(len(self.wards_names) // 2):])
        else:
            self.keyboard = keyboard_maker(self.wards_names)
            self.keyboard2 = None
