import ply.yacc as yacc

from lex_formuleLogique import tokens

# ordre et privilege et associabilite a gauche ou droite
precedence = (
	('right', 'IMPL'),
	('left', 'OR'),
	('left', 'AND'),
	('right', 'NOT')
)

def p_formulePAR(f):
	'''formule : LPAR formule RPAR'''
	f[0] = "(" + f[2] + ")"
	print "Formule reconnu : " + f[0]
#end func

def p_formuleNOT(f):
	'''formule : NOT formule'''
	f[0] = "!" + f[2]
	print "Formule reconnu : " + f[0]
#end func

def p_formuleOPER(f):
	'''formule : formule oper formule'''
	f[0] = f[1] + " " + f[2] + " " + f[3]
#end func

def p_formuleVAR(f):
	'''formule : var formule'''
	f[0] = f[1] + " " + f[2]
#end func

def p_formulePred(f):
	'''formule : pred'''
	f[0] = 

#------------------------------------------------ PREDICAT --------------------------------------------------------


def p_predNarg(p):
	'''pred : ID LPAR arg RPAR'''
	#	-- p[0] = function p[1]
	p[0] = p[1] + "(" + p[3] + p[4] + ")"
#end func


def p_arg(p):
	'''arg 	:  ID SEP arg
			| arg
			| empty
	'''
	if len(p) == 4:
		p[0] = ", " + p[2] + p[3]
	else:
		p[0] = ""
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
