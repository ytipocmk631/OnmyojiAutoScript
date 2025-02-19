# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import copy

from module.atom.image import RuleImage
from module.logger import logger

from tasks.Component.Costume.config import (MainType, CostumeConfig, RealmType,
                                            ThemeType, ShikigamiType, SignType, BattleType)
from tasks.Component.Costume.assets import CostumeAssets
from tasks.Component.CostumeRealm.assets import CostumeRealmAssets
from tasks.Component.CostumeBattle.assets import CostumeBattleAssets

from tasks.GameUi.page import page_main, page_exploration, page_summon, page_town
from tasks.GameUi.assets import GameUiAssets as G, GameUiAssets
from tasks.Pets.assets import PetsAssets

# 庭院皮肤
main_costume_model = {
    MainType.COSTUME_MAIN_1: {'I_CHECK_MAIN': 'I_CHECK_MAIN_1',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_1',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_1',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_1',
                              'I_PET_HOUSE': 'I_PET_HOUSE_1', },
    MainType.COSTUME_MAIN_2: {'I_CHECK_MAIN': 'I_CHECK_MAIN_2',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_2',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_2',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_2',
                              'I_PET_HOUSE': 'I_PET_HOUSE_2', },
    MainType.COSTUME_MAIN_3: {'I_CHECK_MAIN': 'I_CHECK_MAIN_3',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_3',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_3',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_3',
                              'I_PET_HOUSE': 'I_PET_HOUSE_3', },
    MainType.COSTUME_MAIN_4: {'I_CHECK_MAIN': 'I_CHECK_MAIN_4',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_4',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_4',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_4',
                              'I_PET_HOUSE': 'I_PET_HOUSE_4', },
    MainType.COSTUME_MAIN_5: {'I_CHECK_MAIN': 'I_CHECK_MAIN_5',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_5',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_5',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_5',
                              'I_PET_HOUSE': 'I_PET_HOUSE_5', },
    MainType.COSTUME_MAIN_6: {'I_CHECK_MAIN': 'I_CHECK_MAIN_6',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_6',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_6',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_6',
                              'I_PET_HOUSE': 'I_PET_HOUSE_6', },
    MainType.COSTUME_MAIN_7: {'I_CHECK_MAIN': 'I_CHECK_MAIN_7',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_7',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_7',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_7',
                              'I_PET_HOUSE': 'I_PET_HOUSE_7', },
    MainType.COSTUME_MAIN_8: {'I_CHECK_MAIN': 'I_CHECK_MAIN_8',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_8',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_8',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_8',
                              'I_PET_HOUSE': 'I_PET_HOUSE_8', },
    MainType.COSTUME_MAIN_9: {'I_CHECK_MAIN': 'I_CHECK_MAIN_9',
                              'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_9',
                              'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_9',
                              'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_9',
                              'I_PET_HOUSE': 'I_PET_HOUSE_9', },
    MainType.COSTUME_MAIN_10: {'I_CHECK_MAIN': 'I_CHECK_MAIN_10',
                               'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_10',
                               'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_10',
                               'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_10',
                               'I_PET_HOUSE': 'I_PET_HOUSE_10', },
    MainType.COSTUME_MAIN_11: {'I_CHECK_MAIN': 'I_CHECK_MAIN_11',
                               'I_MAIN_GOTO_EXPLORATION': 'I_MAIN_GOTO_EXPLORATION_11',
                               'I_MAIN_GOTO_SUMMON': 'I_MAIN_GOTO_SUMMON_11',
                               'I_MAIN_GOTO_TOWN': 'I_MAIN_GOTO_TOWN_11',
                               'I_PET_HOUSE': 'I_PET_HOUSE_11', },
}

# 结界皮肤
realm_costume_model = {
    RealmType.COSTUME_REALM_1: {'I_SHI_CARD': 'I_SHI_CARD_1',
                                'I_SHI_DEFENSE': 'I_SHI_DEFENSE_1',},
    RealmType.COSTUME_REALM_2: {'I_SHI_CARD': 'I_SHI_CARD_2',
                                'I_SHI_DEFENSE': 'I_SHI_DEFENSE_2',
                                'I_SHI_GROWN': 'I_SHI_GROWN_2',
                                'I_BOX_AP': 'I_BOX_AP_2',
                                'I_BOX_EXP': 'I_BOX_EXP_2'},
}

# 战斗主题
battle_theme_model = {
    BattleType.COSTUME_BATTLE_1: {
        'I_LOCAL': 'I_LOCAL_1',
        'I_EXIT': 'I_EXIT_1',
        'I_FRIENDS': 'I_FRIENDS_1',
    },
    BattleType.COSTUME_BATTLE_2: {
        'I_LOCAL': 'I_LOCAL_2',
        'I_EXIT': 'I_EXIT_2',
        'I_FRIENDS': 'I_FRIENDS_2',
    },
    BattleType.COSTUME_BATTLE_3: {
        'I_LOCAL': 'I_LOCAL_3',
        'I_EXIT': 'I_EXIT_3',
        'I_FRIENDS': 'I_FRIENDS_3',
    },
    BattleType.COSTUME_BATTLE_4: {
        'I_LOCAL': 'I_LOCAL_4',
        'I_EXIT': 'I_EXIT_4',
        'I_FRIENDS': 'I_FRIENDS_4',
    },
    BattleType.COSTUME_BATTLE_5: {
        'I_LOCAL': 'I_LOCAL_5',
        'I_EXIT': 'I_EXIT_5',
        'I_FRIENDS': 'I_FRIENDS_5',
    },
    BattleType.COSTUME_BATTLE_6: {
        'I_LOCAL': 'I_LOCAL_6',
        'I_EXIT': 'I_EXIT_6',
        'I_FRIENDS': 'I_FRIENDS_6',
    },
    BattleType.COSTUME_BATTLE_7: {
        'I_LOCAL': 'I_LOCAL_7',
        'I_EXIT': 'I_EXIT_7',
        'I_FRIENDS': 'I_FRIENDS_7',
    },
    BattleType.COSTUME_BATTLE_8: {
        'I_LOCAL': 'I_LOCAL_8',
        'I_EXIT': 'I_EXIT_8',
        'I_FRIENDS': 'I_FRIENDS_8',
        'I_WIN': 'I_WIN_8',
        'I_DE_WIN': 'I_DE_WIN_8',
        'I_FALSE': 'I_FALSE_8',
    },
    BattleType.COSTUME_BATTLE_9: {
        'I_LOCAL': 'I_LOCAL_9',
        'I_EXIT': 'I_EXIT_9',
        'I_FRIENDS': 'I_FRIENDS_9',
    },
}


class CostumeBase:

    def check_costume(self, config: CostumeConfig=None):
        if config is None:
            config: CostumeConfig = self.config.model.global_game.costume_config
        self.check_costume_main(config.costume_main_type)
        self.check_costume_realm(config.costume_realm_type)
        self.check_costume_battle(config.costume_battle_type)

    def replace_img(self,
                    asset_before: str,
                    asset_after: RuleImage,
                    rp_roi_back: bool = True):
        if not hasattr(self, asset_before):
            return
        # setattr(self, asset_before, asset_after)
        asset_before_object: RuleImage = copy.deepcopy(getattr(self, asset_before))
        asset_before_object.roi_front = asset_after.roi_front
        if rp_roi_back:
            asset_before_object.roi_back = asset_after.roi_back
        asset_before_object.threshold = asset_after.threshold
        asset_before_object.file = asset_after.file
    def flush_costume_check_btn(self,main_type,btn_type,assert_val):
        """
        刷新用于图像匹配的主题按钮
        """
        if main_type == MainType.COSTUME_MAIN:
            # 默认主题
            # Main Home 主页
            page_main.set_check_button(G.I_CHECK_MAIN)
            self.I_CHECK_MAIN = G.I_CHECK_MAIN
            # 召唤summon
            page_main.link(button=G.I_MAIN_GOTO_SUMMON, destination=page_summon)
            # 探索exploration
            page_main.link(button=G.I_MAIN_GOTO_EXPLORATION, destination=page_exploration)
            # 町中town
            page_main.link(button=G.I_MAIN_GOTO_TOWN, destination=page_town)
            # 宠物屋
            self.I_PET_HOUSE = PetsAssets.I_PET_HOUSE


            # print('默认按钮替换')
        else:
            # 自定义主题
            # switch main costume to main_type
            if btn_type == 'I_CHECK_MAIN':
                page_main.set_check_button(assert_val)
                self.I_CHECK_MAIN = assert_val
            elif btn_type =='I_MAIN_GOTO_EXPLORATION':
                page_main.link(button=assert_val, destination=page_exploration)
            elif btn_type == 'I_MAIN_GOTO_SUMMON':
                page_main.link(button=assert_val, destination=page_summon)
            elif btn_type=='I_MAIN_GOTO_TOWN':
                page_main.link(button=assert_val, destination=page_town)
            elif btn_type=='I_PET_HOUSE':
                self.I_PET_HOUSE = assert_val
    def check_costume_main(self, main_type: MainType):
        logger.info(f'Switch main costume to {main_type}')
        if main_type == MainType.COSTUME_MAIN:
            self.flush_costume_check_btn(main_type,'',None)
            return

        costume_assets = CostumeAssets()
        for key, value in main_costume_model[main_type].items():
            assert_value: RuleImage = getattr(costume_assets, value)
            self.replace_img(key, assert_value)
            self.flush_costume_check_btn(main_type,key,assert_value)

    def check_costume_realm(self, realm_type: RealmType):
        if realm_type == RealmType.COSTUME_REALM_DEFAULT:
            return
        logger.info(f'Switch realm theme {realm_type}')
        costume_realm_assets = CostumeRealmAssets()
        for key, value in realm_costume_model[realm_type].items():
            assert_value: RuleImage = getattr(costume_realm_assets, value)
            self.replace_img(key, assert_value)

    def check_costume_battle(self, battle_type: BattleType):
        if battle_type == BattleType.COSTUME_BATTLE_DEFAULT:
            return
        logger.info(f'Switch battle theme {battle_type}')
        costume_battle_assets = CostumeBattleAssets()
        for key, value in battle_theme_model[battle_type].items():
            assert_value: RuleImage = getattr(costume_battle_assets, value)
            # 绿标的坐标点范围不变
            if key == 'I_LOCAL':
                self.replace_img(key, assert_value, rp_roi_back=False)
            else:
                self.replace_img(key, assert_value)

    def refresh_costume(self):
        """
        用于刷新庭院皮肤
        """
        cos = CostumeAssets()
        # 获取cos里的所有属性
        self.screenshot()
        key = '_check_main_'.upper()
        main_type = MainType.COSTUME_MAIN
        for i in dir(cos):
            if key in i:
                rule_img: RuleImage = getattr(cos, i)
                res = self.appear(target=rule_img, interval=1)
                if res:
                    temp = i.split('_')
                    temp = 'COSTUME_MAIN_' + temp[-1]
                    main_type = MainType[temp]
                    break
        self.config.global_game.costume_config.costume_main_type = main_type
        self.check_costume_main(main_type=main_type)

if __name__ == '__main__':
    c = CostumeBase()
    c.check_costume_main(MainType.COSTUME_MAIN_2)
