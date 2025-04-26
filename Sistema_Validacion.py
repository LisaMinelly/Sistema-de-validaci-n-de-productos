# Le da la bienvenida al usuario
print("\nBienvenido a la calculadora de descuentos")

# Solicita el nombre del producto
nombre = input("\nNombre del producto: ")

# Valida que el nombre contenga únicamente letras
if nombre.isalpha():
    
    # Solicita el precio unitario y valida que sea un número positivo
    precioU_input = input("Agregue el precio unitario: ")
    try:
        precioU = float(precioU_input)
        if precioU > 0:
            
            # Solicita la cantidad de productos y valida que sea un entero positivo
            cantidadP_input = input("¿Cuántos productos son?: ")
            try:
                cantidadP = int(cantidadP_input)
                if cantidadP > 0:
                    
                    # Solicita el descuento y valida que esté entre 0 y 100
                    descuento_input = input("Agregue el descuento: ")
                    try:
                        descuento = float(descuento_input)
                        if 0 <= descuento <= 100:
                            
                            # Cálculo del precio base, descuento, subtotal, IVA y total a pagar
                            precio_base = precioU * cantidadP
                            Descuento = precio_base * (descuento / 100)
                            precio_subtotal = precio_base - Descuento
                            iva_porcentaje = 0.19
                            iva_valor = precio_subtotal * iva_porcentaje
                            precio_final = precio_subtotal + iva_valor
                            
                            # Impresión de resultados
                            print(f"\nNombre: {nombre}")
                            print(f"Precio sin descuento: {precio_base}")
                            if descuento == 0:
                                print("Precio con descuento: descuento no válido")
                            else:
                                print(f"Precio con descuento: {precio_subtotal}")
                            print(f"Valor IVA: {iva_valor}")
                            print(f"Precio total a pagar: {precio_final}")

                        else:
                            print("Error: el descuento debe estar entre 0 y 100.")
                    except ValueError:
                        print("Error: el descuento debe ser un número.")
                else:
                    print("Error: la cantidad debe ser mayor que 0.")
            except ValueError:
                print("Error: la cantidad debe ser un número entero.")
        else:
            print("Error: el precio debe ser mayor que 0.")
    except ValueError:
        print("Error: el precio debe ser un número.")
else:
    print("Error: el nombre debe contener únicamente letras.")