import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.keys import KC


keyboard = KMKKeyboard()

macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules.append(macros)
keyboard.modules = [layers, holdtap, encoder_handler]

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3,)
keyboard.row_pins = (board.D4, board.D5,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.Macro(Press(KC.LCTL), Tap(KC.A), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.X), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.C), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.V), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.Z), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.Y), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.F), Release(KC.LCTL)),
     KC.Macro(Press(KC.LCTL), Tap(KC.S), Release(KC.LCTL)),
     ]
]


encoder_handler.pins = (
    (board.D10, board.D9, None,), 
    (board.D8, board.D7, None,),
    )

if __name__ == '__main__':
    keyboard.go()