print("PROGRAMA PARA CONVERTER TEMPERATURAS DE UMA UNIDADE PARA OUTRA")
FimDoPrograma = False

while not FimDoPrograma:

    print ("1)  Converter de Graus Celsius    para Graus Fahrenheit")
    print ("2)  Converter de Graus Fahrenheit para Graus Celsius")
    print ("3)  Converter de Graus Celsius    para Graus Kelvin")
    print ("4)  Converter de Graus Kelvin     para Graus Celsius")
    print ("5)  Converter de Graus Celsius    para Graus Rankine")
    print ("6)  Converter de Graus Rankine    para Graus Celsius")
    print ("7)  Converter de Graus Fahrenheit para Graus Kelvin")
    print ("8)  Converter de Graus Kelvin     para Graus Fahrenheit")
    print ("9)  Converter de Graus Fahrenheit para Graus Rankine")
    print ("10) Converter de Graus Rankine    para Graus Fahrenheit")
    print ("11) Finalizar programa!")
    opcao=input("Digite a sua opção: ")
    print("\n")

    if opcao=="1":
        try:
            celsius=float(input("Digite a temperatura em °C: "))
            fahrenheit=9/5*celsius+32
            print(f'{celsius}°C equivalem a {fahrenheit:.2f}°F.',sep="")
            #print(celsius,"°C equivalem a ",fahrenheit,"°F",sep="")
        except:
            print("Apenas valores numéricos devem ser digitados!")
    elif opcao=="2":
        try:
            fahrenheit=float(input("Digite a temperatura em °F: "))
            celsius=5/9*(fahrenheit-32)
            print(f'{fahrenheit}°F equivalem a {celsius:.2f}°C.',sep="")
           # print(fahrenheit,"°F equivalem a ",celsius,"°C",sep="")
        except:
            print("Apenas valores numéricos devem ser digitados!")
    elif opcao=="3":
        try:
            celsius=float(input("Digite a temperatura em °C: "))
            kelvin=celsius+273.15
            print(f'{celsius}°C equivalem a {kelvin:.2f}°K.',sep="")
            #print(celsius,"°C equivalem a ",kelvin,"°K",sep="")
        except:
            print("Apenas valores numéricos devem ser digitados!")
    elif opcao=="4":
        try:
            kelvin=float(input("Digite a temperatura em °K: "))
            celsius=kelvin-273.15
            print(f'{kelvin}°K equivalem a {celsius:.2f}°C.',sep="")
            #print(kelvin,"°K equivalem a ",celsius,"°C",sep="")
        except:
            print("Apenas valores numéricos devem ser digitados!")
    elif opcao=="5":
        try:
            celsius=float(input("Digite a temperatura em °C: "))
            rankine=1.8*(celsius+273.15)
            print(f'{celsius}°C equivalem a {rankine:.2f}°R.',sep="")
            #print(celsius,"°C equivalem a ",rankine,"°R",sep="")
        except:
            print("Apenas valores numéricos devem ser digitados!")
    elif opcao=="6":
        try:
            rankine=float(input("Digite a temperatura em °R: "))
            celsius=rankine/1.8-273.15
            print(f'{rankine}°R equivalem a {celsius:.2f}°C.',sep="")
            #print(rankine,"°R equivalem a ",celsius,"°C",sep="")
        except:
            print("Apenas valores numéricos devem ser digitados!")
    elif opcao == "7":
        try:
            fahrenheit=float(input("Digite a temperatura em °F: "))
            celsius=5/9*(fahrenheit-32)
            kelvin=celsius+273.15

            print(f"{fahrenheit}°F equivalem a {kelvin}°K.", sep="")
        except:
            print("Apenas valores numéricos devem ser digitados.")
    #print ("8)  Converter de Graus Kelvin     para Graus Fahrenheit")
    elif opcao == "8":
        try:
            kelvin = float(input("Digite a temperatura em °K: "))
            celsius=kelvin-273.15
            fahrenheit=9/5*celsius+32
            print(f"{kelvin}°K equivalem a {fahrenheit}°F.", sep="")

        except:
            print("Apenas valores númerocos devem ser digitados!")

    #print ("9)  Converter de Graus Fahrenheit para Graus Rankine")
    elif opcao == "9":
        try:
            fahrenheit = float(input("Digite a temperatura em °F: "))
            celsius=5/9*(fahrenheit-32)
            rankine=1.8*(celsius+273.15)
            print(f"{fahrenheit}°F equivalem a {rankine}°R.")

        except:
            print("Apenas valores numéricos devem ser digitados.")

    # print ("10) Converter de Graus Rankine    para Graus Fahrenheit")
    elif opcao == "10":
        try:
            rankine = float(input("Digite a temperatura em °R: "))
            celsius=rankine/1.8-273.15
            fahrenheit=9/5*celsius+32
            print(f"{rankine}°R equuivalem a {fahrenheit}°F.")


        except:
            print("Apenas valores numéricos devem ser digitados.")


    elif opcao=="11":
        try:
            FimDoPrograma = True
        except:
            print("Apenas valores numéricos devem ser digitados!")
        
    else:
        print("Opção inválida!")
    print("\n")
    
print("OBRIGADO POR USAR ESTE PROGRAMA!")

