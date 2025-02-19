import time

# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey

from module.atom.image import RuleImage

from tasks.GameUi.assets import GameUiAssets
from tasks.GameUi.game_ui import GameUi
from tasks.Component.GeneralBattle.general_battle import GeneralBattle
from tasks.Component.SwitchSoul.switch_soul import SwitchSoul
from tasks.GameUi.page import page_summon, page_town, page_main, page_exploration
from tasks.Pets.assets import PetsAssets
from tasks.base_task import BaseTask
from module.logger import logger

class ScriptTask(GeneralBattle, GameUi, SwitchSoul, PetsAssets, ):

    def run(self):
        for i in range(0, 5):
            # 召唤测试
            self.ui_get_current_page()
            self.ui_goto(page_summon)
            # 探索测试
            self.ui_get_current_page()
            self.ui_goto(page_exploration)
            # 町中测试
            self.ui_get_current_page()
            self.ui_goto(page_town)
            # 宠物屋测试
            self.ui_get_current_page()
            self.ui_goto(page_main)
            self.ui_click(self.I_PET_HOUSE, self.I_PET_CLAW)
            self.ui_click(self.I_PET_EXIT, self.I_CHECK_MAIN)
            # 回到庭院
            self.ui_get_current_page()
            self.ui_goto(page_main)
            time.sleep(1)


if __name__ == '__main__':
    from module.config.config import Config
    from module.device.device import Device

    c = Config('oas1')
    d = Device(c)
    t = ScriptTask(c, d)
    t.run()


