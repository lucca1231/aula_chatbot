# https://chatterbot.readthedocs.io/en/stable/index.html

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *
import time

### ChatBot ###
perguntas = [
    "Qual é o valor de Pi (π) até 5 casas decimais?",
    "Quantos lados tem um hexágono?",
    "O que é uma equação do segundo grau?",
    "Qual é a fórmula para calcular a área de um círculo?",
    "Qual é o valor de √144?",
    "O que é um número primo?",
    "O que é uma progressão aritmética?",
    "Qual é o teorema de Pitágoras?",
    "Qual é a fórmula para calcular a área de um triângulo?",
    "O que é a constante de Euler (e)?",
    "O que é uma função exponencial?",
    "O que é uma matriz inversa?",
    "O que é uma equação linear?",
    "Qual é o valor de 2³?",
    "Qual é a fórmula para a soma de uma progressão aritmética?",
    "O que é uma função trigonométrica?",
    "Qual é a derivada de f(x) = x²?",
    "O que é uma integral definida?",
    "O que é um número irracional?",
    "Qual é a diferença entre velocidade e aceleração?",
    "Quem é o capitão dos Piratas do Chapéu de Palha?",
    "Qual é o sonho de Monkey D. Luffy?",
    "Quem é o arqueólogo do bando de Luffy?",
    "Qual fruta do diabo Luffy comeu?",
    "Qual é o nome do navio dos Piratas do Chapéu de Palha?",
    "Quem é o espadachim do bando de Luffy?",
    "Qual é o nome da fruta do diabo de Zoro?",
    "Qual é o nome do melhor amigo de Luffy?",
    "Quem foi o primeiro membro a se juntar ao bando de Luffy?",
    "Qual é o nome do pai de Luffy?",
    "Qual é a posição de Nami no bando de Luffy?",
    "Qual é o nome da ilha onde Luffy encontrou Robin?",
    "Quem é o comandante da primeira divisão dos Piratas do Barba Branca?",
    "Qual é o nome do inimigo principal durante a saga de Alabasta?",
    "Quem foi o primeiro Yonkou a ser derrotado por Luffy?",
    "Qual é o nome da organização criminosa que tem como líder Donquixote Doflamingo?",
    "Qual é o nome da técnica de Zoro que envolve cortar várias coisas de uma vez?",
    "Quem é o atual líder dos Revolucionários?",
    "Qual é o nome da ilha onde Luffy enfrenta Crocodile pela primeira vez?",
    "Qual é a maior recompensa de todos os tempos no mundo de One Piece?",
    "Quem é o protagonista principal de Dragon Ball Z?",
    "Qual é o nome do pai de Goku?",
    "Qual é o nome do vilão principal de Dragon Ball Z?",
    "Quem foi o primeiro personagem a se transformar em Super Saiyajin?",
    "Qual é a técnica de luta mais famosa de Goku?",
    "Quem é o príncipe dos Saiyajins?",
    "Qual é o nome do filho de Goku e Chi-Chi?",
    "O que é a Genki Dama?",
    "Quem foi o responsável pela morte de Goku no começo da série?",
    "Qual é o nome da transformação de Vegeta que o torna mais forte?",
    "Quem são os filhos de Vegeta?",
    "O que acontece quando um Saiyajin se transforma em Super Saiyajin?",
    "Quem foi o vilão que Goku enfrentou na luta mais épica de Dragon Ball Z?",
    "Qual é o nome do mestre de Goku quando ele era mais jovem?",
    "O que é a técnica Kamehameha?",
    "Quem é o ser mais forte do universo em Dragon Ball Z?",
    "Qual é o nome do planeta natal de Goku?",
    "Quem é o líder dos Androides em Dragon Ball Z?",
    "O que é o Dragon Shenlong e como ele é invocado?"
]


    
respostas = [
    "O valor de Pi (π) até 5 casas decimais é 3,14159.",
    "Um hexágono possui 6 lados.",
    "Uma equação do segundo grau é uma equação polinomial de grau 2, geralmente representada por ax² + bx + c = 0.",
    "A fórmula para calcular a área de um círculo é A = πr², onde r é o raio.",
    "O valor de √144 é 12.",
    "Um número primo é um número maior que 1 que só é divisível por 1 e por ele mesmo.",
    "Uma progressão aritmética (PA) é uma sequência numérica em que a diferença entre termos consecutivos é constante.",
    "O teorema de Pitágoras afirma que, em um triângulo retângulo, a soma dos quadrados dos catetos é igual ao quadrado da hipotenusa: a² + b² = c².",
    "A fórmula para calcular a área de um triângulo é A = (base × altura) / 2.",
    "A constante de Euler (e) é aproximadamente 2,71828 e é a base do logaritmo natural.",
    "Uma função exponencial é uma função matemática na forma f(x) = a^x, onde a é uma constante positiva.",
    "A matriz inversa é uma matriz que, quando multiplicada por uma matriz original, resulta na matriz identidade.",
    "Uma equação linear é uma equação polinomial de grau 1, na forma ax + b = 0.",
    "O valor de 2³ é 8.",
    "A fórmula para a soma de uma progressão aritmética é S = n/2 × (a₁ + aₙ), onde n é o número de termos, a₁ é o primeiro termo e aₙ é o último.",
    "Uma função trigonométrica é uma função matemática que relaciona os ângulos de um triângulo retângulo com as razões entre os seus lados (ex.: seno, cosseno, tangente).",
    "A derivada de f(x) = x² é f'(x) = 2x.",
    "Uma integral definida é uma operação que calcula a área sob a curva de uma função entre dois limites.",
    "Um número irracional é um número que não pode ser expresso como uma fração exata, e sua representação decimal é infinita e não periódica.",
    "A velocidade é a razão de deslocamento em relação ao tempo, enquanto a aceleração é a taxa de variação da velocidade ao longo do tempo."
    "O capitão dos Piratas do Chapéu de Palha é Monkey D. Luffy.",
    "O sonho de Luffy é se tornar o Rei dos Piratas.",
    "A arqueóloga do bando de Luffy é Nico Robin.",
    "Luffy comeu a Gomu Gomu no Mi (Fruta Gomu Gomu).",
    "O nome do navio dos Piratas do Chapéu de Palha é Going Merry (e depois Thousand Sunny).",
    "O espadachim do bando de Luffy é Roronoa Zoro.",
    "Zoro comeu a fruta do diabo de nome Sandai Kitetsu, uma espada amaldiçoada, não uma fruta do diabo.",
    "O melhor amigo de Luffy é o espadachim Roronoa Zoro.",
    "O primeiro membro a se juntar ao bando de Luffy foi Roronoa Zoro.",
    "O pai de Luffy é Monkey D. Dragon.",
    "A posição de Nami no bando de Luffy é navegadora.",
    "O nome da ilha onde Luffy encontrou Robin é a Ilha de Alabasta.",
    "O comandante da primeira divisão dos Piratas do Barba Branca é Marco, a Fênix.",
    "O inimigo principal durante a saga de Alabasta é Crocodile.",
    "O primeiro Yonkou a ser derrotado por Luffy foi Kaido.",
    "A organização criminosa liderada por Donquixote Doflamingo é chamada de Donquixote Pirates.",
    "A técnica de Zoro que envolve cortar várias coisas de uma vez é chamada de Santoryu (estilo das três espadas).",
    "O líder dos Revolucionários é Monkey D. Dragon.",
    "A ilha onde Luffy enfrenta Crocodile pela primeira vez é a Ilha de Alabasta.",
    "A maior recompensa de todos os tempos no mundo de One Piece é a de Gol D. Roger, que foi de 5.564.800.000 berries.",
    "O protagonista principal de Dragon Ball Z é Goku.",
    "O pai de Goku é Bardock.",
    "O vilão principal de Dragon Ball Z é Freeza (durante a maior parte da saga).",
    "O primeiro personagem a se transformar em Super Saiyajin foi Goku.",
    "A técnica de luta mais famosa de Goku é o Kamehameha.",
    "O príncipe dos Saiyajins é Vegeta.",
    "O filho de Goku e Chi-Chi é Gohan.",
    "A Genki Dama é uma técnica de energia onde Goku coleta energia de todos os seres vivos para lançar uma poderosa esfera de energia.",
    "Raditz, o irmão de Goku, foi o responsável pela morte de Goku no começo da série.",
    "A transformação de Vegeta que o torna mais forte é o Super Saiyajin.",
    "Os filhos de Vegeta são Trunks e Bra (ou Bulla, dependendo da versão).",
    "Quando um Saiyajin se transforma em Super Saiyajin, ele ganha um aumento massivo de poder, com cabelo dourado e olhos verdes ou azuis.",
    "O vilão que Goku enfrentou na luta mais épica de Dragon Ball Z foi Freeza.",
    "O mestre de Goku quando ele era mais jovem era o Mestre Kame (Muten Roshi).",
    "A técnica Kamehameha é uma onda de energia concentrada que Goku aprendeu com o Mestre Kame.",
    "O ser mais forte do universo em Dragon Ball Z é, teoricamente, o próprio Goku após atingir o Super Saiyajin 3, mas durante a saga, o ser mais forte era Freeza, depois Goku e Vegeta.",
    "O planeta natal de Goku é o planeta Vegeta, o planeta dos Saiyajins.",
    "O líder dos Androides em Dragon Ball Z é o Dr. Gero, que criou os androides.",
    "O Dragon Shenlong é o dragão que é invocado quando as Esferas do Dragão são reunidas. Ele pode realizar um desejo, mas desaparece depois de ser invocado."
]

base_treino_teste = []
for i in range(len(perguntas)):
    base_treino_teste.append(perguntas[i])
    base_treino_teste.append(respostas[i])

time.clock = time.time
bot = ChatBot('ChatBot')
bot.storage.drop()
trainer = ListTrainer(bot)
trainer.train(base_treino_teste)
#pergunta = input("Qual a sua dúvida:")
#resposta = bot.get_response(pergunta)
#print(bot.get_response(pergunta))
#print(str(resposta.confidence*100) + " %")
### GUI ###
janela = Tk()
janela.geometry("500x450+540+0")

txt = Text(height=10, width=61, background="darkgreen")
txt.grid(row=0,column=0)
txt.configure(state=DISABLED)

txt_send = Text(height=3, width=61, background="white")
txt_send.grid(row=2,column=0)

btn_send = Button(height=2, width=61, background="white", text="Enviar", fg="blue", command= lambda : enviar())
btn_send.grid(row=3,column=0)

#pergunta = input("Qual a sua dúvida:")
#resposta = bot.get_response(pergunta)
#print(bot.get_response(pergunta))
#print(str(resposta.confidence*100) + " %")

def enviar():
    txt.configure(state=NORMAL)
    txt.insert(END,"Eu disse: " + txt_send.get('1.0',END))
    pergunta = txt_send.get('1.0',END)
    txt_send.delete('1.0',END)
    txt.configure(state=DISABLED)
    resposta(pergunta)

def resposta(perg):
    txt.configure(state=NORMAL)
    txt.insert(END,"CHAT-BOT Disse: " + str(bot.get_response(perg)) + "\n")
    txt.insert(END,str(bot.get_response(perg).confidence*100) + " %\n")
    txt_send.delete('1.0',END)
    txt.configure(state=DISABLED)

janela.mainloop()