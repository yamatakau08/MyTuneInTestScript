#! /usr/bin/env python

import re
import sys
import os
import string
import time

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

from com.dtmilano.android.viewclient import UiDevice
from com.dtmilano.android.viewclient import ViewClient

# the device name which support "Spotify Connect"
TGT_DEVICE_DISPLAY_NAME = 'HT-Z9F'
#TGT_DEVICE_DISPLAY_NAME = 'SRS-ZR7 yama'

execfile('common_lib.py')
execfile('main_content.py')
execfile('mr_chooser_list.py')
execfile('mr_dialog_area.py')

(
# main_content
    SCMD_CAST_ROUTE_MENU_ITEM,
    SCMD_MINI_PLAYER_PLAY_STOP,
# android.widget.ListView tunein.player:id/mr_chooser_list
    SCMD_DEVICE,
    SCMD_IS_MR_CHOOSER_LIST,
# android.widget.LinearLayout tunein.player:id/mr_dialog_area 
    SCMD_STOP_CASTING,
    SCMD_DIALOG_CAST_CONTROL,
    SCMD_IS_MR_DIALOG_AREA,
    SCMD_MR_CLOSE,
) = range(0,8) # (0,X) X: total number of elements

#
# following is main
#
package   = 'tunein.player'
activity  = 'tunein.ui.actvities.TuneInHomeActivity'
component = package + "/" + activity

device, serialno = ViewClient.connectToDeviceOrExit()

if device.isLocked():
    print '[ERROR] Screen is Locked!'
    sys.exit()

# launch app
print 'Start component:"%s"' %component
device.startActivity(component=component)

useuiautomatorhelper = False
vc       = ViewClient(device, serialno,useuiautomatorhelper=useuiautomatorhelper) # vc: ViewClient
uidevice = UiDevice(vc)

# it will fail to set English(United States) "en-rUS" when Language setting is other than "Japanese"
# 
# it will fail to search Language & input when settings in "Japanese"
# languageTo is defined in viewclient.py
# uidevice.changeLanguage(languageTo="en-rUS") # 
# uidevice.openQuickSettingsSettings()

if useuiautomatorhelper:
    vcsleep(2) # workarround to avoid the message "WARNING: xxx not found. Perhaps the device has hardware buttons. "

# sleep 2sec may be better, my smartphone has vc.dump error in next call
vcsleep(2)

# check if mr_chooser_list/mr_dialog_area is opened
ismch = mr_chooser_list(vc,SCMD_IS_MR_CHOOSER_LIST,VOP_EXIST) # ismcl: is mr_chooser_list
ismda = mr_dialog_area(vc,SCMD_IS_MR_DIALOG_AREA,VOP_EXIST)   # ismda: is mr_dialog_area

if   ismch:
    print '[INFO] "mr_chooser_list" is opened'
    print '[INFO] close "mr_chooser_list"'
    device.press('KEYCODE_BACK')
elif ismda:
    print '[INFO] "mr_dialog_area" is opened'
    print '[INFO] close "mr_dialog_area"'
    mr_dialog_area(vc,SCMD_MR_CLOSE,VOP_TOUCH)
else:
    pass

while True:
    print '[INFO] check if "cast_route_menu_item" is enabled'
    ret = main_content(vc,SCMD_CAST_ROUTE_MENU_ITEM,VOP_ENABLED)
    if not ret:
        print '[ERROR] "cast_route_menu_item" is not enabled!'
        # Xperia       Z3(Android v5.0.2) TuneIn Radio v.19.2.1 (230569)
        # second time in this loop, cast_route_menu_item is always be disable
        # Xpeira Table Z2(Android v4.4.2) TuneIn Radio v.16.5(13485)
        # always works fine
        sys.exit()

    print '[INFO] touch "cast_route_menu_item"'
    ret = main_content(vc,SCMD_CAST_ROUTE_MENU_ITEM,VOP_TOUCH)
    if not ret:
        print '[ERROR] failed to toch "cast_route_menu_item"'
        sys.exit()

    if mr_chooser_list(vc,SCMD_IS_MR_CHOOSER_LIST,VOP_EXIST):
        print '[INFO] "mr_chooser_list" is opend!'

        print '[INFO] select "%s" in "mr_chooser_list"' %TGT_DEVICE_DISPLAY_NAME
        debug()
        ret = mr_chooser_list(vc,SCMD_DEVICE,VOP_TOUCH,TGT_DEVICE_DISPLAY_NAME)
        if not ret:
            print '[ERROR] failed to select device "%s" in "mr_choose_list"' %TGT_DEVICE_DISPLAY_NAME
            sys.exit()

        print '[INFO] touch "cast_route_menu_item"'
        ret = main_content(vc,SCMD_CAST_ROUTE_MENU_ITEM,VOP_TOUCH)
        if not ret:
            print '[ERROR] fail touch cast_route_menu_item!'
            sys.exit()

    elif mr_dialog_area(vc,SCMD_IS_MR_DIALOG_AREA,VOP_EXIST): # already in casting
        print '[INFO] "mr_dialog_area" is opend!'
    else:
        print '[ERROR] unknow what dialog is showing!'
        sys.exit()

    print '[INFO] touch "dialog_cast_control" in "mr_dialog_area"'
    ret = mr_dialog_area(vc,SCMD_DIALOG_CAST_CONTROL,VOP_TOUCH)
    if not ret:
        print '[INFO] fail touch "dialog_cast_control"'
        sys.exit()

    vcsleep(15)

    print '[INFO] touch "dialog_cast_control" in "mr_dialog_area"'
    ret = mr_dialog_area(vc,SCMD_DIALOG_CAST_CONTROL,VOP_TOUCH)
    if not ret:
        print '[INFO] fail touch "dialog_cast_control"'
        sys.exit()

    vcsleep(15)

    str = 'stop_casting'
    print '[INFO] touch "%s" in "mr_dialog_area"' %str
    ret = mr_dialog_area(vc,SCMD_STOP_CASTING,VOP_TOUCH)
    if not ret:
        print '[ERROR] failed to touch "%s"!' %str
        sys.exit()

    vcsleep(3)        

if useuiautomatorhelper:
    # to quit appropriately
    # if it's not called the following, command prompt never appear.
    vc.uiAutomatorHelper.quit()
