import time

numero1 = 0
numero2 = 0
operador = '  '
resultado = ''
continuar = True
porcentagem = 0



while continuar != False:
   numero1 = 0

   print(f'''
   
   |---------------|
   | {numero1}
   |---------------|
   | 7 | 8 | 9 | - |
   | - | - | - | + |
   | 4 | 5 | 6 | * |
   | - | - | - | / |
   | 1 | 2 | 3 | % |
   |---------------| ''')

   numero1 = int(input("Digite o primeiro numero: "))

   print(f'''
   
   
   |---------------|
   | {numero1}
   |---------------|''')

   while operador not in '+-%*/':

      operador = str(input('''   
   Escolha um simboolo para fazer a operação de:   
   (-) divisão.
   (+) adição.
   (*) multiplicação.
   (/) divisao.
   (%) resto divisão. 
    
    Digite: '''))


      if operador in '+-%*/':
         continue
      print('   !!!Digite um operador valido!!!')
      time.sleep(3)

   print(f'''
  
  |---------------|
  | {numero1} {operador}
  |---------------|
  | 7 | 8 | 9 | - |
  | - | - | - | + |
  | 4 | 5 | 6 | * |
  | - | - | - | / |
  | 1 | 2 | 3 | % |
  |---------------| ''')

   numero2 = int(input("Digite o segundo numero: "))


   resultado = int()
   if operador == '+':
      resultado = numero1 + numero2
   elif operador == '-':
      resultado = numero1 - numero2
   elif operador == '*':
      resultado = numero1 * numero2
   elif operador == '/':
      resultado = numero1 / numero2
   elif operador == '%':
      resultado = numero1 % numero2

   print(f'''
  
  |---------------|
  | {numero1} {operador} {numero2} = {resultado}
  |---------------|
  | 7 | 8 | 9 | - |
  | - | - | - | + |
  | 4 | 5 | 6 | * |
  | - | - | - | / |
  | 1 | 2 | 3 | % |
  |---------------| ''')
   time.sleep(2)
   print("\n" * 10)
   operador = 'n'
   parar = int(input(f'''
   Escolha:      
   1-para continuar a operando sobre o resultado {resultado}.
   2-para fazer um nova operação.
   3-sair. 
   
   Digite: '''))

   if parar == 1:
      while parar == 1:
         print("\n" * 10)

         while operador not in '+-%*/':

            operador = str(input(f'''   
   |---------------|
   | {resultado}
   |---------------|    
            
   Escolha um simboolo para fazer a operação de:
   (-) divisão.
   (+) adição
   (*) multiplicação
   (/) divisão 
   (%) resto da divisão: 
      
   Digite: '''))

            if operador in '+-%*/':
               continue
            print('   !!!Digite um operador valido!!!')
            time.sleep(2)

         print(f'''
      
   |---------------|
   | {resultado} {operador}
   |---------------|
   | 7 | 8 | 9 | - |
   | - | - | - | + |
   | 4 | 5 | 6 | * |
   | - | - | - | / |
   | 1 | 2 | 3 | % |
   |---------------| ''')

         numero2 = int(input("Digite o segundo numero: "))

         print(f'''
           
   |---------------|
   | {resultado} {operador} {numero2}
   |---------------|
   | 7 | 8 | 9 | - |
   | - | - | - | + |
   | 4 | 5 | 6 | * |
   | - | - | - | / |
   | 1 | 2 | 3 | % |
   |---------------| ''')
         resultadoValor = resultado
         if operador == '+':
            resultado = resultado + numero2
         elif operador == '-':
            resultado = resultado - numero2
         elif operador == '*':
            resultado = resultado * numero2
         elif operador == '/':
            resultado = resultado / numero2
         elif operador == '%':
            resultado = resultado % numero2

         print(f'''
           
   |---------------|
   | {resultadoValor} {operador} {numero2} = {resultado}
   |---------------|
   | 7 | 8 | 9 | - |
   | - | - | - | + |
   | 4 | 5 | 6 | * |
   | - | - | - | / |
   | 1 | 2 | 3 | % |
   |---------------| ''')
         time.sleep(3)
         print("\n" * 10)
         operador = 'n'
         parar = int(input(f'''
   Escolha: 
   
   1-para continuar a operando sobre o resultado {resultado}.
   2-para fazer um nova operação.
   3-sair. 
            
   Digite: '''))
         if parar == 2:
            print("\n" * 10)
            time.sleep(1)
            numero1 = 0
            numero2 = 0
            operador = '  '
            resultado = ''

         elif parar == 3:
            print('  Fim!!!!')
            continuar = False



   elif parar == 2:
      time.sleep(1)
      numero1 = 0
      numero2 = 0
      operador = '  '
      resultado = ''

   elif parar == 3:
      print('  Fim!!!!')
      continuar = False


