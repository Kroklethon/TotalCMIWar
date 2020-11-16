def creecase(var_pour_gen, posx, posy,tableau):
	case_tabl = tableau[pox][posy]
	if case_tabl.statue == 'montagne' :
		pygame.draw.rect(screen, main_var.montagne, rect, var_pour_gen)
	elif case_tabl.statue == 'joueur_1':
		pygame.draw.rect(screen, main_var.joueur_1, rect, var_pour_gen)
	elif case_tabl.statue == 'joueur_2':
		pygame.draw.rect(screen, main_var.joueur_2, rect, var_pour_gen)
	else:
		pygame.draw.rect(screen, main_var.white, rect, var_pour_gen)
