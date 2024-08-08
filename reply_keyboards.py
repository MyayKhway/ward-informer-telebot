from telegram import ReplyKeyboardMarkup

township_first_consonant_keyboard = ReplyKeyboardMarkup(
    [['က', 'ခ', 'စ', 'ဆ', 'တ', ], ['ထ', 'ဒ', 'ပ', 'ဗ', 'မ',], ['ရ', 'လ', 'သ', 'အ', 'ဥ']],
    one_time_keyboard=True, resize_keyboard=True, input_field_placeholder="First consonant of township"
)

township_keyboards_dict = {
    "က": [["ကျောက်တံတား", "ကျောက်တန်း", "ကြည့်မြင်တိုင်"], ["ကမာရွတ်", "ကိုကိုးကျွန်း", "ကော့မှူး", "ကွမ်းခြံကုန်း"]],
    "ခ": [['ခရမ်း', ]],
    "စ": [["စမ်းချောင်း"]],
    "ဆ": [['ဆိပ်ကြီးခနောင်တို',]],
    "တ": [['တာမွေ', 'တိုက်ကြီး',], ['တောင်ဥက္ကလာပ', 'တွံတေး',]],
    "ထ": [['ထန်းတပင်']],
    "ဒ": [["ဒေါပုံ", "အရှေ့ဒဂုံ"], ["တောင်ဒဂုံ", "မြောက် ဒဂုံ"], ["ဒဂုံ", "ဒဂုံဆိပ်ကမ်း", "ဒလ"]],
    "ပ": [["ပုဇွန်တောင်", "ပန်းပဲတန်း"]],
    "ဗ": [["ဗိုလ်တထောင်", "ဗဟန်း"]],
    "မ": [["မင်္ဂလာဒုံ", "မင်္ဂလာတောင်ညွန့်"], ["မရမ်းကုန်း", "မြောက် ဒဂုံ"], ["မြောက်ဥက္ကလာပ"], ["မှော်ဘီ"]],
    "ရ": [["ရွှေပြည်သာ", "ရန်ကင်း"]],
    "လ": [["လမ်းမတော်", "လသာ"], ["လှိုင်", "လှိုင်သာယာအရှေ့ပိုင်း"], ["လှိုင်သာယာအနောက်ပိုင်း", "လှည်းကူး"]],
    "သ": [["သင်္ဃန်းကျွန်း", "သာကေတ"], ["သန်လျင်", "သုံးခွ"]],
    "အ": [["အင်းစိန်", "အလုံ", "အရှေ့ ဒဂုံ"]],
    "ဥ": [["မြောက်ဥက္ကလာပ", "တောင်ဥက္ကလာပ"]]
}

category_keyboard = ReplyKeyboardMarkup(
    [
        ["လမ်းကြောင်း", "ခေတ္တရပ်စောင့်/ကားပေါ််ကခေတ္တဆင်း"], ['ထောက်လှမ်း', "Camp/ဝပ်ကျင်း", "ကင်းပုန်း"],
        ["*စစ်ဆေးခြင်း/ဖမ်းစီးခြင်း*"],
        ["လမ်းအတားအဆီးများ"], ["Others"], ["ပစ်ခတ်/ေပါက်ကွဲသံ"], ["ဒလန်"]
    ], resize_keyboard=True, one_time_keyboard=True
)

check_point_keyboard = ReplyKeyboardMarkup(
    [["ဧည့်စာရင်း", "လူရှာခြင်း"], ["ယာဉ်စစ်", "ဖုန်းစစ်"]], resize_keyboard=True, one_time_keyboard=True
)

Others_keyboard = ReplyKeyboardMarkup(
    [["ခြိမ်းေခြာက်", "Drone", "CCTV"],
     ["လူမှုပြဿနာ", "အိမ်ချိတ်ပိတ်", "လော်‌နဲ့ကြေငြာ"],
     ["မီးကြိုးဖြတ်", "ကျူးရှင်း", "မီးလောင်"],
     ["None of the above"]], resize_keyboard=True, one_time_keyboard=True
)

submission_confirmation_keyboard = ReplyKeyboardMarkup(
    [["Yes", "No"]], resize_keyboard=True, one_time_keyboard=True,
)

township_ward_confirmation_keyboard = ReplyKeyboardMarkup(
    [["မှန်ကန်ပါတယ်", "ပြန်လည်ရွေးချယ်ပါ"]], resize_keyboard=True, one_time_keyboard=True,
)

attachment_confirmation_keyboard = ReplyKeyboardMarkup(
    [["Attachment", "မရှိပါ"]], resize_keyboard=True, one_time_keyboard=True,
)
