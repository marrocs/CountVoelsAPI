BR:

Esta é uma API criada para o processo seletivo de emprego da Blintz startup, em sua versão 1.0.

O objetivo desta API é receber um JSON com strings e retornar um JSON com as mesmas strings, porém em formato 
    de dicionário, contendo a string como chave e o número de vogais como valor.

Para rodar esta API é necessário ter instalado Python 3 em sua máquina. Cumprindo esse requisito, clone o repositório, 
    abra o prompet de comando (se windows) ou terminal (se linux) na pasta chamada 'api' e execute o comando abaixo:

	python api.txt

    e um servidor será inicializado no endereço IP 'http://127.0.0.1:5000' (localhost).

Após, abra o arquivo 'api.txt' e na variavel 'palavras' (linha 7) adicione as palavras que desejar contar as vogais, entre 
    aspas simples e separadas por virgula. Copie e cole essa mesma variavel para dentro da função 'order_array()' (linha 23).

Em seguida, adicione '/api/v1/resources/palavras/all' ao final do endereço IP acima para ver uma lista de todos as palavras
    adicionadas. Ou então, para executar a contagem de vogais, adicione '/api/v1/resources/palavras' ao final do mesmo 
    endereço.

A versão 1.0 organiza o JSON por ordem alfabética das chaves.

ATENÇÃO: ambas as linhas 7 e 23 devem conter os mesmos dados.

EN:

This is an API written for a job interview at Blintz startup, on version 1.0.

This API aims to receive a JSON with strings and return another JSON with those same strings as a dict with strings as keys 
    and the number os voels as values.

To run this API you must have installed Python 3 in your machine. This done, clone the repository, open the command 
    prompet (for windows) or terminal (for linux) at 'api' directory and execute the following command:

	python api.txt

    and a localhost will be initialized at IP adress 'http://127.0.0.1:5000'.

After this, open the 'api.txt' archive and in the 7th line substitute the words at 'palavras' variable for those you
    want to count voels, between simple quotation marks and separeted by commas. Also, copy and paste that variable at the 
    23th line, at 'order_array()'. 

Then, copy and paste '/api/v1/resources/palavras/all' after the localhost adress in your navigator to see a list of all words 
    added. Or copy and paste '/api/v1/resources/palavras' to execute the voel count.

The v1 sorts words in 'palavras' by alfabetical order from keys.

ATTENTION: Both lines 7 and 23 must contain same data.