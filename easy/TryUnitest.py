import pytest
def add(x,y):
    return x+y
#pytest 自動抓取test開頭
def test_add_normal():
    a=1
    b=2
    assert add(a,b) == 3

def test_add_typeError():
    a = "a"
    b = 2
    #用來驗證程式正確處理異常情況。
    with pytest.raises(TypeError):
        add(a,b)

def test_add_Negative():
    a = -1
    b = -33
    assert add(a,b) == -34