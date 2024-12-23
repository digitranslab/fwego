# Generated from FwegoFormula.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FwegoFormula import FwegoFormula
else:
    from FwegoFormula import FwegoFormula

# This class defines a complete generic visitor for a parse tree produced by FwegoFormula.

class FwegoFormulaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FwegoFormula#root.
    def visitRoot(self, ctx:FwegoFormula.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#FieldReference.
    def visitFieldReference(self, ctx:FwegoFormula.FieldReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#StringLiteral.
    def visitStringLiteral(self, ctx:FwegoFormula.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#Brackets.
    def visitBrackets(self, ctx:FwegoFormula.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#BooleanLiteral.
    def visitBooleanLiteral(self, ctx:FwegoFormula.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#RightWhitespaceOrComments.
    def visitRightWhitespaceOrComments(self, ctx:FwegoFormula.RightWhitespaceOrCommentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#DecimalLiteral.
    def visitDecimalLiteral(self, ctx:FwegoFormula.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#LeftWhitespaceOrComments.
    def visitLeftWhitespaceOrComments(self, ctx:FwegoFormula.LeftWhitespaceOrCommentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#FunctionCall.
    def visitFunctionCall(self, ctx:FwegoFormula.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#FieldByIdReference.
    def visitFieldByIdReference(self, ctx:FwegoFormula.FieldByIdReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#LookupFieldReference.
    def visitLookupFieldReference(self, ctx:FwegoFormula.LookupFieldReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#IntegerLiteral.
    def visitIntegerLiteral(self, ctx:FwegoFormula.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#BinaryOp.
    def visitBinaryOp(self, ctx:FwegoFormula.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#ws_or_comment.
    def visitWs_or_comment(self, ctx:FwegoFormula.Ws_or_commentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#func_name.
    def visitFunc_name(self, ctx:FwegoFormula.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#field_reference.
    def visitField_reference(self, ctx:FwegoFormula.Field_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FwegoFormula#identifier.
    def visitIdentifier(self, ctx:FwegoFormula.IdentifierContext):
        return self.visitChildren(ctx)



del FwegoFormula
