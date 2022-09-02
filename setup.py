# -*- coding: utf-8 -*-
# Copyright (C) 2022 besuper <16976439+besuper@users.noreply.github.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of TrackersRemover and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from setuptools import find_packages, setup

__plugin_name__ = 'TrackersRemover'
__author__ = 'besuper'
__author_email__ = '16976439+besuper@users.noreply.github.com'
__version__ = '0.1'
__url__ = 'https://github.com/besuper/TrackersRemover'
__license__ = 'GPLv3'
__description__ = 'Automatically remove trackers from torrents'
__long_description__ = """Automatically remove trackers from torrents when download starts"""
__pkg_data__ = {'deluge_'+__plugin_name__.lower(): ['data/*']}

setup(
    name=__plugin_name__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
    long_description=__long_description__,

    packages=find_packages(),
    package_data=__pkg_data__,

    entry_points="""
    [deluge.plugin.core]
    %s = deluge_%s:CorePlugin
    [deluge.plugin.gtk3ui]
    %s = deluge_%s:Gtk3UIPlugin
    [deluge.plugin.web]
    %s = deluge_%s:WebUIPlugin
    """ % ((__plugin_name__, __plugin_name__.lower()) * 3)
)
