from yacc_formuleLogique import parser

f = raw_input('Formule : ')
# f = "Vx Ey (carre(x) && rond(y)) >> relier(x,y)"
parser.parse(f)
exit(0)