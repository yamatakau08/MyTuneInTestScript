#
# 
#
def find_device(vc,arg,touch=None):

    ATTEMPTS = 4

    vn     = 'mr_chooser_list' # vn: view name
    idlist = package + ":id/" + vn

    # refer AndroidViewClient-13.6.2/src/com/dtmilano/android/viewclient.py line 2045
    for i in range(ATTEMPTS):
        android___id_list = vc.findViewByIdOrRaise(idlist)
        if android___id_list.scrollable():
            view = vc.findViewWithText(arg)
            if view:
                print '"%s" found in "%s"' %(arg,vn)
                if touch:
                    view.touch()
                return True
            else:
                android___id_list.uiScrollable.flingForward()
                vc.sleep(1)
                vc.dump()
        else:
            view = vc.findViewWithText(arg)
            if view:
                print '"%s" found in "%s"' %(arg,vn)
                if touch:
                    view.touch()
                return True
            else:
                print '[ERROR] "%s" not found in "%s"' %(arg,vn)
                return False

    print '[ERROR] "%s" not found in "%s"' %(arg,vn)
    return False

#
#
#
def is_mr_chooser_list(vc):

    vn   = 'mr_chooser_list' # vid: view id
    vid  = package + ":id/" + vn
    view = vc.findViewById(vid)

    if view:
        return True
    else:
        return False
    
#
# main screen dispatch
#
def mr_chooser_list(vc,scmd,arg=None): # scmd: screen command

    vc.dump()

    if scmd == SCMD_FIND_DEVICE:
        return find_device(vc,arg)
    elif scmd == SCMD_SELECT_DEVICE:
        return find_device(vc,arg,touch=True)
    elif scmd == SCMD_IS_MR_CHOOSER_LIST:
        return is_mr_chooser_list(vc)
    else:
        return False

