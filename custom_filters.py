from telegram.ext.filters import MessageFilter


class PlaceConfirmFilter(MessageFilter):
    def filter(self, message):
        return message.text == "မှန်ကန်ပါတယ်" or message.text == "ပြန်လည်ရွေးချယ်ပါ"


class AttachmentConfirmFilter(MessageFilter):
    def filter(self, message):
        return message.text == "Attachment" or message.text == "မရှိပါ"


place_confirm_filter = PlaceConfirmFilter()
attachment_confirm_filter = AttachmentConfirmFilter()
