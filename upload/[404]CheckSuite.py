import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    #400
    def test_redeclared_function_FloatType(self):
        """Simple program: int main() {} """
        input = Program([
                    VarDecl("a",IntType()),
                    VarDecl("d",IntType()),
                    FuncDecl(Id("foo"),[VarDecl("a",FloatType()),VarDecl("c",IntType())],
                        FloatType(),Block([])),
                    VarDecl("b",IntType()),
                    VarDecl("c",FloatType())
                    ])
        expect = "['a', 'd', 'foo', ['a', 'c'], 'b', 'c']"
        self.assertTrue(TestChecker.test(input,expect,400))
    #401
    def test_redeclared_function_StringType(self):
        """More complex program"""
        input = Program([
                    VarDecl("a",BoolType()),
                    VarDecl("a",IntType()),
                    FuncDecl(Id("a"),[],StringType(),Block([])),
                    VarDecl("c",FloatType())
                    ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))
    #402
    def test_redeclared_var_IntType(self):
        """More complex program"""
        input = Program([
                    VarDecl("a",IntType()),
                    VarDecl("a",IntType()),
                    VarDecl("c",FloatType()),
                    FuncDecl(Id("Intlit"),[],IntType(),Block([]))
                    ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))


    #403
    def test_complete_global_decl(self):
        """Simple program: int main() {} """
        input = Program([
                    VarDecl("a",IntType()),
                    FuncDecl(Id("main"),[],IntType(),Block([])),
                    VarDecl("b",BoolType()),
                    VarDecl("c",StringType())
                    ])
        expect = str(['a', 'main', [], 'b', 'c'])
        self.assertTrue(TestChecker.test(input,expect,403))
    #404
    def test_complete_global_decl_1(self):
        """More complex program"""
        input = Program([
                    VarDecl("a",FloatType()),
                    FuncDecl(Id("main"),[],IntType(),Block([])),
                    VarDecl("b",StringType()),
                    VarDecl("c",BoolType())
                    ])
        expect = str(['a', 'main', [], 'b', 'c'])
        self.assertTrue(TestChecker.test(input,expect,404))
    #405
    def test_redeclared_var_BoolType(self):
        """More complex program"""
        input = Program([
                    VarDecl("a",IntType()),
                    FuncDecl(Id("main"),[],IntType(),Block([])),
                    VarDecl("a",BoolType()),
                    VarDecl("c",FloatType())
                    ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))
    