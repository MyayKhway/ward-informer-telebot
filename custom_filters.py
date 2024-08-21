from telegram.ext.filters import MessageFilter
from reply_keyboards import township_keyboards_dict


class PlaceConfirmFilter(MessageFilter):
    def filter(self, message):
        return message.text == "မှန်ကန်ပါတယ်" or message.text == "ပြန်လည်ရွေးချယ်ပါ"


class AttachmentConfirmFilter(MessageFilter):
    def filter(self, message):
        return message.text == "Attachment" or message.text == "မရှိပါ"


class TownshipAlphabetFilter(MessageFilter):
    def filter(self, message):
        return message.text in ['က', 'ခ', 'စ', 'ဆ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဗ', 'မ', 'ရ', 'လ', 'သ', 'အ', 'ဥ']


class TownshipNamesFilter(MessageFilter):
    def filter(self, message):
        township_names_listoflists = list(township_keyboards_dict.values())
        for lst in township_names_listoflists:
            for lst_nest in lst:
                print(lst_nest)
                if message.text in lst_nest:
                    return True
        return False


place_confirm_filter = PlaceConfirmFilter()
attachment_confirm_filter = AttachmentConfirmFilter()
township_alphabet_filter = TownshipAlphabetFilter()
township_names_filter = TownshipNamesFilter()
