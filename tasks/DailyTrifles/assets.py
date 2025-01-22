from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class DailyTriflesAssets: 


	# Image Rule Assets
	# description 
	I_L_FRIENDS = RuleImage(roi_front=(67,625,70,72), roi_back=(67,625,70,72), threshold=0.9, method="Template matching", file="./tasks/DailyTrifles/love/love_l_friends.png")
	# description 
	I_L_LOVE = RuleImage(roi_front=(123,625,67,72), roi_back=(123,625,67,72), threshold=0.9, method="Template matching", file="./tasks/DailyTrifles/love/love_l_love.png")
	# 一键收取 
	I_L_COLLECT = RuleImage(roi_front=(47,537,129,56), roi_back=(47,537,129,56), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/love_l_collect.png")
	# 吉闻 
	I_LUCK_MSG = RuleImage(roi_front=(22,47,46,27), roi_back=(22,47,46,27), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/Screenshots_luck_msg.png")
	# 一键祝福 
	I_ONE_CLICK_BLESS = RuleImage(roi_front=(1115,500,93,33), roi_back=(1115,500,93,33), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/Screenshots_one_click_bless.png")
	# 点击祝福 
	I_CLICK_BLESS = RuleImage(roi_front=(617,442,92,39), roi_back=(617,442,92,39), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/Screenshots_click_bless.png")
	# 吉闻页 
	I_LUCK_TITLE = RuleImage(roi_front=(600,52,131,67), roi_back=(600,52,131,67), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/Screenshots_luck_title.png")
	# 好友羁绊提升弹窗 
	I_FRIENDSHIP_UP = RuleImage(roi_front=(1147,80,27,28), roi_back=(1147,80,27,28), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/love/friendship_up.png")


	# Image Rule Assets
	# 礼包屋 
	I_ROOM_GIFT = RuleImage(roi_front=(1152,644,52,53), roi_back=(1127,611,103,94), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_room_gift.png")
	# description 
	I_GIFT_RECOMMEND = RuleImage(roi_front=(1186,98,53,64), roi_back=(1172,83,83,306), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_gift_recommend.png")
	# 免费一抽 
	I_GIFT_SIGN = RuleImage(roi_front=(236,129,306,218), roi_back=(236,129,306,218), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_gift_sign.png")
	# 体力 
	I_SPECIAL_SUSHI = RuleImage(roi_front=(180,130,800,460), roi_back=(180,130,800,460), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_sushi.png")
	# 购买时货币类型为勾玉 
	I_STORE_COST_TYPE_JADE = RuleImage(roi_front=(600,490,50,60), roi_back=(600,490,50,60), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/store/store_cost_type_jade.png")


	# Ocr Rule Assets
	# 商店Special购买体力所需勾玉数量，roiBack为动态调整，故此设置为0，0，0，0 
	O_STORE_SUSHI_PRICE = RuleOcr(roi=(0,0,0,0), area=(0,0,0,0), mode="Digit", method="Default", keyword="", name="store_sushi_price")


	# Image Rule Assets
	# 点击今忆召唤票 
	I_RECALL_TICKET = RuleImage(roi_front=(595,586,65,76), roi_back=(595,586,65,76), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/summonRecall/recall_ticket.png")
	# 今忆召唤单抽 
	I_RECALL_ONE_TICKET = RuleImage(roi_front=(459,604,76,76), roi_back=(459,604,76,76), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/summonRecall/recall_one_ticket.png")
	# description 
	I_RECALL_SM_CONFIRM = RuleImage(roi_front=(424,628,174,61), roi_back=(424,628,174,61), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/summonRecall/recall_sm_confirm.png")
	# 抽到的时候出现的 
	I_SM_CONFIRM_2 = RuleImage(roi_front=(377,630,206,62), roi_back=(377,630,206,62), threshold=0.8, method="Template matching", file="./tasks/DailyTrifles/summonRecall/sm_sm_confirm_2.png")


	# Ocr Rule Assets
	# 今忆抽卡区域 
	O_RECALL_TICKET_AREA = RuleOcr(roi=(590,660,100,32), area=(590,660,100,32), mode="Single", method="Default", keyword="", name="recall_ticket_area")
	# 选择抽卡区域 
	O_SELECT_SM = RuleOcr(roi=(0,0,100,720), area=(0,0,100,720), mode="Single", method="Default", keyword="", name="select_sm")
	# description 
	O_SELECT_SM1 = RuleOcr(roi=(27,130,45,38), area=(27,130,45,38), mode="Single", method="Default", keyword="", name="select_sm1")
	# description 
	O_SELECT_SM2 = RuleOcr(roi=(26,216,45,38), area=(26,216,45,38), mode="Single", method="Default", keyword="", name="select_sm2")
	# description 
	O_SELECT_SM3 = RuleOcr(roi=(26,304,45,38), area=(26,304,45,38), mode="Single", method="Default", keyword="", name="select_sm3")
	# description 
	O_SELECT_SM4 = RuleOcr(roi=(26,397,45,38), area=(26,397,45,38), mode="Single", method="Default", keyword="", name="select_sm4")


