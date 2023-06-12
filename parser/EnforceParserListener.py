# Generated from EnforceParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .EnforceParser import EnforceParser
else:
    from EnforceParser import EnforceParser

# This class defines a complete listener for a parse tree produced by EnforceParser.
class EnforceParserListener(ParseTreeListener):

    # Enter a parse tree produced by EnforceParser#computationalStart.
    def enterComputationalStart(self, ctx:EnforceParser.ComputationalStartContext):
        pass

    # Exit a parse tree produced by EnforceParser#computationalStart.
    def exitComputationalStart(self, ctx:EnforceParser.ComputationalStartContext):
        pass


    # Enter a parse tree produced by EnforceParser#globalDeclaration.
    def enterGlobalDeclaration(self, ctx:EnforceParser.GlobalDeclarationContext):
        pass

    # Exit a parse tree produced by EnforceParser#globalDeclaration.
    def exitGlobalDeclaration(self, ctx:EnforceParser.GlobalDeclarationContext):
        pass


    # Enter a parse tree produced by EnforceParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:EnforceParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by EnforceParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:EnforceParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by EnforceParser#varAndFunctionBlock.
    def enterVarAndFunctionBlock(self, ctx:EnforceParser.VarAndFunctionBlockContext):
        pass

    # Exit a parse tree produced by EnforceParser#varAndFunctionBlock.
    def exitVarAndFunctionBlock(self, ctx:EnforceParser.VarAndFunctionBlockContext):
        pass


    # Enter a parse tree produced by EnforceParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:EnforceParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by EnforceParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:EnforceParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by EnforceParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:EnforceParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by EnforceParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:EnforceParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by EnforceParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:EnforceParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by EnforceParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:EnforceParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by EnforceParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:EnforceParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by EnforceParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:EnforceParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by EnforceParser#functionParameters.
    def enterFunctionParameters(self, ctx:EnforceParser.FunctionParametersContext):
        pass

    # Exit a parse tree produced by EnforceParser#functionParameters.
    def exitFunctionParameters(self, ctx:EnforceParser.FunctionParametersContext):
        pass


    # Enter a parse tree produced by EnforceParser#functionParameter.
    def enterFunctionParameter(self, ctx:EnforceParser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by EnforceParser#functionParameter.
    def exitFunctionParameter(self, ctx:EnforceParser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by EnforceParser#classDeclaration.
    def enterClassDeclaration(self, ctx:EnforceParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by EnforceParser#classDeclaration.
    def exitClassDeclaration(self, ctx:EnforceParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by EnforceParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:EnforceParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by EnforceParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:EnforceParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by EnforceParser#enumBody.
    def enterEnumBody(self, ctx:EnforceParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by EnforceParser#enumBody.
    def exitEnumBody(self, ctx:EnforceParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by EnforceParser#enumValue.
    def enterEnumValue(self, ctx:EnforceParser.EnumValueContext):
        pass

    # Exit a parse tree produced by EnforceParser#enumValue.
    def exitEnumValue(self, ctx:EnforceParser.EnumValueContext):
        pass


    # Enter a parse tree produced by EnforceParser#expression.
    def enterExpression(self, ctx:EnforceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by EnforceParser#expression.
    def exitExpression(self, ctx:EnforceParser.ExpressionContext):
        pass


    # Enter a parse tree produced by EnforceParser#castExpression.
    def enterCastExpression(self, ctx:EnforceParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by EnforceParser#castExpression.
    def exitCastExpression(self, ctx:EnforceParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by EnforceParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:EnforceParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by EnforceParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:EnforceParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by EnforceParser#objectCreation.
    def enterObjectCreation(self, ctx:EnforceParser.ObjectCreationContext):
        pass

    # Exit a parse tree produced by EnforceParser#objectCreation.
    def exitObjectCreation(self, ctx:EnforceParser.ObjectCreationContext):
        pass


    # Enter a parse tree produced by EnforceParser#functionCall.
    def enterFunctionCall(self, ctx:EnforceParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by EnforceParser#functionCall.
    def exitFunctionCall(self, ctx:EnforceParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by EnforceParser#parenthesisedExpression.
    def enterParenthesisedExpression(self, ctx:EnforceParser.ParenthesisedExpressionContext):
        pass

    # Exit a parse tree produced by EnforceParser#parenthesisedExpression.
    def exitParenthesisedExpression(self, ctx:EnforceParser.ParenthesisedExpressionContext):
        pass


    # Enter a parse tree produced by EnforceParser#functionCallParameters.
    def enterFunctionCallParameters(self, ctx:EnforceParser.FunctionCallParametersContext):
        pass

    # Exit a parse tree produced by EnforceParser#functionCallParameters.
    def exitFunctionCallParameters(self, ctx:EnforceParser.FunctionCallParametersContext):
        pass


    # Enter a parse tree produced by EnforceParser#functionCallParameterList.
    def enterFunctionCallParameterList(self, ctx:EnforceParser.FunctionCallParameterListContext):
        pass

    # Exit a parse tree produced by EnforceParser#functionCallParameterList.
    def exitFunctionCallParameterList(self, ctx:EnforceParser.FunctionCallParameterListContext):
        pass


    # Enter a parse tree produced by EnforceParser#functionCallParameter.
    def enterFunctionCallParameter(self, ctx:EnforceParser.FunctionCallParameterContext):
        pass

    # Exit a parse tree produced by EnforceParser#functionCallParameter.
    def exitFunctionCallParameter(self, ctx:EnforceParser.FunctionCallParameterContext):
        pass


    # Enter a parse tree produced by EnforceParser#optionalParameter.
    def enterOptionalParameter(self, ctx:EnforceParser.OptionalParameterContext):
        pass

    # Exit a parse tree produced by EnforceParser#optionalParameter.
    def exitOptionalParameter(self, ctx:EnforceParser.OptionalParameterContext):
        pass


    # Enter a parse tree produced by EnforceParser#statementSingleOrBlock.
    def enterStatementSingleOrBlock(self, ctx:EnforceParser.StatementSingleOrBlockContext):
        pass

    # Exit a parse tree produced by EnforceParser#statementSingleOrBlock.
    def exitStatementSingleOrBlock(self, ctx:EnforceParser.StatementSingleOrBlockContext):
        pass


    # Enter a parse tree produced by EnforceParser#statementBlock.
    def enterStatementBlock(self, ctx:EnforceParser.StatementBlockContext):
        pass

    # Exit a parse tree produced by EnforceParser#statementBlock.
    def exitStatementBlock(self, ctx:EnforceParser.StatementBlockContext):
        pass


    # Enter a parse tree produced by EnforceParser#statement.
    def enterStatement(self, ctx:EnforceParser.StatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#statement.
    def exitStatement(self, ctx:EnforceParser.StatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#threadStatement.
    def enterThreadStatement(self, ctx:EnforceParser.ThreadStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#threadStatement.
    def exitThreadStatement(self, ctx:EnforceParser.ThreadStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#gotoStatement.
    def enterGotoStatement(self, ctx:EnforceParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#gotoStatement.
    def exitGotoStatement(self, ctx:EnforceParser.GotoStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#ifStatement.
    def enterIfStatement(self, ctx:EnforceParser.IfStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#ifStatement.
    def exitIfStatement(self, ctx:EnforceParser.IfStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#elseStatement.
    def enterElseStatement(self, ctx:EnforceParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#elseStatement.
    def exitElseStatement(self, ctx:EnforceParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#deleteStatement.
    def enterDeleteStatement(self, ctx:EnforceParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#deleteStatement.
    def exitDeleteStatement(self, ctx:EnforceParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#forStatement.
    def enterForStatement(self, ctx:EnforceParser.ForStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#forStatement.
    def exitForStatement(self, ctx:EnforceParser.ForStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#foreachStatement.
    def enterForeachStatement(self, ctx:EnforceParser.ForeachStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#foreachStatement.
    def exitForeachStatement(self, ctx:EnforceParser.ForeachStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#whileStatement.
    def enterWhileStatement(self, ctx:EnforceParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#whileStatement.
    def exitWhileStatement(self, ctx:EnforceParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#switchStatement.
    def enterSwitchStatement(self, ctx:EnforceParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#switchStatement.
    def exitSwitchStatement(self, ctx:EnforceParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#returnStatement.
    def enterReturnStatement(self, ctx:EnforceParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#returnStatement.
    def exitReturnStatement(self, ctx:EnforceParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#breakStatement.
    def enterBreakStatement(self, ctx:EnforceParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#breakStatement.
    def exitBreakStatement(self, ctx:EnforceParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#continueStatement.
    def enterContinueStatement(self, ctx:EnforceParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#continueStatement.
    def exitContinueStatement(self, ctx:EnforceParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#lambdaStatement.
    def enterLambdaStatement(self, ctx:EnforceParser.LambdaStatementContext):
        pass

    # Exit a parse tree produced by EnforceParser#lambdaStatement.
    def exitLambdaStatement(self, ctx:EnforceParser.LambdaStatementContext):
        pass


    # Enter a parse tree produced by EnforceParser#forControl.
    def enterForControl(self, ctx:EnforceParser.ForControlContext):
        pass

    # Exit a parse tree produced by EnforceParser#forControl.
    def exitForControl(self, ctx:EnforceParser.ForControlContext):
        pass


    # Enter a parse tree produced by EnforceParser#typeExtension_Child.
    def enterTypeExtension_Child(self, ctx:EnforceParser.TypeExtension_ChildContext):
        pass

    # Exit a parse tree produced by EnforceParser#typeExtension_Child.
    def exitTypeExtension_Child(self, ctx:EnforceParser.TypeExtension_ChildContext):
        pass


    # Enter a parse tree produced by EnforceParser#identifier.
    def enterIdentifier(self, ctx:EnforceParser.IdentifierContext):
        pass

    # Exit a parse tree produced by EnforceParser#identifier.
    def exitIdentifier(self, ctx:EnforceParser.IdentifierContext):
        pass


    # Enter a parse tree produced by EnforceParser#expressionList.
    def enterExpressionList(self, ctx:EnforceParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by EnforceParser#expressionList.
    def exitExpressionList(self, ctx:EnforceParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by EnforceParser#arrayIndex.
    def enterArrayIndex(self, ctx:EnforceParser.ArrayIndexContext):
        pass

    # Exit a parse tree produced by EnforceParser#arrayIndex.
    def exitArrayIndex(self, ctx:EnforceParser.ArrayIndexContext):
        pass


    # Enter a parse tree produced by EnforceParser#literalArray.
    def enterLiteralArray(self, ctx:EnforceParser.LiteralArrayContext):
        pass

    # Exit a parse tree produced by EnforceParser#literalArray.
    def exitLiteralArray(self, ctx:EnforceParser.LiteralArrayContext):
        pass


    # Enter a parse tree produced by EnforceParser#literalString.
    def enterLiteralString(self, ctx:EnforceParser.LiteralStringContext):
        pass

    # Exit a parse tree produced by EnforceParser#literalString.
    def exitLiteralString(self, ctx:EnforceParser.LiteralStringContext):
        pass


    # Enter a parse tree produced by EnforceParser#literalInteger.
    def enterLiteralInteger(self, ctx:EnforceParser.LiteralIntegerContext):
        pass

    # Exit a parse tree produced by EnforceParser#literalInteger.
    def exitLiteralInteger(self, ctx:EnforceParser.LiteralIntegerContext):
        pass


    # Enter a parse tree produced by EnforceParser#literalNull.
    def enterLiteralNull(self, ctx:EnforceParser.LiteralNullContext):
        pass

    # Exit a parse tree produced by EnforceParser#literalNull.
    def exitLiteralNull(self, ctx:EnforceParser.LiteralNullContext):
        pass


    # Enter a parse tree produced by EnforceParser#literalFloat.
    def enterLiteralFloat(self, ctx:EnforceParser.LiteralFloatContext):
        pass

    # Exit a parse tree produced by EnforceParser#literalFloat.
    def exitLiteralFloat(self, ctx:EnforceParser.LiteralFloatContext):
        pass


    # Enter a parse tree produced by EnforceParser#literalBoolean.
    def enterLiteralBoolean(self, ctx:EnforceParser.LiteralBooleanContext):
        pass

    # Exit a parse tree produced by EnforceParser#literalBoolean.
    def exitLiteralBoolean(self, ctx:EnforceParser.LiteralBooleanContext):
        pass


    # Enter a parse tree produced by EnforceParser#foreachVariable.
    def enterForeachVariable(self, ctx:EnforceParser.ForeachVariableContext):
        pass

    # Exit a parse tree produced by EnforceParser#foreachVariable.
    def exitForeachVariable(self, ctx:EnforceParser.ForeachVariableContext):
        pass


    # Enter a parse tree produced by EnforceParser#switchLabel.
    def enterSwitchLabel(self, ctx:EnforceParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by EnforceParser#switchLabel.
    def exitSwitchLabel(self, ctx:EnforceParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by EnforceParser#defaultSwitchLabel.
    def enterDefaultSwitchLabel(self, ctx:EnforceParser.DefaultSwitchLabelContext):
        pass

    # Exit a parse tree produced by EnforceParser#defaultSwitchLabel.
    def exitDefaultSwitchLabel(self, ctx:EnforceParser.DefaultSwitchLabelContext):
        pass


    # Enter a parse tree produced by EnforceParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:EnforceParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by EnforceParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:EnforceParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by EnforceParser#emptyBlock.
    def enterEmptyBlock(self, ctx:EnforceParser.EmptyBlockContext):
        pass

    # Exit a parse tree produced by EnforceParser#emptyBlock.
    def exitEmptyBlock(self, ctx:EnforceParser.EmptyBlockContext):
        pass


    # Enter a parse tree produced by EnforceParser#typedefDeclaration.
    def enterTypedefDeclaration(self, ctx:EnforceParser.TypedefDeclarationContext):
        pass

    # Exit a parse tree produced by EnforceParser#typedefDeclaration.
    def exitTypedefDeclaration(self, ctx:EnforceParser.TypedefDeclarationContext):
        pass


    # Enter a parse tree produced by EnforceParser#typedefType.
    def enterTypedefType(self, ctx:EnforceParser.TypedefTypeContext):
        pass

    # Exit a parse tree produced by EnforceParser#typedefType.
    def exitTypedefType(self, ctx:EnforceParser.TypedefTypeContext):
        pass


    # Enter a parse tree produced by EnforceParser#keyword.
    def enterKeyword(self, ctx:EnforceParser.KeywordContext):
        pass

    # Exit a parse tree produced by EnforceParser#keyword.
    def exitKeyword(self, ctx:EnforceParser.KeywordContext):
        pass


    # Enter a parse tree produced by EnforceParser#typeList.
    def enterTypeList(self, ctx:EnforceParser.TypeListContext):
        pass

    # Exit a parse tree produced by EnforceParser#typeList.
    def exitTypeList(self, ctx:EnforceParser.TypeListContext):
        pass


    # Enter a parse tree produced by EnforceParser#genericType.
    def enterGenericType(self, ctx:EnforceParser.GenericTypeContext):
        pass

    # Exit a parse tree produced by EnforceParser#genericType.
    def exitGenericType(self, ctx:EnforceParser.GenericTypeContext):
        pass


    # Enter a parse tree produced by EnforceParser#genericTypeDeclarationList.
    def enterGenericTypeDeclarationList(self, ctx:EnforceParser.GenericTypeDeclarationListContext):
        pass

    # Exit a parse tree produced by EnforceParser#genericTypeDeclarationList.
    def exitGenericTypeDeclarationList(self, ctx:EnforceParser.GenericTypeDeclarationListContext):
        pass


    # Enter a parse tree produced by EnforceParser#genericTypeDeclaration.
    def enterGenericTypeDeclaration(self, ctx:EnforceParser.GenericTypeDeclarationContext):
        pass

    # Exit a parse tree produced by EnforceParser#genericTypeDeclaration.
    def exitGenericTypeDeclaration(self, ctx:EnforceParser.GenericTypeDeclarationContext):
        pass


    # Enter a parse tree produced by EnforceParser#annotation.
    def enterAnnotation(self, ctx:EnforceParser.AnnotationContext):
        pass

    # Exit a parse tree produced by EnforceParser#annotation.
    def exitAnnotation(self, ctx:EnforceParser.AnnotationContext):
        pass


    # Enter a parse tree produced by EnforceParser#classReference.
    def enterClassReference(self, ctx:EnforceParser.ClassReferenceContext):
        pass

    # Exit a parse tree produced by EnforceParser#classReference.
    def exitClassReference(self, ctx:EnforceParser.ClassReferenceContext):
        pass


    # Enter a parse tree produced by EnforceParser#leftShift.
    def enterLeftShift(self, ctx:EnforceParser.LeftShiftContext):
        pass

    # Exit a parse tree produced by EnforceParser#leftShift.
    def exitLeftShift(self, ctx:EnforceParser.LeftShiftContext):
        pass


    # Enter a parse tree produced by EnforceParser#rightShift.
    def enterRightShift(self, ctx:EnforceParser.RightShiftContext):
        pass

    # Exit a parse tree produced by EnforceParser#rightShift.
    def exitRightShift(self, ctx:EnforceParser.RightShiftContext):
        pass


    # Enter a parse tree produced by EnforceParser#typeModifer.
    def enterTypeModifer(self, ctx:EnforceParser.TypeModiferContext):
        pass

    # Exit a parse tree produced by EnforceParser#typeModifer.
    def exitTypeModifer(self, ctx:EnforceParser.TypeModiferContext):
        pass


    # Enter a parse tree produced by EnforceParser#variableModifier.
    def enterVariableModifier(self, ctx:EnforceParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by EnforceParser#variableModifier.
    def exitVariableModifier(self, ctx:EnforceParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by EnforceParser#functionModifier.
    def enterFunctionModifier(self, ctx:EnforceParser.FunctionModifierContext):
        pass

    # Exit a parse tree produced by EnforceParser#functionModifier.
    def exitFunctionModifier(self, ctx:EnforceParser.FunctionModifierContext):
        pass



del EnforceParser