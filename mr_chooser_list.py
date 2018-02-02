#
# 
#
def find_device(vc,vop,arg):

    ATTEMPTS = 4

    vn     = 'mr_chooser_list' # vn: view name
    idlist = package + ":id/" + vn
    view   = None

    # refer AndroidViewClient-13.6.2/src/com/dtmilano/android/viewclient.py line 2045
    for i in range(ATTEMPTS):
        android___id_list = vc.findViewByIdOrRaise(idlist)
        if android___id_list.scrollable():
            view = vc.findViewWithText(arg)
            if view:
                break
            else:
                android___id_list.uiScrollable.flingForward()
                vc.sleep(1)
                vc.dump()
        else:
            view = vc.findViewWithText(arg)
            if view:
                break

   if view:
       print '[INFO] "%s" found in "%s"' %(arg,vn)
       if vop == VOP_TOUCH:
           view.touch()
       else:
           print '[ERROR] vop:"%s" is not supported in find_device()!' %(vop)
       return True
   else:
       print '[ERROR] "%s" not found in "%s"' %(arg,vn)
       return False

#
#
#
def is_mr_chooser_list(vc,vop,debug=True):
    vn       = 'mr_chooser_list' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_op(vc,vn,vid_type,vop,debug)

    
#
# main screen dispatch
#
def mr_chooser_list(vc,scmd,vop,arg=None): # scmd: screen command

    vc.dump()

    if   scmd == SCMD_DEVICE:
        return find_device(vc,vop,arg)
    elif scmd == SCMD_IS_MR_CHOOSER_LIST:
        return is_mr_chooser_list(vc,vop,debug=False)
    else:
        return False

