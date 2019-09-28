# macae-tech-meetup-machine-learning
Código fonte do modelo de ML para inferência de resultados de batalhas pokemon

* Para instalar o Anaconda:</h1>
  * Download -> https://www.anaconda.com/distribution/
  * Tutorial de instalação -> https://docs.anaconda.com/anaconda/install/
  * O jupyter e o spider já vem com o Anaconda. Após instalado, basta clicar em Launch.

* Para rodar a API:
  * Será necessário criar um environment no anaconda e instalar lá os pacotes utilizados neste exemplo. Este processo de instalação será mais detalhado posteriormente em futuras postagens em medium.com/cinthiabpessanha. Segui este tutorial para criar minha API: https://abndistro.com/post/2019/01/20/using-flask-to-deploy-predictive-models/

* Para rodar o app Angular, será necessário:
  * Instalar o node.js -> https://nodejs.org/en/download/
  * Instalar o Angular -> https://www.devmedia.com.br/angular-cli-instalacao/38247
  * Instalar o VSCode -> https://code.visualstudio.com/download
  * Instalar as bibliotecas utilizadas, via CLI. O próprio código, ao acionar ng-serve via terminal, irá indicar o que está faltando. 

* Fonte dos dados (disponível na pasta Datasets): https://www.kaggle.com/terminus7/pokemon-challenge
* Não foi possível subir o modelo gerado no jupyter, pois o Git não permite arquivos maiores que 100MB. Para gerar o arquivo, basta abrir o arquivo RandomForest-test-selection - Meetup - final.ipynb (encontra-se dentro do folder Notebook Jupyter) e executar cada célula (Shift + enter). 
  * Copie os arquivos finalized_model.sav e encoder.sav no diretório API Flask
 
* Lembrando que todo esse processo será descrito detalhadamente em posts no meu blog medium.com/cinthiabpessanha
