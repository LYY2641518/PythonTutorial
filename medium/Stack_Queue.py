# 13
# 寫一個 class：
# class Stack:
# 支援 push / pop / peek / size
# （用 Python list 實作，但封裝起來）
class Stack:
    def __init__(self,*arg):
        self.m_Stack1 =[]
        for ele in arg:
            self.m_Stack1.append(ele)
            
    def push(self,new_element):
        self.m_Stack1.append(new_element)
    def pop(self):
        try:
            return self.m_Stack1.pop()
        except IndexError:
            raise IndexError
    def peek(self):
        return self.m_Stack1[-1]
    def size(self):
        return len(self.m_Stack1)
    def __str__(self):
        return self.m_Stack1.__str__()
    def __len__(self):
        return self.size()

#兩個 Stack 實作 Queue
#行為模式 
# SetStack 負責enqueue存入
# GetStack 反轉SetStack的順序後存入,所以最外面會是SetStack的最裡面 
class MyQue:
    def __init__(self,*arg):
        self.m_SetStack = Stack()
        self.m_GetStack = Stack()
        for ele in arg:
            self.m_SetStack.push(ele)
    def enqueue(self,*arg):
        # 將元素加入 Queue（尾端）
        # 直接放入SetStack
        for ele in arg:
            self.m_SetStack.push(ele)
    def revers_stack(self):
        while self.m_SetStack.size()>0 :
            ele = self.m_SetStack.pop()
            self.m_GetStack.push(ele)

    def dequeue(self):  
    # 移除並回傳 Queue 最前面的元素
    # 如果GetStack為空 則反轉SetStack給GetStack
        if self.m_GetStack.size()== 0:
            self.revers_stack()
        if self.m_GetStack.size()== 0:
            raise IndexError("pop empty Queue")
        return self.m_GetStack.pop()
    # 回傳最前面的元素（不移除）
    def peek(self):
        if self.m_GetStack.size() == 0:
            self.revers_stack()
        if self.m_GetStack.size()== 0:
            raise IndexError("peek empty Queue")
        return self.m_GetStack.peek()

    # 回傳目前元素數量
    def size(self):
        return len(self.m_GetStack)+len(self.m_SetStack)
    def __str__(self):
        return str(self.m_GetStack.m_Stack1[::-1])+str(self.m_SetStack.m_Stack1)

