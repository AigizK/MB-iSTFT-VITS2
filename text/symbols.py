'''
Defines the set of symbols used in text input to the model.
'''

'''# japanese_cleaners
_pad        = '_'
_punctuation = ',.!?-'
_letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧ↓↑ '
'''

'''
# japanese_cleaners2
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧʦ↓↑ '
'''

'''
# korean_cleaners
_pad        = '_'
_punctuation = ',.!?…~'
_letters = 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅓㅗㅜㅡㅣㅐㅔ '
'''

'''# chinese_cleaners
_pad        = '_'
_punctuation = '，。！？—…'
_letters = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩˉˊˇˋ˙ '
'''

'''# zh_ja_mixture_cleaners
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'AEINOQUabdefghijklmnoprstuvwyzʃʧʦɯɹəɥ⁼ʰ`→↓↑ '
'''

'''# sanskrit_cleaners
_pad        = '_'
_punctuation = '।'
_letters = 'ँंःअआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहऽािीुूृॄेैोौ्ॠॢ '
'''

'''# cjks_cleaners
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'NQabdefghijklmnopstuvwxyzʃʧʥʦɯɹəɥçɸɾβŋɦː⁼ʰ`^#*=→↓↑ '
'''

'''# thai_cleaners
_pad        = '_'
_punctuation = '.!? '
_letters = 'กขฃคฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลวศษสหฬอฮฯะัาำิีึืุูเแโใไๅๆ็่้๊๋์'
'''

""" default
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'NQabdefghijklmnopstuvwxyzɑæʃʑçɯɪɔɛɹðəɫɥɸʊɾʒθβŋɦ⁼ʰ`^#*=ˈˌ→↓↑ '

_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ" # !
"""

'''# shanghainese_cleaners
_pad        = '_'
_punctuation = ',.!?…'
_letters = 'abdfghiklmnopstuvyzøŋȵɑɔɕəɤɦɪɿʑʔʰ̩̃ᴀᴇ15678 '
'''

'''# chinese_dialect_cleaners
_pad        = '_'
_punctuation = ',.!?~…─'
_letters = '#Nabdefghijklmnoprstuvwxyzæçøŋœȵɐɑɒɓɔɕɗɘəɚɛɜɣɤɦɪɭɯɵɷɸɻɾɿʂʅʊʋʌʏʑʔʦʮʰʷˀː˥˦˧˨˩̥̩̃̚ᴀᴇ↑↓∅ⱼ '
'''

_pad = '_'
# _punctuation = ';:,.!?¡¿—…"«»“” '
_punctuation = ' !+,-.:;?—'
# _letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюяё'
_letters = ''
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
_letters_ipa+="xfmasiyk\"pjzrtdvbne^`uol"

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

import json

config = {
    "phoneme_map": {},
    "phoneme_id_map": {
        "_": [
            0
        ],
        "^": [
            1
        ],
        "$": [
            2
        ],
        " ": [
            3
        ],
        "!": [
            4
        ],
        "'": [
            5
        ],
        "(": [
            6
        ],
        ")": [
            7
        ],
        ",": [
            8
        ],
        "-": [
            9
        ],
        ".": [
            10
        ],
        ":": [
            11
        ],
        ";": [
            12
        ],
        "?": [
            13
        ],
        "a0": [
            14
        ],
        "a1": [
            15
        ],
        "b": [
            16
        ],
        "bj": [
            17
        ],
        "c": [
            18
        ],
        "ch": [
            19
        ],
        "d": [
            20
        ],
        "dj": [
            21
        ],
        "e0": [
            22
        ],
        "e1": [
            23
        ],
        "f": [
            24
        ],
        "fj": [
            25
        ],
        "g": [
            26
        ],
        "gj": [
            27
        ],
        "h": [
            28
        ],
        "hj": [
            29
        ],
        "i0": [
            30
        ],
        "i1": [
            31
        ],
        "j": [
            32
        ],
        "k": [
            33
        ],
        "kj": [
            34
        ],
        "l": [
            35
        ],
        "lj": [
            36
        ],
        "m": [
            37
        ],
        "mj": [
            38
        ],
        "n": [
            39
        ],
        "nj": [
            40
        ],
        "o0": [
            41
        ],
        "o1": [
            42
        ],
        "p": [
            43
        ],
        "pj": [
            44
        ],
        "r": [
            45
        ],
        "rj": [
            46
        ],
        "s": [
            47
        ],
        "sch": [
            48
        ],
        "sh": [
            49
        ],
        "sj": [
            50
        ],
        "t": [
            51
        ],
        "tj": [
            52
        ],
        "u0": [
            53
        ],
        "u1": [
            54
        ],
        "v": [
            55
        ],
        "vj": [
            56
        ],
        "y0": [
            57
        ],
        "y1": [
            58
        ],
        "z": [
            59
        ],
        "zh": [
            60
        ],
        "zj": [
            61
        ],
        "kk": [62],
        "kkj": [63],
        "gg": [64],
        "ggj": [65],
        "th": [66],
        "thj": [67],
        "dh": [68],
        "dhj": [69],
        "hh": [70],
        "hhj": [71],
        "ng": [72],
        "ngj": [73],
        "w": [74],
        "wj": [75],
        "ae0": [76],
        "ae1": [77],
        "oo0": [78],
        "oo1": [79],
        "uu0": [80],
        "uu1": [81]
    },
    "num_symbols": 82,
    "num_speakers": 1,
    "speaker_id_map": {}
}
sorted_by_id = sorted(config["phoneme_id_map"].items(), key=lambda x:x[1])

symbols=[]
for ch,id in sorted_by_id:
    symbols+=[ch]
# Special symbol ids
SPACE_ID = symbols.index(" ")

