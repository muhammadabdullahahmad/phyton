#!/usr/bin/env python3
"""
Advanced Calculator (CLI) — safe, extensible, and handy for daily use.

Features
- Safe expression evaluator (AST-based, no eval)
- Arithmetic with parentheses and power (**)
- Built-in math functions: sin, cos, tan, asin, acos, atan, log, ln, log10, sqrt, exp,
  factorial, degrees, radians, comb, perm, gcd, lcm, hypot
- Constants: pi, e, tau, inf, nan
- Utility funcs: avg(*xs), sum(*xs), min(*xs), max(*xs), pct(a, b) -> a * b / 100
- Variable assignments: x = 2, rate = pct(15, 240)
- History & variables listing, clearing, saving
- Commands (type :help):
    :help         Show help
    :vars         Show variables
    :hist         Show history
    :clear        Clear variables and history
    :save <file>  Save session (variables + history) to JSON
    :load <file>  Load session (variables + history) from JSON
    :quit         Exit

Usage
$ python advanced_calculator.py
>> 2 + 3 * 4
14
>> x = 10
x = 10
>> sin(pi/2) + log10(100)
3.0
>> :vars
x = 10
>> :hist
1: 2 + 3 * 4 = 14
2: x = 10
3: sin(pi/2) + log10(100) = 3.0

Notes
- Integer division: //, power: **, modulo: %
- Use ln(x) for natural log (alias of log(x)).
- Complex numbers (e.g., 1+2j) are allowed as literals, but math.* functions don't accept complex.
  If you need complex functions, try complex-aware functions exposed under `c_*` (e.g., c_sin) below.
"""
from __future__ import annotations

import ast
import json
import math
import cmath
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

# Whitelisted names (functions & constants)
MATH_FUNCS = {
    # Real-valued math
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'log': math.log,      # natural log
    'ln': math.log,       # alias
    'log10': math.log10,
    'sqrt': math.sqrt,
    'exp': math.exp,
    'factorial': math.factorial,
    'degrees': math.degrees,
    'radians': math.radians,
    'comb': getattr(math, 'comb', None),
    'perm': getattr(math, 'perm', None),
    'gcd': math.gcd,
    'lcm': getattr(math, 'lcm', None),
    'hypot': math.hypot,
}
# Remove None entries for Python versions without those functions
MATH_FUNCS = {k: v for k, v in MATH_FUNCS.items() if v is not None}

# Complex-capable functions (prefixed with c_)
C_MATH_FUNCS = {
    'c_sin': cmath.sin,
    'c_cos': cmath.cos,
    'c_tan': cmath.tan,
    'c_log': cmath.log,  # natural log
    'c_sqrt': cmath.sqrt,
    'c_exp': cmath.exp,
    'c_phase': cmath.phase,
    'c_polar': cmath.polar,
    'c_rect': cmath.rect,
}

UTIL_FUNCS = {
    'avg': lambda *xs: (sum(xs) / len(xs)) if xs else float('nan'),
    'sum': lambda *xs: sum(xs),
    'min': lambda *xs: min(xs),
    'max': lambda *xs: max(xs),
    'pct': lambda a, b: a * b / 100.0,
}

CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
    'tau': math.tau,
    'inf': math.inf,
    'nan': math.nan,
}

ALLOWED_GLOBALS: Dict[str, Any] = {}
ALLOWED_GLOBALS.update(MATH_FUNCS)
ALLOWED_GLOBALS.update(C_MATH_FUNCS)
ALLOWED_GLOBALS.update(UTIL_FUNCS)
ALLOWED_GLOBALS.update(CONSTANTS)

ALLOWED_NODES = (
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Num,       # Py<3.8
    ast.Constant,  # Py>=3.8
    ast.Name,
    ast.Load,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,
    ast.UAdd, ast.USub,
    ast.Call,
    ast.Tuple,
    ast.List,
)

@dataclass
class EvalResult:
    expr: str
    value: Any
    is_assignment: bool = False

class SafeEvaluator:
    def __init__(self, variables: Dict[str, Any] | None = None):
        self.vars: Dict[str, Any] = variables or {}

    def _check_node(self, node: ast.AST) -> None:
        if not isinstance(node, ALLOWED_NODES):
            raise ValueError(f"Unsupported expression element: {type(node).__name__}")
        for child in ast.iter_child_nodes(node):
            self._check_node(child)

    def eval_expr(self, expr: str) -> Any:
        # Parse and validate AST
        try:
            tree = ast.parse(expr, mode='eval')
        except SyntaxError as e:
            raise ValueError(f"Syntax error: {e}") from None
        self._check_node(tree)
        return self._eval(tree.body)

    def _eval(self, node: ast.AST) -> Any:
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            name = node.id
            if name in self.vars:
                return self.vars[name]
            if name in ALLOWED_GLOBALS:
                return ALLOWED_GLOBALS[name]
            raise NameError(f"Unknown name: {name}")
        if isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
            if isinstance(node.op, ast.FloorDiv):
                return left // right
            if isinstance(node.op, ast.Mod):
                return left % right
            if isinstance(node.op, ast.Pow):
                return left ** right
            raise ValueError("Unsupported operator")
        if isinstance(node, ast.UnaryOp):
            operand = self._eval(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +operand
            if isinstance(node.op, ast.USub):
                return -operand
            raise ValueError("Unsupported unary operator")
        if isinstance(node, ast.Tuple):
            return tuple(self._eval(elt) for elt in node.elts)
        if isinstance(node, ast.List):
            return [self._eval(elt) for elt in node.elts]
        if isinstance(node, ast.Call):
            func = self._eval(node.func)
            if callable(func):
                args = [self._eval(a) for a in node.args]
                kwargs = {kw.arg: self._eval(kw.value) for kw in node.keywords}
                return func(*args, **kwargs)
            raise ValueError("Attempted to call non-callable")
        raise ValueError(f"Unsupported node: {type(node).__name__}")


class Calculator:
    def __init__(self) -> None:
        self.evaluator = SafeEvaluator()
        self.history: List[EvalResult] = []

    def assign(self, name: str, expr: str) -> EvalResult:
        name = name.strip()
        if not name.isidentifier():
            raise ValueError("Invalid variable name")
        value = self.evaluator.eval_expr(expr)
        self.evaluator.vars[name] = value
        res = EvalResult(expr=f"{name} = {expr}", value=value, is_assignment=True)
        self.history.append(res)
        return res

    def evaluate(self, expr: str) -> EvalResult:
        value = self.evaluator.eval_expr(expr)
        res = EvalResult(expr=expr, value=value)
        self.history.append(res)
        return res

    def save(self, path: str) -> None:
        data = {
            'variables': self.evaluator.vars,
            'history': [(h.expr, h.value, h.is_assignment) for h in self.history],
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)

    def load(self, path: str) -> None:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.evaluator.vars = data.get('variables', {})
        self.history = [EvalResult(expr=e, value=v, is_assignment=b) for e, v, b in data.get('history', [])]

    def clear(self) -> None:
        self.evaluator.vars.clear()
        self.history.clear()


def print_help() -> None:
    print(__doc__.strip())


def repl() -> None:
    calc = Calculator()
    print("Advanced Calculator — type :help for help. Ctrl+C to exit.")
    while True:
        try:
            line = input('>> ').strip()
            if not line:
                continue
            if line.startswith(':'):
                parts = line.split()
                cmd = parts[0][1:]
                if cmd == 'help':
                    print_help()
                elif cmd == 'vars':
                    if not calc.evaluator.vars:
                        print("(no variables)")
                    else:
                        for k, v in calc.evaluator.vars.items():
                            print(f"{k} = {v}")
                elif cmd == 'hist':
                    if not calc.history:
                        print("(no history)")
                    else:
                        for i, h in enumerate(calc.history, 1):
                            print(f"{i}: {h.expr} = {h.value}")
                elif cmd == 'clear':
                    calc.clear()
                    print("Cleared variables and history.")
                elif cmd == 'save':
                    if len(parts) < 2:
                        print("Usage: :save <file>")
                    else:
                        calc.save(parts[1])
                        print(f"Saved to {parts[1]}")
                elif cmd == 'load':
                    if len(parts) < 2:
                        print("Usage: :load <file>")
                    else:
                        calc.load(parts[1])
                        print(f"Loaded from {parts[1]}")
                elif cmd in ('quit', 'q', 'exit'):
                    print("Bye!")
                    return
                else:
                    print("Unknown command. Type :help")
                continue

            # Assignment support: name = expr (but not equality test)
            if '=' in line and '==' not in line:
                lhs, rhs = line.split('=', 1)
                res = None
                try:
                    res = calc.assign(lhs, rhs)
                    print(f"{lhs.strip()} = {res.value}")
                except Exception as e:
                    print(f"Error: {e}")
                continue

            try:
                res = calc.evaluate(line)
                print(res.value)
            except Exception as e:
                print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nBye!")
            return
        except EOFError:
            print("\nBye!")
            return


if __name__ == '__main__':
    repl()
