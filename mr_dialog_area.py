#
# 
#
def stop_casting(vc):
    vt = 'Stop casting' # vt: view text
    view = vc.findViewWithText(vt)

    if view:
        view.touch()
        return True
    else:
        print '[ERROR] Can\'t find "%s" in mr_dialog_area!"' %vt
        return False

#
# 
#
def cast_control(vc):
    vn  = 'dialog_cast_control' # vn: view name
    vid = package + ":id/" + vn
    view = vc.findViewById(vid)

    if view:
        view.touch()
        return True
    else:
        print '[ERROR] %s is not found!' %vn
        return False

#
# 
#
def is_mr_dialog_area(vc):
    vn   = 'mr_dialog_area' # vn: view name
    vid  = package + ":id/" + vn
    view = vc.findViewById(vid)

    if view:
        return True
    else:
        return False

#
#
#
def mr_close(vc):
    vn   = 'mr_close' # vn: view name
    vid  = package + ":id/" + vn
    view = vc.findViewById(vid)

    if view:
        view.touch()
        return True
    else:
        print '[ERROR] Can\'t find "%s" in mr_dialog_area!' %vn
        return False

#
# main screen dispatch
#
def mr_dialog_area(vc,scmd,arg=None): # scmd: screen command

    vc.dump()

    if   scmd == SCMD_STOP_CASTING:
        return stop_casting(vc)
    elif scmd == SCMD_DIALOG_CAST_CONTROL:
        return cast_control(vc)
    elif scmd == SCMD_IS_MR_DIALOG_AREA:
        return is_mr_dialog_area(vc)
    elif scmd == SCMD_MR_CLOSE:
        return mr_close(vc)
    else:
        return False

