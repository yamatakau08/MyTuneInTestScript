#
# touch btn_connect
#
def cast_route_menu_item(vc,vop):
    vn       = 'cast_route_menu_item' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_op(vc,vn,vid_type,vop)

#
#
#
def mini_player_play_stop(vc,vop):
    vn       = 'mini_player_play_stop' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_op(vc,vn,vid_type,vop)

#
# main screen dispatch
#
def main_content(vc,scmd,vop): # scmd: screen command

    vc.dump()

    if scmd == SCMD_CAST_ROUTE_MENU_ITEM:
        return cast_route_menu_item(vc,vop)
    elif scmd == SCMD_MINI_PLAYER_PLAY_STOP:
        return mini_player_play_stop(vc,vop)
    else:
        return False
