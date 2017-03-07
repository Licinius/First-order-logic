import ply.lex as lex

# tokens utlises par yacc
tokens = (
	'NOT',
	'OR',
	'AND',
	'IMPL',
	'ID',
	'LPAR',
	'RPAR',
	'QUANT',
	'SEP'
)

t_AND	= r'&{1,2}' 			# & ou &&
t_OR	= r'\|{1,2}'			# | ou ||
t_IMPL	= r'>{1,2}|[-][>]'		# > ou >> ou ->
t_NOT	= r'[!~]'				# ! ou ~
t_LPAR	= r'\('					# (
t_RPAR	= r'\)'					# )
t_ID	= r'[a-z][a-z0-9]*'		# une lettre minuscule suivit de lettres minuscules et/ou chiffres (ex: var2)
t_QUANT	= r'[VE]'				# V (pour tout) ou E (il existe)
t_SEP	= r'[.,:;]'				# . ou , ou : ou ;

t_ignore = ' \t'				#ignore les espaces et les tabulations

def t_error(t):
	print("Charactere inconnu : '%s'" % t.value[0])
	exit(-1)
# end function

# lancement de la tokenisation
lex.lex() 
