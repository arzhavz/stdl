from .kuso_info import App as KusonimeGUI
from .otds_info import App as OtakudesuGUI
from .smhd_info import App as SamehadakuGUI
from .komik_info import App as KomikuGUI


class Anime:
	Kusonime = KusonimeGUI
	Otakudesu = OtakudesuGUI
	Samehadaku = SamehadakuGUI

class Manga:
	Komiku = KomikuGUI