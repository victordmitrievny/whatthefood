from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import pandas as pd
from sqlalchemy import create_engine
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

app = Flask(__name__, template_folder="templates") 

#------Import data from Excel or DB and make a dataframe (2ND PLACE WITH STORED DATA, JUST TO BE SAFE)
# df = pd.DataFrame()
# df = pd.read_excel(r"/Users/victordmitirev/Desktop/Python/Whatthefood/Foods.xlsx")
# df = df.drop(df.index[-1])
# print(df.iloc[:, :4])

#Read data from SQL database and create a DataFrame
engine = create_engine('mysql+pymysql://z8dn4axxh4kmzt6n:kbwpqkywfh67drep@x8autxobia7sgh74.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/rr3v23rfcclbicza') 
df = pd.read_sql_table('whatthefood', engine)
df = df.drop(df.index[-1])
print(df.iloc[:, :4])

#Launch Frontend
@app.route("/")
def hello(): 
    return render_template('index.html', text="") 

#Launch backend script
@app.route('/uploadimage', methods=['POST'])
def upload_file():
    print('Code is running')
    print('______________')
    uploaded_file = request.files['uploadedFile']
    if uploaded_file.filename != '':

        #Image to text processing using tesseract
        img_var = Image.open(uploaded_file)

        try:
            text_img = pytesseract.image_to_string(img_var)
            print('Text')
            print('______________')
            print(text_img)
            print('Fomatted text')
            print('______________')


            #-------------------------DATA FORMATTING ALGORITHM-----------------


            #------------Replace any connection point between items with ","
            replace_list = ["And", "Or", "Contains", "/", ".", "(",")", 
                            "[", "]", "Ingredients", "Ingredient", "Golden"]
            
            text_string = text_img.lower().title()
            for string in replace_list:
                text_string = text_string.replace(string, ",")
            text_list = text_string.split(",")
            text_formatted = []

            #--------------Remove any unnecessary symbols
            replace_list = ["\n", "]", "[", ")", "(", "!", ":", 
                            "&", "And", "Vitamins", "Minerals", 
                            "Ingredients", "Ingredient"]
            
            for item in text_list:
                for string in replace_list:
                    item = item.replace(string, "")
                    item = item.lstrip().rstrip()
                text_formatted.append(item)
            print(text_formatted)


            print("______________")
            print("Convert complete")
            print("______________")

            for i in text_formatted:
                print(i)

            print("______________")

            #----------Algorithm to find wether parsed ingridients are present within ingridients database 
            output = ""
            result = ""
            dlist = []
            for row in range(0,len(df)):
                db_element = df.iloc[row,1]
                for parsed_element in text_formatted:
                    if db_element in parsed_element:
                        #Print wether its safe to consume
                        ingredient = df.iloc[row,1] + " - " + df.iloc[row,2] + " - " + df.iloc[row,3] + "."
                        print(ingredient)

                        #Create JSON dictionary here
                        dict = {"name": df.iloc[row,1], "category": df.iloc[row,2], "effect": df.iloc[row,3] }
                        dlist.append(dict)

                        break
                    
            print("_______________________")
            print("_________DICTIONARY________")
            print(dlist)

            print("_______________________")
            print("_________HTML________")



            #-------------------Render a dynamic HTML table for the contents
            table = """<div class ="output-div">
                        <div class ="inner-output-div">
                            <div class = table-row>
                                <div class = table-cell> NAME:       </div>
                                <div class = table-cell> CATEGORY:   </div>
                                <div class = table-cell> EFFECT:     </div>
                            </div>
                            <div class = table-row>
                                <div class = table-cell>  &nbsp       </div>
                                <div class = table-cell>              </div>
                                <div class = table-cell>              </div>
                            </div>
                        
                        """
            sus_presence = False
            for element in dlist:
                if element['effect'] in "Suspicious ":
                    css = "table-cell-red"
                    sus_presence = True
                else:
                    css = "table-cell"
                table_row = "<div class =" + "table-row" + ">"
                table_cell1 = "<div class =" + css + ">" + element['name'] + "</div>"
                table_cell2 = "<div class =" + css + ">" + element['category'] + "</div>"
                table_cell3 = "<div class =" + css + ">" + element['effect'] + "</div>"
                closediv = "</div>"
                table = table + table_row + table_cell1 + table_cell2 + table_cell3 + closediv
            #Close table with a div
            table = table + """</div>
                                    </div>"""


            #Create several "static" elements for an HTML output

            no_conclusion = False #The program assume we'll find some ingredients against our database
            if dlist != []:
                identified_string =  "WE'VE IDENTIFIED THE FOLLOWING COMPOUNDS IN YOUR PRODUCT:"
            else:
                identified_string = "THIS PRODUCT CONTAINS NO COMPOUNDS AVAILABLE IN OUR DATABASE"
                no_conclusion = True 

                
            identified_string_container =   """ <div class="center-container"> 
                                                    <p>
                                            """         + identified_string + """     
                                                    </p> 
                                                </div>
                                            """
                
            if sus_presence == True:
                conclusion = "YOUR PRODUCT CONTAINS POTENTIALLY DANGEROUS COMPOUNDS. MORE RESEARCH IS ADVISED."
                conclusion_css = "conclusion-container-red"
            if sus_presence == False:
                conclusion = "NO HARMFUL COMPOUNDS IDENTIFIED. YOUR PRODUCT IS LIKELY SAFE TO CONSUME."
                conclusion_css = "conclusion-container"   
            if no_conclusion == True: #if there is no conclusion due to not being able to identify any compounds, I am not displaying conclusion string + setting opacity of the table to 0
                conclusion_css = """ "conclusion-container-red" style= "display: none" """
                table = """<div class ="output-div" style = "opacity: 0">
                            <div class ="inner-output-div" style = "opacity: 0">"""

            
            conclusion_container = """<div class= """ + conclusion_css + """> 
                                        <p>
                                            <span style="color: #475549; font-size: 20px;">CONCLUSION: </span>
                                    """     + conclusion + """
                                        </p>
                                    </div>"""

            print(table)

            output = identified_string_container + table + conclusion_container


            return output, 200
        
        except Exception as e:
            print(f'An exception occurred: {e}')
            print('______________')
            output =  """<div class= "conclusion-container"> 
                                        <p>
                                            <span style="color: #475549; font-size: 20px;">
                                                UNEXPECTED ERROR OCCURRED. TRY UPLOADING ANOTHER FILE.
                                            </span>
                                        </p>
                                    </div>"""
            return output, 200

    else:

        print("No file selected")
        return "No file selected."

if __name__ == '__main__':
    app.run()







