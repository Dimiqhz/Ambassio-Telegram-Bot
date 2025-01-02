import asyncio
import logging
import sys
import yaml

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

##################
# Main functions #
##################

def config_manager(mv):
    match mv:
        case "gettoken":
            with open("config.yaml", "r") as cfg:
                data = yaml.safe_load(cfg)
                return data

######################
# Get main variables #
######################

token = config_manager("gettoken")
dp = Dispatcher()
router = Router()