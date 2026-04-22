def precioTotalProducto():
    nombre_producto = input("nombre del producto")
    precio_por_unidad = float(input("precio del producto por unidad"))
    cantidad_de_producto = int(input("cantidad de producto"))
    descuento_porcentaje = int(input("descuento en porcentaje"))
    iva_porcentaje = int(input("iva en porcentaje"))
    
    
    precio_total = precio_por_unidad * cantidad_de_producto
    descuento = precio_total * (descuento_porcentaje / 100)
    precio_con_descuento = precio_total - descuento
    iva = precio_con_descuento *(iva_porcentaje / 100)
    precio_final = precio_con_descuento + iva

    return precio_final

resultado = precioTotalProducto()
print(resultado)