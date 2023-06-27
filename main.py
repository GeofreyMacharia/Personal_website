#---------------------------------------------------------------IMPORTS------------------------------------------------------------------------
import base64
import streamlit as st
from PIL import Image
import json
# import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
# load lottiefile
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
from streamlit_option_menu import option_menu
st.set_page_config(
        page_title="GeoFreyMacharia",
        page_icon="speech_balloon",
        layout="wide",
    )
# -------------------------------------------------------------FOREGROUND----------------------------------------------------------------------------------
# # remove space at the top
st.markdown("""<style> 
                .block-container {
                    padding-top: 2.5%; 
                    padding-bottom: 0%;
                    }
            </style>""", unsafe_allow_html=True
)

# get background image from local machine
@st.cache_data()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .anim {
    background-image: url("data:image/png;base64,%s");
    background-repeat: no-repeat;
    background-size:contain;
    background-position: center center;
    
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


@st.cache_data()
def get_base64_of_bin_file2(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg2(png_file):
    bin_str2 = get_base64_of_bin_file2(png_file)
    page_bg_img2 = '''
    <style>
    .hobby{
    background-image: url("data:image/png;base64,%s");
    background-repeat: no-repeat;
    background-size:contain;
    background-position: center center;
    }
    </style>
    ''' % bin_str2
    
    st.markdown(page_bg_img2, unsafe_allow_html=True)
    return


@st.cache_data()
def get_base64_of_bin_file3(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg3(png_file):
    bin_str3 = get_base64_of_bin_file3(png_file)
    page_bg_img3 = '''
    <style>
    .My_face{
    background-image: url("data:image/png;base64,%s");
    background-repeat: no-repeat;
    background-size:contain;
    background-position: center center;
    

    }
    </style>
    ''' % bin_str3
    
    st.markdown(page_bg_img3, unsafe_allow_html=True)
    return

@st.cache_data()
def get_base64_of_bin_file4(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg4(png_file):
    bin_str4 = get_base64_of_bin_file4(png_file)
    page_bg_img4 = '''
    <style>
    .coming{
    background-image: url("data:image/png;base64,%s");
    background-repeat: no-repeat;
    background-size:contain;
    background-position: center center;
    

    }
    </style>
    ''' % bin_str4
    
    st.markdown(page_bg_img4, unsafe_allow_html=True)
    return


@st.cache_data()
def get_base64_of_bin_file5(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg5(png_file):
    bin_str5 = get_base64_of_bin_file(png_file)
    page_bg_img5 = '''
    <style>
    .cont {
    background-image: url("data:image/png;base64,%s");
    background-repeat: no-repeat;
    background-size:contain;
    background-position: center center;
    
    }
    </style>
    ''' % bin_str5
    
    st.markdown(page_bg_img5, unsafe_allow_html=True)
    return


def st_button(icon, url, iconsize):
    if icon == 'youtube':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
                    <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                </svg> 
            </a>
        </p>'''
    elif icon == 'linkedin':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
            </a>
        </p>''' 
    return st.markdown(button_code, unsafe_allow_html=True)
icon_size = 30




# -----------------------------------------------------------------------TABS---------------------------------------------------------------------------------
st.write(' ')
tab1, tab2, tab3, tab4 = st.tabs(["Home", "About", "Projects", "Contact"])
font_css = """ 
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
    margin-top:30px;
    padding-bottom:25px;
    margin-right:20px;
    margin-left:15px;
    font-size: 20px;
}
</style>
"""

st.write(font_css, unsafe_allow_html=True)
#`````````````````````````````````````````````````````````````BACKGROUND IMAGE AND NAMES``````````````````````````````````````````````````````````````````````````
with tab1:
    main_con = st.container()
    with main_con:
        
        main_col1, main_col2, main_col3, main_col4 = st.columns([.5 , 1 , 1 , .5]) 
        with main_col2:
            st.markdown('''<div class="Home"></div>''',unsafe_allow_html=True)
            st.markdown('''<div class="My_face"></div>''',unsafe_allow_html=True)
            set_png_as_page_bg3('images\\Profile_face.png')
            st.markdown('''<div class="My_name"> Geofrey Macharia</div>''',unsafe_allow_html=True)
            st.markdown('''<div class="My_work">Data scientist | Data Analyst | Software Engineer </div>''',unsafe_allow_html=True)

            st.markdown('''
                <div class="linkedIN">
                    <a href="https://www.linkedin.com/in/geofrey-macharia-52b172226/" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                        <svg xmlns="http://www.w3.org/2000/svg" width=30 height=30 fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                            <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                        </svg>
                    </a>
                </div>''', unsafe_allow_html=True)
            st.markdown('''
                <div class="GitHub">
                    <a href="https://github.com/GeofreyMacharia/" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width=30 height=30 fill="currentColor">
                    <path data-name="layer2"d="M32 0a32.021 32.021 0 0 0-10.1 62.4c1.6.3 2.2-.7 2.2-1.5v-6c-8.9 1.9-10.8-3.8-10.8-3.8-1.5-3.7-3.6-4.7-3.6-4.7-2.9-2 .2-1.9.2-1.9 3.2.2 4.9 3.3 4.9 3.3 2.9 4.9 7.5 3.5 9.3 2.7a6.93 6.93 0 0 1 2-4.3c-7.1-.8-14.6-3.6-14.6-15.8a12.27 12.27 0 0 1 3.3-8.6 11.965 11.965 0 0 1 .3-8.5s2.7-.9 8.8 3.3a30.873 30.873 0 0 1 8-1.1 30.292 30.292 0 0 1 8 1.1c6.1-4.1 8.8-3.3 8.8-3.3a11.965 11.965 0 0 1 .3 8.5 12.1 12.1 0 0 1 3.3 8.6c0 12.3-7.5 15-14.6 15.8a7.746 7.746 0 0 1 2.2 5.9v8.8c0 .9.6 1.8 2.2 1.5A32.021 32.021 0 0 0 32 0z">fill="#202020"</path>
                    <path data-name="layer1" d="M12.1 45.9c-.1.2-.3.2-.5.1s-.4-.3-.3-.5.3-.2.6-.1c.2.2.3.4.2.5zm1.3 1.5a.589.589 0 0 1-.8-.8.631.631 0 0 1 .7.1.494.494 0 0 1 .1.7zm1.3 1.8a.585.585 0 0 1-.7-.3.6.6 0 0 1 0-.8.585.585 0 0 1 .7.3c.2.3.2.7 0 .8zm1.7 1.8c-.2.2-.5.1-.8-.1-.3-.3-.4-.6-.2-.8a.619.619 0 0 1 .8.1.554.554 0 0 1 .2.8zm2.4 1c-.1.3-.4.4-.8.3s-.6-.4-.5-.7.4-.4.8-.3c.3.2.6.5.5.7zm2.6.2c0 .3-.3.5-.7.5s-.7-.2-.7-.5.3-.5.7-.5c.4.1.7.3.7.5zm2.4-.4q0 .45-.6.6a.691.691 0 0 1-.8-.3q0-.45.6-.6c.5-.1.8.1.8.3z" fill="#202020"></path>
                    </svg>
                    </a>
                </div>''', unsafe_allow_html=True)


        with main_col3:
            st.markdown('''<div class="My_profession"></div>''',unsafe_allow_html=True)
            st.markdown('''<div class="greetings"><b>Hello</b>,</div>''',unsafe_allow_html=True)
            st.markdown('''<div class="intro">glad to have you drop by :)</div>''', unsafe_allow_html=True)
            st.markdown('''<div class="Me"><b>Me, Myself and I </b></div>''', unsafe_allow_html=True)
            st.markdown('''<div class="home_details"> I am a passionate engineer with the expertise and desire for providing insight and solving problems.
            <br>My primary interests lie in Artificial and business Intelligence, health care, software development and the list grows on.</div>''', unsafe_allow_html=True)

# ----------------------------------------------------------------------ABOUT ME-----------------------------------------------------------------------------
with tab2:
    about_con = st.container()
    with about_con:
        
        # st.markdown('''<div style=' height:5vh; width:40%; margin-left:42%; margin-top:-1%; margin-bottom:2%;
        #     font-size:15px; '>Get to know more about me :)</div>''', unsafe_allow_html=True)
        inner_about = st.container()
        with inner_about:
            abt_img, abt_info,= st.columns([.6, 1])
        with abt_img:
            personal_img = Image.open('images\\Profile_face.png')
            st.image(personal_img)


        with abt_info:
            st.markdown("<div style='text-align: center; font-size:30px; font-weight:600; text-decoration: underline; margin-top:5%; margin-bottom:5%;'> PERSONAL DETAILS </div>", unsafe_allow_html=True)
            # st.write(''' As a child I would often question the workings of things in the present worked and with the passing of age
            # I performed a substantial number experiments however trivial, that would provide answers to questions i thought off.''')
            # st.markdown('''My Interest in  Data Science was brought to life by my desire to know what entails the creation of AI based applications,
            # which lead me down the data journey, further enriching my mind as i uncovered insights from data.I have been in the data science field for nearly half a decade. The time encompasses my learning process as well as
            # aiding over 50 clients with their respective projects. ''')
            # st.markdown('''Would you like to work together?  Please reach out to me via e-mail. ''')
            st.markdown('''<div class='personal_me'> My Interest in  Data Science was brought to life by my desire to know what entails the creation of AI based applications,
            which lead me down the data journey, further enriching my mind as i uncovered insights from data.I have been in the data science field for nearly half a decade. The time encompasses my learning process as well as
            aiding over 50 clients with their respective projects. 
            <br> <br> Would love to work with you :) <br>  Please reach out to me via e-mail.  </div>''',unsafe_allow_html=True)

        about_tab1, about_tab2, about_tab3 = st.tabs(["Work n Skills", "Education", "Hobbies"])

        with about_tab1:
            st.markdown('''<div class="Net_intern"> <b>Network Engineer Intern</b> <br> ICT Authority <br> Sept 2021 - Dec 2021 </div>''', unsafe_allow_html=True)
            st.markdown('''<div class="Net_intern_info"> Identified issues and provided crucial troubleshooting analysis of servers. <br>Configured back up for Government Common Core Network and National Optical Fiber Backbone. <br>
            </div>''', unsafe_allow_html=True)
            
            st.markdown('''<div class="Free"> <b>Free Lancer</b> <br> July 2022 - Present </div>''', unsafe_allow_html=True)
            st.markdown('''<div class="Free_info">Built, Refined, and Documented machine learning based
             projects. <br> Designed and executed deep learning, image processing and convolutional neural network projects.</div>''', unsafe_allow_html=True)
            st.markdown('''<div class = "vertical"></div>''', unsafe_allow_html=True)

            st.markdown("<h3 style='text-align: center; text-decoration: underline; margin-left:-22%; margin-bottom:2%; '> Skills </h3>", unsafe_allow_html=True)

            st.markdown('''<div class="Data_analysis"><b>Data Analysis</b></div>
            ''', unsafe_allow_html=True)
            st.markdown('''<div class="Data_viz"><b>Data Visualization</b></div>
            ''', unsafe_allow_html=True)
            st.markdown('''<div class="Data_extract"><b>Data Transformation</b></div>
            ''', unsafe_allow_html=True)
            
            st.markdown('''<div class="web_dev"><b>Web Development</b></div>
            ''', unsafe_allow_html=True)
            st.markdown('''<div class="Data_pred"><b>Predictive Modelling</b></div>
            ''', unsafe_allow_html=True)
            st.markdown('''<div class="python_prog"><b>Python Programming</b></div>
            ''', unsafe_allow_html=True)

            st.markdown('''<div class="sql"><b>SQL</b></div>
            ''', unsafe_allow_html=True)
            st.markdown('''<div class="Ml"><b>Machine Learning</b></div>
            ''', unsafe_allow_html=True)
            st.markdown('''<div class="front_end"><b>Frontend Development</b></div>
            ''', unsafe_allow_html=True)

            st.markdown('''<div class='anim'></div>''',unsafe_allow_html=True)
            set_png_as_page_bg('anime\\programming.gif')

        
        
        
        
        
        
        with about_tab2:
            left_about, right_about = st.columns([.5,.5],gap='small')
            with left_about:
                st.markdown('''<div class="Bachelors"> <b>Bachelor's Degree</b> <br>Sept 2018 - Nov 2022 </div>''', unsafe_allow_html=True)
                st.markdown('''<div class="Ml_cert"> <b>Machine Learning Certification </b> <br>Nov 2021 </div>''', unsafe_allow_html=True)
                st.markdown('''<div class="Ds_cert"> <b>Data Science  Certification </b> <br>Nov 2021 </div>''', unsafe_allow_html=True)
                st.markdown('''<div class="High"> <b>High School Degree</b> <br>Feb 2014 - Dec 2017 </div>''', unsafe_allow_html=True)
                
            with right_about:

                st.markdown('''<div class="Bachelors_info"> <b>Murang'a University of Technology</b> <br>
                Majored in Information technology. Graduated with Second Upper honors. Former Chess captain of school team.  </div>''', unsafe_allow_html=True)
                
                
                st.markdown('''<div class="Ml_cert_info"> <b>365 Data Science </b> <br>Award for completion of the course. 
                Entails theoretical and practical information regarding machine learning.</div>''', unsafe_allow_html=True)
                
                st.markdown('''<div class="Ds_cert_info"> <b>365 Data Science </b> <br>Award for completion of the course.
                A complete introduction to big data and data science. </div>''', unsafe_allow_html=True)
                st.markdown('''<div class="High_info"> <b>Menengai High School</b> <br>Graduated with C+ performance on the national examination. </div>''', unsafe_allow_html=True)
            
            st.markdown('''<div class = "vertical2"></div>''', unsafe_allow_html=True)
            
            
        
        
        
        
        with about_tab3:
            st.markdown('''<div class='hobby' style=' height:40vh; width:75%; margin-left:10%; margin-top:5%;'></div>''',unsafe_allow_html=True)
            set_png_as_page_bg2('anime\\not.gif')



#-----------------------------------------------------------------------PROJECTS---------------------------------------------------------------------------------
with tab3:
    project_con = st.container()

    with project_con:
        st.markdown("<h3 style='text-align: center; text-decoration: underline; '> PROJECTS </h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; margin-bottom:2%;  font-size:14px; font-weight:200; '>Take a look at my recent work. </h5>", unsafe_allow_html=True)
        proj2, proj3,proj4 = st.columns([.3,.274,.2368])
        with proj2:
            vina_home = Image.open("images\\Home.png")
            st.image(vina_home)
            st.markdown('---')
            st.markdown('''<div class="Vina"><a href=" https://vina-homes.onrender.com"><b>VINA HOMES</b></a></div>''', unsafe_allow_html=True)
            st.markdown('''<div class="Vina_info"'>Deployed web application made using python and streamlit
            which uses two machine learning algorithms to predict the price based on the values selected by the user.</div>''', unsafe_allow_html=True)
            st.markdown('''<div class= "Vina_further"><a href="https://github.com/GeofreyMacharia/Vina-House"><b>Further details</b></a></div>''', unsafe_allow_html=True)
        with proj3:
            time_img = Image.open("images\\time-series.png")
            st.image(time_img)
            st.markdown('---')
            st.markdown('''<div class="Time"><a href=" https://github.com/GeofreyMacharia/Timeseries-Analysis-and-Forecasting-Projects"><b>TIME SERIES</b></a></div>''', unsafe_allow_html=True)
            st.markdown('''<div class="Time_info" >An analysis of multiple timeseries datasets which entails stationarity examination
            as well as, forecasting techniques and results.</div>''', unsafe_allow_html=True)
            st.markdown('''<div class= "Time_further">
            <a href="https://github.com/GeofreyMacharia/Timeseries-Analysis-and-Forecasting-Projects"><b>Further details</b></a></div>''', unsafe_allow_html=True)


        with proj4:
            personal_web = Image.open("images\\personal.png")
            st.image(personal_web)
            st.markdown('---')
            st.markdown('''<div class= "Personal"><a href=" https://vina-homes.onrender.com"><b>PERSONAL WEBSITE</b></a></div>''', unsafe_allow_html=True)
            st.markdown('''<div class= "Personal_info" >Deployed website providing details about myself as well as the providing a gateway to
            my achievements.</div>''', unsafe_allow_html=True)
            st.markdown('''<div class= "Personal_further" >
            <a href="https://github.com/GeofreyMacharia/Vina-House"><b>Further details</b></a></div>''', unsafe_allow_html=True)
        
        proj5, proj6,proj7 = st.columns([.3,.3335,.25])
        with proj5:
            heart = Image.open('images\\heart2_.png')
            st.image(heart)
            st.markdown('---')
            st.markdown('''<div class= "Heart"><a href=" https://github.com/GeofreyMacharia/Heart-Disease-Detection"><b>HEART DISEASE DETECTION</b></a></div>''', unsafe_allow_html=True)
            st.markdown('''<div class= "Heart_info" >Analysis of heart disease causes, with the goal of predicting the likelihood
             of people falling prey to heart disease..</div>''', unsafe_allow_html=True)
            st.markdown('''<div class= "Heart_further" >
            <a href="https://github.com/GeofreyMacharia/Heart-Disease-Detection"><b>Further details</b></a></div>''', unsafe_allow_html=True)
        

        with proj6:
            
            natural_images = Image.open('images\\conv2.jpg')
            st.image(natural_images)
            st.markdown('---')
            st.markdown('''<div class= "Neural"><a href=" https://github.com/GeofreyMacharia/Natural-Images-with-CNN"><b>NATURAL IMAGES CLASSIFICATION </b></a></div>''', unsafe_allow_html=True)
            st.markdown('''<div class= "Neural_info" >Convolutional neural network classifying 8 different classes of images.</div>''', unsafe_allow_html=True)
            st.markdown('''<div class= "Neural_further">
            <a href="https://github.com/GeofreyMacharia/Natural-Images-with-CNN"><b>Further details</b></a></div>''', unsafe_allow_html=True)
        
        # with proj7:
        #     financial = Image.open('images\\financial2.png')
        #     st.image(financial)



# -------------------------------------------------------------------------CONTACT-------------------------------------------------------------------------------------------------------------------------
# read css local file
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)

with tab4:
    contact_con = st.container()
    with contact_con:
        st.markdown("<h4 style='text-align: center; text-decoration: underline; font-size:30px;'> CONTACT </h4>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; font-size:16px; margin-left:1%; margin-bottom:3%; font-weight:300; '> Let's get in touch 😊 </h5>", unsafe_allow_html=True)
        contact_col1, contact_col2 , contact_col3 = st.columns([.3, .5,.5])
        with contact_col1:
            st.markdown('''<div class='cont'></div>''',unsafe_allow_html=True)
            set_png_as_page_bg5('anime\\contact.gif')

            # lottie_contact = load_lottiefile("anime\\contact.json")
            # st.lottie(lottie_contact,speed= 1.5,reverse=False,
            #     loop= True,height=200,width=200,key=None,
            #     quality="low", # high, low
            #     # renderer="svg", #  canvas
            # )
        with contact_col2:
            st.markdown("<div class='about_app_title'> <b>About Website.</b></div>", unsafe_allow_html=True)
            st.markdown('''<div class='about_app'>This website was coded in python, CSS, and streamlit.
            It is hosted on render server accessed from my github page.</div>''', unsafe_allow_html=True)
        with contact_col3:
            st.write(' ')
            st.write(' ')
            contact_form = '''<form id="my_form" action="https://formsubmit.co/geofreymacharia09@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="email" name="email" placeholder= "Your Email" required>
            <textarea name="message" placeholder="Name and Message"></textarea>
            <button id="submit_butt" type="submit">Send</button>
                            </form>'''
                
            st.markdown(contact_form, unsafe_allow_html=True)
            local_css("style\\style.css")
    




