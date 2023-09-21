import customtkinter as custk
import tensorflow as tf
from configparser import ConfigParser
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
from helper_functions import translations, callback, check_directory_exists, replace_special_char, restore_special_char
from model_functions import predict_one, return_result, test_real, predict_and_save_results

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# PAGES
def identif_page():# MAIN PAGE
    idf_0 = custk.CTkToplevel()
    idf_0.title("Type identif")
    idf_0.wm_iconbitmap("midia/icons/Search_white.ico")

    idf_0.minsize(1120, 450)
    idf_0.maxsize(1120, 450)

    global s_length_label, s_width_label, p_length_label, p_width_label, result_one_label, identif_one_btn, identif_file_btn
    data_frame = custk.CTkFrame(master=idf_0, width=1800)
    data_frame.grid(row=1, column=0, columnspan=2, pady=20, padx=50)

    s_length_label = custk.CTkLabel(data_frame, text="S.largura", font=("defalt", 12), anchor='w')
    s_length_label.grid(row=0, column=0)

    s_width_label = custk.CTkLabel(data_frame, text="S.comprimento", font=("defalt", 12), anchor='w')
    s_width_label.grid(row=0, column=1)

    p_length_label = custk.CTkLabel(data_frame, text="P.largura", font=("defalt", 12), anchor='w')
    p_length_label.grid(row=0, column=2)

    p_width_label = custk.CTkLabel(data_frame, text="P.comprimento", font=("defalt", 12), anchor='w')
    p_width_label.grid(row=0, column=3)

    result_one_label = custk.CTkLabel(data_frame, text="Resultado", font=("defalt", 12), anchor='w')
    result_one_label.grid(row=0, column=4)
    
    global s_length_entry, s_width_entry, p_length_entry, p_width_entry, result_one_entry, info_label

    s_length_entry = custk.CTkEntry(data_frame)
    s_length_entry.grid(row=1, column=0, padx=5)

    s_width_entry = custk.CTkEntry(data_frame)
    s_width_entry.grid(row=1, column=1, padx=5)

    p_length_entry = custk.CTkEntry(data_frame)
    p_length_entry.grid(row=1, column=2, padx=5)

    p_width_entry = custk.CTkEntry(data_frame)
    p_width_entry.grid(row=1, column=3, padx=5)

    result_one_entry = custk.CTkEntry(data_frame)
    result_one_entry.grid(row=1, column=4, ipadx=75, padx=5)

    identif_one_btn = custk.CTkButton(data_frame, text="Identificar um", command=lambda:get_one_data(MODEL), anchor= CENTER)
    identif_one_btn.grid(row=0, column=5, padx=5, pady=2)

    identif_file_btn = custk.CTkButton(data_frame, text="Identificar Arquivo", command=predict_and_save_results, anchor= CENTER)
    identif_file_btn.grid(row=1, column=5, padx=5, pady=2)

    info_label = custk.CTkLabel(data_frame, text="S = Sepala ; P = Petala ; Length - Comprimento ; Width - Largura ; Todos em cm", font=("defalt", 8), anchor='w')
    info_label.grid(row=2, column=0, columnspan=2)

    
    types_img = custk.CTkImage(Image.open("midia/1_YYiQed4kj_EZ2qfg_imDWA.png"), size=(700,300))
    types_img_label = custk.CTkLabel(idf_0, text="", image=types_img)
    types_img_label.grid(row=3, column=0, padx=5)

    descript_img_ = custk.CTkImage(Image.open("midia/sepals_and_petals_600w.jpg"), size=(300,300))
    descript_img_label = custk.CTkLabel(idf_0, text="", image=descript_img_)
    descript_img_label.grid(row=3, column=1, padx=5)

    parser.read("iris_ops.ini")
    saved_language = parser.get('visuals', 'language')
    change_language(saved_language, 'identif')

def option_page():# OPTION PAGE
    """ Opens test page that gives option to test varios functions like style, chrome webdriver, and database location"""
    list_color = 'System', 'Light', 'Dark'
    list_language = 'Portugues', 'English'

    global tets
    tets = custk.CTkToplevel()
    tets.title("Options menu")
    tets.wm_iconbitmap("midia/icons/cogflat_106041.ico")

    tets.geometry("360x300")
    tets.minsize(360, 300)
    tets.maxsize(380, 350)

    parser = ConfigParser()
    parser.read("iris_ops.ini")
    saved_language = parser.get('visuals', 'language')
    model_saved = restore_special_char(str(parser.get('file_local', 'model')))

    global men_title, color_label, idioma_label, model_label, apli_model_btn, informations_btn
    men_title = custk.CTkLabel(tets, text="Menu de Opções", anchor=CENTER, padx=3, pady=2, font=("Times New Roman", 25))
    men_title.grid(column=0, row=0, padx=10, pady=5)


    color_label = custk.CTkLabel(tets, text="Tema", anchor=CENTER, padx=3, pady=2,  font=("Times New Roman",21))
    color_label.grid(column=0, row=1, padx=10)  

    var_col = custk.StringVar(value=f'{saved_color}', name='var_col')
    color_menu = custk.CTkOptionMenu(tets, values = list_color, variable= var_col, command=color_opt)    
    color_menu.grid(column=0, row=2, pady=5)

    idioma_label = custk.CTkLabel(tets, text="Idioma", anchor=CENTER, padx=3, pady=2,  font=("Times New Roman",21))
    idioma_label.grid(column=0, row=3, padx=10)  

    var_language = custk.StringVar(value=f'{saved_language}', name='var_language')
    language_menu = custk.CTkOptionMenu(tets, values = list_language, variable= var_language, command=change_language)    
    language_menu.grid(column=0, row= 4, pady=5)

    global model_entry
    model_frame = custk.CTkFrame(master=tets, width=450)
    model_frame.grid(column=0, row=5, pady=10, padx=10)

    model_label = custk.CTkLabel(model_frame, text="Localização Modelo", anchor=CENTER, padx=3, pady=2,  font=("Times New Roman",21))
    model_label.grid(column=0, row=0)

    model_entry = custk.CTkEntry(model_frame, width=10)
    model_entry.grid(column=0, row=1, ipadx=200)

    apli_model_btn = custk.CTkButton(model_frame, text="Aplicar Mudança", command=lambda:change_model())
    apli_model_btn.grid(column=0, row = 2, pady=10)

    model_entry.insert(0, model_saved)
    parser.read("iris_ops.ini")
    saved_language = parser.get('visuals', 'language')
    change_language(saved_language, 'option')

def information_page():# INFORMATION PAGE
    inf = custk.CTkToplevel()
    inf.title("Info. project")
    inf.wm_iconbitmap("midia/icons/agenda_white.ico")

    inf.minsize(720, 750)
    inf.maxsize(720, 750)

    main_frame = custk.CTkFrame(inf)
    main_frame.pack(fill=BOTH, expand=1)

    canva_scroll = Canvas(main_frame)
    canva_scroll.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canva_scroll.yview)
    my_scrollbar.pack(side=RIGHT, fill=BOTH)
    canva_scroll.configure(yscrollcommand=my_scrollbar.set)
    canva_scroll.bind('<Configure>', lambda e: canva_scroll.configure(scrollregion = canva_scroll.bbox("all")))
    second_frame = custk.CTkFrame(canva_scroll, width=1000)
    canva_scroll.create_window((0,0), window=second_frame, anchor="nw")

    global main_title_info, project_exp_header, project_exp, types_img_label, app_acept_info, model_info_header, model_info, DB_exp_text_header, DB_exp_text, credit_txt

    main_title_info = custk.CTkLabel(second_frame, text="Informações do projeto", pady=2, font=("Times New Roman", 40))
    main_title_info.grid(column=0, row=0)

    project_exp_header = custk.CTkLabel(second_frame, text="# Explicação sobre o projeto", anchor=CENTER, padx=3, pady=2, font=("Times New Roman", 25))
    project_exp =  custk.CTkLabel(second_frame, pady=5,	justify="left", text="""
Este projeto é uma demonstração das habilidades que adquiri no curso CS50AI oferecido pela HarvardX, 
com foco na tecnologia TensorFlow. Ele utiliza um banco de dados para descrever o comprimento e a 
largura de três espécies de íris (Iris Setosa, Iris Virginica e Iris Versicolor) 
que são encontradas principalmente nos Estados Unidos.

O projeto em si consiste em um aplicativo desenvolvido em Python, com a interface do usuário criada 
utilizando a biblioteca Tkinter, com a extensão CustomTkinter. O aplicativo recebe as medidas de 
comprimento e largura em centímetros das pétalas e sépalas da planta. Com base nesses dados, ele faz 
uma suposição sobre a espécie da íris, escolhendo a que possui a maior probabilidade de corresponder.

A seguir, apresento um mapa da área de distribuição das três espécies de flores:""")
    
    types_img = custk. CTkImage(Image.open("midia/sign_18_6_26_fig-2.jpeg"), size=(500,150))
    types_img_label = custk.CTkLabel(second_frame, text="", image=types_img)
    
    app_acept_info = custk.CTkLabel(second_frame, pady=5, justify="left", text="""
Opcionalmente, o aplicativo aceita arquivos .DATA, assim como dados usados para treinar o modelo, e 
também arquivos Excel, desde que estejam formatados da seguinte maneira:

.DATA:
Comprimento da Pétala, Largura da Pétala, Comprimento da Sépala, Largura da Sépala e Classe (Espécie).
Os objetos devem ser separados por uma vírgula (',') e todos os valores devem estar em centímetros. 
A classe pode estar vazia ou conter dados, mas o arquivo não deve conter cabeçalho.

Excel:
Comprimento da Pétala, Largura da Pétala, Comprimento da Sépala, Largura da Sépala e Classe (Espécie).
Todos os valores devem estar em centímetros, e o campo da classe pode estar vazio. O arquivo não deve conter cabeçalho.

Os resultados serão salvos em um arquivo Excel formatado da seguinte maneira:
Compri. da Pétala, Larg. da Pétala, Compri. da Sépala, Larg. da Sépala, Classe (Espécie) e Classe prevista (Espécie).""")

    model_info_header = custk.CTkLabel(second_frame, pady=5, text="# Informações sobre o modelo", font=("Times New Roman", 25))
    model_info = custk.CTkLabel(second_frame, pady=5, justify="left", text="""
O projeto tem foco na tecnologia TensorFlow, sendo produzido no arquivo 'model_functions.py' 
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
Tipos de ativação = A fórmula matemática pela qual determina o raciocínio usado em cada neurônio.
""")

    DB_exp_text_header = custk.CTkLabel(second_frame, pady=5, text="# Informações sobre Banco de dados", font=("Times New Roman", 25))
    DB_exp_text =  custk.CTkLabel(second_frame, pady=5, justify="left", text="""
*Banco de dados se encontra na pasta 'iris_DIR'*
Se você já ensinou ou aprendeu estatística, ciência de dados ou Machine Learning, 
é bem provável que você tenha se deparado com o conjunto de dados da íris. 
Ele inclui quatro medições em cada uma das 50 plantas de três espécies diferentes de íris. 
Ele foi usado pela primeira vez como exemplo por R. A. Fisher em 1936, 
e agora pode ser encontrado em vários arquivos e repositórios on-line, 
além de ser incluído como parte do pacote básico da linguagem de programação R.
                                   
Origem do banco de dados
O conjunto de dados da íris é um dos conjuntos de dados mais conhecidos e 
mais amplamente usados em estatística e ciência de dados. 
Mas as origens de pelo menos parte dos dados têm sido um mistério há décadas.""")
    
    credit_txt =  custk.CTkLabel(second_frame, pady=5, text='Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.',anchor=W, font=("Times New Roman", 10), cursor="hand2", text_color='blue')
    credit_txt.bind("<ButtonPress-1>", lambda e:callback("https://doi.org/10.24432/C56C76"))

    project_exp_header.grid(column=0, row=1, sticky=W)
    project_exp.grid(column=0, row=2, sticky=W)
    types_img_label.grid(column=0, row=3, pady=10)
    app_acept_info.grid(column=0, row=4, sticky=W)
    model_info_header.grid(column=0, row=5, sticky=W)
    model_info.grid(column=0, row=6, sticky=W)
    DB_exp_text_header.grid(column=0, row=7, sticky=W)
    DB_exp_text.grid(column=0, row=8, sticky=W)
    credit_txt.grid(column=0, row=9, sticky=W)

    parser.read("iris_ops.ini")
    saved_language = parser.get('visuals', 'language')
    change_language(saved_language, 'info')

# Helper functions 
def get_one_data(model_dir):
    s_len = s_length_entry.get()
    s_wid = s_width_entry.get()
    p_len = p_length_entry.get()
    p_wid = p_width_entry.get()

    data_str = f"{s_len},{s_wid},{p_len},{p_wid}, Predict"
    predicted_class = predict_one(data_str, model_dir)

    result = return_result(predicted_class)

    result_one_entry.delete(0)
    result_one_entry.insert(0, result) 
 
# Helper Functions options menu    
def color_opt(selection):
    selection_color = selection
    custk.set_appearance_mode(selection_color)

    parser = ConfigParser()
    parser.read("iris_ops.ini")
    parser.set('visuals', 'color', selection)
    with open("iris_ops.ini", 'w') as configfile:
        parser.write(configfile)

def change_language(selection, current_page=any or None):
    global translations
    current_language = selection
    translated_texts = translations[current_language]

    main_title.configure(text=translated_texts['main_title'])
    identif_btn.configure(text=translated_texts['identif_btn_text'])
    inf_btn.configure(text=translated_texts['inf_btn_text'])
    options_btn.configure(text=translated_texts['options_btn_text'])
    credit.configure(text=translated_texts['credit_btn'])

    if current_page != 'main':
            main_title.configure(text=translated_texts['main_title'])
            identif_btn.configure(text=translated_texts['identif_btn_text'])
            inf_btn.configure(text=translated_texts['inf_btn_text'])
            options_btn.configure(text=translated_texts['options_btn_text'])
            credit.configure(text=translated_texts['credit_btn'])

    if current_page == "option":
            men_title.configure(text=translated_texts['men_title'])
            color_label.configure(text=translated_texts['color_label_text'])
            idioma_label.configure(text=translated_texts['idioma_label_text'])
            model_label.configure(text=translated_texts['model_label_text'])
            apli_model_btn.configure(text=translated_texts['apli_model_btn_text'])

    if current_page == 'identif':
            s_length_label.configure(text=translated_texts['s_length_label_text'])
            s_width_label.configure(text=translated_texts['s_width_label_text'])
            p_length_label.configure(text=translated_texts['p_length_label_text'])
            p_width_label.configure(text=translated_texts['p_width_label_text'])
            result_one_label.configure(text=translated_texts['result_label'])
            identif_one_btn.configure(text=translated_texts['identif_one_btn_text'])
            identif_file_btn.configure(text=translated_texts['identif_file_btn_text'])
            info_label.configure(text=translated_texts['result_one_label_info_text'])

    if current_page == 'info':
            global main_title_info, project_exp_header, project_exp, app_acept_info, model_info_header, model_info, DB_exp_text_header, DB_exp_text, credit_txt
            main_title_info.configure(text=translated_texts['main_title_info'])
            project_exp_header.configure(text=translated_texts['project_exp_header'])
            project_exp.configure(text=translated_texts['project_exp'])
            app_acept_info.configure(text=translated_texts['app_acept_info'])
            model_info_header.configure(text=translated_texts['model_info_header'])
            model_info.configure(text=translated_texts['model_info'])
            DB_exp_text_header.configure(text=translated_texts['DB_exp_text_header'])
            DB_exp_text.configure(text=translated_texts['DB_exp_text'])
         
    parser = ConfigParser()
    parser.read("iris_ops.ini")
    global saved_language
    saved_language = parser.get('visuals', 'language')
    parser.set('visuals', 'language', selection)
    with open("iris_ops.ini", 'w') as configfile:
        parser.write(configfile)

    try_change_all(current_language)

def try_change_all(current_language):
    translated_texts = translations[current_language]

    try:
        main_title.configure(text=translated_texts['main_title'])
        identif_btn.configure(text=translated_texts['identif_btn_text'])
        inf_btn.configure(text=translated_texts['inf_btn_text'])
        options_btn.configure(text=translated_texts['options_btn_text'])
        credit.configure(text=translated_texts['credit_btn'])
    except:
        pass

    try:
        men_title.configure(text=translated_texts['men_title'])
        color_label.configure(text=translated_texts['color_label_text'])
        idioma_label.configure(text=translated_texts['idioma_label_text'])
        model_label.configure(text=translated_texts['model_label_text'])
        apli_model_btn.configure(text=translated_texts['apli_model_btn_text'])
    except:
        pass

    try:
        men_title.configure(text=translated_texts['men_title'])
        color_label.configure(text=translated_texts['color_label_text'])
        idioma_label.configure(text=translated_texts['idioma_label_text'])
        model_label.configure(text=translated_texts['model_label_text'])
        apli_model_btn.configure(text=translated_texts['apli_model_btn_text'])
        informations_btn.configure(text=translated_texts['informations_btn_text'])
    except:
        pass

    try:
        s_length_label.configure(text=translated_texts['s_length_label_text'])
        s_width_label.configure(text=translated_texts['s_width_label_text'])
        p_length_label.configure(text=translated_texts['p_length_label_text'])
        p_width_label.configure(text=translated_texts['p_width_label_text'])
        result_one_label.configure(text=translated_texts['result_label'])
        identif_one_btn.configure(text=translated_texts['identif_one_btn_text'])
        identif_file_btn.configure(text=translated_texts['identif_file_btn_text'])
        info_label.configure(text=translated_texts['result_one_label_info_text'])
    except:
        pass

    try:
        main_title_info.configure(text=translated_texts['main_title_info'])
        project_exp_header.configure(text=translated_texts['project_exp_header'])
        project_exp.configure(text=translated_texts['project_exp'])
        app_acept_info.configure(text=translated_texts['app_acept_info'])
        model_info_header.configure(text=translated_texts['model_info_header'])
        model_info.configure(text=translated_texts['model_info'])
        DB_exp_text_header.configure(text=translated_texts['DB_exp_text_header'])
        DB_exp_text.configure(text=translated_texts['DB_exp_text'])
    except:
         pass
    
def change_model():
    directory = model_entry.get()
    result = check_directory_exists(directory)
    if result:
        pass
    else:
        messagebox.showerror("Unable to make change", "Error! No such directory")
        return False
    
    try:
        model = tf.keras.models.load_model(directory)
        test_real(model)

        parser = ConfigParser()
        parser.read("iris_ops.ini")
        dir_save =  replace_special_char(directory)

        parser.set('file_local', 'model', dir_save)
        with open("iris_ops.ini", 'w') as configfile:
                parser.write(configfile)

        messagebox.showinfo("Success", "Success! Saved model location succesfully")
        global MODEL
        MODEL = restore_special_char(str(parser.get('file_local', 'model')))

    except:
        messagebox.showerror("Unable to make change", "Error! not a valid model (.h5) file")
        return False    


if __name__ == "__main__": # MAIN PAGE
    root = custk.CTk()
    root.title("Identificação da Íris")
    root.wm_iconbitmap("midia/icons/flower_icon-icons.com_61045-removebg-preview.ico")

    root.minsize(410, 350)
    root.maxsize(420, 350)

    parser = ConfigParser()
    parser.read("iris_ops.ini")
    saved_language = parser.get('visuals', 'language')
    saved_color = parser.get('visuals', 'color')

    custk.set_appearance_mode(saved_color)
    custk.set_default_color_theme('dark-blue')
    MODEL = restore_special_char(str(parser.get('file_local', 'model')))

    #Style for treeview
    style = ttk.Style()
    style.theme_use("classic")

    main_title = custk.CTkLabel(root, text="Iris Identification", anchor=CENTER, padx=3, pady=2, font=("Times New Roman", 40))
    main_title.grid(column=0, row=0, columnspan=3, pady=40, padx=50)

    credit = custk.CTkLabel(root, text="Feito por Superjoa10 (click link)", padx=10, pady=50, anchor=W, font=("Times New Roman", 10), cursor="hand2", text_color='blue')
    credit.grid(column=0, row=4)
    credit.bind("<ButtonPress-1>", lambda e:callback("https://github.com/Superjoa10"))

    identif_btn = custk.CTkButton(root, text="Iniciar identif.", command=identif_page, anchor= CENTER)
    identif_btn.grid(column=0, row=1, columnspan=3, pady=5)

    inf_btn = custk.CTkButton(root, text="Inf. sobre o projeto", command=information_page, anchor= CENTER)
    inf_btn.grid(column=0, row=2, columnspan=3, pady=5)

    options_btn = custk.CTkButton(root, text="Opções", command=option_page, anchor=CENTER, fg_color='darkgreen')
    options_btn.grid(column=0, row=3, columnspan=3, pady=5)
    
    change_language(saved_language, 'main')
    root.mainloop()
