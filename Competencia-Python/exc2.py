with open('sapatos.txt', 'r') as file:
    file_content = file.read()

linhas = file_content.split('\n') #separa o conteudo do txt linha por linha

while(linhas):
    quantidade = int(linhas[0]) #adiquire a quantidade de sapatos de acordo com o valor da primeira linha
    linhas.remove(linhas[0])  
    
    print("quantidade:", quantidade)
     
    sapato = []
    matrix = []
    
    for i in range(quantidade): 
        palavras = linhas[0].split() #separa essas linhas pelos espaços entre elas, dividendo assim o n[umero do sapato e o lado]
        linhas.remove(linhas[0])
        n_sapato = int(palavras[0])
        lado_sapato = palavras[1]
        status = 0  #0 -> sapato sem par identificado, 1 -> sapato com par completo
    
        matrix.append([n_sapato, lado_sapato, status])
        
    pares = 0 #contador de pares de sapato
    for i in range(quantidade): 
        for j in range(i+1,quantidade):
            if(matrix[i][0] == matrix[j][0] and matrix[i][1] != matrix[j][1] and matrix[i][2] == 0 and matrix[j][2] == 0 ):
                matrix[i][2] = 1 #muda o status dos sapatos para ocupado
                matrix[j][2] = 1
                pares += 1
    
    print(matrix)               
    print(pares)
    
    
    

    
            
        
    

    


    
    
    