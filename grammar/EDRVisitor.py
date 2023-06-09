# Generated from EDR.g by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EDRParser import EDRParser
else:
    from EDRParser import EDRParser

# This class defines a complete generic visitor for a parse tree produced by EDRParser.

class EDRVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EDRParser#root.
    def visitRoot(self, ctx:EDRParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#column.
    def visitColumn(self, ctx:EDRParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#multi_line_inscription.
    def visitMulti_line_inscription(self, ctx:EDRParser.Multi_line_inscriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#no_word_break.
    def visitNo_word_break(self, ctx:EDRParser.No_word_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#excess_new_line.
    def visitExcess_new_line(self, ctx:EDRParser.Excess_new_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#single_line_inscription.
    def visitSingle_line_inscription(self, ctx:EDRParser.Single_line_inscriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#continuation.
    def visitContinuation(self, ctx:EDRParser.ContinuationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#content.
    def visitContent(self, ctx:EDRParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#row.
    def visitRow(self, ctx:EDRParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#perp.
    def visitPerp(self, ctx:EDRParser.PerpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#horz.
    def visitHorz(self, ctx:EDRParser.HorzContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#line.
    def visitLine(self, ctx:EDRParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#term.
    def visitTerm(self, ctx:EDRParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#figural.
    def visitFigural(self, ctx:EDRParser.FiguralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#normal_misspell.
    def visitNormal_misspell(self, ctx:EDRParser.Normal_misspellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#no_space_misspell.
    def visitNo_space_misspell(self, ctx:EDRParser.No_space_misspellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#unsure_misspell.
    def visitUnsure_misspell(self, ctx:EDRParser.Unsure_misspellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#unsure_no_space_misspell.
    def visitUnsure_no_space_misspell(self, ctx:EDRParser.Unsure_no_space_misspellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#normal_abbr.
    def visitNormal_abbr(self, ctx:EDRParser.Normal_abbrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#uncertain_abbr.
    def visitUncertain_abbr(self, ctx:EDRParser.Uncertain_abbrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#unknown_abbr1.
    def visitUnknown_abbr1(self, ctx:EDRParser.Unknown_abbr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#unknown_abbr2.
    def visitUnknown_abbr2(self, ctx:EDRParser.Unknown_abbr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#desc.
    def visitDesc(self, ctx:EDRParser.DescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#string.
    def visitString(self, ctx:EDRParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#word.
    def visitWord(self, ctx:EDRParser.WordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#line_in_bracket.
    def visitLine_in_bracket(self, ctx:EDRParser.Line_in_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#term_in_bracket.
    def visitTerm_in_bracket(self, ctx:EDRParser.Term_in_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#string_in_bracket.
    def visitString_in_bracket(self, ctx:EDRParser.String_in_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#word_in_bracket.
    def visitWord_in_bracket(self, ctx:EDRParser.Word_in_bracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#missing_chunk.
    def visitMissing_chunk(self, ctx:EDRParser.Missing_chunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#standard_chunk.
    def visitStandard_chunk(self, ctx:EDRParser.Standard_chunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#chunk.
    def visitChunk(self, ctx:EDRParser.ChunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#normal_chunk.
    def visitNormal_chunk(self, ctx:EDRParser.Normal_chunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#under_chunk.
    def visitUnder_chunk(self, ctx:EDRParser.Under_chunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#under_helper.
    def visitUnder_helper(self, ctx:EDRParser.Under_helperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#dot_chunk.
    def visitDot_chunk(self, ctx:EDRParser.Dot_chunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#dot_helper.
    def visitDot_helper(self, ctx:EDRParser.Dot_helperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#erased.
    def visitErased(self, ctx:EDRParser.ErasedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#lost_chunk.
    def visitLost_chunk(self, ctx:EDRParser.Lost_chunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#lost_with_gap.
    def visitLost_with_gap(self, ctx:EDRParser.Lost_with_gapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#gap_unknown.
    def visitGap_unknown(self, ctx:EDRParser.Gap_unknownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#illegible.
    def visitIllegible(self, ctx:EDRParser.IllegibleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#lost_lines_unknown.
    def visitLost_lines_unknown(self, ctx:EDRParser.Lost_lines_unknownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#lost_chars_known.
    def visitLost_chars_known(self, ctx:EDRParser.Lost_chars_knownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#lost_line.
    def visitLost_line(self, ctx:EDRParser.Lost_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#lost_lines.
    def visitLost_lines(self, ctx:EDRParser.Lost_linesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#surplus.
    def visitSurplus(self, ctx:EDRParser.SurplusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#joined.
    def visitJoined(self, ctx:EDRParser.JoinedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#joined_helper.
    def visitJoined_helper(self, ctx:EDRParser.Joined_helperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#joined_letters.
    def visitJoined_letters(self, ctx:EDRParser.Joined_lettersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#symbol.
    def visitSymbol(self, ctx:EDRParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#lost_chars.
    def visitLost_chars(self, ctx:EDRParser.Lost_charsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#dashes.
    def visitDashes(self, ctx:EDRParser.DashesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#editorial.
    def visitEditorial(self, ctx:EDRParser.EditorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#vacat.
    def visitVacat(self, ctx:EDRParser.VacatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#ianua.
    def visitIanua(self, ctx:EDRParser.IanuaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#subaudible.
    def visitSubaudible(self, ctx:EDRParser.SubaudibleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EDRParser#omitted.
    def visitOmitted(self, ctx:EDRParser.OmittedContext):
        return self.visitChildren(ctx)



del EDRParser