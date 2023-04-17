def value_validation(input_value: str):
    try:
        input_value = float(input_value)
        if input_value < 0:
            print("por favor digite números maiores que zero!!")
        else:
            return input_value

    except Exception as error:
        print(error)
        print("por favor digite números")
        return None


while True:
    while True:
        geometric_form = input("Digite 1, 2 ou 3 para quadrado, triângulo ou círculo respectivamente: ")
        if geometric_form in ["1", "2", "3"]:
            break

    if geometric_form == "1":
        while True:
            sides_sides = input("Digite o tamanho dos lados do quadrado: ")
            sides_sides = value_validation(sides_sides)
            if sides_sides:
                break

        print("Area calculada:", "{:.2f}".format(sides_sides * sides_sides))

    elif geometric_form == "2":
        while True:
            base = input("Digite o tamanho da base do triangulo: ")
            base = value_validation(base)
            if base:
                break

        while True:
            height = input("Digite a altura do triangulo: ")
            height = value_validation(height)
            if height:
                break

        print("Area calculada:", "{:.2f}".format((base * height)/2))

    elif geometric_form == "3":
        while True:
            radius = input("Digite o raio do circulo: ")
            radius = value_validation(radius)
            if radius:
                break

        print("Area calculada:", "{:.2f}".format(3.14 * radius * radius))

    while True:
        user_continue = input("Deseja continuar? ( S ou N): ").lower()
        if user_continue in ["s", "n"]:
            break

    if user_continue == "n":
        break
