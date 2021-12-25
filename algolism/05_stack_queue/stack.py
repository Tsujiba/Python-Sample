"""
stack_quiz
JSONのフォーマットを正せ
Input：{'Key1':'value1', 'key2':[1, 2, 3], 'key3':(1, 2, 3)} Output True
"""

def validate_format(chars: str) -> bool:
    stack = []
    target_set_push = ('{', '[', '(' )
    for char in chars:
        if char in target_set_push:
            stack.append(char)
        elif char == '}':
            if not stack:
                return False
            pop_char = stack.pop()
            if pop_char != '{':
                return False
        elif char == ']':
            if not stack:
                return False
            pop_char = stack.pop()
            if pop_char != '[':
                return False
        elif char == ')':
            if not stack:
                return False
            pop_char = stack.pop()
            if pop_char != '(':
                return False
        
    if len(stack) != 0:
        return False
    else:
        return True

if __name__ == '__main__':
    json_char = "]'Key1':'value1', 'key2':[1, 2, 3], 'key3':(1, 2, 3)}"
    print(validate_format(json_char))
        
        