# General Imports
import streamlit as st

# Package Imports
from utils.input_format import InputFormat
from utils.api_caller import get_predictions

def prediction():
    """Returns the prediction page of the app"""
    try:
        st.write("# Prediction Form 👇")
        st.write(
                """
                Enter the details of the job posting in the form below.
                """
        )
        st.write("Is salary mentioned in the job description?")
        salary_range = st.selectbox("",["Not Mentioned","Mentioned"],key="salary_range")
        st.markdown("""---""")
        st.write("Does the job require telecommuting? (0 = No, 1 = Yes)")
        telecommuting = st.selectbox("",[0,1],key="telecommuting")
        st.markdown("""---""")
        st.write("Does the company have a logo?" "(0 = No, 1 = Yes)")
        has_company_logo = st.selectbox("",[0,1],key="has_company_logo")
        st.markdown("""---""")
        st.write("Does the company have questions?" "(0 = No, 1 = Yes)")
        has_questions = st.selectbox("",[0,1],key="has_questions")
        st.markdown("""---""")
        st.write("What is the employment type of the job?")
        employment_type = st.selectbox("",['Full-time', 'Not Mentioned', 'Contract', 'Part-time', 'Temporary', 'Other'],key="employment_type")
        st.markdown("""---""")
        st.write("What is the required experience level for the job?")
        required_experience = st.selectbox("",['Not Mentioned','Mid-Senior level','Entry level','Associate','Not Applicable','Director','Internship','Executive'],key="required_experience")
        st.markdown("""---""")
        st.write("What is the required education level for the job?")
        required_education = st.selectbox("",['Not Mentioned',"Bachelor's Degree",'High School or equivalent','Unspecified',"Master's Degree",'Associate Degree','Certification','Some College Coursework Completed','Professional','Vocational','Some High School Coursework','Doctorate','Vocational - HS Diploma','Vocational - Degree'],key="required_education")
        st.markdown("""---""")
        st.write("Enter the job title")
        title = st.text_input("",key="title")
        st.markdown("""---""")
        st.write("Enter the job location")
        location = st.text_input("",key="location")
        st.markdown("""---""")
        st.write("Enter the job department")
        department = st.text_input("",key="department")
        st.markdown("""---""")
        st.write("Enter the company profile")
        company_profile = st.text_input("",key="company_profile")
        st.markdown("""---""")
        st.write("Enter the job description")
        description = st.text_input("",key="description")
        st.markdown("""---""")
        st.write("Enter the job requirements")
        requirements = st.text_input("",key="requirements")
        st.markdown("""---""")
        st.write("Enter the job benefits")
        benefits = st.text_input("",key="benefits")
        st.markdown("""---""")
        st.write("Enter the job industry")
        industry = st.text_input("",key="industry")
        st.markdown("""---""")
        st.write("Enter the job function")
        function = st.text_input("",key="function")
        st.markdown("""---""")

        if st.button("Predict"):
            input_data = InputFormat(
                salary_range=salary_range,
                telecommuting=telecommuting,
                has_company_logo=has_company_logo,
                has_questions=has_questions,
                employment_type=employment_type,
                required_experience=required_experience,
                required_education=required_education,
                title=title,
                location=location,
                department=department,
                company_profile=company_profile,
                description=description,
                requirements=requirements,
                benefits=benefits,
                industry=industry,
                function=function
            )

            predictions = get_predictions(input_data)

            st.markdown("---")
            st.subheader("🔍 Prediction Result")

            col1, col2 = st.columns(2)

            with col1:
                if predictions["fraudulent"] == 1:
                    st.error("⚠️ The job posting is **Fraudulent**.")
                else:
                    st.success("✅ The job posting is **Not Fraudulent**.")

            with col2:
                st.markdown("### 📊 Probability Details")
                st.metric(
                    label="Fraudulent Probability",
                    value=f"{predictions['fraudulent_probability'] * 100:.2f} %"
                )
                st.metric(
                    label="Non-Fraudulent Probability",
                    value=f"{predictions['non_fraudulent_probability'] * 100:.2f} %"
                )

            st.markdown("---")
            st.caption("This prediction is based on the trained ML model for fake job detection.")
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred. Please try again later: {str(e)}")
    

    
    
    