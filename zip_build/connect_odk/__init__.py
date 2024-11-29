# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ConnectODK
                                 A QGIS plugin
 Connects to ODK central to post process data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-11-27
        copyright            : (C) 2024 by Felix Mutua
        email                : mutua@ags.co.ke
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ConnectODK class from file ConnectODK.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .connect_odk import ConnectODK
    return ConnectODK(iface)
