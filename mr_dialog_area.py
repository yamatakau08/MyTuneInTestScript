#
# 
#
def stop_casting(vc,vop):
    ''' # language: en
    vt       = 'Stop casting' # vt: view text
    vid_type = VID_TYPE_TEXT
    return view_op(vc,vt,vid_type,vop)
    '''
    vn       = 'button1' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_op(vc,vn,vid_type,vop,vpackage='android')

#
# 
#
def cast_control(vc,vop):
    vn       = 'dialog_cast_control' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_op(vc,vn,vid_type,vop)

#
# 
#
def is_mr_dialog_area(vc,vop):
    vn       = 'mr_dialog_area' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_op(vc,vn,vid_type,vop,vpackage=None,debug=False)

#
#
#
def mr_close(vc,vop):
    vn       = 'mr_close' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_op(vc,vn,vid_type,vop)

#
# main screen dispatch
#
def mr_dialog_area(vc,scmd,vop,arg=None): # scmd: screen command

    vc.dump()

    if   scmd == SCMD_STOP_CASTING:
        return stop_casting(vc,vop)
    elif scmd == SCMD_DIALOG_CAST_CONTROL:
        return cast_control(vc,vop)
    elif scmd == SCMD_IS_MR_DIALOG_AREA:
        return is_mr_dialog_area(vc,vop)
    elif scmd == SCMD_MR_CLOSE:
        return mr_close(vc,vop)
    else:
        return False
