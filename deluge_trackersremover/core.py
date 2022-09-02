# -*- coding: utf-8 -*-
# Copyright (C) 2022 besuper <16976439+besuper@users.noreply.github.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of TrackersRemover and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from __future__ import unicode_literals

import logging

import deluge.configmanager
from deluge.core.rpcserver import export
from deluge.plugins.pluginbase import CorePluginBase
from twisted.internet.task import LoopingCall
import deluge.core.torrentmanager as torrentmanager
import deluge.component as component
import deluge.core.torrent as torrent

log = logging.getLogger(__name__)

DEFAULT_PREFS = {
    'test': 'NiNiNi'
}


class Core(CorePluginBase):
    def enable(self):
        log.debug("Trackers remover enabled")

        self.config = deluge.configmanager.ConfigManager('trackersremover.conf', DEFAULT_PREFS)
        self.torrent_manager = component.get("TorrentManager")
        self.untracked = []

        self.update_interval = LoopingCall(self.update_)
        self.update_interval.start(1)

    def disable(self):
        self.update_interval.stop()

    def update(self):
        pass

    def update_(self):
        for torrentId in self.torrent_manager.get_torrent_list():
            if torrentId not in self.untracked:
                currentTorrent = self.torrent_manager[torrentId]
                currentState = currentTorrent.state

                if currentState == "Downloading":
                    currentSpeed = currentTorrent.get_eta()

                    if currentSpeed > 10:
                        # Replace trackers by a random tracker
                        currentTorrent.set_trackers([{'url': "udp://tracker.leechers-paradise.org:6969", 'tier': 0}])
                        self.untracked.append(torrentId)

    @export
    def set_config(self, config):
        "sets the config dictionary"
        for key in config.keys():
            self.config[key] = config[key]
        self.config.save()

    @export
    def get_config(self):
        "returns the config dictionary"
        return self.config.config
