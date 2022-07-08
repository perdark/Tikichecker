import os , random , datetime , base64 , logging , asyncio , time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon.tl import functions, types
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.types import ( 
    ChannelParticipantsAdmins, 
    ChannelParticipantsKicked, 
    ChatBannedRights, 
    UserStatusEmpty, 
    UserStatusLastMonth, 
    UserStatusLastWeek, 
    UserStatusOffline, 
    UserStatusOnline, 
    UserStatusRecently
)
from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
y = datetime.datetime.now().year;m = datetime.datetime.now().month;dayy = datetime.datetime.now().day;day = datetime.datetime.now().strftime("%A");m9zpi = f"{y}/{m}/{dayy} - {day}";sec = time.time();mshor = ["اليسا","اصالة","جورجينا","انجلينا جولي","مايا","ليسا","رحمة","نانسي","مريم غريبة","سيلينا","جيسيكا","جوليا","ايما","مارينا","لانا",""];mss = random.choice(mshor);msss = random.choice(mshor)


APP_ID  = 10743318
API_HASH = "371d1dc33eccaa19bb0814a27bb98f3c"
sedthon = TelegramClient("session", APP_ID, API_HASH)
sedthon.start()
LOGS = logging.getLogger(__name__)
logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await sedthon(JoinChannelRequest("@sedthon"))
    except BaseException:
        pass
 
 
GCAST_BLACKLIST = [
    -1001118102804,
    -1001161919602,
]

DEVS = [
    1361835146,
]
DEL_TIME_OUT = 60
normzltext = "1234567890"
namerzfont = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
if 1 == 1:
    name = "Profile Photos"
    client = sedthon

    @sedthon.on(events.NewMessage(outgoing=True, pattern=".صور"))
    async def potocmd(event):
        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await sedthon.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("`ايدي الشخص غير صالح !`")
                    return
            except:
                 await event.edit("`هل انت كوميدي ؟`")
                 return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await sedthon.send_file(event.chat_id, send_photos)
            else:
                await event.edit("`ليس لديه صورة يا ذكي !`")
                return

@sedthon.on(events.NewMessage(outgoing=True, pattern=".ذاتية"))
async def roz(bakar):
    if not bakar.is_reply:
        return await bakar.edit(
            "يستعمل الامر بالرد على الصورة او الفيديو !"
        )
    rr9r7 = await bakar.get_reply_message()
    pic = await rr9r7.download_media()
    await sedthon.send_file(
        "me", pic, caption=f"تم حفظ الصورة او الفيديز الذاتي هنا : "
    )
    await bakar.delete()       
@sedthon.on(events.NewMessage(pattern=r".ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await sedthon(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)
@sedthon.on(events.NewMessage(outgoing=True, pattern=".اسم وقتي"))
async def _(event):
    await event.edit("تم انشاء اسم وقتي")
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{HM}"
        LOGS.info(name)
        try:
            await sedthon(
                functions.account.UpdateProfileRequest(
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
@sedthon.on(events.NewMessage(outgoing=True, pattern=".بايو وقتي"))
async def _(event):
    await event.edit("تم انشاء بايو وقتي")
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%l:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = HM
        LOGS.info(bio)
        try:
            await sedthon(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )
           
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
@sedthon.on(events.NewMessage(outgoing=True, pattern=".غادر"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`سأغادر هذه المجموعة .`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await sedthon(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`سيدي هذه ليست مجموعة !`')

@sedthon.on(events.NewMessage(outgoing=True, pattern=".كروب(?: |$)(.*)"))
async def gcast(event):
    sedthon = event.pattern_match.group(1)
    if sedthon:
        msg = sedthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )
@sedthon.on(events.NewMessage(outgoing=True, pattern=".خاص(?: |$)(.*)"))
async def gucast(event):
    sedthon = event.pattern_match.group(1)
    if sedthon:
        msg = sedthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )
@sedthon.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "رفع مشرف":

        await event.edit(input_str)

        animation_chars = [
        
            "جارِ رفعه ..",
            "تتم اضافة الصلاحيات الآتية : ",
            "ارسال الوسائط",
            "حذف رسائل الاخرين",
            "ارسال المتحركات",    
            "تعديل رسائل الاخرين",
            "نشر الرسائل",
            "ادارة المحادثات المرئية",
            "دعوة مستخدمين جدد",
            "اضافة مشرفين جدد",
            "تثبيت الرسائل",
            "تغيير معلومات المحادثة",
            "تم اكتمال جميع الصلاحيات ..",
            "sedthon Src : @sedthon\nsedthon Dev : @Dar4k"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])

@sedthon.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass
@sedthon.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
@sedthon.on(events.NewMessage(outgoing=True, pattern=".اشتراكاتي"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    u = 0 # number of users
    g = 0 # number of basic groups
    c = 0 # number of super groups
    bc = 0 # number of channels
    b = 0 # number of bots
    await event.edit("يتم التعداد ..")
    async for d in sedthon.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            logger.info(d.stringify())
    end = datetime.datetime.now()
    ms = (end - start).seconds
    await event.edit("""تم استخراجها في {} ثواني
`الاشخاص :\t{}
المجموعات العادية :\t{}
المجموعات الخارقة :\t{}
القنوات :\t{}
البوتات :\t{}
`""".format(ms, u, g, c, bc, b))

@sedthon.on(events.NewMessage(pattern=r".ملصق", outgoing=True))

async def _(event):

    if event.fwd_from:

        return 

    if not event.reply_to_msg_id:

       await event.edit("`يجب الرد على رسالة !`")

       return

    reply_message = await event.get_reply_message() 

    if not reply_message.text:

       await event.edit("`يجب الرد على رسالة !`")

       return

    chat = "@QuotLyBot"

    sender = reply_message.sender

    if reply_message.sender.bot:

       await event.edit("```Reply to actual users message.```")

       return

    await event.edit("`جار تحويل النص الى ملصق ..`")

    async with event.client.conversation(chat) as conv:

          try:     

              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))

              await event.client.forward_messages(chat, reply_message)

              response = await response 

          except YouBlockedUserError: 

              await event.reply("```Please unblock me (@QuotLyBot) u Nigga```")

              return

          if response.text.startswith("Hi!"):

             await event.edit("```Can you kindly disable your forward privacy settings for good?```")

          else: 

             await event.delete()

             await event.client.send_message(event.chat_id, response.message)


@sedthon.on(events.NewMessage(pattern=r".تفليش", outgoing=True))
async def _(event):
    result = await event.client.get_permissions(event.chat_id, 1361835146)
    if not result:
        return await edit_or_reply( 
            event, "عذر ليس لديك الصلاحيات الكافية لاستخدام هذا الامر"
             )
        ksmkksmk = await edit_or_reply(event, "جارِ")
        admins = await event.client.get_participants( 
            event.chat_id, filter=ChannelParticipantsAdmins 
        )
        admins_id = [i.id for i in admins]
        total = 0
        success = 0
        async for user in event.client.iter_participants(event.chat_id):
            total += 1
            try:
                if user.id not in admins_id:
                    await event.client( 
                        EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS) 
                    )
                    success += 1
                    await sleep(0.1)
            except Exception as e:
                LOGS.info(str(e))
                await sleep(0.1)
                await ksmkksmk.edit(f"تم بنجاح التفليش {success} من {total} الاعضاء")
@sedthon.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""- sedthon Userbot .
اوامر السورس :
.فحص | فحص السورس
-- -- -- -- -- -- -- -- --
.مؤقت + وقت + عدد + الجملة | تكرار مؤقت للكلام 
-- -- -- -- -- -- -- -- --
.تكرار + كلام | تكرار لا نهائي للكلام
-- -- -- -- -- -- -- -- --
.خاص + النص \ اذاعة لجميع الاشخاص في حسابك
-- -- -- -- -- -- -- -- --
.ضيف + رابط | ارسل الامر في مجموعتك
-- -- -- -- -- -- -- -- --
.كروب + النص | اذاعة لجميع الكروبات في حسابك
-- -- -- -- -- -- -- -- --
.اسم وقتي | اسم وقتي في حسابك !
-- -- -- -- -- -- -- -- --
.بايو وقتي | بايو وقتي في حسابك !
-- -- -- -- -- -- -- -- --
.ذاتية | حفظ الصور والفيديوهات ذاتية التدمير
-- -- -- -- -- -- -- -- --
.فك حظر | فك حظر جميع المستخدمين الذين حظرتهم في حسابك
-- -- -- -- -- -- -- -- --
.الوقت | الوقت والتاريخ والخ ..
-- -- -- -- -- -- -- -- --
.اسمي | اسم حسابك
-- -- -- -- -- -- -- -- --
.نبذتي | بايو حسابك
-- -- -- -- -- -- -- -- --
.معرفي | معرف حسابك
-- -- -- -- -- -- -- -- --
.الثواني | الثواني الحالية في هذا اليوم
-- -- -- -- -- -- -- -- --
.اليوم | اليوم الحالي
-- -- -- -- -- -- -- -- --
.تاريخ اليوم | تاريخ اليوم بالشهر
-- -- -- -- -- -- -- -- --
.الشهر | في اي شهر نحن الآن
-- -- -- -- -- -- -- -- --
.السنة | في اي سنة نحن الان
-- -- -- -- -- -- -- -- --
.البنك او .بنك | سرعة النت
-- -- -- -- -- -- -- -- --
.ادمن | القنوات الي انت ادمن فيها
-- -- -- -- -- -- -- -- --
.تاك | تستعمل بالرد على رسالتك ويقوم بعمل 100 تاك لأعضاء الكروب
-- -- -- -- -- -- -- -- --
.اشتراكاتي | القنوات والكروبات والأشخاص في حسابك
-- -- -- -- -- -- -- -- --
.التاريخ | التاريخ باليوم والشهر والسنة .
-- -- -- -- -- -- -- -- --
.صور + عدد | يجيب لك صور الشخص حسب العدد بالرد على رسالته
""")
@sedthon.on(events.NewMessage(outgoing=True, pattern=".اوامري"))
async def _(event):
      await event.edit("""- sedthon Userbot .
اوامر السورس :
.فحص | فحص السورس
-- -- -- -- -- -- -- -- --
.مؤقت + وقت + عدد + الجملة | تكرار مؤقت للكلام 
-- -- -- -- -- -- -- -- --
.تكرار + كلام | تكرار لا نهائي للكلام
-- -- -- -- -- -- -- -- --
.خاص + النص \ اذاعة لجميع الاشخاص في حسابك
-- -- -- -- -- -- -- -- --
.ضيف + رابط | ارسل الامر في مجموعتك
-- -- -- -- -- -- -- -- --
.كروب + النص | اذاعة لجميع الكروبات في حسابك
-- -- -- -- -- -- -- -- --
.اسم | اسم وقتي في حسابك !
-- -- -- -- -- -- -- -- --
.بايو | بايو وقتي في حسابك !
-- -- -- -- -- -- -- -- --
.ذاتية | حفظ الصور والفيديوهات ذاتية التدمير
-- -- -- -- -- -- -- -- --
.فك حظر | فك حظر جميع المستخدمين الذين حظرتهم في حسابك
-- -- -- -- -- -- -- -- --
.الوقت | الوقت والتاريخ والخ ..
-- -- -- -- -- -- -- -- --
.اسمي | اسم حسابك
-- -- -- -- -- -- -- -- --
.نبذتي | بايو حسابك
-- -- -- -- -- -- -- -- --
.معرفي | معرف حسابك
-- -- -- -- -- -- -- -- --
.الثواني | الثواني الحالية في هذا اليوم
-- -- -- -- -- -- -- -- --
.اليوم | اليوم الحالي
-- -- -- -- -- -- -- -- --
.تاريخ اليوم | تاريخ اليوم بالشهر
-- -- -- -- -- -- -- -- --
.الشهر | في اي شهر نحن الآن
-- -- -- -- -- -- -- -- --
.السنة | في اي سنة نحن الان
-- -- -- -- -- -- -- -- --
.البنك او .بنك | سرعة النت
-- -- -- -- -- -- -- -- --
.ادمن | القنوات الي انت ادمن فيه
-- -- -- -- -- -- -- -- --
.تاك | تستعمل بالرد على رسالتك ويقوم بعمل 100 تاك لأعضاء الكروب
-- -- -- -- -- -- -- -- --
.اشتراكاتي | القنوات والكروبات والأشخاص في حسابك
-- -- -- -- -- -- -- -- --
.التاريخ | التاريخ باليوم والشهر والسنة .
-- -- -- -- -- -- -- -- --
.صور + عدد | يجيب لك صور الشخص حسب العدد بالرد على رسالته
""")      
@sedthon.on(events.NewMessage(outgoing=True, pattern=".اوامر"))
async def _(event):
      await event.edit("""- sedthon Userbot .
اوامر السورس :
.فحص | فحص السورس
-- -- -- -- -- -- -- -- --
.مؤقت + وقت + عدد + الجملة | تكرار مؤقت للكلام 
-- -- -- -- -- -- -- -- --
.تكرار + كلام | تكرار لا نهائي للكلام
-- -- -- -- -- -- -- -- --
.خاص + النص \ اذاعة لجميع الاشخاص في حسابك
-- -- -- -- -- -- -- -- --
.ضيف + رابط | ارسل الامر في مجموعتك
-- -- -- -- -- -- -- -- --
.كروب + النص | اذاعة لجميع الكروبات في حسابك
-- -- -- -- -- -- -- -- --
.اسم | اسم وقتي في حسابك !
-- -- -- -- -- -- -- -- --
.بايو | بايو وقتي في حسابك !
-- -- -- -- -- -- -- -- --
.ذاتية | حفظ الصور والفيديوهات ذاتية التدمير
-- -- -- -- -- -- -- -- --
.فك حظر | فك حظر جميع المستخدمين الذين حظرتهم في حسابك
-- -- -- -- -- -- -- -- --
.الوقت | الوقت والتاريخ والخ ..
-- -- -- -- -- -- -- -- --
.اسمي | اسم حسابك
-- -- -- -- -- -- -- -- --
.نبذتي | بايو حسابك
-- -- -- -- -- -- -- -- --
.معرفي | معرف حسابك
-- -- -- -- -- -- -- -- --
.الثواني | الثواني الحالية في هذا اليوم
-- -- -- -- -- -- -- -- --
.اليوم | اليوم الحالي
-- -- -- -- -- -- -- -- --
.تاريخ اليوم | تاريخ اليوم بالشهر
-- -- -- -- -- -- -- -- --
.الشهر | في اي شهر نحن الآن
-- -- -- -- -- -- -- -- --
.السنة | في اي سنة نحن الان
-- -- -- -- -- -- -- -- --
.البنك او .بنك | سرعة النت
-- -- -- -- -- -- -- -- --
.ادمن | القنوات الي انت ادمن فيها
-- -- -- -- -- -- -- -- --
.تاك | تستعمل بالرد على رسالتك ويقوم بعمل 100 تاك لأعضاء الكروب
-- -- -- -- -- -- -- -- --
.اشتراكاتي | القنوات والكروبات والأشخاص في حسابك
-- -- -- -- -- -- -- -- --
.التاريخ | التاريخ باليوم والشهر والسنة .
-- -- -- -- -- -- -- -- --
.صور + عدد | يجيب لك صور الشخص حسب العدد بالرد على رسالته
""")
@sedthon.on(events.NewMessage(outgoing=True, pattern=".فحص"))
async def _(event):
      start = datetime.datetime.now()
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
Ok ..
-- -- -- -- -- -- -- -- --"""
)
      end = datetime.datetime.now()
      ms = (end - start).microseconds / 1000
      await event.edit(f"""
- -- -- -- -- -- -- -- --
sedthon Userbot
Python : 3.9
sedthon : 1.2
Ping : `{ms}`
Date : `{m9zpi}`
Id : `{event.sender_id}`
Dev : @Dar4k
Source Ch : @sedthon
-- -- -- -- -- -- -- -- --""")
@sedthon.on(events.NewMessage(outgoing=True, pattern=".سيدثون"))
async def _(event):
      start = datetime.datetime.now()
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
Ok ..
-- -- -- -- -- -- -- -- --"""
)
      end = datetime.datetime.now()
      ms = (end - start).microseconds / 1000
      await event.edit(f"""
- -- -- -- -- -- -- -- --
sedthon Userbot
Python : 3.9
sedthon : 1.2
Ping : `{ms}`
Date : `{m9zpi}`
Id : `{event.sender_id}`
Dev : @Dar4k
Source Ch : @sedthon
-- -- -- -- -- -- -- -- --""")
@sedthon.on(events.NewMessage(outgoing=True, pattern=".التاريخ"))
async def _(event):
      await event.reply(f"""
`-- -- -- -- -- -- -- -- --
التاريخ : {m9zpi}
-- -- -- -- -- -- -- -- --`"""
)

@sedthon.on(events.NewMessage(outgoing=True, pattern=".نبذتي"))
async def _(event):
      await event.reply(f"""
-- -- -- -- -- -- -- -- --
نبذتك : `{bio}`
-- -- -- -- -- -- -- -- --"""
)      
@sedthon.on(events.NewMessage(outgoing=True, pattern=".المطور"))
async def _(event):
      await event.reply(f"""
`-- -- -- -- -- -- -- -- --
- Dark
- Day : {day}
- sedthon Version : 1.2
- Account : @Dar4k
- Source sedthon : @sedthon
-- -- -- -- -- -- -- -- --`"""
) 
@sedthon.on(events.NewMessage(outgoing=True, pattern=".مطور"))
async def _(event):
      await event.reply(f"""
`-- -- -- -- -- -- -- -- --
- Drak
- Day : {day}
- sedthon Version : 1.2
- Account : @Dar4k
- Source sedthon : @sedthon
-- -- -- -- -- -- -- -- --`"""
)     
@sedthon.on(events.NewMessage(outgoing=True, pattern=".المبرمج"))
async def _(event):
      await event.reply(f"""
`-- -- -- -- -- -- -- -- --
- Dark
- Day : {day}
- sedthon Version : 1.2
- Account : @Dar4k
- Source sedthon : @sedthon
-- -- -- -- -- -- -- -- --`"""
)     
@sedthon.on(events.NewMessage(outgoing=True, pattern=".مبرمج"))
async def _(event):
      await event.reply(f"""
-- -- -- -- -- -- -- -- --
- Dark
- Day : {day}
- sedthon Version : 1.2
- Account : @Dar4k
- Source sedthon : @sedthon
-- -- -- -- -- -- -- -- --"""
)     





@sedthon.on(events.NewMessage(outgoing=True, pattern=".نسخ"))
async def _(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        return
    await event.respond(m)




@sedthon.on(events.NewMessage(outgoing=True, pattern=".بنك"))
async def _(event):
      start = datetime.datetime.now()
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
يتم ..
-- -- -- -- -- -- -- -- --"""
)
      end = datetime.datetime.now()
      ms = (end - start).microseconds / 1000
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
- تمت الاستجابة
- البنك : {ms}
-- -- -- -- -- -- -- -- --"""
)


@sedthon.on(events.NewMessage(outgoing=True, pattern=".الثواني"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً مبرمجي !
الثواني الحالية : {sec}
-- -- -- -- -- -- -- -- --"""
)




@sedthon.on(events.NewMessage(outgoing=True, pattern=".السنة"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً مبرمجي !
السنة : {y}
-- -- -- -- -- -- -- -- --"""
)

@sedthon.on(events.NewMessage(outgoing=True, pattern=".الشهر"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً مبرمجي !
الشهر : {m}
-- -- -- -- -- -- -- -- --"""
)

@sedthon.on(events.NewMessage(outgoing=True, pattern=".انشاء (g|c) (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "g":
        try:
            result = await sedthon(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                users=["@GoogleIMGBot"],
                # Not enough users (to create a chat, for example)
                # Telegram, no longer allows creating a chat with ourselves
                title=group_name
            ))
            created_chat_id = result.chats[0].id
            await sedthon(functions.messages.DeleteChatUserRequest(
                chat_id=created_chat_id,
                user_id="@GoogleIMGBot"
            ))
            result = await sedthon(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await event.edit("تم انشاء كروب `{}` بنجاح\nالرابط : {}".format(group_name, result.link))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    elif type_of_group == "g" or type_of_group == "c":
        try:
            r = await sedthon(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                title=group_name,
                about="@sedthon | @sedthonGrpup",
                megagroup=False if type_of_group == "c" else True
            ))
            created_chat_id = r.chats[0].id
            result = await sedthon(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await event.edit("تم انشاء قناة `{}` بنجاح\nالرابط : {}".format(group_name, result.link))
        except Exception as e:
            await event.edit(str(e))
    else:
        await event.edit("Read .helpme to know how to use me")

@sedthon.on(events.NewMessage(outgoing=True, pattern=".تاريخ اليوم"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً مبرمجي !
تاريخ اليوم : {dayy}
-- -- -- -- -- -- -- -- --"""
)

@sedthon.on(events.NewMessage(outgoing=True, pattern=".اليوم"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً مبرمجي !
اليوم : {day}
-- -- -- -- -- -- -- -- --"""
)


@sedthon.on(events.NewMessage(outgoing=True, pattern=".الوقت"))
async def _(event):
      await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً مبرمجي !
السنة : {y}
الشهر : {m}
تاريخ اليوم : {dayy}
اليوم : {day}
الثواني الان : {sec}
-- -- -- -- -- -- -- -- --"""
)


@sedthon.on(events.NewMessage(outgoing=True, pattern=".روسيا"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("روسيا")
    animation_chars = [
        """-- -- -- -- -- -- -- --
⬜⬜⬜⬜⬜
🟦🟦🟦🟦🟦
🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
 ⬜⬜⬜⬜⬜
 🟦🟦🟦🟦🟦
 🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
  ⬜⬜⬜⬜⬜
  🟦🟦🟦🟦🟦
  🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
   ⬜⬜⬜⬜⬜
   🟦🟦🟦🟦🟦
   🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
    ⬜⬜⬜⬜⬜
    🟦🟦🟦🟦🟦
    🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
     ⬜⬜⬜⬜⬜
     🟦🟦🟦🟦🟦
     🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
@sedthon.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
@sedthon.on(events.NewMessage(outgoing=True, pattern=".تهكير"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "جارِ الاتصال بقاعدة البيانات ..",
        "جارِ البحث عن بيانات المستخدم",
        "يتم الاختراق 20%  ●●●○○○○○○○",
        "يتم الاختراق 45%  ●●●●○○○○○○",
        "يتم الاختراق 87%  ●●●●●●●○○○",
        "يتم الاختراق 100% ●●●●●●●●●●",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])
        
@sedthon.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
       "❤️","🖤","💜","🧡","💛","💚","💙"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])
     
@sedthon.on(events.NewMessage(outgoing=True, pattern=".مربعات"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "🟧",
        "🟧🟧",
        "🟧🟧🟧",
        "🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧🟧",
        ".عكس",
        "🟧🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧",
        "🟧🟧🟧",
        "🟧🟧",
        "🟧",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])
@sedthon.on(events.NewMessage(outgoing=True, pattern=".السورس"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "يتم جلب معلومات السورس ..",
        "انتظر قليلاً من فضلك ..",
        "تمت العملية !",
        f"""`حالة السورس : يعمل بنجاح
        اسم السورس : اكسثون | sedthon
        أوامر التسلية : .اكسثون تسلية
        أوامر الحساب : .اكسثون
        اوامر العلم : .علمي
        اوامر الشعر : .ادبي
        قناة السورس : @sedthon
        مطور السورس : @DAR4K""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])
@sedthon.on(events.NewMessage(outgoing=True, pattern=".سورس"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "يتم جلب معلومات السورس ..",
        "انتظر قليلاً من فضلك ..",
        "تمت العملية !",
        f"""`حالة السورس : يعمل بنجاح
        اسم السورس : اكسثون | sedthon
        أوامر التسلية : .تسلية
        أوامر الحساب : .اكسثون
        اوامر العلم : .علمي
        اوامر الشعر : .ادبي
        قناة السورس : @sedthon
        مطور السورس : @DAR4K""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])

@sedthon.on(events.NewMessage(outgoing=True, pattern=".ضيف"))
async def get_users(event):
    legen_ = event.text[10:]
    sedthon_chat = legen_.lower
    restricted = ["@sedthon", "@sedthongroup"]
    sedthon = await event.edit(f"يتم اضافة اعضاء من كروب : {legen_}")
    if sedthon_chat in restricted:
        return await sedthon.edit(
            event, "تريد تخمط اعضائي بسورسي ؟"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await sedthon.edit("انتظر قليلاً ..")
    else:
        await sedthon.edit("انتظر قليلاً ..")
    if event.is_private:
        return await sedthon.edit("لا يمكنك اضافه الاعضاء هناا")
    s = 0
    f = 0
    error = "None"
    await sedthon.edit(
        "يتم جمع معلومات المستخدمين .."
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await sedthon.edit(
                    f"تم الانتهاء من الاضافة ولكن مع وجود بعض الاخطاء\nالخطأ : {error}\nاضافة : {s}\nخطأ باضافة : {f}"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await sedthon(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await sedthon.edit(
                f"تتم الاضافة ..\nاضيف : {s}\nخطأ بأضافة : {f}\nاخر خطأ : {error}"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await sedthon.edit(
        f"اكتملت الإضافة ..\nنجحنا بأضافة : {s}\nخطأ بأضافة : {f}"
    )
async def unblock_users(sedthon):
    @sedthon.on(events.NewMessage(outgoing=True, pattern='.فك حظر'))
    async def _(event):
        list = await sedthon(GetBlockedRequest(offset=0, limit=1000000))
        if len(list.blocked) == 0 :
            razan = await event.edit(f'ليس لديك اي شخص محظور !')
        else :
            unblocked_count = 1
            for user in list.blocked :
                UnBlock = await sedthon(UnblockRequest(id=int(user.peer_id.user_id)))
                unblocked_count += 1
                razan = await event.edit(f'جارِ الغاء الحظر : {round((unblocked_count * 100) / len(list.blocked), 2)}%')
            unblocked_count = 1
            razan = await event.edit(f'تم الغاء حظر : {len(list.blocked)}')
print("- sedthon Userbot Running ..")
sedthon.run_until_disconnected()
loop.create_task(unblock_users(sedthon))
