
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

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
    local_envi =[


    ]
            
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        global_envi = [

        ]
        for x in ast.decl:
            temp = self.visit(x,global_envi)
            if isinstance(temp,list):
                global_envi.extend(temp)
            else:
                global_envi.append(temp)
        # print(global_envi)
        return global_envi
        #return [self.visit(x,c) for x in ast.decl]

        # return reduce(lambda x,y: x + self.visit(y,x),ast.decl,c)

    def visitFuncDecl(self,ast, c):
        local_envi = [
                
            ]
        if ast.name.name in c:
            raise Redeclared(Function(),ast.name.name)
        else:
            for x in ast.param:
                temp = self.visit(x,local_envi)
                local_envi.append(temp)
            # print('local_envi = ',local_envi)
            func_envi = (c,local_envi)
            for y in ast.body.member:
                self.visit(y,func_envi)
            return ast.name.name

        #return list(map(lambda x: self.visit(x,(c,True)),ast.body.member)) 

        # if self.lookup(ast.name.name,c,lambda x: x) is None:
        #     return [ast.name.name]
        # else:
        #     raise Redeclared(Function(),ast.name.name)

    def visitVarDecl(self,ast,c):
        if isinstance(c,tuple):
            if self.lookup(ast.variable,c[1],lambda x:x) is not None:
                raise Redeclared(Variable(), ast.variable)
            return ast.variable
        elif ast.variable in c:
            raise Redeclared(Variable(), ast.variable)
        return ast.variable

        # if self.lookup(ast.name,c,lambda x: x) is None:
        #     return [ast.name]
        # else:
        #     return raise Redeclared(Variable(),ast.name)

    def visitId(self,ast,c):
        if self.lookup(ast.name,c[0],lambda x:x) is not None:
            return str('Global (' + ast.name +')')
        elif self.lookup(ast.name,c[1],lambda x:x) is not None:
            return str('Local('+ast.name+')')
        else:
            print(Undeclared(Identifier(),ast.name))
            raise Undeclared(Identifier(),ast.name)


    def visitCallExpr(self, ast, c): 
        pass
        # at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        # res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        # if res is None or not type(res.mtype) is MType:
        #     raise Undeclared(Function(),ast.method.name)
        # elif len(res.mtype.partype) != len(at):
        #     if c[1]:
        #         raise TypeMismatchInStatement(ast)
        #     else:
        #         raise TypeMismatchInExpression(ast)
        # else:
        #     return res.name

    def visitIntLiteral(self,ast, c): 
        return IntType()
    

