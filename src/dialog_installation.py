# dialog_installation.py
#
# Copyright 2022 Mirko Brombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-only

from gi.repository import Gtk, GObject, Adw


@Gtk.Template(resource_path='/org/vanillaos/ControlCenter/gtk/dialog-installation.ui')
class VanillaDialogInstallation(Adw.Window):
    __gtype_name__ = 'VanillaDialogInstallation'

    progressbar = Gtk.Template.Child()

    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)
        self.set_transient_for(window)
        window.connect('installation-finished', self.on_installation_finished)
        self.__pulse()

    def __pulse(self):
        self.progressbar.pulse()
        GObject.timeout_add(100, self.__pulse)

    def on_installation_finished(self, window, drivers):
        self.destroy()
        