#
# Wolfinch Auto trading Bot screener
#
#  Copyright: (c) 2017-2021 Joshith Rayaroth Koderi
#  This file is part of Wolfinch.
# 
#  Wolfinch is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  Wolfinch is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with Wolfinch.  If not, see <https://www.gnu.org/licenses/>.

# from decimal import Decimal
from .screener_base import Screener

class VOL_SPIKE(Screener):
    def __init__(self, interval=300):
        super().__init__("VOL_SPIKE", interval)
#         self.name = "VOL_SPIKE"
#         self.interval = interval
    def update(self):
        pass
    def screen(self):
        pass
    def get_screened(self):
        pass

#EOF
