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

    def evaluate(self):
        return self._evaluate_recur(self.get_root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.get_element())
        else:
            op = p.get_element()
            l_val = self._evaluate_recur(self.get_left_child(p))
            r_val = self._evaluate_recur(self.get_right_child(p))
            if op == '+':
                return l_val + r_val
            elif op == '-':
                return l_val - r_val
            elif op == '/':
                return l_val / r_val
            else:
                return l_val * r_val


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


# expression = '( 2 + 3 )'
expression = '( ( 2 + 3 ) + 4 )'
expression = '( ( ( 2 + 3 ) + 4 ) * 2 )'

expr_tree = build_expression_tree(expression)
print(expr_tree)
print(expr_tree.evaluate())
