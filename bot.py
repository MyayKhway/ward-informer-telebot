from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler,
)
from telegram import ReplyKeyboardMarkup, Update
from send_to_AT import upload
from inline_kb import WardsKeyboard
from townships_and_villages import wards_LUT_key_search
from reply_keyboards import (
    township_first_consonant_keyboard,
    township_keyboards_dict,
    township_ward_confirmation_keyboard,
    attachment_confirmation_keyboard,
    submission_confirmation_keyboard
)
from dotenv.main import load_dotenv
import logging
import os
from custom_filters import (
    place_confirm_filter,
    attachment_confirm_filter
)

# Enable Loggin
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR
)

logger = logging.getLogger(__name__)

TOWN_ALPHABET, TOWNSHIP, WARD, TOWNSHIP_WARD_CONFIRM, NAME, ADDRESS, ATTACHMENT, ATTACHMENT_CONFIRMATION, DETAILS, ADDITIONAL_INFO, CONFIRMATION, CONFIRMED = range(12)


async def start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        """
        မိမိတိုနေထိုင်ရာ ရပ်ကွက်ဝန်းကျင် အနီးဆုံးက စစ်တပ်ထောက်တိုင် လက်ပါးစေဖြစ်တဲ့ ရပ်ကွက်အုပ်ချုပ်ရေးမှူး (အုပ်ကြီး) တွေအကြောင်း မိမိကိုယ်တိုင် သတင်းပေးနိုင်ဖို ရည်ရွယ်ပါတယ်။
        အုပ်ကြီးသတင်း ပေးပို့လိုသော မြိုနယ်နာမည်၏ ပထမဆုံးအက္ခရာကိုရွေးချယ်ပါ။ (ဥပမာ - ကမာရွတ်မြိုနယ်အတွက် “က”)
        """,
        reply_markup=township_first_consonant_keyboard,
    )
    return TOWN_ALPHABET


async def choose_township(update: Update, context: CallbackContext) -> int:
    # choose the township
    kb_dict = township_keyboards_dict
    chosen_consonant = update.message.text
    await update.message.reply_text(
        "အုပ်ကြီးသတင်း ပေးပို့လိုသော မြိုနယ်ကို ရွေးချယ်ပါ။",
        reply_markup=ReplyKeyboardMarkup(
            kb_dict.get(chosen_consonant), resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Township"),
    )
    return TOWNSHIP


async def ask_ward(update: Update, context: CallbackContext) -> int:
    """Save township and ask ward"""
    township = update.message.text
    context.user_data['township'] = township
    wards_kb_obj = WardsKeyboard(township)
    wards_keyboard = wards_kb_obj.keyboard
    wards_keyboard2 = wards_kb_obj.keyboard2 if wards_kb_obj.keyboard2 is not None else None
    await update.message.reply_text(
        "အုပ်ကြီးသတင်း ပေးပို့လိုသော ရပ်ကွက်/ကျေးရွာအုပ်စု၏အမည်ကို ရွေးချယ်ပါ။",
        reply_markup=wards_keyboard,
    )
    if wards_keyboard2 is not None:
        await update.message.reply_text(
            "အုပ်ကြီးသတင်း ပေးပို့လိုသော ရပ်ကွက်/ကျေးရွာအုပ်စု၏အမည်ကို ရွေးချယ်ပါ။",
            reply_markup=wards_keyboard2,
        )
    return WARD


async def save_ward_ask_township_confirmation(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    print(query.data)
    await query.answer()
    township = context.user_data["township"]
    context.user_data["ward"] = wards_LUT_key_search(township, query.data)
    ward = context.user_data["ward"]
    await context.application.bot.send_message(
        update.effective_chat.id,
        f"{township} မြိုနယ်၊ {ward} ရပ်ကွက်/ကျေးရွာအုပ်စုက အုပ်ကြီးအကြာင်း သတင်း‌ပေးပို့လိုတာ မှန်ကန်ပါသလား။",
        reply_markup=township_ward_confirmation_keyboard
    )
    return TOWNSHIP_WARD_CONFIRM


async def save_place_ask_name(update: Update, context: CallbackContext) -> int:
    reply = update.message.text
    if reply == township_ward_confirmation_keyboard.keyboard[0][1].text:
        del context.user_data["ward"]
        del context.user_data["township"]
        await update.message.reply_text(
            """အုပ်ကြီးသတင်း ပေးပို့လိုသော မြိုနယ်နာမည်၏ ပထမဆုံးအက္ခရာကိုရွေးချယ်ပါ။ (ဥပမာ - ကမာရွတ်မြိုနယ်အတွက် “က”)
        """,
            reply_markup=township_first_consonant_keyboard,
        )
        return TOWN_ALPHABET
    elif reply == township_ward_confirmation_keyboard.keyboard[0][0].text:
        await update.message.reply_text(
            """ရပ်ကွက်/ကျေးရွာအုပ်စုက အုပ်ချုပ်ရေးမှူး၏ နာမည်အပြည့်အစုံနှင့် အများခေါ်သော အမည်များကို ရေးသားပေးပို့ပါ။ """
        )
        return NAME


async def save_name_ask_address(update: Update, context: CallbackContext) -> int:
    context.user_data["target_name"] = update.message.text
    await update.message.reply_text(
        """အုပ်ချုပ်ရေးမှူး (အုပ်ကြီး) ၏ နေရပ်လိပ်စာနှင့် လမ်းညွှန်ကို ရေးသားပေးပို့ပါ။"""
    )
    return ADDRESS


async def save_address_ask_for_attachment_consent(update: Update, context: CallbackContext) -> int:
    context.user_data['address'] = update.message.text
    await update.message.reply_text(
        "အုပ်ချုပ်ရေးမှူး (အုပ်ကြီး) ၏ ဓာတ်ပုံ (သို) ရုပ်သံဗီဒီယိုဖိုင်များ ရှိပါက ပေးပို့ ပါ။",
        reply_markup=attachment_confirmation_keyboard
    )
    return ATTACHMENT_CONFIRMATION


async def ask_for_attachment(update: Update, context: CallbackContext) -> int:
    reply = update.message.text
    if reply == attachment_confirmation_keyboard.keyboard[0][1].text:
        await update.message.reply_text(
            "အုပ်ချုပ်ရေးမှူး (အုပ်ကြီး) ၏ ပို့င်ဆိုင်မှုများ၊ စီးပွားရေးများ၊ လုပ်ကွက်များ၊ ချစားမှုများ၊ ယုတ်မာမှုများနှင့် ပက်သက်‌သော သတင်းပေးချက်များ ရေးသားပေးပို့ပါ။"
        )
        return DETAILS
    elif reply == attachment_confirmation_keyboard.keyboard[0][0].text:
        await update.message.reply_text(
            """📎 ကိုနှိပ်ပြီး ပေးပို့ နိုင်ပါသည်။ """
        )
        return ATTACHMENT


async def save_photo_ask_details(update: Update, context: CallbackContext) -> int:
    file = await update.message.photo[-1].get_file()
    filename = context.user_data["township"]
    context.user_data["attachment"] = [
        {
            "url": file.file_path,
            "filename": filename
        }
    ]
    await update.message.reply_text(
        "အုပ်ချုပ်ရေးမှူး (အုပ်ကြီး) ၏ ပိုင်ဆိုင်မှုများ၊ စီးပွားရေးများ၊ လုပ်ကွက်များ၊ ချစားမှုများ၊ ယုတ်မာမှုများနှင့် ပက်သက်‌သော သတင်းပေးချက်များ ရေးသားပေးပို့ပါ။"
    )
    return DETAILS


async def save_audio_ask_details(update: Update, context: CallbackContext) -> int:
    file = await update.message.audio.get_file()
    filename = context.user_data["township"]
    context.user_data["attachment"] = [
        {
            "url": file.file_path,
            "filename": filename
        }
    ]
    await update.message.reply_text(
        "အုပ်ချုပ်ရေးမှူး (အုပ်ကြီး) ၏ ပိုင်ဆိုင်မှုများ၊ စီးပွားရေးများ၊ လုပ်ကွက်များ၊ ချစားမှုများ၊ ယုတ်မာမှုများနှင့် ပက်သက်‌သော သတင်းပေးချက်များ ရေးသားပေးပို့ပါ။"
    )
    return DETAILS


async def save_video_ask_details(update: Update, context: CallbackContext) -> int:
    file = await update.message.video.get_file()
    filename = context.user_data["township"]
    context.user_data["attachment"] = [
        {
            "url": file.file_path,
            "filename": filename
        }
    ]
    await update.message.reply_text(
        "အုပ်ချုပ်ရေးမှူး (အုပ်ကြီး) ၏ ပိုင်ဆိုင်မှုများ၊ စီးပွားရေးများ၊ လုပ်ကွက်များ၊ ချစားမှုများ၊ ယုတ်မာမှုများနှင့် ပက်သက်‌သော သတင်းပေးချက်များ ရေးသားပေးပို့ပါ။"
    )
    return DETAILS


async def save_document_ask_details(update: Update, context: CallbackContext) -> int:
    file = await update.message.document.get_file()
    filename = context.user_data["township"]
    context.user_data["attachment"] = [
        {
            "url": file.file_path,
            "filename": filename
        }
    ]
    await update.message.reply_text(
        "အုပ်ချုပ်ရေးမှူး (အုပ်ကြီး) ၏ ပိုင်ဆိုင်မှုများ၊ စီးပွားရေးများ၊ လုပ်ကွက်များ၊ ချစားမှုများ၊ ယုတ်မာမှုများနှင့် ပက်သက်‌သော သတင်းပေးချက်များ ရေးသားပေးပို့ပါ။"
    )
    return DETAILS


async def save_details_ask_additional_info(update: Update, context: CallbackContext) -> int:
    context.user_data["details"] = update.message.text
    await update.message.reply_text(
        "သီးခြား ဖြည့်စွက်သတင်းပေးလိုမှု ရှိပါက ရေးသားပေးပို့ပါ။"
    )
    return ADDITIONAL_INFO


async def save_additional_info_ask_confirmation(update: Update, context: CallbackContext) -> int:
    context.user_data["additional"] = update.message.text
    data = context.user_data
    confirm_text = "{township} မြိုနယ်၊ {ward} အုပ်ချုပ်ရေးမှူး\nအမည် - {name}\nနေရပ်လိပ်စာ - {address}\nစီပွားရေး/လှုပ်ရှားမှုများ - {details}\n ဖြည့်စွက်သတင်းပေးချက် - {additional}\n သတင်းပေးပို့မှုကို အတည်ပြုပါ။"
    formatted_string = confirm_text.format(
        township=data["township"],
        ward=data["ward"],
        name=data["target_name"],
        address=data["address"],
        details=data["details"],
        additional=data["additional"],
    )
    await update.message.reply_text(
        formatted_string, reply_markup=submission_confirmation_keyboard
    )
    return CONFIRMED


async def end_convo(update: Update, context: CallbackContext) -> int:
    context.user_data["reporter_telegram_id"] = str(update.message.from_user.id)
    context.user_data["reporter_telegram_name"] = update.message.from_user.name
    print(context.user_data)
    if (update.message.text == "Yes"):
        print("upload")
        upload(context.user_data)
    await update.message.reply_text(
        """စစ်ကျွန်အုပ်ချုပ်ရေးယန္တရားကို အောက်အခြေကစ ဖြိုချ‌တော်လှန်ရာမှာ မိမိတိုကိုယ်တိုင် ပူးပေါင်းပါဝင်ပေးတဲ့အတွက် ကျေးဇူးအထူးတင်ရှိပြီး ကျန်းမာဘေးကင်းစေဖို ဆန္ဒပြုပါတယ်။
        ထပ်မံသတင်းပို့ရန် /start သို့မဟုတ် /inform ကိုနှိပ်ပါ။""",
    )
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    return ConversationHandler.END


def main() -> None:
    load_dotenv()
    TOKEN = os.environ.get("BOTTOKEN")
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), CommandHandler('inform', start)],
        states={
            TOWN_ALPHABET: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_township)],
            TOWNSHIP: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_ward)],
            WARD: [CallbackQueryHandler(save_ward_ask_township_confirmation)],
            TOWNSHIP_WARD_CONFIRM: [MessageHandler(place_confirm_filter, save_place_ask_name)],
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_name_ask_address)],
            ADDRESS: [MessageHandler(filters.TEXT, save_address_ask_for_attachment_consent)],
            ATTACHMENT_CONFIRMATION: [MessageHandler(attachment_confirm_filter, ask_for_attachment)],
            ATTACHMENT: [
                MessageHandler(filters.PHOTO, save_photo_ask_details),
                MessageHandler(filters.VIDEO, save_video_ask_details),
                MessageHandler(filters.Document.ALL, save_document_ask_details),
                MessageHandler(filters.AUDIO, save_audio_ask_details),
            ],
            DETAILS: [MessageHandler(filters.TEXT, save_details_ask_additional_info)],
            ADDITIONAL_INFO: [MessageHandler(filters.TEXT, save_additional_info_ask_confirmation)],
            CONFIRMED: [MessageHandler(filters.TEXT & ~filters.COMMAND & filters.Regex("(Yes|No)"), end_convo)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        conversation_timeout=300,
        allow_reentry=True,
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
