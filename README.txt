BR:

Esta é uma API criada para o processo seletivo de emprego da Blintz startup, em sua versão 1.1.

O objetivo desta API é receber um JSON com strings e retornar um JSON com as mesmas strings, porém em formato 
    de dicionário, contendo a string como chave e o número de vogais como valor.

Para rodar esta API é necessário ter instalado Python 3 em sua máquina. Cumprido esse requisito, clone o repositório, 
    abra o prompet de comando (se windows) ou terminal (se linux) na pasta chamada 'api' e execute o comando abaixo:

	python api.txt

    e um servidor será inicializado no endereço IP 'http://127.0.0.1:5000' (localhost).

Após, abra o arquivo 'api.txt' e na linha 4, no lugar indicado cole o endereço completo do local em seu disco de onde 
    está o arquivo contendo as palavras que desejar contar as vogais, incluindo o nome do arquivo. Faça a mesma 
    alteração na linha 23.

Em seguida, adicione '/api/v1/resources/palavras/all' ao final do endereço IP acima para ver uma lista de todos as palavras
    adicionadas. Ou então, para executar a contagem de vogais, adicione '/api/v1/resources/palavras' ao final do mesmo 
    endereço.


ATENÇÃO: 
    Ambas as linhas 4 e 23 devem conter os mesmos dados. Do contrario, será levantado um 
        FileNotFoundError: [Errno 2] No such file or directory: '__archive__full__path__here__';
    O arquivo a ser lido deve estar, preferencialmente, estar formatado em uma palavra por linha, separados por vírgula 
        e conter apenas strings;

A versão 1.0 organiza as palavras pela ordem alfabética das chaves.
A versão 1.1 recebe arquivo .json.

A FAZER: tirar os '\n' do retorno em json; implementar formatação inicial; 

EN:

This is an API written for a job interview at Blintz startup, on version 1.1.

This API aims to receive a JSON with strings and return another JSON with those same strings as a dict with strings as keys 
    and the number os voels as values.

To run this API you must have installed Python 3 in your machine. This done, clone the repository, open the command 
    prompet (for windows) or terminal (for linux) at 'api' directory and execute the following command:

	python api.txt

    and a localhost will be initialized at IP adress 'http://127.0.0.1:5000'.

After this, open the 'api.txt' archive and in the 4th line paste the full path in your computer where is located the file where is 
    written the words you want to count voels, including the name of the archive. Repeat the process at line 23. 

Then, copy and paste '/api/v1/resources/palavras/all' after the localhost adress in your navigator to see a list of all words 
    added. Or copy and paste '/api/v1/resources/palavras' to execute the voel count.


ATTENTION: 
    Both lines 4 and 23 must contain same data. Otherwise, there will be raised an 
        FileNotFoundError: [Errno 2] No such file or directory: '__archive__full__path__here__';
    The file to be read should be in format of one word per line, separeted by comma and contain only string format;

v.1 sorts words in 'palavras' by alfabetical order from keys.
v.1.1 read json.file.

TODO: clear '\n' from the json return; implement initial format
