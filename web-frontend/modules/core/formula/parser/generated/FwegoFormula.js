// Generated from FwegoFormula.g4 by ANTLR 4.9
// jshint ignore: start
import antlr4 from 'antlr4';
import FwegoFormulaListener from './FwegoFormulaListener.js';
import FwegoFormulaVisitor from './FwegoFormulaVisitor.js';


const serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786",
    "\u5964\u0003U`\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004\t",
    "\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007\u0003",
    "\u0002\u0003\u0002\u0003\u0002\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0005",
    "\u0003-\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0007\u00037\n\u0003\f\u0003",
    "\u000e\u0003:\u000b\u0003\u0005\u0003<\n\u0003\u0003\u0003\u0003\u0003",
    "\u0005\u0003@\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0007\u0003S\n\u0003\f\u0003\u000e\u0003V\u000b\u0003\u0003",
    "\u0004\u0003\u0004\u0003\u0005\u0003\u0005\u0003\u0006\u0003\u0006\u0003",
    "\u0007\u0003\u0007\u0003\u0007\u0002\u0003\u0004\b\u0002\u0004\u0006",
    "\b\n\f\u0002\u000b\u0003\u0002\u0006\u0007\u0004\u0002\u0010\u0010K",
    "K\u0004\u0002??EE\u0004\u0002  BB\u0004\u0002+,67\u0004\u0002\'\'))",
    "\u0003\u0002\u0003\u0005\u0003\u0002\u001b\u001c\u0003\u0002\u001d\u001e",
    "\u0002l\u0002\u000e\u0003\u0002\u0002\u0002\u0004?\u0003\u0002\u0002",
    "\u0002\u0006W\u0003\u0002\u0002\u0002\bY\u0003\u0002\u0002\u0002\n[",
    "\u0003\u0002\u0002\u0002\f]\u0003\u0002\u0002\u0002\u000e\u000f\u0005",
    "\u0004\u0003\u0002\u000f\u0010\u0007\u0002\u0002\u0003\u0010\u0003\u0003",
    "\u0002\u0002\u0002\u0011\u0012\b\u0003\u0001\u0002\u0012@\u0007\u001b",
    "\u0002\u0002\u0013@\u0007\u001c\u0002\u0002\u0014@\u0007\u0018\u0002",
    "\u0002\u0015@\u0007\u0017\u0002\u0002\u0016@\t\u0002\u0002\u0002\u0017",
    "\u0018\u0005\u0006\u0004\u0002\u0018\u0019\u0005\u0004\u0003\u000e\u0019",
    "@\u0003\u0002\u0002\u0002\u001a\u001b\u0007\u0011\u0002\u0002\u001b",
    "\u001c\u0005\u0004\u0003\u0002\u001c\u001d\u0007\u0012\u0002\u0002\u001d",
    "@\u0003\u0002\u0002\u0002\u001e\u001f\u0007\b\u0002\u0002\u001f \u0007",
    "\u0011\u0002\u0002 !\u0005\n\u0006\u0002!\"\u0007\u0012\u0002\u0002",
    "\"@\u0003\u0002\u0002\u0002#$\u0007\t\u0002\u0002$%\u0007\u0011\u0002",
    "\u0002%&\u0007\u0018\u0002\u0002&@\u0007\u0012\u0002\u0002\'(\u0007",
    "\n\u0002\u0002()\u0007\u0011\u0002\u0002)*\u0005\n\u0006\u0002*,\u0007",
    "\u000b\u0002\u0002+-\u0007\u0005\u0002\u0002,+\u0003\u0002\u0002\u0002",
    ",-\u0003\u0002\u0002\u0002-.\u0003\u0002\u0002\u0002./\u0005\n\u0006",
    "\u0002/0\u0007\u0012\u0002\u00020@\u0003\u0002\u0002\u000212\u0005\b",
    "\u0005\u00022;\u0007\u0011\u0002\u000238\u0005\u0004\u0003\u000245\u0007",
    "\u000b\u0002\u000257\u0005\u0004\u0003\u000264\u0003\u0002\u0002\u0002",
    "7:\u0003\u0002\u0002\u000286\u0003\u0002\u0002\u000289\u0003\u0002\u0002",
    "\u00029<\u0003\u0002\u0002\u0002:8\u0003\u0002\u0002\u0002;3\u0003\u0002",
    "\u0002\u0002;<\u0003\u0002\u0002\u0002<=\u0003\u0002\u0002\u0002=>\u0007",
    "\u0012\u0002\u0002>@\u0003\u0002\u0002\u0002?\u0011\u0003\u0002\u0002",
    "\u0002?\u0013\u0003\u0002\u0002\u0002?\u0014\u0003\u0002\u0002\u0002",
    "?\u0015\u0003\u0002\u0002\u0002?\u0016\u0003\u0002\u0002\u0002?\u0017",
    "\u0003\u0002\u0002\u0002?\u001a\u0003\u0002\u0002\u0002?\u001e\u0003",
    "\u0002\u0002\u0002?#\u0003\u0002\u0002\u0002?\'\u0003\u0002\u0002\u0002",
    "?1\u0003\u0002\u0002\u0002@T\u0003\u0002\u0002\u0002AB\f\u000b\u0002",
    "\u0002BC\t\u0003\u0002\u0002CS\u0005\u0004\u0003\fDE\f\n\u0002\u0002",
    "EF\t\u0004\u0002\u0002FS\u0005\u0004\u0003\u000bGH\f\t\u0002\u0002H",
    "I\t\u0005\u0002\u0002IS\u0005\u0004\u0003\nJK\f\b\u0002\u0002KL\t\u0006",
    "\u0002\u0002LS\u0005\u0004\u0003\tMN\f\u0007\u0002\u0002NO\t\u0007\u0002",
    "\u0002OS\u0005\u0004\u0003\bPQ\f\r\u0002\u0002QS\u0005\u0006\u0004\u0002",
    "RA\u0003\u0002\u0002\u0002RD\u0003\u0002\u0002\u0002RG\u0003\u0002\u0002",
    "\u0002RJ\u0003\u0002\u0002\u0002RM\u0003\u0002\u0002\u0002RP\u0003\u0002",
    "\u0002\u0002SV\u0003\u0002\u0002\u0002TR\u0003\u0002\u0002\u0002TU\u0003",
    "\u0002\u0002\u0002U\u0005\u0003\u0002\u0002\u0002VT\u0003\u0002\u0002",
    "\u0002WX\t\b\u0002\u0002X\u0007\u0003\u0002\u0002\u0002YZ\u0005\f\u0007",
    "\u0002Z\t\u0003\u0002\u0002\u0002[\\\t\t\u0002\u0002\\\u000b\u0003\u0002",
    "\u0002\u0002]^\t\n\u0002\u0002^\r\u0003\u0002\u0002\u0002\b,8;?RT"].join("");


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.PredictionContextCache();

export default class FwegoFormula extends antlr4.Parser {

    static grammarFileName = "FwegoFormula.g4";
    static literalNames = [ null, null, null, null, null, null, null, null,
                            null, "','", "':'", "'::'", "'$'", "'$$'", "'*'",
                            "'('", "')'", "'['", "']'", null, null, null,
                            null, null, "'.'", null, null, null, null, "'&'",
                            "'&&'", "'&<'", "'@@'", "'@>'", "'@'", "'!'",
                            "'!!'", "'!='", "'^'", "'='", "'=>'", "'>'",
                            "'>='", "'>>'", "'#'", "'#='", "'#>'", "'#>>'",
                            "'##'", "'->'", "'->>'", "'-|-'", "'<'", "'<='",
                            "'<@'", "'<^'", "'<>'", "'<->'", "'<<'", "'<<='",
                            "'<?>'", "'-'", "'%'", "'|'", "'||'", "'||/'",
                            "'|/'", "'+'", "'?'", "'?&'", "'?#'", "'?-'",
                            "'?|'", "'/'", "'~'", "'~='", "'~>=~'", "'~>~'",
                            "'~<=~'", "'~<~'", "'~*'", "'~~'", "';'" ];
    static symbolicNames = [ null, "BLOCK_COMMENT", "LINE_COMMENT", "WHITESPACE",
                             "TRUE", "FALSE", "FIELD", "FIELDBYID", "LOOKUP",
                             "COMMA", "COLON", "COLON_COLON", "DOLLAR",
                             "DOLLAR_DOLLAR", "STAR", "OPEN_PAREN", "CLOSE_PAREN",
                             "OPEN_BRACKET", "CLOSE_BRACKET", "BIT_STRING",
                             "REGEX_STRING", "NUMERIC_LITERAL", "INTEGER_LITERAL",
                             "HEX_INTEGER_LITERAL", "DOT", "SINGLEQ_STRING_LITERAL",
                             "DOUBLEQ_STRING_LITERAL", "IDENTIFIER", "IDENTIFIER_UNICODE",
                             "AMP", "AMP_AMP", "AMP_LT", "AT_AT", "AT_GT",
                             "AT_SIGN", "BANG", "BANG_BANG", "BANG_EQUAL",
                             "CARET", "EQUAL", "EQUAL_GT", "GT", "GTE",
                             "GT_GT", "HASH", "HASH_EQ", "HASH_GT", "HASH_GT_GT",
                             "HASH_HASH", "HYPHEN_GT", "HYPHEN_GT_GT", "HYPHEN_PIPE_HYPHEN",
                             "LT", "LTE", "LT_AT", "LT_CARET", "LT_GT",
                             "LT_HYPHEN_GT", "LT_LT", "LT_LT_EQ", "LT_QMARK_GT",
                             "MINUS", "PERCENT", "PIPE", "PIPE_PIPE", "PIPE_PIPE_SLASH",
                             "PIPE_SLASH", "PLUS", "QMARK", "QMARK_AMP",
                             "QMARK_HASH", "QMARK_HYPHEN", "QMARK_PIPE",
                             "SLASH", "TIL", "TIL_EQ", "TIL_GTE_TIL", "TIL_GT_TIL",
                             "TIL_LTE_TIL", "TIL_LT_TIL", "TIL_STAR", "TIL_TIL",
                             "SEMI", "ErrorCharacter" ];
    static ruleNames = [ "root", "expr", "ws_or_comment", "func_name", "field_reference",
                         "identifier" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = FwegoFormula.ruleNames;
        this.literalNames = FwegoFormula.literalNames;
        this.symbolicNames = FwegoFormula.symbolicNames;
    }

    get atn() {
        return atn;
    }

    sempred(localctx, ruleIndex, predIndex) {
    	switch(ruleIndex) {
    	case 1:
    	    		return this.expr_sempred(localctx, predIndex);
        default:
            throw "No predicate with index:" + ruleIndex;
       }
    }

    expr_sempred(localctx, predIndex) {
    	switch(predIndex) {
    		case 0:
    			return this.precpred(this._ctx, 9);
    		case 1:
    			return this.precpred(this._ctx, 8);
    		case 2:
    			return this.precpred(this._ctx, 7);
    		case 3:
    			return this.precpred(this._ctx, 6);
    		case 4:
    			return this.precpred(this._ctx, 5);
    		case 5:
    			return this.precpred(this._ctx, 11);
    		default:
    			throw "No predicate with index:" + predIndex;
    	}
    };




	root() {
	    let localctx = new RootContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, FwegoFormula.RULE_root);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 12;
	        this.expr(0);
	        this.state = 13;
	        this.match(FwegoFormula.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


	expr(_p) {
		if(_p===undefined) {
		    _p = 0;
		}
	    const _parentctx = this._ctx;
	    const _parentState = this.state;
	    let localctx = new ExprContext(this, this._ctx, _parentState);
	    let _prevctx = localctx;
	    const _startState = 2;
	    this.enterRecursionRule(localctx, 2, FwegoFormula.RULE_expr, _p);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 61;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case FwegoFormula.SINGLEQ_STRING_LITERAL:
	            localctx = new StringLiteralContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;

	            this.state = 16;
	            this.match(FwegoFormula.SINGLEQ_STRING_LITERAL);
	            break;
	        case FwegoFormula.DOUBLEQ_STRING_LITERAL:
	            localctx = new StringLiteralContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 17;
	            this.match(FwegoFormula.DOUBLEQ_STRING_LITERAL);
	            break;
	        case FwegoFormula.INTEGER_LITERAL:
	            localctx = new IntegerLiteralContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 18;
	            this.match(FwegoFormula.INTEGER_LITERAL);
	            break;
	        case FwegoFormula.NUMERIC_LITERAL:
	            localctx = new DecimalLiteralContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 19;
	            this.match(FwegoFormula.NUMERIC_LITERAL);
	            break;
	        case FwegoFormula.TRUE:
	        case FwegoFormula.FALSE:
	            localctx = new BooleanLiteralContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 20;
	            _la = this._input.LA(1);
	            if(!(_la===FwegoFormula.TRUE || _la===FwegoFormula.FALSE)) {
	            this._errHandler.recoverInline(this);
	            }
	            else {
	            	this._errHandler.reportMatch(this);
	                this.consume();
	            }
	            break;
	        case FwegoFormula.BLOCK_COMMENT:
	        case FwegoFormula.LINE_COMMENT:
	        case FwegoFormula.WHITESPACE:
	            localctx = new LeftWhitespaceOrCommentsContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 21;
	            this.ws_or_comment();
	            this.state = 22;
	            this.expr(12);
	            break;
	        case FwegoFormula.OPEN_PAREN:
	            localctx = new BracketsContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 24;
	            this.match(FwegoFormula.OPEN_PAREN);
	            this.state = 25;
	            this.expr(0);
	            this.state = 26;
	            this.match(FwegoFormula.CLOSE_PAREN);
	            break;
	        case FwegoFormula.FIELD:
	            localctx = new FieldReferenceContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 28;
	            this.match(FwegoFormula.FIELD);
	            this.state = 29;
	            this.match(FwegoFormula.OPEN_PAREN);
	            this.state = 30;
	            this.field_reference();
	            this.state = 31;
	            this.match(FwegoFormula.CLOSE_PAREN);
	            break;
	        case FwegoFormula.FIELDBYID:
	            localctx = new FieldByIdReferenceContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 33;
	            this.match(FwegoFormula.FIELDBYID);
	            this.state = 34;
	            this.match(FwegoFormula.OPEN_PAREN);
	            this.state = 35;
	            this.match(FwegoFormula.INTEGER_LITERAL);
	            this.state = 36;
	            this.match(FwegoFormula.CLOSE_PAREN);
	            break;
	        case FwegoFormula.LOOKUP:
	            localctx = new LookupFieldReferenceContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 37;
	            this.match(FwegoFormula.LOOKUP);
	            this.state = 38;
	            this.match(FwegoFormula.OPEN_PAREN);
	            this.state = 39;
	            this.field_reference();
	            this.state = 40;
	            this.match(FwegoFormula.COMMA);
	            this.state = 42;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===FwegoFormula.WHITESPACE) {
	                this.state = 41;
	                this.match(FwegoFormula.WHITESPACE);
	            }

	            this.state = 44;
	            this.field_reference();
	            this.state = 45;
	            this.match(FwegoFormula.CLOSE_PAREN);
	            break;
	        case FwegoFormula.IDENTIFIER:
	        case FwegoFormula.IDENTIFIER_UNICODE:
	            localctx = new FunctionCallContext(this, localctx);
	            this._ctx = localctx;
	            _prevctx = localctx;
	            this.state = 47;
	            this.func_name();
	            this.state = 48;
	            this.match(FwegoFormula.OPEN_PAREN);
	            this.state = 57;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << FwegoFormula.BLOCK_COMMENT) | (1 << FwegoFormula.LINE_COMMENT) | (1 << FwegoFormula.WHITESPACE) | (1 << FwegoFormula.TRUE) | (1 << FwegoFormula.FALSE) | (1 << FwegoFormula.FIELD) | (1 << FwegoFormula.FIELDBYID) | (1 << FwegoFormula.LOOKUP) | (1 << FwegoFormula.OPEN_PAREN) | (1 << FwegoFormula.NUMERIC_LITERAL) | (1 << FwegoFormula.INTEGER_LITERAL) | (1 << FwegoFormula.SINGLEQ_STRING_LITERAL) | (1 << FwegoFormula.DOUBLEQ_STRING_LITERAL) | (1 << FwegoFormula.IDENTIFIER) | (1 << FwegoFormula.IDENTIFIER_UNICODE))) !== 0)) {
	                this.state = 49;
	                this.expr(0);
	                this.state = 54;
	                this._errHandler.sync(this);
	                _la = this._input.LA(1);
	                while(_la===FwegoFormula.COMMA) {
	                    this.state = 50;
	                    this.match(FwegoFormula.COMMA);
	                    this.state = 51;
	                    this.expr(0);
	                    this.state = 56;
	                    this._errHandler.sync(this);
	                    _la = this._input.LA(1);
	                }
	            }

	            this.state = 59;
	            this.match(FwegoFormula.CLOSE_PAREN);
	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	        this._ctx.stop = this._input.LT(-1);
	        this.state = 82;
	        this._errHandler.sync(this);
	        let _alt = this._interp.adaptivePredict(this._input,5,this._ctx)
	        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
	            if(_alt===1) {
	                if(this._parseListeners!==null) {
	                    this.triggerExitRuleEvent();
	                }
	                _prevctx = localctx;
	                this.state = 80;
	                this._errHandler.sync(this);
	                var la_ = this._interp.adaptivePredict(this._input,4,this._ctx);
	                switch(la_) {
	                case 1:
	                    localctx = new BinaryOpContext(this, new ExprContext(this, _parentctx, _parentState));
	                    this.pushNewRecursionContext(localctx, _startState, FwegoFormula.RULE_expr);
	                    this.state = 63;
	                    if (!( this.precpred(this._ctx, 9))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 9)");
	                    }
	                    this.state = 64;
	                    localctx.op = this._input.LT(1);
	                    _la = this._input.LA(1);
	                    if(!(_la===FwegoFormula.STAR || _la===FwegoFormula.SLASH)) {
	                        localctx.op = this._errHandler.recoverInline(this);
	                    }
	                    else {
	                    	this._errHandler.reportMatch(this);
	                        this.consume();
	                    }
	                    this.state = 65;
	                    this.expr(10);
	                    break;

	                case 2:
	                    localctx = new BinaryOpContext(this, new ExprContext(this, _parentctx, _parentState));
	                    this.pushNewRecursionContext(localctx, _startState, FwegoFormula.RULE_expr);
	                    this.state = 66;
	                    if (!( this.precpred(this._ctx, 8))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 8)");
	                    }
	                    this.state = 67;
	                    localctx.op = this._input.LT(1);
	                    _la = this._input.LA(1);
	                    if(!(_la===FwegoFormula.MINUS || _la===FwegoFormula.PLUS)) {
	                        localctx.op = this._errHandler.recoverInline(this);
	                    }
	                    else {
	                    	this._errHandler.reportMatch(this);
	                        this.consume();
	                    }
	                    this.state = 68;
	                    this.expr(9);
	                    break;

	                case 3:
	                    localctx = new BinaryOpContext(this, new ExprContext(this, _parentctx, _parentState));
	                    this.pushNewRecursionContext(localctx, _startState, FwegoFormula.RULE_expr);
	                    this.state = 69;
	                    if (!( this.precpred(this._ctx, 7))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 7)");
	                    }
	                    this.state = 70;
	                    localctx.op = this._input.LT(1);
	                    _la = this._input.LA(1);
	                    if(!(_la===FwegoFormula.AMP_AMP || _la===FwegoFormula.PIPE_PIPE)) {
	                        localctx.op = this._errHandler.recoverInline(this);
	                    }
	                    else {
	                    	this._errHandler.reportMatch(this);
	                        this.consume();
	                    }
	                    this.state = 71;
	                    this.expr(8);
	                    break;

	                case 4:
	                    localctx = new BinaryOpContext(this, new ExprContext(this, _parentctx, _parentState));
	                    this.pushNewRecursionContext(localctx, _startState, FwegoFormula.RULE_expr);
	                    this.state = 72;
	                    if (!( this.precpred(this._ctx, 6))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 6)");
	                    }
	                    this.state = 73;
	                    localctx.op = this._input.LT(1);
	                    _la = this._input.LA(1);
	                    if(!(((((_la - 41)) & ~0x1f) == 0 && ((1 << (_la - 41)) & ((1 << (FwegoFormula.GT - 41)) | (1 << (FwegoFormula.GTE - 41)) | (1 << (FwegoFormula.LT - 41)) | (1 << (FwegoFormula.LTE - 41)))) !== 0))) {
	                        localctx.op = this._errHandler.recoverInline(this);
	                    }
	                    else {
	                    	this._errHandler.reportMatch(this);
	                        this.consume();
	                    }
	                    this.state = 74;
	                    this.expr(7);
	                    break;

	                case 5:
	                    localctx = new BinaryOpContext(this, new ExprContext(this, _parentctx, _parentState));
	                    this.pushNewRecursionContext(localctx, _startState, FwegoFormula.RULE_expr);
	                    this.state = 75;
	                    if (!( this.precpred(this._ctx, 5))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 5)");
	                    }
	                    this.state = 76;
	                    localctx.op = this._input.LT(1);
	                    _la = this._input.LA(1);
	                    if(!(_la===FwegoFormula.BANG_EQUAL || _la===FwegoFormula.EQUAL)) {
	                        localctx.op = this._errHandler.recoverInline(this);
	                    }
	                    else {
	                    	this._errHandler.reportMatch(this);
	                        this.consume();
	                    }
	                    this.state = 77;
	                    this.expr(6);
	                    break;

	                case 6:
	                    localctx = new RightWhitespaceOrCommentsContext(this, new ExprContext(this, _parentctx, _parentState));
	                    this.pushNewRecursionContext(localctx, _startState, FwegoFormula.RULE_expr);
	                    this.state = 78;
	                    if (!( this.precpred(this._ctx, 11))) {
	                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 11)");
	                    }
	                    this.state = 79;
	                    this.ws_or_comment();
	                    break;

	                }
	            }
	            this.state = 84;
	            this._errHandler.sync(this);
	            _alt = this._interp.adaptivePredict(this._input,5,this._ctx);
	        }

	    } catch( error) {
	        if(error instanceof antlr4.error.RecognitionException) {
		        localctx.exception = error;
		        this._errHandler.reportError(this, error);
		        this._errHandler.recover(this, error);
		    } else {
		    	throw error;
		    }
	    } finally {
	        this.unrollRecursionContexts(_parentctx)
	    }
	    return localctx;
	}



	ws_or_comment() {
	    let localctx = new Ws_or_commentContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, FwegoFormula.RULE_ws_or_comment);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 85;
	        _la = this._input.LA(1);
	        if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << FwegoFormula.BLOCK_COMMENT) | (1 << FwegoFormula.LINE_COMMENT) | (1 << FwegoFormula.WHITESPACE))) !== 0))) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	func_name() {
	    let localctx = new Func_nameContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, FwegoFormula.RULE_func_name);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 87;
	        this.identifier();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	field_reference() {
	    let localctx = new Field_referenceContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, FwegoFormula.RULE_field_reference);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 89;
	        _la = this._input.LA(1);
	        if(!(_la===FwegoFormula.SINGLEQ_STRING_LITERAL || _la===FwegoFormula.DOUBLEQ_STRING_LITERAL)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	identifier() {
	    let localctx = new IdentifierContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, FwegoFormula.RULE_identifier);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 91;
	        _la = this._input.LA(1);
	        if(!(_la===FwegoFormula.IDENTIFIER || _la===FwegoFormula.IDENTIFIER_UNICODE)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

FwegoFormula.EOF = antlr4.Token.EOF;
FwegoFormula.BLOCK_COMMENT = 1;
FwegoFormula.LINE_COMMENT = 2;
FwegoFormula.WHITESPACE = 3;
FwegoFormula.TRUE = 4;
FwegoFormula.FALSE = 5;
FwegoFormula.FIELD = 6;
FwegoFormula.FIELDBYID = 7;
FwegoFormula.LOOKUP = 8;
FwegoFormula.COMMA = 9;
FwegoFormula.COLON = 10;
FwegoFormula.COLON_COLON = 11;
FwegoFormula.DOLLAR = 12;
FwegoFormula.DOLLAR_DOLLAR = 13;
FwegoFormula.STAR = 14;
FwegoFormula.OPEN_PAREN = 15;
FwegoFormula.CLOSE_PAREN = 16;
FwegoFormula.OPEN_BRACKET = 17;
FwegoFormula.CLOSE_BRACKET = 18;
FwegoFormula.BIT_STRING = 19;
FwegoFormula.REGEX_STRING = 20;
FwegoFormula.NUMERIC_LITERAL = 21;
FwegoFormula.INTEGER_LITERAL = 22;
FwegoFormula.HEX_INTEGER_LITERAL = 23;
FwegoFormula.DOT = 24;
FwegoFormula.SINGLEQ_STRING_LITERAL = 25;
FwegoFormula.DOUBLEQ_STRING_LITERAL = 26;
FwegoFormula.IDENTIFIER = 27;
FwegoFormula.IDENTIFIER_UNICODE = 28;
FwegoFormula.AMP = 29;
FwegoFormula.AMP_AMP = 30;
FwegoFormula.AMP_LT = 31;
FwegoFormula.AT_AT = 32;
FwegoFormula.AT_GT = 33;
FwegoFormula.AT_SIGN = 34;
FwegoFormula.BANG = 35;
FwegoFormula.BANG_BANG = 36;
FwegoFormula.BANG_EQUAL = 37;
FwegoFormula.CARET = 38;
FwegoFormula.EQUAL = 39;
FwegoFormula.EQUAL_GT = 40;
FwegoFormula.GT = 41;
FwegoFormula.GTE = 42;
FwegoFormula.GT_GT = 43;
FwegoFormula.HASH = 44;
FwegoFormula.HASH_EQ = 45;
FwegoFormula.HASH_GT = 46;
FwegoFormula.HASH_GT_GT = 47;
FwegoFormula.HASH_HASH = 48;
FwegoFormula.HYPHEN_GT = 49;
FwegoFormula.HYPHEN_GT_GT = 50;
FwegoFormula.HYPHEN_PIPE_HYPHEN = 51;
FwegoFormula.LT = 52;
FwegoFormula.LTE = 53;
FwegoFormula.LT_AT = 54;
FwegoFormula.LT_CARET = 55;
FwegoFormula.LT_GT = 56;
FwegoFormula.LT_HYPHEN_GT = 57;
FwegoFormula.LT_LT = 58;
FwegoFormula.LT_LT_EQ = 59;
FwegoFormula.LT_QMARK_GT = 60;
FwegoFormula.MINUS = 61;
FwegoFormula.PERCENT = 62;
FwegoFormula.PIPE = 63;
FwegoFormula.PIPE_PIPE = 64;
FwegoFormula.PIPE_PIPE_SLASH = 65;
FwegoFormula.PIPE_SLASH = 66;
FwegoFormula.PLUS = 67;
FwegoFormula.QMARK = 68;
FwegoFormula.QMARK_AMP = 69;
FwegoFormula.QMARK_HASH = 70;
FwegoFormula.QMARK_HYPHEN = 71;
FwegoFormula.QMARK_PIPE = 72;
FwegoFormula.SLASH = 73;
FwegoFormula.TIL = 74;
FwegoFormula.TIL_EQ = 75;
FwegoFormula.TIL_GTE_TIL = 76;
FwegoFormula.TIL_GT_TIL = 77;
FwegoFormula.TIL_LTE_TIL = 78;
FwegoFormula.TIL_LT_TIL = 79;
FwegoFormula.TIL_STAR = 80;
FwegoFormula.TIL_TIL = 81;
FwegoFormula.SEMI = 82;
FwegoFormula.ErrorCharacter = 83;

FwegoFormula.RULE_root = 0;
FwegoFormula.RULE_expr = 1;
FwegoFormula.RULE_ws_or_comment = 2;
FwegoFormula.RULE_func_name = 3;
FwegoFormula.RULE_field_reference = 4;
FwegoFormula.RULE_identifier = 5;

class RootContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = FwegoFormula.RULE_root;
    }

	expr() {
	    return this.getTypedRuleContext(ExprContext,0);
	};

	EOF() {
	    return this.getToken(FwegoFormula.EOF, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterRoot(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitRoot(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitRoot(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class ExprContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = FwegoFormula.RULE_expr;
    }



		copyFrom(ctx) {
			super.copyFrom(ctx);
		}

}


class FieldReferenceContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	FIELD() {
	    return this.getToken(FwegoFormula.FIELD, 0);
	};

	OPEN_PAREN() {
	    return this.getToken(FwegoFormula.OPEN_PAREN, 0);
	};

	field_reference() {
	    return this.getTypedRuleContext(Field_referenceContext,0);
	};

	CLOSE_PAREN() {
	    return this.getToken(FwegoFormula.CLOSE_PAREN, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterFieldReference(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitFieldReference(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitFieldReference(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.FieldReferenceContext = FieldReferenceContext;

class StringLiteralContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	SINGLEQ_STRING_LITERAL() {
	    return this.getToken(FwegoFormula.SINGLEQ_STRING_LITERAL, 0);
	};

	DOUBLEQ_STRING_LITERAL() {
	    return this.getToken(FwegoFormula.DOUBLEQ_STRING_LITERAL, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterStringLiteral(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitStringLiteral(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitStringLiteral(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.StringLiteralContext = StringLiteralContext;

class BracketsContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	OPEN_PAREN() {
	    return this.getToken(FwegoFormula.OPEN_PAREN, 0);
	};

	expr() {
	    return this.getTypedRuleContext(ExprContext,0);
	};

	CLOSE_PAREN() {
	    return this.getToken(FwegoFormula.CLOSE_PAREN, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterBrackets(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitBrackets(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitBrackets(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.BracketsContext = BracketsContext;

class BooleanLiteralContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	TRUE() {
	    return this.getToken(FwegoFormula.TRUE, 0);
	};

	FALSE() {
	    return this.getToken(FwegoFormula.FALSE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterBooleanLiteral(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitBooleanLiteral(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitBooleanLiteral(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.BooleanLiteralContext = BooleanLiteralContext;

class RightWhitespaceOrCommentsContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	expr() {
	    return this.getTypedRuleContext(ExprContext,0);
	};

	ws_or_comment() {
	    return this.getTypedRuleContext(Ws_or_commentContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterRightWhitespaceOrComments(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitRightWhitespaceOrComments(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitRightWhitespaceOrComments(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.RightWhitespaceOrCommentsContext = RightWhitespaceOrCommentsContext;

class DecimalLiteralContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	NUMERIC_LITERAL() {
	    return this.getToken(FwegoFormula.NUMERIC_LITERAL, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterDecimalLiteral(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitDecimalLiteral(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitDecimalLiteral(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.DecimalLiteralContext = DecimalLiteralContext;

class LeftWhitespaceOrCommentsContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	ws_or_comment() {
	    return this.getTypedRuleContext(Ws_or_commentContext,0);
	};

	expr() {
	    return this.getTypedRuleContext(ExprContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterLeftWhitespaceOrComments(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitLeftWhitespaceOrComments(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitLeftWhitespaceOrComments(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.LeftWhitespaceOrCommentsContext = LeftWhitespaceOrCommentsContext;

class FunctionCallContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	func_name() {
	    return this.getTypedRuleContext(Func_nameContext,0);
	};

	OPEN_PAREN() {
	    return this.getToken(FwegoFormula.OPEN_PAREN, 0);
	};

	CLOSE_PAREN() {
	    return this.getToken(FwegoFormula.CLOSE_PAREN, 0);
	};

	expr = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExprContext);
	    } else {
	        return this.getTypedRuleContext(ExprContext,i);
	    }
	};

	COMMA = function(i) {
		if(i===undefined) {
			i = null;
		}
	    if(i===null) {
	        return this.getTokens(FwegoFormula.COMMA);
	    } else {
	        return this.getToken(FwegoFormula.COMMA, i);
	    }
	};


	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterFunctionCall(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitFunctionCall(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitFunctionCall(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.FunctionCallContext = FunctionCallContext;

class FieldByIdReferenceContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	FIELDBYID() {
	    return this.getToken(FwegoFormula.FIELDBYID, 0);
	};

	OPEN_PAREN() {
	    return this.getToken(FwegoFormula.OPEN_PAREN, 0);
	};

	INTEGER_LITERAL() {
	    return this.getToken(FwegoFormula.INTEGER_LITERAL, 0);
	};

	CLOSE_PAREN() {
	    return this.getToken(FwegoFormula.CLOSE_PAREN, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterFieldByIdReference(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitFieldByIdReference(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitFieldByIdReference(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.FieldByIdReferenceContext = FieldByIdReferenceContext;

class LookupFieldReferenceContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	LOOKUP() {
	    return this.getToken(FwegoFormula.LOOKUP, 0);
	};

	OPEN_PAREN() {
	    return this.getToken(FwegoFormula.OPEN_PAREN, 0);
	};

	field_reference = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(Field_referenceContext);
	    } else {
	        return this.getTypedRuleContext(Field_referenceContext,i);
	    }
	};

	COMMA() {
	    return this.getToken(FwegoFormula.COMMA, 0);
	};

	CLOSE_PAREN() {
	    return this.getToken(FwegoFormula.CLOSE_PAREN, 0);
	};

	WHITESPACE() {
	    return this.getToken(FwegoFormula.WHITESPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterLookupFieldReference(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitLookupFieldReference(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitLookupFieldReference(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.LookupFieldReferenceContext = LookupFieldReferenceContext;

class IntegerLiteralContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        super.copyFrom(ctx);
    }

	INTEGER_LITERAL() {
	    return this.getToken(FwegoFormula.INTEGER_LITERAL, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterIntegerLiteral(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitIntegerLiteral(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitIntegerLiteral(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.IntegerLiteralContext = IntegerLiteralContext;

class BinaryOpContext extends ExprContext {

    constructor(parser, ctx) {
        super(parser);
        this.op = null; // Token;
        super.copyFrom(ctx);
    }

	expr = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(ExprContext);
	    } else {
	        return this.getTypedRuleContext(ExprContext,i);
	    }
	};

	SLASH() {
	    return this.getToken(FwegoFormula.SLASH, 0);
	};

	STAR() {
	    return this.getToken(FwegoFormula.STAR, 0);
	};

	PLUS() {
	    return this.getToken(FwegoFormula.PLUS, 0);
	};

	MINUS() {
	    return this.getToken(FwegoFormula.MINUS, 0);
	};

	AMP_AMP() {
	    return this.getToken(FwegoFormula.AMP_AMP, 0);
	};

	PIPE_PIPE() {
	    return this.getToken(FwegoFormula.PIPE_PIPE, 0);
	};

	GT() {
	    return this.getToken(FwegoFormula.GT, 0);
	};

	LT() {
	    return this.getToken(FwegoFormula.LT, 0);
	};

	GTE() {
	    return this.getToken(FwegoFormula.GTE, 0);
	};

	LTE() {
	    return this.getToken(FwegoFormula.LTE, 0);
	};

	EQUAL() {
	    return this.getToken(FwegoFormula.EQUAL, 0);
	};

	BANG_EQUAL() {
	    return this.getToken(FwegoFormula.BANG_EQUAL, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterBinaryOp(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitBinaryOp(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitBinaryOp(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}

FwegoFormula.BinaryOpContext = BinaryOpContext;

class Ws_or_commentContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = FwegoFormula.RULE_ws_or_comment;
    }

	BLOCK_COMMENT() {
	    return this.getToken(FwegoFormula.BLOCK_COMMENT, 0);
	};

	LINE_COMMENT() {
	    return this.getToken(FwegoFormula.LINE_COMMENT, 0);
	};

	WHITESPACE() {
	    return this.getToken(FwegoFormula.WHITESPACE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterWs_or_comment(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitWs_or_comment(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitWs_or_comment(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class Func_nameContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = FwegoFormula.RULE_func_name;
    }

	identifier() {
	    return this.getTypedRuleContext(IdentifierContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterFunc_name(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitFunc_name(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitFunc_name(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class Field_referenceContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = FwegoFormula.RULE_field_reference;
    }

	SINGLEQ_STRING_LITERAL() {
	    return this.getToken(FwegoFormula.SINGLEQ_STRING_LITERAL, 0);
	};

	DOUBLEQ_STRING_LITERAL() {
	    return this.getToken(FwegoFormula.DOUBLEQ_STRING_LITERAL, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterField_reference(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitField_reference(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitField_reference(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class IdentifierContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = FwegoFormula.RULE_identifier;
    }

	IDENTIFIER() {
	    return this.getToken(FwegoFormula.IDENTIFIER, 0);
	};

	IDENTIFIER_UNICODE() {
	    return this.getToken(FwegoFormula.IDENTIFIER_UNICODE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.enterIdentifier(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof FwegoFormulaListener ) {
	        listener.exitIdentifier(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof FwegoFormulaVisitor ) {
	        return visitor.visitIdentifier(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}




FwegoFormula.RootContext = RootContext;
FwegoFormula.ExprContext = ExprContext;
FwegoFormula.Ws_or_commentContext = Ws_or_commentContext;
FwegoFormula.Func_nameContext = Func_nameContext;
FwegoFormula.Field_referenceContext = Field_referenceContext;
FwegoFormula.IdentifierContext = IdentifierContext;
