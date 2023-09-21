import streamlit as st
from generate_documentation import get_documentation, combine_documentation

st.set_page_config(layout="wide", page_title="Crayon Documentation Generator", page_icon="📄")

############################################################################################
############## LOGIC #######################################################################
###### Multiple code files -> Documentation for each file -> Combine Documentation #########
###### Generate a technical blog post based on the documentation by chunking ###############

def process_files(project_details_input, uploaded_files):
    file_contents = []
    documentation = []
    for file in uploaded_files:
        file_contents.append(file.getvalue().decode())
    
    for file_text in file_contents:
        documentation.append(get_documentation(project_details_input, file_text))

    return documentation

def process_project_details():
    pass

def main():
    st.title("Crayon Documentation Generator")

    # Divide the screen into 2 columns: left_column and right_column
    left_column, right_column = st.columns([1, 2])

    # Use the left column for input
    with left_column:
        project_details_input = st.text_area("Enter a little bit about your project including any text involving solution design", height=100)
        
        uploaded_files = st.file_uploader("Upload code files as txt, up to 1500 lines per file", type=["txt"], accept_multiple_files=True)
        
        documentation = st.button("Generate Documentation", help="Click to process uploaded files")

    # If "Process" button is clicked, show the output in the right column
    if documentation:
        result = process_files(project_details_input, uploaded_files)
        result_text=' '.join(result)
        resulting_documentation = combine_documentation(project_details_input, result_text)
        with right_column:
            st.markdown(resulting_documentation)

if __name__ == "__main__":
    main()
