#%%
import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import tkinter as tk
#%%


ventana = tk.Tk()
ventana.geometry('200x200')



input_puesto = tk.StringVar()
input_ubicacion = tk.StringVar()
input_skill = tk.StringVar()


def enviar(input_puesto, input_ubicacion, input_skill):
    return input_puesto, input_ubicacion, input_skill


tk.Label(ventana, text = 'Puesto').pack()
input_puesto = tk.StringVar()
cuadro_puesto = tk.Entry(ventana, textvariable = input_puesto).pack()

tk.Label(ventana, text = 'ubicacion').pack()
input_ubicacion = tk.StringVar()
cuadro_puesto = tk.Entry(ventana, textvariable = input_ubicacion).pack()

tk.Label(ventana, text = 'skill').pack()
input_skill = tk.StringVar()
cuadro_skill = tk.Entry(ventana, textvariable = input_skill).pack()

enviar = tk.Button(ventana, text= 'Iniciar', command=enviar(input_puesto.get(),input_ubicacion.get(),input_skill.get())).pack()
ventana.mainloop()

#%%

input_puesto = input_puesto.get()
input_ubicacion = input_ubicacion.get()
input_skill = input_skill.get()

#%%


print(input_skill)
"""
input_puesto = input('Ingrese un puesto de trabajo: ')
input_ubicacion = input('Ingrese la ubicacion de preferencia: ')
input_skill = input('Ingrese herramienta tecnica deseada: ')"""


print("Linkedin Scrapper - Inicio")
inicio = datetime.datetime.now() 

driver = webdriver.Chrome(r'C:\\Users\\gboschin\Desktop\\LI SCRAPER\\chromedriver.exe')
time.sleep(3) 

email = "elincognito1996@gmail.com"
password = "holamundo123"

driver.get('https://www.linkedin.com/login') 
driver.maximize_window()
time.sleep(3) 

driver.find_element(By.ID, 'username').send_keys(email) 
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'password').send_keys(Keys.RETURN)
time.sleep(5)


driver.get("https://www.linkedin.com/")
time.sleep(5)

timer = datetime.datetime.now()
print('Tiempo: ', timer - inicio,' - loggeado') 
time.sleep(10)


search = driver.find_element_by_xpath("//input[@aria-label='Buscar']")
#input_puesto = input('Ingrese un puesto de trabajo: ')
#keywords = 'Data engineer'
search.send_keys(input_puesto)
time.sleep(3)
search.send_keys(Keys.ENTER)
time.sleep(10)

timer = datetime.datetime.now()
print('Tiempo: ', timer - inicio,' - busqueda iniciada') 
time.sleep(5)


#personas = driver.find_element_by_id('Personas')                          
personas = driver.find_element_by_css_selector('#search-reusables__filters-bar > ul > li:nth-child(1) > button')
time.sleep(5)
personas.click()
time.sleep(5)



ubicacion = driver.find_element_by_xpath('//button[@aria-label="Filtro «Ubicaciones». Al hacer clic en este botón, se muestran todas las opciones del filtro «Ubicaciones»."]')
ubicacion.click()
time.sleep(3)
ubicacion = driver.find_element_by_xpath("//input[@aria-label='Añade una ubicación']")
#input_ubicacion = input('Ingrese la ubicacion de preferencia: ')
#keywords = "Argentina"
ubicacion.send_keys(input_ubicacion)
time.sleep(5)
ubicacion.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
ubicacion.send_keys(Keys.TAB, Keys.ESCAPE)
time.sleep(5)



filtros = driver.find_element_by_xpath('//*[@id="search-reusables__filters-bar"]/div/div/button').click()
time.sleep(5)
filtros = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/li[12]/ul/li[3]/label/input')
time.sleep(5)
#input_skill = input('Ingrese herramienta tecnica deseada: ')
#keywords = "Python"
filtros.send_keys(input_skill)
time.sleep(5)
filtros = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div/button[2]').click()
time.sleep(5)

timer = datetime.datetime.now()
print('Tiempo: ', timer - inicio,' - filtros agregados') 
time.sleep(5)




todos = []
n=0
direcciones = []
name_list = []
cargo_list = []
locality_list = []
about_list = []
job_list = []

#%%
n = 0

while n < 5:
    n += 1
    # Traemos webelements de los 10 candidatos mostrados en pantalla
    candidatos = driver.find_elements_by_class_name("reusable-search__result-container")
    time.sleep(2)
    #candidatos = list(candidatos)
            
    timer = datetime.datetime.now()
    print('Tiempo: ',timer - inicio, ' - iteracion numero ', n ,'')
    time.sleep(2)

    # Traemos el link de cada webelement de los perfiles

    for i in range(len(candidatos)):
        direcciones.append(candidatos[i].find_elements_by_class_name("app-aware-link")[1].get_attribute('href'))
        time.sleep(2)

    for people in candidatos:
        people_str = str(people.text).split("\n")
        try:
            name = people_str[0]
        except:
            name = "none"
        try:
            cargo = people_str[4]
        except:
            cargo = "none"
        try:
            locality = people_str[5]
        except:
            locality = "none"
        try:
            job = people_str[6]
        except:
            job = "none"    
            
        name_list.append(name)
        cargo_list.append(cargo)
        locality_list.append(locality)
        job_list.append(job)   

        # tengo que eliminar duplicados porque por cada iteracion estoy volviendo agregar los datos
    
    try:            
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        driver.implicitly_wait(5)
        search_button = driver.find_element(By.XPATH,"//button[@aria-label='Siguiente']")
        search_button.click()
        time.sleep(3)
    except:
        try:
            xpath = "//button[@aria-label='Siguiente']"
            timeout = 15    
            WebDriverWait(driver, timeout).until(ec.presence_of_element_located(By.XPATH))
            driver.find_element_by_xpath(xpath).click()
            #WebDriverWait(driver, 20).until(EC.visibility_of_element_located(By.XPATH,"//button[@aria-label='Siguiente']"))
        except:
            continue

"""print('periles obtenidos: ', len(name_list))

print('candidatos: ', len(candidatos))
print('name list: ', len(name_list))
print('cargo_list: ', len(cargo_list))
print('locality_list: ', len(locality_list))
print('job_list: ', len(job_list))


print('candidatos: ', candidatos)
print('name list: ', name_list)
print('cargo_list: ', cargo_list)
print('locality_list: ', locality_list)
print('job_list: ', job_list)

print(candidatos[0].tag_name)
"""


timer= datetime.datetime.now()
print('Tiempo: ',timer - inicio,' - traemos lista de perfiles')




if os.path.exists('profiles.xlsx'):
    os.remove('profiles.xlsx')

df_profiles = pd.DataFrame(list(zip(name_list,cargo_list,locality_list,job_list,direcciones)),
                                    columns= ['Nombre','Cargo','Localidad','Trabajo','links'])

df_profiles.to_excel('profiles.xlsx')

timer= datetime.datetime.now()
print('Tiempo: ', timer - inicio, ' - Perfiles exportados en excel como "profiles.xlsx',)



######################## limpieza #################################

#pd.set_option('max_rows', None)

# Crear Dataframe de la nomina de empleados de NTT
df_nomina = pd.read_excel("C:\\Users\\gboschin\\Desktop\\LI SCRAPER\\Script\\nomina.xlsx", header=None, names=["Nombres", "Vacío" ,"Links"])
# Crear DF con las personas contactadas recientemente 
df_contactados = pd.read_excel("C:\\Users\\gboschin\\Desktop\\LI SCRAPER\\Script\\Candidatos contactados - PA.xlsx", names=["Nombres","LinkedIn","Ultima fecha de contacto"])
# Crear DF con los datos obtenidos del scrapper
df_profiles = pd.read_excel("C:\\Users\\gboschin\\Desktop\\LI SCRAPER\\Script\\profiles.xlsx")


df_nomina.drop(['Vacío'], axis=1, inplace=True)

df_nomina["NTT"] = "Sí, no contactar"

# Agrego una columna para identificar quienes fueron contactados recientemente

df_contactados["Candidato reciente"] = "Sí, no contactar"

# Dividir el los registros de la columna links. Me quedo con la primera parte, para que sea igual a la de la nómina de empleados de NTT y agrego una '/'

df_profiles['links'] = df_profiles['links'].apply(lambda x: x.split('?')[0] + '/')

# Agregar las columnas de la nómina al df_profiles

df_profiles = df_profiles.join(df_nomina.set_index('Links'), on='links')

# Agregar las columnas del df_contactados al df_profiles

df_profiles = df_profiles.join(df_contactados.set_index('LinkedIn'), on='links', how='left', lsuffix='_left', rsuffix='_right')

# Reemplazar los NAN

df_profiles["NTT"].fillna("No", inplace=True)
df_profiles["Candidato reciente"].fillna("No", inplace=True)

# Eliminar columnas: Unnamed: 0, Nombres_left, Nombres_right, Ultima fecha de contacto

df_profiles.drop(['Unnamed: 0'], axis=1, inplace=True)
df_profiles.drop(['Nombres_left'], axis=1, inplace=True)
df_profiles.drop(['Nombres_right'], axis=1, inplace=True)
df_profiles.drop(['Ultima fecha de contacto'], axis=1, inplace=True)




if os.path.exists('lista_contactar.xlsx'):
    os.remove('lista_contactar.xlsx')

df_profiles.to_excel('lista_contactar.xlsx')

timer= datetime.datetime.now()
print('Tiempo: ', timer - inicio, ' - Perfiles exportados en excel como "lista_conectar.xlsx')


# %%
