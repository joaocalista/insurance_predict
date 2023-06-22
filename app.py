import pickle
import gradio as gr
import pandas as pd

#codigo css para centralizar texto
css = """
#centered-text {text-align: center;}
}

"""

#funcao que centraliza o texto do output
def format_output(text):
    width = 380 
    text_len = len(text)
    padding = ' ' * ((width - text_len) // 2)
    return padding + text + padding


#funcao que faz o pre-processamento dos daddos
def preprocess_data(age_input, sex_input, bmi_input, children_input, smoker_input, region_input):

    with open("preprocessor.pkl", "rb") as d:
        preprocessor  = pickle.load(d)
    
    return preprocessor.transform(pd.DataFrame({'age': [age_input], 'sex': [sex_input], 'bmi': [bmi_input], 'children': [children_input], 'smoker': [smoker_input], 'region': [region_input]}))



#funcao que realiza as predicoes
def make_prediction(age_input, sex_input, bmi_input, children_input, smoker_input, region_input):

    #verifica se todos os campos estao preenchidos
    if age_input and sex_input and bmi_input and smoker_input and region_input:

        preprocessed_data = preprocess_data(age_input, sex_input, bmi_input, children_input, smoker_input, region_input)

        with open("model_insurance.pkl", "rb") as f:
            model  = pickle.load(f)

        pred = model.predict(preprocessed_data)
        
        return format_output(f'$ {round(pred[0], 2):,.2f}')

    else:
        return format_output('Incorrect Informations!')
    

#funcao que apaga os registros
def clear():
    return [None for i in range(7)]


#bloco que cria todo o layout
with gr.Blocks(title='HealthSure', theme='gradio/dracula_revamped', css=css) as app:

    gr.Markdown('# Insurance Premium Prediction 🏥', elem_id="centered-text")

    #inputs
    age_inp = gr.Number(label = "Enter Age (must be 18 or older)", maximum=130, minimum=18)
    sex_inp = gr.Dropdown(['male', 'female'], label='Enter Sex')
    bmi_inp = gr.Slider(0, 200, label = "Enter BMI", step=0.1)
    children_inp = gr.Number(label = "Enter the Number of Dependents", minimum=0)
    smoker_inp = gr.Radio(['yes', 'no'], label = 'Is the Individual a Smoker?')
    region_inp = gr.Radio(['southwest', 'southeast', 'northwest', 'northeast'], label = 'Inform the Region in Which the Individual Lives')

    #cria botoes
    with gr.Row():
        predict_btn = gr.Button('Predict')
        clear_btn = gr.Button('Clean')

    #define o output (local em que sera mostrada a predicao)
    output = gr.Textbox(label = 'Premium', elem_id='centered-text')

    #define o que acontece quando os botoes sao acionados
    predict_btn.click(fn = make_prediction, inputs=[age_inp, sex_inp, bmi_inp, children_inp, smoker_inp, region_inp], outputs=[output])
    clear_btn.click(fn=clear, inputs=[], outputs=[age_inp, sex_inp, bmi_inp, children_inp, smoker_inp, region_inp, output])


if __name__ == '__main__':
        
    app.launch()
