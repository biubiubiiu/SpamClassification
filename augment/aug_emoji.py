import emoji
import pypinyin

from .base_operation import BaseOperation
from .utils import is_chinese_character


class ToEmoji(BaseOperation):
    """Transform chinese characters to Emoji"""

    def __init__(self):
        super(ToEmoji, self).__init__()
        self.dict = _dict_char2emoji()

    def can_replace(self, s):
        return any(is_chinese_character(c) and pypinyin.lazy_pinyin(c)[0] in self.dict for c in s)

    def transform(self, s):
        chars = list(s)
        for i, c in enumerate(chars):
            chars[i] = self.dict.get(pypinyin.lazy_pinyin(c)[0], c)
        return ''.join(chars)


def _dict_char2emoji():
    return {
        'a': emoji.emojize('🅰'),
        'ai': emoji.emojize('❤'),
        'an': emoji.emojize('🌚'),
        'ang': emoji.emojize('🦖'),
        'ao': emoji.emojize('🇦🇺'),
        'ba': emoji.emojize('🎱'),
        'bai': emoji.emojize('⚪'),
        'ban': emoji.emojize('🦓'),
        'bang': emoji.emojize('👬'),
        'bao': emoji.emojize('👜'),
        'bei': emoji.emojize('🛏'),
        'ben': emoji.emojize('🏃'),
        'beng': emoji.emojize('🗜'),
        'bi': emoji.emojize('🖊'),
        'bian': emoji.emojize('💩'),
        'biao': emoji.emojize('⏲'),
        'bie': emoji.emojize('📎'),
        'bin': emoji.emojize('🍪'),
        'bing': emoji.emojize('🍪'),
        'bo': emoji.emojize('🌊'),
        'bu': emoji.emojize('🙅‍'),
        'ca': emoji.emojize('✖'),
        'cai': emoji.emojize('👎'),
        'can': emoji.emojize('🎇'),
        'cang': emoji.emojize('🐹'),
        'cao': emoji.emojize('🍓'),
        'ce': emoji.emojize('📏'),
        'cen': emoji.emojize('🤲'),
        'ceng': emoji.emojize('🏢'),
        'cha': emoji.emojize('✖'),
        'chai': emoji.emojize('🛠'),
        'chan': emoji.emojize('👋'),
        'chang': emoji.emojize('🏭'),
        'chao': emoji.emojize('🙉'),
        'che': emoji.emojize('🚗'),
        'chen': emoji.emojize('🍊'),
        'cheng': emoji.emojize('🍊'),
        'chi': emoji.emojize('😋'),
        'chong': emoji.emojize('🐛'),
        'chou': emoji.emojize('💩'),
        'chu': emoji.emojize('➗'),
        'chuai': emoji.emojize('🏃‍'),
        'chuan': emoji.emojize('👔'),
        'chuang': emoji.emojize('🛏'),
        'chui': emoji.emojize('🌬'),
        'chun': emoji.emojize('🌼'),
        'chuo': emoji.emojize('👈'),
        'ci': emoji.emojize('🗡'),
        'cong': emoji.emojize('🐛'),
        'cou': emoji.emojize('💩'),
        'cu': emoji.emojize('☠'),
        'cui': emoji.emojize('🔨'),
        'cun': emoji.emojize('📥'),
        'cuo': emoji.emojize('❌'),
        'da': emoji.emojize('🤛'),
        'dai': emoji.emojize('👝'),
        'dan': emoji.emojize('🍳'),
        'dang': emoji.emojize('🔔'),
        'dao': emoji.emojize('🔪'),
        'de': emoji.emojize('🇩🇪'),
        'dei': emoji.emojize('🉐'),
        'den': emoji.emojize('💡'),
        'deng': emoji.emojize('💡'),
        'di': emoji.emojize('👦'),
        'dia': emoji.emojize('😊'),
        'dian': emoji.emojize('⚡'),
        'diao': emoji.emojize('😎'),
        'die': emoji.emojize('👨'),
        'ding': emoji.emojize('⬆'),
        'diu': emoji.emojize('🚮'),
        'dong': emoji.emojize('➡'),
        'dou': emoji.emojize('♒'),
        'du': emoji.emojize('🌡'),
        'duan': emoji.emojize('🛤'),
        'dui': emoji.emojize('✔'),
        'dun': emoji.emojize('🐇'),
        'duo': emoji.emojize('🌸'),
        'e': emoji.emojize('🇷🇺'),
        'ei': emoji.emojize('🤨'),
        'en': emoji.emojize('😐'),
        'eng': emoji.emojize('😐'),
        'er': emoji.emojize('👂'),
        'fa': emoji.emojize('🇫🇷'),
        'fan': emoji.emojize('🍚'),
        'fang': emoji.emojize('⬛'),
        'fei': emoji.emojize('🕊'),
        'fen': emoji.emojize('💩'),
        'feng': emoji.emojize('🌬'),
        'fo': emoji.emojize('🙏'),
        'fou': emoji.emojize('❎'),
        'fu': emoji.emojize('👨'),
        'ga': emoji.emojize('🦆'),
        'gai': emoji.emojize('🌃'),
        'gan': emoji.emojize('✏'),
        'gang': emoji.emojize('❌'),
        'gao': emoji.emojize('⛏'),
        'ge': emoji.emojize('🈹'),
        'gei': emoji.emojize('👨‍❤️‍👨'),
        'gen': emoji.emojize('🌲'),
        'geng': emoji.emojize('🌲'),
        'gong': emoji.emojize('⚔'),
        'gou': emoji.emojize('🐶'),
        'gu': emoji.emojize('🥁'),
        'gua': emoji.emojize('🍉'),
        'guai': emoji.emojize('👹'),
        'guan': emoji.emojize('🍼'),
        'guang': emoji.emojize('💡'),
        'gui': emoji.emojize('🐢'),
        'gun': emoji.emojize('😠'),
        'guo': emoji.emojize('🍎'),
        'ha': emoji.emojize('😄'),
        'hai': emoji.emojize('🌅'),
        'han': emoji.emojize('😓'),
        'hang': emoji.emojize('🛰'),
        'hao': emoji.emojize('👌'),
        'he': emoji.emojize('🈴'),
        'hei': emoji.emojize('🖤'),
        'hen': emoji.emojize('😠'),
        'heng': emoji.emojize('😠'),
        'hong': emoji.emojize('❤'),
        'hou': emoji.emojize('🐵'),
        'hu': emoji.emojize('🐅'),
        'hua': emoji.emojize('🌺'),
        'huai': emoji.emojize('👎'),
        'huan': emoji.emojize('🖇'),
        'huang': emoji.emojize('💛'),
        'hui': emoji.emojize('↩'),
        'hun': emoji.emojize('👻'),
        'huo': emoji.emojize('🔥'),
        'ji': emoji.emojize('🐔'),
        'jia': emoji.emojize('➕'),
        'jian': emoji.emojize('➖'),
        'jiang': emoji.emojize('🏆'),
        'jiao': emoji.emojize('🍌'),
        'jie': emoji.emojize('👧'),
        'jin': emoji.emojize('🈲'),
        'jing': emoji.emojize('🈲'),
        'jiong': emoji.emojize('😳'),
        'jiu': emoji.emojize('9️⃣'),
        'ju': emoji.emojize('🏵'),
        'juan': emoji.emojize('🌯'),
        'jue': emoji.emojize('🐋'),
        'jun': emoji.emojize('💂'),
        'ka': emoji.emojize('💳'),
        'kai': emoji.emojize('🔓'),
        'kan': emoji.emojize('👀'),
        'kang': emoji.emojize('🏥'),
        'kao': emoji.emojize('🐨'),
        'ke': emoji.emojize('🉑'),
        'ken': emoji.emojize('🕳'),
        'keng': emoji.emojize('🕳'),
        'kong': emoji.emojize('🈳'),
        'kou': emoji.emojize('👄'),
        'ku': emoji.emojize('😭'),
        'kua': emoji.emojize('🤸‍'),
        'kuai': emoji.emojize('💨'),
        'kuan': emoji.emojize('💴'),
        'kuang': emoji.emojize('🔲'),
        'kui': emoji.emojize('💸'),
        'kun': emoji.emojize('😴'),
        'kuo': emoji.emojize('➿'),
        'la': emoji.emojize('🌶'),
        'lai': emoji.emojize('👋'),
        'lan': emoji.emojize('💙'),
        'lang': emoji.emojize('🐺'),
        'lao': emoji.emojize('👴'),
        'le': emoji.emojize('😀'),
        'lei': emoji.emojize('😓'),
        'leng': emoji.emojize('❄'),
        'li': emoji.emojize('🍐'),
        'lia': emoji.emojize('👭'),
        'lian': emoji.emojize('🙂'),
        'liang': emoji.emojize('2️⃣'),
        'liao': emoji.emojize('💬'),
        'lie': emoji.emojize('📃'),
        'lin': emoji.emojize('🏕'),
        'ling': emoji.emojize('0️⃣'),
        'liu': emoji.emojize('6️⃣'),
        'long': emoji.emojize('🐉'),
        'lou': emoji.emojize('🏙'),
        'lu': emoji.emojize('🦌'),
        'luan': emoji.emojize('🚯'),
        'lun': emoji.emojize('📃'),
        'luo': emoji.emojize('🔞'),
        'lv': emoji.emojize('💚'),
        'lve': emoji.emojize('⏩'),
        'ma': emoji.emojize('🐴'),
        'mai': emoji.emojize('🎙'),
        'man': emoji.emojize('🈵'),
        'mang': emoji.emojize('😤'),
        'mao': emoji.emojize('🐱'),
        'me': emoji.emojize('❓'),
        'mei': emoji.emojize('🍓'),
        'men': emoji.emojize('🚪'),
        'meng': emoji.emojize('💤'),
        'mi': emoji.emojize('㊙'),
        'mian': emoji.emojize('🍝'),
        'miao': emoji.emojize('🐱'),
        'mie': emoji.emojize('😈'),
        'min': emoji.emojize('💋'),
        'ming': emoji.emojize('🆔'),
        'miu': emoji.emojize('μ'),
        'mo': emoji.emojize('🤟'),
        'mou': emoji.emojize('🐮'),
        'mu': emoji.emojize('🌲'),
        'na': emoji.emojize('👉'),
        'nai': emoji.emojize('🥛'),
        'nan': emoji.emojize('🚹'),
        'nang': emoji.emojize('💊'),
        'nao': emoji.emojize('🧠'),
        'ne': emoji.emojize('❓'),
        'nei': emoji.emojize('↙'),
        'nen': emoji.emojize('🌱'),
        'neng': emoji.emojize('🌱'),
        'ni': emoji.emojize('👉'),
        'nian': emoji.emojize('🗓'),
        'niang': emoji.emojize('👩'),
        'niao': emoji.emojize('🐤'),
        'nie': emoji.emojize('👋'),
        'nin': emoji.emojize('🍋'),
        'ning': emoji.emojize('🍋'),
        'niu': emoji.emojize('🐮'),
        'nong': emoji.emojize('👨‍🌾'),
        'nu': emoji.emojize('😡'),
        'nuan': emoji.emojize('☀'),
        'nuo': emoji.emojize('🍚'),
        'nv': emoji.emojize('🚺'),
        'nue': emoji.emojize('😱'),
        'o': emoji.emojize('😮'),
        'ou': emoji.emojize('🕊'),
        'pa': emoji.emojize('😖'),
        'pai': emoji.emojize('🥧'),
        'pan': emoji.emojize('🍳'),
        'pang': emoji.emojize('🐷'),
        'pao': emoji.emojize('🏃'),
        'pei': emoji.emojize('🔓'),
        'pen': emoji.emojize('🚿'),
        'peng': emoji.emojize('💨'),
        'pi': emoji.emojize('💼'),
        'pian': emoji.emojize('🎴'),
        'piao': emoji.emojize('☁'),
        'pie': emoji.emojize('丿'),
        'pin': emoji.emojize('🍼'),
        'ping': emoji.emojize('🍼'),
        'po': emoji.emojize('🔥'),
        'pou': emoji.emojize('🔪'),
        'pu': emoji.emojize('🍇'),
        'qi': emoji.emojize('7️⃣'),
        'qia': emoji.emojize('👄'),
        'qian': emoji.emojize('💴'),
        'qiang': emoji.emojize('👍'),
        'qiao': emoji.emojize('🌉'),
        'qie': emoji.emojize('🔪'),
        'qin': emoji.emojize('😙'),
        'qing': emoji.emojize('☀'),
        'qiong': emoji.emojize('💸'),
        'qiu': emoji.emojize('🏀'),
        'qu': emoji.emojize('🌫'),
        'quan': emoji.emojize('👊'),
        'que': emoji.emojize('♿'),
        'qun': emoji.emojize('👨‍👦‍👦'),
        'ran': emoji.emojize('🔥'),
        'rang': emoji.emojize('🤬'),
        'rao': emoji.emojize('🔄'),
        're': emoji.emojize('☀'),
        'ren': emoji.emojize('👤'),
        'reng': emoji.emojize('👤'),
        'ri': emoji.emojize('☀'),
        'rong': emoji.emojize('💧'),
        'rou': emoji.emojize('🥩'),
        'ru': emoji.emojize('➡'),
        'ruan': emoji.emojize('🛋'),
        'rui': emoji.emojize('🏵'),
        'run': emoji.emojize('🌧'),
        'ruo': emoji.emojize('🤕'),
        'sa': emoji.emojize('🎊'),
        'sai': emoji.emojize('🆚'),
        'san': emoji.emojize('🌂'),
        'sang': emoji.emojize('☠'),
        'sao': emoji.emojize('📇'),
        'se': emoji.emojize('😍'),
        'sen': emoji.emojize('🏞'),
        'seng': emoji.emojize('🛐'),
        'sha': emoji.emojize('🔪'),
        'shai': emoji.emojize('☀'),
        'shan': emoji.emojize('🗻'),
        'shang': emoji.emojize('⬆'),
        'shao': emoji.emojize('🥄'),
        'she': emoji.emojize('🐍'),
        'shei': emoji.emojize('👥'),
        'shen': emoji.emojize('🈸'),
        'sheng': emoji.emojize('🈸'),
        'shi': emoji.emojize('🔟'),
        'shou': emoji.emojize('✋'),
        'shu': emoji.emojize('📕'),
        'shua': emoji.emojize('🤹‍'),
        'shuai': emoji.emojize('😎'),
        'shuan': emoji.emojize('🔒'),
        'shuang': emoji.emojize('➿'),
        'shui': emoji.emojize('💧'),
        'shun': emoji.emojize('🔜'),
        'shuo': emoji.emojize('💬'),
        'si': emoji.emojize('4️⃣'),
        'song': emoji.emojize('🎁'),
        'sou': emoji.emojize('🔍'),
        'su': emoji.emojize('🏨'),
        'suan': emoji.emojize('🍋'),
        'sui': emoji.emojize('💧'),
        'sun': emoji.emojize('👶'),
        'suo': emoji.emojize('🔒'),
        'ta': emoji.emojize('👦'),
        'tai': emoji.emojize('🇹🇼'),
        'tan': emoji.emojize('🗣'),
        'tang': emoji.emojize('🥣'),
        'tao': emoji.emojize('🍑'),
        'te': emoji.emojize('👋'),
        'tei': emoji.emojize('👋'),
        'teng': emoji.emojize('💢'),
        'ti': emoji.emojize('🏃‍'),
        'tian': emoji.emojize('🌫'),
        'tiao': emoji.emojize('💃'),
        'tie': emoji.emojize('🗒'),
        'ting': emoji.emojize('👂'),
        'tong': emoji.emojize('👦'),
        'tou': emoji.emojize('😶'),
        'tu': emoji.emojize('🤮'),
        'tuan': emoji.emojize('👥'),
        'tui': emoji.emojize('🔙'),
        'tun': emoji.emojize('🐬'),
        'tuo': emoji.emojize('🐫'),
        'wu': emoji.emojize('5️⃣'),
        'wa': emoji.emojize('🐸'),
        'wai': emoji.emojize('↖'),
        'wan': emoji.emojize('🎮'),
        'wang': emoji.emojize('📶'),
        'wei': emoji.emojize('📞'),
        'wen': emoji.emojize('😚'),
        'weng': emoji.emojize('😚'),
        'wo': emoji.emojize('🐌'),
        'xi': emoji.emojize('⬅'),
        'xia': emoji.emojize('↓'),
        'xian': emoji.emojize('🧚‍'),
        'xiang': emoji.emojize('💩'),
        'xiao': emoji.emojize('😀'),
        'xie': emoji.emojize('✍'),
        'xin': emoji.emojize('♥'),
        'xing': emoji.emojize('👌'),
        'xiong': emoji.emojize('🐻'),
        'xiu': emoji.emojize('🛠'),
        'xu': emoji.emojize('🤫'),
        'xuan': emoji.emojize('📢'),
        'xue': emoji.emojize('❄'),
        'xun': emoji.emojize('👎'),
        'ya': emoji.emojize('🦆'),
        'yan': emoji.emojize('👁'),
        'yang': emoji.emojize('🐏'),
        'yao': emoji.emojize('1️⃣'),
        'ye': emoji.emojize('🥥'),
        'yin': emoji.emojize('🎵'),
        'ying': emoji.emojize('🦅'),
        'yong': emoji.emojize('🏊‍'),
        'you': emoji.emojize('→'),
        'yu': emoji.emojize('🐟'),
        'yuan': emoji.emojize('⚪'),
        'yue': emoji.emojize('🈷'),
        'yun': emoji.emojize('😵'),
        'za': emoji.emojize('💣'),
        'zai': emoji.emojize('👶'),
        'zan': emoji.emojize('👍'),
        'zang': emoji.emojize('⚰'),
        'zao': emoji.emojize('🛀'),
        'ze': emoji.emojize('😗'),
        'zei': emoji.emojize('👹'),
        'zen': emoji.emojize('❓'),
        'zeng': emoji.emojize('📈'),
        'zha': emoji.emojize('💣'),
        'zhai': emoji.emojize('🏡'),
        'zhan': emoji.emojize('🚞'),
        'zhang': emoji.emojize('📈'),
        'zhao': emoji.emojize('🔍'),
        'zhe': emoji.emojize('👉'),
        'zhen': emoji.emojize('📌'),
        'zheng': emoji.emojize('➕'),
        'zhi': emoji.emojize('☞'),
        'zhong': emoji.emojize('🀄'),
        'zhou': emoji.emojize('⛵'),
        'zhu': emoji.emojize('🐷'),
        'zhua': emoji.emojize('🖐'),
        'zhuai': emoji.emojize('😎'),
        'zhuan': emoji.emojize('🔄'),
        'zhuang': emoji.emojize('💼'),
        'zhui': emoji.emojize('🏃'),
        'zhun': emoji.emojize('⏲'),
        'zhuo': emoji.emojize('🖐'),
        'zi': emoji.emojize('👶'),
        'zong': emoji.emojize('🀄'),
        'zou': emoji.emojize('🚶'),
        'zu': emoji.emojize('⚰'),
        'zuan': emoji.emojize('💎'),
        'zui': emoji.emojize('👄'),
        'zun': emoji.emojize('🛐'),
        'zuo': emoji.emojize('👈'),
    }
