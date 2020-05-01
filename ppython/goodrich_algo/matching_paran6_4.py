from ppython.goodrich_algo.stack.array_stack import ArrayStack


def is_matched(expr):
    st = ArrayStack()
    open_b = '([{'
    close_b = '}])'
    # <!note><!better> good way to match other bracket
    matching_p = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    for ch in expr:
        if ch in open_b:
            st.push(ch)
        elif ch in close_b:
            if st.is_empty():
                return False
            if matching_p[st.pop()] != ch:
                return False
    if not st.is_empty():
        return False
    else:
        return True


if __name__ == '__main__':
    print(is_matched('(3 + 4) - 2'))
    print(is_matched('((3 + 4) - 2'))
