print("olá jovem guerreiro para iniciar suas aventurar no incrivel mundo de Eldramar")
nick = input("para começar digite o seu nick ")
print(f"exelente, {nick}")
while True:
    classe =input("agora para prosseguimos escolha uma classe. ladino/barbaro/mago ").strip().lower()
    if classe in ["ladino","barbaro","mago"]:
        print(f"exelente {nick} O {classe}")
        break
    else: print("escolha uma classe valida.")
print("voce está na entrada do reino de feynore um lugar totalmente desconhecido")
print("voce ve uns guardas e decide ir falar com eles")
print(f"{nick}: olá senhor meu nome é {nick} eu estou perdido o senhor poderia me ajudar?")
print("guarda1: olá jovem florasteiro seja bem vindo ao reino de feynore eu sou chefe da 3 divisao de guardas do rei, me chamo Thalen Grimward, mas pode me chamar de Thalen")
feynore1 = input(f"deseja entrar no reino de feynore {nick}? (sim/nao) ").strip().lower()
if feynore1 == "sim":
    print(f"seja bem vindo {nick}.")
    print("caminhando nas ruas medievais do reino de feynore voce se depara com uma taverna e decide entrar")
    print("ja dentro da taverna voce encosta na parede e aguarda alguma coisa acontecer, quanto derrepende voce ouve duas pessoas conversando")
    print("pessoa1: voce viu que o rei esta fazendo um torneio?")
    print("pessoa2: nao, que torneio é esse?")
    print("pessoa1: é um torneio para assumir o lugar de um dos chefes da guarda do rei que faleceu em batalha voce pode se inscrever a qualquer momento com o Thalen")
    print("pessoa1: porem tem que ser no minimo lv 2")
    print("após ouvir isso voce sai do reino em busca de chegar ao lv 2")
else:
    print(f"ok {nick}, volte quando quiser.")
    print("ao sair do reino voceee ve duas pessoas fofocando sobre um torneio que o rei ira fazer")
    print("voce pode saber mais sobre o torneio falando com Thalen.")
xp = 0
lv = 1
def subir_de_nivel():
    global lv, xp
    if xp >= 10:
        lv = lv + 1
        print("parabens voce chegou ao lv 2")
    xp_necessario = lv * 10
    while xp >= xp_necessario:
        xp -= xp_necessario
        lv = lv + 1
        print(f"parabens voce chegou a o lv {lv}")
   
print("voce estava caminhando pela floresta quando derrepende voce encontra um goblin roubando o tesouro de um viajante")
print("voce pode reeagir:")
print("1 atacar o goblin furtivamente")
print("2 chamar o goblin e o atacar")
reaçao =input("como deseja reagir? (1/2) ").strip().lower()
if reaçao == "1":
    if classe == "mago":
        print("voce pega seu cajado, e conjura um ataque de mana grande")
        print("voce derrotou o goblin")
        print("viajante: obrigado senhor tome isso com recompensa")
        print("parabens voce conseguiu +10 xp e 10 moeda de prata")
        xp += 10
        subir_de_nivel()
    elif classe == "ladino":
        print("voce pega sua adaga e apunhala o goblin pela as costas bem na garganta")
        print("voce derrotou o goblin")
        print("viajante: obrigado senhor tome isso com recompensa")
        print("parabens voce conseguiu +10 xp e 10 moeda de prata")
        xp += 10
        subir_de_nivel()
    elif classe == "barbaro":
        print("voce pega seu machado e crava se machado nas costas do goblin")
        print("voce derrotou o goblin")
        print("viajante: obrigado senhor tome isso com recompensa")
        print("parabens voce conseguiu +10 xp e 10 moeda de prata")
        xp += 10
        subir_de_nivel()
if reaçao == "2":
    if classe == "barbaro":
        print("voce da um grito amedrontando o goblin ele foge sem nem lutar")
        print("voce derrotou o goblin")
        print("viajante: obrigado senhor tome isso com recompensa")
        print("parabens voce conseguiu +10 xp e 10 moeda de prata")
        xp += 10
        subir_de_nivel()
    elif classe == "ladino":
        print("voce rapidamente cutuca o goblin")
        print("ele olha para tras desesprado")
        print("voce usa sua adaga para fazer um corte na garganta do goblin")
        print("voce derrotou o goblin")
        print("viajante: obrigado senhor tome isso com recompensa")
        print("parabens voce conseguiu +10 xp e 10 moeda de prata")
        xp += 10
        subir_de_nivel()
    elif classe  == "mago":
        print("voce começa a pronunciar um frase em latim")
        print("o g oblin olha para tras com uma expressao aterrorizada")
        print("voce lança um feitiço de gelo, congelando o goblin")
        print("voce derrotou o goblin")
        print("viajante: obrigado senhor tome isso com recompensa")
        print("parabens voce conseguiu +10 xp e 10 moeda de prata")
        xp += 10
        subir_de_nivel()
print("voltando para o reino de feynore voce se depara com um feirante e vai falar com ele")
print("feirante: olá viajante, o que procura?")
Compras = ["pedra de amolar", "runa de mana"]
print(f"{nick}:olá senhor procuro algum recurso.")
if classe == "mago":
    print("feirante: recomendo a runa de  mana")
    print(Compras)
elif classe == "ladino":
    print("feirante: recomendo a pedra de amolar")
    print(Compras)
elif classe  == "barbaro":
    print("feirante: recomendo a pedra de amolar")
    print(Compras)
print("feirante: cada item custa 10 moedas de prata")
while  True:
    feirante = input("deseja comprar algo? (sim/nao) ").strip().lower()
    if feirante == "nao":
        print("feirante: ok, volte sempre")
        break
    elif feirante == "sim":
        print("o que deseja comprar? ")
        feirante2  = input("pedra de amolar ou runa de mana (1/2) ")
    if feirante2 == "1":
            print("obrigado, volte sempre!")
            break
    elif feirante2 == "2":
            print("obrigado, volte sempre!")
            break
    if feirante2 == "2":
     print("a runa aumentou seu dano magico em 10%")
    elif feirante2 == "1":
     if classe == "ladino":
        print("a pedra afiou a sua adaga +10 de dano fisico")
    elif classe == "barbaro":
        print("a pedra afiou o seu machado +10 de dano fisico")

print("enquanto caminhava de volta ao reino voce encontra o Thalen e ele vem falar com voce")
print(f"Thalen: olá {nick}, quanto tempo vejo que ficou mais forte ")
while True:
    torneiopt1 = input("o rei está fazendo um torneio de força, deseja se inscrever? (sim/nao)").strip().lower()
    if torneiopt1 == "sim":
        print("exelente o torneio começa em dois dias, pode treinar até la")
        break
    elif torneiopt1 == "nao":
        print("ok, voce tem dois dias para mudar de ideia")
        break
