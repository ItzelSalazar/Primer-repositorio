#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Importando base de datos.
from lifestore_file import lifestore_sales,lifestore_products,lifestore_searches


# In[ ]:


#Accesos al sistema;        USUARIO: itzel       CONTRASEÑA: itzel22

#Definiendo el acceso False por default
acceso=False

#Contador de intentos para acceder 
intento=0

#Mensaje de bienvenida cuando logre accesar
bienvenida='Excelente, bienvenid@ al sistema!.'

#bucle iterativo que pida usuario y password para que con ayuda de un bucle condicional se validen
#los accesos (limite del while: 3 veces), en caso de no accesar se sale automaticamente de los intentos.
while not acceso:
  usuario=input('Ingresa usuario: ')
  contra=input('Ingresa password: ')
  intento+=1
  if usuario=='itzel' and contra=='itzel22':
    acceso=True
    print(bienvenida)
  elif usuario=='itzel' and contra!='itzel22':
    print('Usuario correcto, te equivocaste en el password, vuelve a intentarlo, te quedan',3-intento,'intentos')
  elif usuario!='itzel' and contra=='itzel22':
    print('Password correcto,te equivocaste en el usuario, vuelve a intentarlo, te quedan',3-intento,'intentos')
  else:
    print('Usuario y password incorrectos, vuelve a intentarlo, te quedan',3-intento,'intentos')
  if intento==3:
    exit()


# In[41]:


#Creando lista vacía para guardar información de frecuencia de los productos vendidos.
aux1=[]

#Creando lista vacía para guardar id_product,frecuencia y/o conteo de producto vendido, nombre del producto 
#y categoría.
aux2=[]

#Creando una lista que guarde los productos vendidos, obtenidos de lifestore_sales y guardar la frecuencia en aux1, 
# UNICAMENTE se consideró a los productos sin devolución.
columnaaux=[fila[1] for fila in lifestore_sales if fila[4]==0]

#Bucle para iterar de 0 a tanto elementos tenga lifestore_products
for i in range(0, len(lifestore_products)):
    #Bucle condicional que cuente los productos únicos.
  if aux1.count(lifestore_products[i][0])==0:
#Con append añadimos a la lista aux1 el id_producto y en aux2 id_product,frecuencia y/o conteo de producto vendido,
# nombre del producto y categoría.
   aux1.append(lifestore_products[i][0])
   aux2.append([lifestore_products[i][0], columnaaux.count(lifestore_products[i][0]),lifestore_products[i][1],
                lifestore_products[i][3]])

#Creando lista vacía para guardar información de frecuencia de los productos buscados.
aux3=[]

#Creando lista vacía para guardar id_product,frecuencia y/o conteo de producto buscado, nombre del producto 
# y categoría.
aux4=[]

#Creando una lista que guarde los productos buscados, obtenidos de lifestore_searches y guardar la frecuencia en aux3.
# Se consideró a todos los productos.
columnaaux2=[fila[1] for fila in lifestore_searches]

#Bucle para iterar de 0 a tanto elementos tenga lifestore_products
for i in range(0, len(lifestore_products)):
    #Bucle condicional que cuente los productos únicos.
  if aux3.count(lifestore_products[i][0])==0:
    #Con append añadimos a la lista aux3 el id_producto y en aux4 id_product,frecuencia y/o conteo de producto 
    #buscado, nombre del producto y categoría.
   aux3.append(lifestore_products[i][0])
   aux4.append([lifestore_products[i][0], columnaaux2.count(lifestore_products[i][0]),lifestore_products[i][1],
                lifestore_products[i][3]])

#Generar un listado ORDENADO de los 5 productos con mayores ventas, usando sorted para ordenar por frecuencia de venta
# de id_product en orden descendiente
listaOrdenada_productos_mas_vendidos = sorted(aux2, key = lambda productos: productos[1], reverse = True)[:5]

#Generando un listado ORDENADO con los 10 productos con mayor busqueda, usando sorted para ordenar por frecuencia 
#de venta de id_product en orden descendiente
listaOrdenada_productos_mas_buscados = sorted(aux4, key = lambda busqueda: busqueda[1], reverse = True)[:10]

#Generar un listado ORDENADO de los 5 productos con menores ventas, usando sorted para ordenar por categoría los 5 
# productos con menos ventas (orden ascendente)
listaOrdenada_productos_menos_vendidos = sorted(aux2, key = lambda producto: (producto[3],producto[1]),
                                                reverse = False)

#Generar un listado ORDENADO de los 10 productos con menos búscados, usando sorted pra ordenar por categoría los 5 
# productos con menos ventas (orden ascendente)
listaOrdenada_productos_menos_buscados = sorted(aux4, key = lambda producto: (producto[3],producto[1]), 
                                                reverse = False)


# ### 1.1 Genera un listado con los 5 productos de mayores ventas 

# In[31]:


for j in range(0,len(listaOrdenada_productos_mas_vendidos)):
  print('El top ',j+1,' de venta es el producto: ',listaOrdenada_productos_mas_vendidos[j][2][:20],
';con id_product:',listaOrdenada_productos_mas_vendidos[j][0],' se vendió ',
listaOrdenada_productos_mas_vendidos[j][1],'veces.')


# ### 1.2 Genera un listado con los 10 productos de mayores busquedas

# In[32]:


for j in range(0,len(listaOrdenada_productos_mas_buscados)):
  print('El top ',j+1,' de busqueda es el producto: '
,listaOrdenada_productos_mas_buscados[j][2][:20],';con id_product:',listaOrdenada_productos_mas_buscados[j][0],
' se buscó ', listaOrdenada_productos_mas_buscados[j][1],'veces.')


# ### 1.3 Genera un listado por categoría de los 5 productos con menores ventas

# In[48]:


#Iniciando contador llamado "z"
z=0
for j in range(0,len(listaOrdenada_productos_menos_vendidos)):
    #Blucle que considere unicamente los 5 productos con menores ventas
  if z<5:
    #Indicando a la categoría a la que pertenecen los 5 productos con menor venta
    print('Categoria',listaOrdenada_productos_menos_vendidos[j][3])
    print('El low ',z+1,' de venta es el producto: ',listaOrdenada_productos_menos_vendidos[j][2][:35],
          ' se vendió ',
          listaOrdenada_productos_menos_vendidos[j][1],'veces.')
    z=z+1
  if j+1 < len(listaOrdenada_productos_menos_vendidos): 
    #Inicializar el contador "z" en cero si es que el producto no pertenece a la misma categoría
    if listaOrdenada_productos_menos_vendidos[j+1][3]!= listaOrdenada_productos_menos_vendidos[j][3]:
      z=0


# ### 1.4 Generar un listado por categoría con los 10 productos menos buscados

# In[47]:


#Iniciando contador llamado "z" en cero.
z=0
for j in range(0,len(listaOrdenada_productos_menos_buscados)):
    #Contador que sea menor a 10 (por los productos buscados) para que se impriman dichos productos.
  if z<10:
    #indicar la categoría a la que pertenecen los primeros 10 productos mnos buscados
    print('Categoría',listaOrdenada_productos_menos_buscados[j][3])
    print('El low ',z+1,' de busqueda es el producto: ',listaOrdenada_productos_menos_buscados[j][2][:35],
          ' se buscó ',
          listaOrdenada_productos_menos_buscados[j][1],'veces.')
    z=z+1
  if j+1 < len(listaOrdenada_productos_menos_buscados)-1:  
    if listaOrdenada_productos_menos_buscados[j+1][3]!= listaOrdenada_productos_menos_buscados[j][3]:
        #Inicializar el contador "z" en cero si es que el producto no pertenece a la misma categoría.
      z=0


# ### Mostrar dos listados de 5 productos cada una, un listado para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución (no considerar productos sin reseñas)
# 

# In[49]:


#Genarando una lista vacía para guardar el id_producto y score como valor único, obtenido de lifestore_sales
aux5=[]

#Generando una lista vacía para guardar el id_product, score/resena (puntaje de 1-5) y la frecuencia.
aux6=[]

#Generando lista con 2 entradas obteniendo el id_product y score del producto
#Se considero a TODOS los PRODUCTOS VENDIDOS aunque haya habido DEVOLUCION.
columna=[[fila[1],fila[2]] for fila in lifestore_sales] 

for i in range(0, len(columna)):
    # El bucle consicional solo va a guardar a los valores con id_product y scrore unicos, es decri sin repetición.
  if aux5.count(columna[i])==0:
   aux5.append(columna[i])
# La lista aux6 va a guardar id_product, score y la frecuencia de dichos elementos incluidos en la lista columna.
   aux6.append([columna[i][0], columna[i][1], columna.count(columna[i])])


# ### 2.1 Genera una lista de los 5 productos con mejor reseña

# In[54]:


#Generando una lista ORDENADA de manera descendiente que muestre los primeros 5 productos con mejor score.
listaOrdenada_productos_score = sorted(aux6, key = lambda score: (score[1], score[2]), reverse = True)[:5]

for j in range(0,len(listaOrdenada_productos_score)):
  print('El id_product ',listaOrdenada_productos_score[j][0],' tiene score: ',listaOrdenada_productos_score[j][1],
        '; con frecuencia:',listaOrdenada_productos_score[j][2])


# ### 2.2 Genera un listado de los 5 productos con peor reseña

# In[56]:


#Generando una lista ORDENADA de manera ascendente que muestre los primeros 5 productos con peor score.
listaOrdenada_productos_score = sorted(aux6, key = lambda score: (score[1], -score[2]), reverse = False)[:5]

for j in range(0,len(listaOrdenada_productos_score)):
  print('El id_product ',listaOrdenada_productos_score[j][0],' tiene score: ',listaOrdenada_productos_score[j][1],
        '; con frecuencia:',listaOrdenada_productos_score[j][2])


# ### Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año

# In[96]:


# A continuación se genera una lista de los productos vendidos "NO devueltos" que incluye id_producto, la fecha de 
# venta con mes y year.
fecha_venta=[[sale[1], (sale[3].split('/')[1]),(sale[3].split('/')[2])] for sale in lifestore_sales if sale[4]==0]

#Generando listas de valores únicos usando list(set()) tanto para mes como para year de venta.
column_mes=list(set([fila[1] for fila in fecha_venta]))
column_year=list(set([fila[2] for fila in fecha_venta]))

#Creando una lista vacía que guardará:
# 0. id_producto
# 1. *venta total del producto* (lifestore_products[i][2]*aux); donde lifestore_products[i][2] es el precio del 
# producto y aux es la frecuencia del producto vendido por mes y año
# 2. frecuencia del producto vendido por mes y año
# 3. mes
# 4. year
aux7=[]

# Bucle for anidado para que valide las ventas por mes y year, de esa manera agregar a la lista aux7.
for i in range(0, len(lifestore_products)):
  for j in column_year:
    for k in column_mes:
      aux=fecha_venta.count([lifestore_products[i][0], k, j])
      if aux!=0:
        aux7.append([lifestore_products[i][0], lifestore_products[i][2]*aux, aux, k, j])

# Creando una lista vacía para guaradar el mes, ingresos totales de productos ventidos al mes , cantidad total 
# de productos vendidos al mes, venta promedio por mes       
ingresos_total_mes=[]

#Iniciando el contador ingreso anual en cero
suma_anual=0

#Iniciando el contador de productos vendidos anual en cero
suma_productos_vendidos_anual=0

#Bucle que itere sobre el mes
for i in column_mes:
    # contador de ingreso mensual inicial en cero
  suma=0
   #contador inicial de productos vendidos inicial en cero
  suma_productos_por_mes=0

#Bucle que itere sobre la cantidad de elementos que tiene la lsita aux7
  for j in aux7:
        # condicional Renglon "j" entrada 3 (frecuencia del producto vendido en el "mes tal" del "year tal" igual 
        # al mes
    if j[3]==i:
        # En caso de que la condición se cumpla se suma el ingreso de los productos vendidos en "tal mes" del 
        # "year tal"
      suma=suma+j[1]
        # Contando los productos vendidos por mes (j[2])
      suma_productos_por_mes=suma_productos_por_mes+j[2]
  # Calculando la venta promedio por mes  
  promedio_venta=round(suma/suma_productos_por_mes,2)
  ingresos_total_mes.append([i,suma,suma_productos_por_mes,promedio_venta])
  #Calculando el ingreso anual de las ventas
  suma_anual=suma_anual+suma
  #Calculando la venta anual de los productos
  suma_productos_vendidos_anual=suma_productos_vendidos_anual+suma_productos_por_mes


# ### 3.1 Calcula la venta promedio mensual

# In[92]:


#Creando una lista ORDENADA ascendentemente por mes de la venta promedio
listaOrdenada_ingresos=sorted(ingresos_total_mes, key= lambda mes:mes[0])
for i in range(0,len(listaOrdenada_ingresos)):
   print(f'Mes:',listaOrdenada_ingresos[i][0],'tiene venta promedio de $',listaOrdenada_ingresos[i][3])


# ### 3.2 Calcula el número de ventas mensuales

# In[93]:


#Creando una lista ORDENADA ascendentemente por mes de los productos vendidos 
listaOrdenada_productos_mes=sorted(ingresos_total_mes, key= lambda productos_mes:productos_mes[2])
for i in range(0,len(listaOrdenada_ingresos)):
   print(f'Mes:',listaOrdenada_ingresos[i][0],'se vendieron',listaOrdenada_ingresos[i][2])
print('En los meses que no aparecen significa que no hubó venta.')


# ### 3.3 Calcula el ingreso anual 

# In[94]:


print('El ingreso anual 2020 es de $',suma_anual)


# ### 3.4 Calcula el numero de productos vendidos anual

# In[101]:


print('En 2020 se vendieron', suma_productos_vendidos_anual, 'productos.')

