#
# touch btn_connect
#
def cast_route_menu_item(vc,arg):

    vn   = 'cast_route_menu_item' # vn: view name
    vid  = package + ":id/" + vn
    view = vc.findViewById(vid)

    if view:
        if arg == CAST_ROUTE_MENU_ITEM_TOUCH:
            view.touch()
        elif arg == CAST_ROUTE_MENU_ITEM_ENABLED:
            return view.enabled()
        else:
            pass
        return True
    else:
        print '[ERROR] %s is not found!' %vn
        return False

#
#
#
def mini_player_play_stop(vc):
    vn   = 'mini_player_play_stop' # vn: view name
    vid  = package + ":id/" + vn
    view = vc.findViewById(vid)

    if view:
        view.touch()
        return True
    else:
        print '[ERROR] %s is not found!' %vn
        return False

#
# main screen dispatch
#
def main_content(vc,scmd,arg): # scmd: screen command

    vc.dump()

    if scmd == SCMD_CAST_ROUTE_MENU_ITEM:
        return cast_route_menu_item(vc,arg)
    elif scmd == SCMD_MINI_PLAYER_PLAY_STOP:
        return mini_player_play_stop(vc)
    else:
        return False
