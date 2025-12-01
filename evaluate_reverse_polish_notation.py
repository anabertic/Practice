class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        stack = []
        for i in range(0,len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(operand1+operand2)
                if tokens[i] == '-':
                    stack.append(operand2-operand1)
                if tokens[i] == '*':
                    stack.append(operand1*operand2)
                if tokens[i] == '/':
                    stack.append(operand2/operand1)
        return int(stack.pop())
            
