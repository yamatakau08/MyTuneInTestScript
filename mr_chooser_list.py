#
# 
#
def find_device(vc,vop,arg):
    vn       = 'mr_chooser_list' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_list_op(vc,vn,vid_type,vop,arg)

#
#
#
def is_mr_chooser_list(vc,vop):
    vn       = 'mr_chooser_list' # vn: view name
    vid_type = VID_TYPE_NAME
    return view_op(vc,vn,vid_type,vop,vpackage=None,debug=False)
    
#
# main screen dispatch
#
def mr_chooser_list(vc,scmd,vop,arg=None): # scmd: screen command

    vc.dump()

    if   scmd == SCMD_DEVICE:
        return find_device(vc,vop,arg)
    elif scmd == SCMD_IS_MR_CHOOSER_LIST:
        return is_mr_chooser_list(vc,vop)
    else:
        return False
