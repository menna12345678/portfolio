import streamlit as st

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Menna Elgabry | Portfolio",
    page_icon="🤖",
    layout="centered"  # CHANGED TO centered
)

# ---------------------------
# Custom CSS for Modern Styling
# ---------------------------
st.markdown("""
<style>
    /* Center everything */
    .main > div {
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Card style */
    .card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 30px;
        margin: 20px 0;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Force image centering */
    .center-image {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 0 0 20px 0;
    }
    
    .center-image img {
        border-radius: 50%;
        border: 4px solid #ff4b4b;
        box-shadow: 0 4px 20px rgba(255,75,75,0.3);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Profile Section
# ---------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

# SIMPLE COLUMNS APPROACH - THIS WILL WORK
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("my_pic.jpg", width=150)

st.markdown("# 👩‍💻 Menna Elgabry")
st.markdown("### 🚀 Machine Learning Engineer | AI Researcher")
st.markdown("""
<div style="display: flex; justify-content: center; gap: 20px; margin: 20px 0;">
    <a href="mailto:mennayasser891@gmail.com" style="background: #ff4b4b; color: white; padding: 10px 20px; border-radius: 25px; text-decoration: none;">📧 Email</a>
    <a href="https://www.linkedin.com/in/menna-yasser-0029221b4/" style="background: #ff4b4b; color: white; padding: 10px 20px; border-radius: 25px; text-decoration: none;">💼 LinkedIn</a>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# About
# ---------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🌟 About Me")
st.markdown("""
I help researchers, startups, and businesses turn raw data into intelligent solutions that save time,
uncover insights, and support better decisions. With expertise across supervised and unsupervised learning,
computer vision, and large language models, I design AI systems that tackle real challenges like fraud detection,
customer feedback analysis, trend prediction, image-based diagnosis, and automated reporting.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Education
# ---------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🎓 Education")
st.markdown("""
- **BSc Computer Science, MSA University** (2022 - 2026)
- **BSc Computer Science, Greenwich University** (2022 - 2026)
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Work Experience
# ---------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 💼 Work Experience")
st.markdown("""
- **Machine Learning Intern** – Hands-on AI development pipeline (ML + DL)
- **Digital Egyptian Pioneers Intern** – Digital transformation, data literacy, analytics
- **CIB Summer Intern** – Applied data solutions to banking and financial scenarios
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Projects
# ---------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📂 Projects")
st.markdown("""
- **Sign Language Recognition** (EfficientNet) – Selected for MSA Deep Minds 5 🎉
- **Student & Staff Feedback Monitoring System** – Selected for MSA Deep Minds 3 🏆
- **Image Segmentation** (U-Net + Attention)
- **Emotion Detection Bot using LLMs**
- **Mini Games Development** (C++, C#, .NET, Visual Studio)
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Research
# ---------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📑 Research")
st.markdown("""
**Optimizing Sign Language Detection with Deep Learning and Preprocessing: A Comparative Study of CNN-Based Models**  
- Accepted at ICEEM-IEEE 2025  
- Benchmarked preprocessing methods (grayscale, CLAHE, gamma correction, contrast stretching)  
- Identified EfficientNet as best model for ASL recognition  
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Skills
# ---------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🧠 Technical Skills")
st.markdown("""
- Machine Learning: Supervised, Unsupervised, CNN, ResNet, LSTM, Autoencoders, GANs, LLMs  
- Data Structures & Algorithms  
- Web Development: HTML, CSS, JS, PHP, WAMP, XAMPP  
- Databases: MySQL, MongoDB  
- OOP, OOSE  
""")
st.markdown("### 🤝 Personal Skills")
st.markdown("Communication | Adaptability | Teamwork")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Certifications
# ---------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📜 Certifications")
st.markdown("""
- Generative AI (Transformers) – IBM + Coursera (Ongoing)  
- Deep Learning – Neurotech (June 2024)  
- Machine Learning – DEPI (2025)  
- CIB Summer Internship Program (2024)  
- Ethical Hacking – EC-Council (July 2023)  
- Introduction to MongoDB – Mahara-Tech (2023)  
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("""
<div style="text-align: center; margin-top: 30px; font-style: italic; color: #666;">
💡 <strong>If you want to save time and money, let's work together!</strong>
</div>
""", unsafe_allow_html=True)