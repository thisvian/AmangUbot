from pyrogram import Client, filters
from Ubot import cmds, app, BOTLOG_CHATID
from Ubot.core import *
from Ubot.logging import LOGGER
from ubotlibs.ubot import Ubot
import os
import sys
from os import environ, execle, path, remove
from .help import add_command_help
add_command_help = add_command_help

ADMINS = [1054295664, 1889573907, 1898065191]

BL_GCAST = [-1001599474353, -1001692751821, -1001473548283, -1001459812644, -1001433238829, -1001476936696, -1001327032795, -1001294181499, -1001419516987, -1001209432070, -1001296934585, -1001481357570, -1001459701099, -1001109837870, -1001485393652, -1001354786862, -1001109500936, -1001387666944, -1001390552926, -1001752592753, -1001777428244, -1001771438298, -1001287188817, -1001812143750, -1001883961446, -1001753840975, -1001896051491, -1001578091827]


BL_UBOT = [-1001812143750]
DEVS = [
  874946835,
  1488093812,
  1720836764,
  1883494460,
  2003295492,
  951454060,
  1646020461,
  910766621,
  1725671304,
  1694909518,
  5876222922,
  1191668125,
  5077932806,
  1897354060,
  1054295664,
  1755047203,
  5063062493,
  1889573907,
  1729700147,
  1898065191,
  1898065191,
  5640938393,
  ]

def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Ubot"])