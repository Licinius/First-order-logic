import ply.yacc as yacc

from lex_formuleLogique import tokens

# ordre et privilege et associabilite a gauche ou droite
precedence = (
	('right', 'IMPL'),
	('left', 'OR'),
	('left', 'AND'),
	('right', 'NOT')
)

def p_formule(f):
	'''formule  : LPAR formule RPAR
				| var listPred1
	'''
	if len(f) == 4:
		f[0] = "(" + f[2] + ")"
	else:
		f[0] = f[1] + " " + f[2]
	
	print("J'ai reconnu : " + f[0])
#end func

#------------------------------------------------ PREDICAT --------------------------------------------------------

def p_pred1(p):
	'''listPred1 : listPred1 listPred2
				 | LPAR listPred1 RPAR
				 | pred
	'''
	if len(p) == 3:
		p[0] = p[1] + " " + p[2]
	else:
		p[0] = p[1]
	
#end func

def p_pred2(p):
	'''listPred2 : oper listPred1
				 | empty
	'''
	if len(p) == 3:
		p[0] = p[1] + " " + p[2]
	else:
		p[0] = ""
#end func

def p_predNarg(p):
	'''pred : ID LPAR ID arg RPAR'''
	#	-- p[0] = function p[1]
	p[0] = p[1] + "(" + p[3] + p[4] + ")"
#end func

def p_arg(p):
	'''arg 	: SEP ID arg
			| empty
	'''
	if len(p) == 4:
		p[0] = ", " + p[2] + p[3]
	else:
		p[0] = ""
#end func

def p_NOTpred(p):
	'''pred : NOT pred'''
	#	--	p[0] = node not -> node p[2]
	p[0] = "!" + p[2]
#end func

#------------------------------------------------- OPERATEUR ------------------------------------------------------

def p_oper_OR(op):
	'''oper : OR'''
	#	--	op[0] = node OU
	op[0] = op[1]
#end func

def p_oper_AND(op):
	'''oper : AND'''
	#	--	op[0] = node ET
	op[0] = op[1]
#end func

def p_oper_IMPL(op):
	'''oper : IMPL'''
	#	--	op[0] = node IMPL
	op[0] = op[1]
#end func

#--------------------------------------------------- RESTE --------------------------------------------------------

def p_var(v):
	'''var 	: QUANT ID var
			| empty'''
	#	--	v[0] = node v[1] relier a node v[2]
	if len(v) == 4:
		v[0] = v[1] + v[2] + " " + v[3]
	else:
		v[0] = ""
#end func

def p_empty(e):
	'''empty :'''
	pass
#end func

def p_error(p):
	print( "Erreur synthaxe ! Le caractere '" + p.value + "' n'etait pas attendu ici")
	exit(-1)
#end func

# lancement du parseur
parser = yacc.yacc(tabmodule='parserTab')
