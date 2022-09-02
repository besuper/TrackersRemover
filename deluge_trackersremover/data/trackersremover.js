/**
 * Script: trackersremover.js
 *     The client-side javascript code for the TrackersRemover plugin.
 *
 * Copyright:
 *     (C) besuper 2022 <16976439+besuper@users.noreply.github.com>
 *
 *     This file is part of TrackersRemover and is licensed under GNU GPL 3.0, or
 *     later, with the additional special exception to link portions of this
 *     program with the OpenSSL library. See LICENSE for more details.
 */

TrackersRemoverPlugin = Ext.extend(Deluge.Plugin, {
    constructor: function(config) {
        config = Ext.apply({
            name: 'TrackersRemover'
        }, config);
        TrackersRemoverPlugin.superclass.constructor.call(this, config);
    },

    onDisable: function() {
        deluge.preferences.removePage(this.prefsPage);
    },

    onEnable: function() {
        this.prefsPage = deluge.preferences.addPage(
            new Deluge.ux.preferences.TrackersRemoverPage());
    }
});
new TrackersRemoverPlugin();
