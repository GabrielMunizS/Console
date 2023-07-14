import random
def Roberto ():
  fuga = 0
  while fuga < 1:

    resposta = input("enter command: ")

    if resposta == "/help":
      print("/printrn                 prints a random number")
      print("/cowboyh                 prints a cowboy hat")
      print("/ijdk                    prints something special")
      print("/close                    close the app")
    elif resposta == "/printrn":
      numero_aleatorio = random.randint(0, 10)
      print(numero_aleatorio)
    elif resposta == "/cowboyh":
      print("                                    ▒▒▒▒        ▒▒▒▒                                    ")
      print("                                  ▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒                                  ")
      print("                                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                  ")
      print("                                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                  ")
      print("                                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                ")
      print("                  ▒▒▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          ▒▒▒▒                  ")
      print("                  ▒▒▒▒▒▒        ████████████████████████        ▒▒▒▒▒▒                  ")
      print("                    ▒▒▒▒▒▒▒▒▒▒▒▒████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒                    ")
      print("                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒                      ")
      print("                          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                          ")
      print("                                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                ")
    elif resposta == "/ijdk":
      print("You, you are special <3")
    elif resposta == "/close":
      fuga =+ 1
    else:
      print(resposta + " is not a real answer try tiping /help insteady")
