'''
    Altspell  Soundspel plugin for altspell.
    Copyright (C) 2024  Nicholas Johnson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from altspell.plugin import PluginBase
from .convert import Converter


class Plugin(PluginBase):
    def __init__(self):
        self._fwd_converter = Converter(fwd=True)
        self._rev_converter = Converter(fwd=False)

    def convert_to_altspell(self, tradspell_text: str) -> str:
        return self._fwd_converter.convert_para(tradspell_text)

    def convert_to_tradspell(self, altspell_text: str) -> str:
        return self._rev_converter.convert_para(altspell_text)
