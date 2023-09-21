import webbrowser
import os

translations = {
    'English': {
        'main_title': 'Iris Identification',
        'identif_btn_text': 'Start Identification',
        'inf_btn_text': 'About the Project',
        'options_btn_text': 'Options',
        'credit_btn': 'Made by Superjoa10 (click link)',


        'men_title': 'Options Menu',
        'color_label_text': 'Theme',
        'idioma_label_text': 'Language',
        'model_label_text': 'Model Location',
        'apli_model_btn_text': 'Apply Change',


        's_length_label_text': 'S.Length',
        's_width_label_text': 'S.Width',
        'p_length_label_text': 'P.Length',
        'p_width_label_text': 'P.Width',
        'result_label': 'Result',
        'identif_one_btn_text': 'Identify One',
        'identif_file_btn_text': 'Identify File',
        'result_one_label_info_text': 'S = Sepal ; P = Petal; All in cm',


        'main_title_info' : 'Information about the project',
        'project_exp_header' : '# Explanetion about the project',
 
        'project_exp': '''This project is a demonstration of the skills I acquired in the CS50AI course offered by HarvardX, 
with a focus on TensorFlow technology. It uses a database to describe the length and 
width of three species of iris (Iris Setosa, Iris Virginica and Iris Versicolor) 
which are found mainly in the United States.

The project itself consists of an application developed in Python, with the user interface created using the Tkinter library. 
using the Tkinter library, with the CustomTkinter extension. The application receives the 
length and width in centimetres of the plant's petals and sepals. Based on this data, it makes 
makes an assumption about the iris species, choosing the one with the highest probability of matching.

Below is a map of the distribution area of the three flower species:''',

        'app_acept_info': '''Optionally, the application accepts .DATA files, as well as data used to train the model, and also Excel 
Excel files, provided they are formatted as follows:

.DATA:
Petal Length, Petal Width, Sepal Length, Sepal Width and Class (Species).
Objects must be separated by a comma (',') and all values must be in centimetres. 
The class can be empty or contain data, but the file must not contain a header.

Excel:
Petal Length, Petal Width, Sepal Length, Sepal Width and Class (Species).
All values must be in centimetres, and the class field can be empty. The file must not contain a header.

The results will be saved in an Excel file formatted as follows:
Petal Length, Petal Width, Sepal Length, Sepal Width, Class (Species) and Predicted Class (Species).''',

        'model_info_header': '# Information about the model',

        'model_info': '''The project focuses on TensorFlow technology and is produced in the file 'model_functions.py' 
on line 11, in the 'get_model' function. The model's input is the same as that described above in the
files. Below is information about the base model that comes with the application, in the 
Models' folder, indicated in the options (iris_identif\models\model_0.9833.h5).

TensorFlow model type: Keras
Precision: 0.9833
Epochs: 10
No. of Hidden Layers: 4
Activation Types: tanh, relu, Softmax (Output layer)
Optimiser: Adam

Epochs = Number of instances to create the model.
Hidden Layers = The layers through which the data passes before reaching the final layer, 
with several neurons per layer.
Activation Types = The mathematical formula by which the reasoning used in each neuron is determined.''',

        'DB_exp_text_header': '# Information about the database',

        'DB_exp_text': '''
*Data Base located at directory 'iris_DIR'*
If you've ever taught or learnt statistics, data science or Machine Learning, 
chances are you've come across the iris dataset. 
It includes four measurements on each of 50 plants from three different species of iris. 
It was first used as an example by R. A. Fisher in 1936,1 and can now be found in various archives and online repositories, 
as well as being included as part of the basic R programming language package.
                                   
Origin of the database
The iris dataset is one of the best known and most widely used datasets in statistics and data science. 
But the origins of at least part of the data have been a mystery for decades.''',
    },
    'Portugues': {
        'main_title': 'Identificação da Íris',
        'identif_btn_text': 'Iniciar Identificação',
        'inf_btn_text': 'Sobre o Projeto',
        'options_btn_text': 'Opções',
        'credit_btn': 'Feito por Superjoa10 (click link)',

        'men_title': 'Menu de Opções',
        'color_label_text': 'Tema',
        'idioma_label_text': 'Idioma',
        'model_label_text': 'Localização do Modelo',
        'apli_model_btn_text': 'Aplicar Mudança',

        's_length_label_text': 'S.Comprimento',
        's_width_label_text': 'S.Largura',
        'p_length_label_text': 'P.Comprimento',
        'p_width_label_text': 'P.Largura',
        'result_label': 'Resultado',
        'identif_one_btn_text': 'Identificar Um',
        'identif_file_btn_text': 'Identificar Arquivo',
        'result_one_label_info_text': 'S = Sépala ; P = Pétala ; Length - Comprimento ; Width - Largura ; All in cm',

        'main_title_info' : 'Informações do projeto',
        'project_exp_header' : '# Explicação sobre o projeto',

        'project_exp': '''Este projeto é uma demonstração das habilidades que adquiri no curso CS50AI oferecido pela HarvardX, 
com foco na tecnologia TensorFlow. Ele utiliza um banco de dados para descrever o comprimento e a 
largura de três espécies de íris (Iris Setosa, Iris Virginica e Iris Versicolor) 
que são encontradas principalmente nos Estados Unidos.

O projeto em si consiste em um aplicativo desenvolvido em Python, com a interface do usuário criada 
utilizando a biblioteca Tkinter, com a extensão CustomTkinter. O aplicativo recebe as medidas de 
comprimento e largura em centímetros das pétalas e sépalas da planta. Com base nesses dados, ele faz 
uma suposição sobre a espécie da íris, escolhendo a que possui a maior probabilidade de corresponder.

A seguir, apresento um mapa da área de distribuição das três espécies de flores:''',

        'app_acept_info': '''Opcionalmente, o aplicativo aceita arquivos .DATA, assim como dados usados para treinar o modelo, e 
também arquivos Excel, desde que estejam formatados da seguinte maneira:

.DATA:
Comprimento da Pétala, Largura da Pétala, Comprimento da Sépala, Largura da Sépala e Classe (Espécie).
Os objetos devem ser separados por uma vírgula (',') e todos os valores devem estar em centímetros. 
A classe pode estar vazia ou conter dados, mas o arquivo não deve conter cabeçalho.

Excel:
Comprimento da Pétala, Largura da Pétala, Comprimento da Sépala, Largura da Sépala e Classe (Espécie).
Todos os valores devem estar em centímetros, e o campo da classe pode estar vazio. O arquivo não deve conter cabeçalho.

Os resultados serão salvos em um arquivo Excel formatado da seguinte maneira:
Compri. da Pétala, Larg. da Pétala, Compri. da Sépala, Larg. da Sépala, Classe (Espécie) e Classe prevista (Espécie).''',

        'model_info_header': '# Informações sobre o model',

        'model_info': '''O projeto tem foco na tecnologia TensorFlow, sendo produzido no arquivo 'model_functions.py' 
na linha 11, na função 'get_model'. O modelo tem como input igual ao descrito acima nos arquivos
aceitos. Abaixo, seguem as informações sobre o modelo base que vem junto ao aplicativo, na 
pasta 'Models', apontado nas opções (iris_identif\models\model_0.9833.h5).

Tipo de modelo TensorFlow: Keras
Precisão: 0.9833
Epochs: 10
Nº de 'Hidden Layers': 4
Tipos de Ativações: tanh, relu, Softmax (Output layer)
Otimizador: Adam

Epochs = Número de instâncias para criação do modelo.
Hidden Layers = São as camadas pelas quais os dados passam antes de chegar à camada final, 
possuindo diversos neurônios por camada.
Tipos de ativação = A fórmula matemática pela qual determina o raciocínio usado em cada neurônio.''',

        'DB_exp_text_header': '# Informações sobre Banco de dados',

        'DB_exp_text': '''
*Banco de dados se encontra na pasta 'iris_DIR'*
Se você já ensinou ou aprendeu estatística, ciência de dados ou Machine Learning, 
é bem provável que você tenha se deparado com o conjunto de dados da íris. 
Ele inclui quatro medições em cada uma das 50 plantas de três espécies diferentes de íris. 
Ele foi usado pela primeira vez como exemplo por R. A. Fisher em 1936, 
e agora pode ser encontrado em vários arquivos e repositórios on-line, 
além de ser incluído como parte do pacote básico da linguagem de programação R.
                                   
Origem do banco de dados
O conjunto de dados da íris é um dos conjuntos de dados mais conhecidos 
e mais amplamente usados em estatística e ciência de dados. 
Mas as origens de pelo menos parte dos dados têm sido um mistério há décadas.''',
    }
}

callback = lambda url: webbrowser.open_new(url)

check_directory_exists = lambda directory: os.path.exists(directory)

def replace_special_char(input_str):
    modified_str = input_str.replace('ã', '*')
    return modified_str

def restore_special_char(input_str):
    modified_str = input_str.replace('*', 'ã')
    return modified_str
