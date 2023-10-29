def rev(_str):
    _str = _str[::-1]
    return _str
    
def chkPalindrome(_str):
    if(_str != _str[::-1]):
        return False
    return True
