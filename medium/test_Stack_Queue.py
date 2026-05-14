import Stack_Queue as SQ
import pytest

def test_MyQue_dequeue_normal():
    que1 = SQ.MyQue(1,[1,2,3],"a",(1,2))
    assert que1.dequeue() == 1
    assert que1.dequeue() == [1,2,3]
    assert que1.dequeue() == "a"
    assert que1.dequeue() == (1,2)

def test_MyQue_dequeue_empty():
    que1 = SQ.MyQue()
    with pytest.raises(IndexError): 
        que1.dequeue()

