from linked_binary_tree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be a string')

        self._add_root(token)

        if left:
            if token not in '+-*/':
                raise ValueError('token must be valid operator')
            self._attach(self.get_root(), left, right)

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.get_root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, res):
        if self.is_leaf(p):
            res.append(str(p.get_element()) + ' ')
        else:
            res.append('( ')
            self._parenthesize_recur(self.get_left_child(p), res)
            res.append(p.get_element() + ' ')
            self._parenthesize_recur(self.get_right_child(p), res)
            res.append(') ')


def build_expression_tree(expr_str):
    expr_stack = []

    tokens = expr_str.split()
    for a_token in tokens:
        if a_token in '+-/*':
            expr_stack.append(a_token)
        elif a_token not in '()':
            expr_stack.append(ExpressionTree(a_token))
        elif a_token == ')':
            right = expr_stack.pop()
            op = expr_stack.pop()
            left = expr_stack.pop()
            expr_stack.append(ExpressionTree(op, left, right))
    return expr_stack.pop()


expression = ' ( 2 + 3 ) '
print(build_expression_tree(expression))
