print('Olá mundo!')

while True:
   heroi = input('Digite o nome do herói: ')
   if heroi == heroi:
	   break
   
xp=float(input('Digite a quantidade de XP do seu herói: '))

if xp < 1000:
  nivel = 'Ferro'

elif xp > 1000:
    nivel = 'Bronze'

elif xp > 2001:
	nivel= 'Prata'

elif xp > 6001:
	nivel = 'Ouro'

elif xp > 7001:
	nivel = 'Platina'

elif xp > 8001:
	nivel = 'Ascendente'
 
elif xp > 9000:
	nivel = 'Imortal'
  
elif xp >= 10.001:
	nivel = 'Radiante'
   
print(f'O Herói {heroi} está no nível de {nivel}')