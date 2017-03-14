import ply.yacc as yacc

from lex_formuleLogique import tokens
from Formule_Logique.Couple import Couple
from Formule_Logique.Quantificateur import Quantificateur
from Formule_Logique.Connecteur import Connecteur
from Formule_Logique.Predicat import Predicat
from Formule_Logique.Noeud_Binaire import Noeud_Binaire
from Formule_Logique.Noeud_Unaire import Noeud_Unaire
from Formule_Logique.Connecteur_Unaire import Connecteur_Unaire
from Formule_Logique.ListPredicats import ListPredicats

# ordre et privilege et associabilite a gauche ou droite
precedence = (
	('right', 'IMPL'),
	('left', 'OR'),
	('left', 'AND'),
	('right', 'NOT')
)
#def ligne(l):
#	'''ligne : formule \r | formule \n | formule'''
#	print(l[1])
#	l[0]=l[1]
#end func

def p_formulePAR(f):
	'''formule : LPAR formule RPAR'''
	f[0]=f[2]
#end func

def p_formuleNOT(f):
	'''formule : NOT formule'''
	f[0]=Noeud_Unaire(Connecteur_Unaire.NEG,f[1])
#end func

def p_formuleOPER(f):
	'''formule : formule oper formule'''
	f[0]= Noeud_Binaire(f[2],g=f[1],d=f[3])
#end func

def p_formuleVAR(f):
	'''formule : var formule'''
	f[0]=Noeud_Unaire(f[1],g=f[2])
#end func

def p_formulePred(f):
	'''formule : pred'''
	
	f[0]=Noeud_Unaire(f[1])
#end func 

#------------------------------------------------ PREDICAT --------------------------------------------------------


def p_predNarg(p):
	'''pred : ID LPAR ID listarg RPAR'''
	
	arg = []
	arg.append(p[3])
	arg.extend(p[4])
	nameFunction = p[1] + "_" + str(len(arg))
	function = ListPredicats.dic[nameFunction].getFunction()
	p[0]=Predicat(p[1],listPred=arg,fun=function)
#end func

def p_listarg(arg):
	''' listarg : SEP ID listarg
				| empty'''
	tmp =[]
	if(len(arg) == 4):
		tmp.extend(arg[2])
		tmp.extend(arg[3])
	arg[0] =tmp
#end func
	


#------------------------------------------------- OPERATEUR ------------------------------------------------------

def p_oper_OR(op):
	'''oper : OR'''
	op[0] = Connecteur.OU
#end func

def p_oper_AND(op):
	'''oper : AND'''
	op[0]=Connecteur.ET
#end func

def p_oper_IMPL(op):
	'''oper : IMPL'''
	op[0]=Connecteur.IMP

#end func

#--------------------------------------------------- RESTE --------------------------------------------------------

def p_var(v):
	'''var 	: QUANT ID '''
	
	if(v[1]=='V'):
		v[0]= Couple(Quantificateur.pour_tout,v[2])
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
