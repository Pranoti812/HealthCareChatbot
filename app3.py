import streamlit as st

# Predefined cancer-related questions and answers
qa_pairs = [
    {
        "question": "What are the common symptoms of breast cancer?",
        "answer": (
            "Common symptoms of breast cancer include:\n"
            "- A lump or mass in the breast\n"
            "- Change in breast size or shape\n"
            "- Dimpling or puckering of the skin\n"
            "- Nipple discharge or inversion\n"
            "- Redness or scaling of the breast skin or nipple\n"
            "If you notice any of these symptoms, it's important to consult a healthcare professional."
        )
    },
    {
        "question": "How is lung cancer diagnosed?",
        "answer": (
            "Lung cancer is typically diagnosed through a combination of imaging tests (such as chest X-rays and CT scans), "
            "biopsies, and laboratory tests. If lung cancer is suspected, a healthcare provider may recommend these tests "
            "to confirm the diagnosis and determine the stage of the cancer."
        )
    },
    {
        "question": "What are the treatment options for prostate cancer?",
        "answer": (
            "Treatment options for prostate cancer depend on the stage and grade of the cancer, as well as the patient's overall health. "
            "Common treatments include active surveillance, surgery (prostatectomy), radiation therapy, hormone therapy, and chemotherapy. "
            "It's important to discuss with a healthcare provider to determine the best treatment plan."
        )
    },
    {
        "question": "Can lifestyle changes reduce the risk of colorectal cancer?",
        "answer": (
            "Yes, certain lifestyle changes can help reduce the risk of colorectal cancer. These include:\n"
            "- Maintaining a healthy weight\n"
            "- Engaging in regular physical activity\n"
            "- Eating a diet rich in fruits, vegetables, and whole grains\n"
            "- Limiting red and processed meat consumption\n"
            "- Avoiding excessive alcohol intake\n"
            "- Not smoking\n"
            "Regular screenings are also important for early detection and prevention."
        )
    },
    {
        "question": "What is the importance of genetic testing in ovarian cancer?",
        "answer": (
            "Genetic testing can identify inherited mutations, such as BRCA1 and BRCA2, that increase the risk of ovarian cancer. "
            "Knowing your genetic status can help guide treatment decisions and inform family members about their potential risks. "
            "It's advisable to discuss genetic testing with a healthcare provider or genetic counselor."
        )
    },
    {
        "question": "What are the symptoms of cancer?",
        "answer":(
            "A significant, unintentional weight loss can be an early sign of cancer.\n"
            "A persistent fever can be a common symptom of certain cancers.\n"
            "Unusual lumps or swellings anywhere on the body.\n"
            
        )
    },
    {
        "question": "Can stress cause cancer?",
        "answer":(
            "While stress can have various negative effects on health, there is no conclusive evidence that stress directly causes cancer.\n" 
            "However, chronic stress may lead to unhealthy behaviors, such as smoking or overeating, which can increase cancer risk.\n"
        )
    },
    {
        "question": "What is cancer?",
        "answer": (
            "Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. These cells can form tumors, invade nearby tissues, and potentially spread to other parts of the body through the bloodstream or lymphatic system."
            "The process of cancer spreading to other parts of the body is called metastasis."
        )
    },
    {
        "question": "What is a risk factor?",
        "answer": "A risk factor is anything that increases a person's chance of developing a disease, such as cancer. Risk factors can be behavioral, environmental, genetic, or related to lifestyle choices. Having one or more risk factors does not mean you will definitely develop cancer, but it can increase your likelihood."
    },
    {
        "question": "Can injuries cause cancer?",
        "answer": "No, injuries themselves do not cause cancer. While some people may believe that physical injuries can lead to cancer, there is no scientific evidence to support this. Cancer is primarily caused by genetic mutations and environmental factors, not by physical trauma."
    },
    {
        "question": "Can stress cause cancer?",
        "answer": "While stress can have various negative effects on health, there is no conclusive evidence that stress directly causes cancer. However, chronic stress may lead to unhealthy behaviors, such as smoking or overeating, which can increase cancer risk."
    },
    {
        "question": "Does sugar feed cancer?",
        "answer": "All cells, including cancer cells, use glucose (a type of sugar) for energy. However, there is no evidence that consuming sugar will directly cause cancer cells to grow faster. That said, a diet high in sugar can lead to obesity, which is a risk factor for several types of cancer."
    },
    {
        "question": "What is the most common cancer?",
        "answer": "Globally, lung cancer is the most common cancer, closely followed by breast cancer. In the UK, the most common cancers are breast and prostate cancer. The incidence of specific cancer types can vary based on factors like geography, lifestyle, and screening practices."
    },
    {
        "question": "Why is cancer on the rise?",
        "answer": "The main reason cancer rates are increasing is because people are living longer; the older you are, the more likely you are to develop cancer. However, increasing rates of obesity and physical inactivity, the rise of smoking in low- and middle-income countries, and people eating unhealthy diets are also contributing to a rise in preventable cancers."
    },
    {
        "question": "Which foods cause cancer?",
        "answer": "There is no single food or ingredient that will have a large impact on whether you do or don’t get cancer. Rather, the regular patterns of what we eat combine to make us more or less susceptible to cancer. For example, eating lots of fruit, vegetables, beans, pulses, and whole grains lowers your risk of cancer, but eating too much red or processed meat increases your risk of bowel cancer."
    },
    {
        "question": "How does cancer spread?",
        "answer": "Cancers are usually named after the organ in which they start, for example, bowel cancer. However, some cancers spread, either locally (into the tissues surrounding the cancer) or into other parts of the body – a process called metastasis. This happens when cancer cells break away from the tumor and move through the bloodstream or lymphatic system. They can end up in another organ such as the liver or lungs and begin replicating to form another tumor."
    },
    {
        "question": "What do cancer grade and stage mean?",
        "answer": "Cancer grade is based on how the cancer cells look. Knowing the cancer grade helps doctors predict how fast the cancer will grow and how likely it is to spread. Grade is usually described using a number from 1 to 3 or 4. The higher the number, the more different the cancer cells look from healthy cells and the faster they are growing. Cancer stage refers to the size of the cancer and how far it has spread. Staging helps determine the severity of the cancer and guides treatment decisions."
    },
    {
        "question": "What are the symptoms of cancer?",
        "answer": "Signs and symptoms caused by cancer will vary depending on what part of the body is affected. Some early warning signs of cancer include unexplained weight loss, persistent fatigue, changes in bowel or bladder habits, unexplained bleeding, and persistent cough or hoarseness. It's important to consult a healthcare provider if you experience any persistent or unusual symptoms."
    },
    {
        "question": "How is cancer treated?",
        "answer": "Cancer can be treated in different ways including surgery, radiotherapy, chemotherapy, immunotherapy, targeted therapy, and hormone therapy. Most people will have a combination of these, and people with the same cancer may receive different treatment based on: the type of cancer, the size of the tumor, whether it has spread, and your general health. It's important to discuss treatment options with your healthcare team to determine the best approach for your specific situation."
    },
    {
        "question": "Is there a vaccine for cancer?",
        "answer": "There is no vaccine for cancer. But there are vaccines for some viruses that are known to cause cancer, such as the human papillomavirus (HPV) and hepatitis B. HPV can cause cancer and getting vaccinated against it can help protect against the types of HPV that can lead to cervical, anal, throat, and penile cancers, along with some other forms of cancer. The HPV vaccine protects against many strains of the virus that can cause these cancers."
    },
    {
        "question": "Can cancer be prevented?",
        "answer": "While not all cancers can be prevented, adopting healthy lifestyle habits can significantly reduce the risk of developing certain types of cancer. This includes avoiding tobacco, limiting alcohol consumption, maintaining a healthy weight, staying physically active, eating a balanced diet rich in fruits and vegetables, and protecting your skin from excessive sun exposure. Regular screenings and vaccinations can also help in early detection and prevention."
    },
    {
        "question": "Is cancer genetic?",
        "answer": "Anyone can get cancer, but a small number – about 5–10% – are strongly inherited, meaning they are passed from parents to child. One example is a certain type of breast cancer that occurs due to mutations, or errors, in two genes: BRCA1 (BReast CAncer gene one) and BRCA2 (BReast CAncer gene two). However, inheriting a mutated gene does not mean you will definitely get that cancer; rather that you have a higher risk."
    },
    {
        "question": "What is the prognosis for cancer patients?",
        "answer": "The prognosis for cancer patients varies widely depending on factors such as the type and stage of cancer, the patient's overall health, and how well the cancer responds to treatment. Some cancers have high survival rates, especially when detected early, while others are more aggressive. It's important to discuss your specific situation with your healthcare provider to understand your prognosis."
    },
    {
        "question": "What is cancer?",
        "answer": "Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. These cells can form tumors, invade nearby tissues, and potentially spread to other parts of the body through the bloodstream or lymphatic system. The process of cancer spreading to other parts of the body is called metastasis."
    },
    {
        "question": "How does cancer develop in the body?",
        "answer": "Cancer develops when genetic mutations disrupt normal cell regulation, leading to uncontrolled cell division. These mutations can be inherited or acquired due to environmental exposures or lifestyle factors. As these abnormal cells proliferate, they can form tumors and potentially spread to other parts of the body."
    },
    {
        "question": "Is cancer contagious?",
        "answer": "No, cancer is not contagious. It cannot be transmitted from one person to another through direct contact, sharing utensils, or other means. However, certain viruses associated with cancer risk, such as human papillomavirus (HPV) and hepatitis B and C, can be transmitted between individuals. It's important to note that while these viruses can increase cancer risk, the cancers themselves are not contagious."
    },
    {
        "question": "Is cancer hereditary?",
        "answer": "While most cancers are caused by genetic mutations that occur during a person's lifetime, some cancers can be inherited. Inherited genetic mutations play a role in approximately 5-10% of all cancers. Having a family history of certain cancers can increase an individual's risk, but it does not guarantee that cancer will develop."
    },
    {
        "question": "What are the common risk factors for cancer?",
        "answer": "Several factors can increase the risk of developing cancer, including:\n\n- **Age**: The risk of cancer increases as people age.\n- **Lifestyle factors**: Smoking, excessive alcohol consumption, poor diet, physical inactivity, and being overweight can contribute to cancer risk.\n- **Environmental exposures**: Exposure to certain chemicals, radiation, and prolonged sun exposure can increase risk.\n- **Family history**: A family history of certain cancers can indicate a higher risk.\n- **Infections**: Certain infections, such as HPV and hepatitis, are linked to an increased risk of specific cancers."
    },
    {
        "question": "Can lifestyle changes reduce my risk of developing cancer?",
        "answer": "Yes, adopting healthy lifestyle habits can help reduce the risk of developing cancer. These include:\n\n- **Avoiding tobacco**: Eliminating smoking and avoiding secondhand smoke.\n- **Limiting alcohol consumption**: Reducing alcohol intake.\n- **Maintaining a healthy weight**: Achieving and maintaining a healthy body weight.\n- **Staying physically active**: Engaging in regular physical activity.\n- **Eating a balanced diet**: Consuming a diet rich in fruits, vegetables, and whole grains.\n- **Protecting against infections**: Getting vaccinated against viruses like HPV and hepatitis B."
    },
    {
        "question": "Are there specific screenings or tests I should undergo to detect cancer early?",
        "answer": "Regular screenings can help detect certain cancers early, when treatment is more effective. Common screenings include:\n\n- **Mammograms**: For breast cancer detection.\n- **Pap smears and HPV tests**: For cervical cancer detection.\n- **Colonoscopy**: For colorectal cancer detection.\n- **Low-dose CT scans**: For lung cancer detection in high-risk individuals.\n\nIt's important to discuss with a healthcare provider which screenings are appropriate based on individual risk factors."
    },
    {
        "question": "What are the general symptoms of cancer?",
        "answer": "Cancer symptoms can vary depending on the type and location but may include:\n\n- **Unexplained weight loss**: Losing weight without trying.\n- **Fatigue**: Persistent tiredness that doesn't improve with rest.\n- **Pain**: New or unexplained pain.\n- **Skin changes**: New moles, sores that don't heal, or changes in existing moles.\n- **Changes in bowel or bladder habits**: Persistent constipation, diarrhea, or changes in urine frequency.\n- **Unusual bleeding or discharge**: Unexpected bleeding from any body part.\n- **Persistent cough or hoarseness**: Especially if it doesn't go away.\n\nExperiencing these symptoms does not necessarily mean one has cancer, but it's important to consult a healthcare provider for evaluation."
    },
    {
        "question": "How is cancer diagnosed?",
        "answer": "Cancer diagnosis typically involves a combination of:\n\n- **Physical examination**: Assessing for lumps or abnormalities.\n- **Laboratory tests**: Analyzing blood, urine, or other body fluids.\n- **Imaging studies**: Such as X-rays, CT scans, MRI, or PET scans to visualize internal structures.\n- **Biopsy**: Removing a sample of tissue for microscopic examination to confirm the presence of cancer cells.\n\nThe specific tests used depend on the suspected cancer type and location."
    },
    {
        "question": "What does cancer staging mean?",
        "answer": "Cancer staging describes the extent of cancer in the body, including factors like tumor size, lymph node involvement, and whether it has spread to other parts. Staging helps guide treatment decisions and provides insight into prognosis."
    },
    {
        "question":  "What are the symptoms of leukemia?",
        "answer": "Leukemia symptoms include frequent infections, unexplained weight loss, easy bruising, excessive sweating, and swollen lymph nodes."
    },
    {
        "question": "What are the side effects of chemotherapy?",
        "answer": "Side effects may include nausea, hair loss, fatigue, increased infection risk, and changes in appetite."
    },
    {
        "question": "Is cancer preventable?",
        "answer": "While not all cancers can be prevented, lifestyle changes like a healthy diet, exercise, and avoiding smoking can lower the risk."
    },
    {
        "question": "What are the stages of cancer?",
        "answer": "Cancer stages range from Stage 0 (early) to Stage IV (advanced). Staging depends on tumor size, lymph node involvement, and spread."
    },
    {
        "question": "How is lung cancer diagnosed?",
        "answer": (
            "Lung cancer is typically diagnosed through a combination of imaging tests (such as chest X-rays and CT scans), "
            "biopsies, and laboratory tests. If lung cancer is suspected, a healthcare provider may recommend these tests "
            "to confirm the diagnosis and determine the stage of the cancer."
        )
    }

]

st.set_page_config(page_title="Healthcare Chatbot", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #f5f7fa; }
    .chat-container { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); }
    .assistant { color: #0a74da; font-weight: bold; }
    .user { color: #333333; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Center the chatbot interface
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.title("🩺 Healthcare Chatbot")
    st.write("Ask me cancer related !")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        role_class = "assistant" if message["role"] == "assistant" else "user"
        st.markdown(f"<p class='{role_class}'>{message['role'].capitalize()}: {message['content']}</p>", unsafe_allow_html=True)

    # User input
    user_input = st.chat_input("Type your question here...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Search for a predefined answer
        response = next((qa["answer"] for qa in qa_pairs if qa["question"].lower() == user_input.lower()), "I'm sorry, I don't have information on that topic.")

        st.session_state.messages.append({"role": "assistant", "content": response})

        # Display assistant response