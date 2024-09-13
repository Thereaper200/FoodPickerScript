import random
from time import sleep

lista_de_comida = ('Pizza', 'Hamburguesa', 'Tacos', 'Subway', 'Crepas', 'Cafenio', 'KFC')

numero_random = random.randint(0, 6)


print('Cargando: [#         ]')
sleep(1.0)
print('Cargando: [####      ]')
sleep(1.0)
print('Cargando: [######    ]')
sleep(1.0)
print('Cargando: [########  ]')
sleep(1.0)
print('Cargando: [######### ]')
sleep(1.0)
print('Cargando: [######### ]\n YA CASI')
sleep(1.0)
print('Cargando: [######### ]\n A PUNTO DE DARTE EL RESULTADO')
sleep(1.0)
print('SE TRABÓ 🥲')
sleep(3.0)
print('Cargando: [######### ]\n NO CIERTO, AHI VAAAAAAA')
sleep(2.0)
print('Cargando: [######### ]\n Y hoy COMERAAAAAN: ')
sleep(2.0)
print('Cargando: [######### ]\n Redoble de Tambores')
sleep(2.0)
print('Cargando: [##########]')
sleep(1.0)
print(f'Hoy se come: {lista_de_comida[numero_random]}')
