# Laboratorio: hashes

## Ejercicio 1

La implementación de las funciones de hash con distintos algoritmos se encuentra en [explorar_hashes.ipynb](src/explorar_hashes.ipynb)

Los resultados fueron los siguientes:

![img1](imgs/table1.png)

Para ver los bits que cambiaron, se implemento la siguiente función:

```python
def xor_diff_bits(a: bytes, b: bytes):
    x = strxor(a, b)
    return sum(bin(byte).count("1") for byte in x)
```

Al implementarla con los hashes de los mensajes, se obtuvo que 139 bits cambiaron, esto muestra la propiedad de avalancha, un pequeño cambio genera hashes totalmente diferentes.

![img2](imgs/bits_changed.png)

MD5 es inseguro porque el hash solo genera 128 bits, es un espacio bastante pequeño y reduce la cantidad de posibles hashes, esto facilita encontrar colisiones. 

## Ejercicio 2

Se implementó en el archivo [api_search.ipynb)](src/api_search.ipynb)

El resultado fue:

![img3](imgs/table2.png)

Nos indica que solamente la contraseña con el nombre de la empresa no ha sido expuesta varias veces en filtraciones, esto se debe a que, como es un nmbre inventado, nadie nunca ha usado un nombre similar como contraseña y por lo tanto nunca se ha filtrado. 

## Ejercicio 3

Se implementó el generador en: [generar_manifiesto.py](src/generar_manifiesto.py)
El verficador en: [verificar_paquete.py](src/verificar_paquete.py)

Se obtuvo este resultado al alterar el archivo 5:

![img4](imgs/table3.png)

Para utilizarlo:


- Primero crear los archivos desados en la carpeta files o usar los que ya existen 
- Luego, ejecutar el siguiente comando desde la raíz del proyecto

```bash
uv run python src/generar_manifiesto.py files/actualizacion1.txt files/actualizacion2.txt files/actualización3.txt files/actualización4.txt files/actualización5.txt ... otros archivos
```

- Ahora ejecutar este comando para obtener resultados 

```bash
uv run python src/verificar_paquete.py
```

## Ejercicio 4


