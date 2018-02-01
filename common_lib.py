#
# common lib(function)
#
def printViewsById(vc):
    dict_ids = vc.getViewsById() # getViewsById returns dict type
    for k, v in dict_ids.items():
        print k,dict_ids[k]
    return dict_ids

def vcsleep(sec):
    print 'ViwewClient.sleep(%s)' %sec
    ViewClient.sleep(sec)

def tsleep(sec):
    print 'time.sleep(%s)' %sec
    time.sleep(sec)

def debug():
    import pdb; pdb.set_trace()    

def pick_idno(idstr):
    # idstr assume the following style
    # 'id/no_id/16'
    arr  = idstr.split('/')
    size = len(arr)
    if size > 0 :
        # asuume arr[size-1] the last element is 'no' itself
        if arr[size-1].isdigit():
            return True, int(arr[size-1])
        else:
            return False
    else:
        return False
