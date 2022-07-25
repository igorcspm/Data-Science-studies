# Projeto Web Scraping + Scanner + User Interface
Esse projeto reúne três técnicas diferentes: web scraping, scanner e UI. Com elas montei um aplicativo para Desktop em que o usuário pode verificar, através do número
do código de barras do produto, os preços desse produto na cidade de Maceió, Alagoas (minha cidade). 

#### Parte 1: Web Scraping
Nessa parte eu utilizo as informações públicas do site do Governo de Alagoas, https://economizaalagoas.sefaz.al.gov.br/. Com isso, para extrair as informações do site, eu 
utilizei as bibliotecas Selenium e BeautifulSoup. Em seguida, tratei os dados para ficarem mais apresentáveis ao usuário final e os inseri em um DataFrame do Pandas.

#### Parte 2: Scanner
Após feita a parte de web scraping, para dar mais opções, decidi criar um scanner, em que permite o usuário pesquisar através de uma foto do código de barras ou apenas 
apontando a câmera para um código de barras. Nesse caso, utilizei o OpenCV em conjunto com o PyZBAR para extrair o número do código de barras do frame, já que esse número 
é necessário para executar o web scraping.

#### Parte 3: User Interface
Por fim, minha escolha foi customizar um aplicativo de Desktop para que o usuário fosse capaz de obter as informações do modo que quisesse, seja através de uma foto, 
apontando a câmera para um código de barras ou apenas inserindo o número do código de barras para efetuar a pesquisa. Além disso, a interface deixa a visualização dos dados
mais intuitiva e acessível. Para realizar essa parte do projeto utilizei a biblioteca CustomTkinter, que é uma versão customizada, com um visual mais moderno, do Tkinter 
do Python.
