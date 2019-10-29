
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    # Symbol("getInt",MType([],IntType())),
    # Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        globalList = []
        for x in ast.decl:
            temp = self.visit(x,globalList)
            if isinstance(temp,list):
                globalList.extend(temp)
            else:
                globalList.append(temp)
        return globalList
        #return [self.visit(x,c) for x in ast.decl]
        #return reduce(lambda x,y: x + self.visit(y,x),ast.decl,[])
    def visitFuncDecl(self,ast, c):
        if ast.name.name in c:
            raise Redeclared(Function(),ast.name.name)
        else:
            paramList =[]
            for x in ast.param:
                temp = self.visit(x,paramList)
                paramList.append(temp)
            return [ast.name.name ,paramList]
        #return list(map(lambda x: self.visit(x,(c,True)),ast.body.member)) 

        # if self.lookup(ast.name.name,c,lambda x: x): is None:
        #     return [ast.name.name]
        # else:
        #     return raise Redeclared(Function(),ast.name.name)

    def visitVarDecl(self,ast,c):
        if ast.variable in c:
            raise Redeclared(Variable(), ast.variable)
        return ast.variable


        # if self.lookup(ast.name,c,lambda x: x) is None:
        #     return [ast.name]
        # else:
        #     return raise Redeclared(Variable(),ast.name)








    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.name

    def visitIntLiteral(self,ast, c): 
        return IntType()
    

