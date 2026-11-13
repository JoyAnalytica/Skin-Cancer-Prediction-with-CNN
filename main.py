import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import hashlib

# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="DermaAI | Skin Cancer Detection",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# 2. CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* Global */
.stApp {
    background: #f4f7fc;
    color: #172b4d;
}

header[data-testid="stHeader"] {
    background: #f4f7fc;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

/* Navigation */
.navbar {
    background: linear-gradient(135deg, #102d50 0%, #1e4b82 100%);
    padding: 18px 28px;
    border-radius: 16px;
    margin-bottom: 28px;
    box-shadow: 0 4px 15px rgba(16, 45, 80, 0.1);
}

.navbar h2 {
    color: white !important;
    margin: 0;
    font-size: 24px;
    font-weight: 700;
}

.navbar span {
    color: #ff6677 !important;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #102d50 0%, #155d9a 60%, #167bb5 100%);
    padding: 50px 40px;
    border-radius: 24px;
    margin-bottom: 35px;
    box-shadow: 0 12px 35px rgba(16, 45, 80, 0.18);
}

.hero-tag {
    background: #ff4d6d;
    color: white !important;
    padding: 6px 16px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 800;
    display: inline-block;
    letter-spacing: 0.5px;
}

.hero h1 {
    color: white !important;
    font-size: 42px;
    font-weight: 850;
    margin-top: 18px;
    margin-bottom: 12px;
}

.hero p {
    color: #e2efff !important;
    font-size: 17px;
    line-height: 1.8;
    max-width: 750px;
}

/* Section titles */
.section-heading {
    color: #12365b !important;
    font-size: 26px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 6px;
}

.section-description {
    color: #66788e !important;
    font-size: 15px;
    margin-bottom: 22px;
}

/* Cards */
.feature-card {
    background: white;
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #e1eaf5;
    min-height: 210px;
    box-shadow: 0 6px 20px rgba(22, 50, 90, 0.04);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(22, 50, 90, 0.08);
}

.feature-card h3 {
    color: #174c80 !important;
    font-size: 18px;
    margin-top: 14px;
    margin-bottom: 8px;
}

.feature-card p {
    color: #62748a !important;
    font-size: 14px;
    line-height: 1.7;
    margin: 0;
}

.feature-icon {
    font-size: 34px;
}

/* Upload card */
.upload-card {
    background: white;
    padding: 28px;
    border: 1px solid #e1eaf5;
    border-radius: 20px;
    box-shadow: 0 6px 20px rgba(22, 50, 90, 0.05);
}

.upload-card h3 {
    color: #174c80 !important;
    margin-top: 0;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: #f8fbff;
    border: 2px dashed #9bc3ef;
    padding: 15px;
    border-radius: 14px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #e63950, #f04c61);
    color: white !important;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 750;
    min-height: 50px;
    width: 100%;
    box-shadow: 0 4px 15px rgba(230, 57, 80, 0.3);
    transition: 0.2s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #cd263e, #dc384e);
    box-shadow: 0 6px 20px rgba(230, 57, 80, 0.4);
    color: white !important;
}

/* Result card */
.result-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #e1eaf5;
    text-align: center;
    box-shadow: 0 8px 25px rgba(22, 50, 90, 0.07);
}

.result-card h2 {
    color: #173d65 !important;
    font-size: 22px;
    margin-top: 0;
}

.result-name {
    font-size: 34px;
    font-weight: 850;
    margin: 15px 0;
}

.benign {
    color: #0d9463 !important;
}

.malignant {
    color: #e63946 !important;
}

.result-confidence {
    color: #45617e !important;
    font-size: 18px;
    font-weight: 700;
}

/* Probability labels */
.prob-label {
    color: #23476b !important;
    font-size: 14px;
    font-weight: 700;
    margin-top: 10px;
}

/* Info box */
.info-box {
    background: #eaf3ff;
    border-left: 5px solid #176db2;
    padding: 20px;
    border-radius: 12px;
    color: #244b70 !important;
    line-height: 1.8;
}

/* Warning box */
.warning-box {
    background: #fff8f0;
    border-left: 5px solid #f29e38;
    padding: 22px;
    border-radius: 12px;
    color: #704c1c !important;
    line-height: 1.8;
}

/* ABCDE */
.abc-card {
    background: white;
    padding: 18px 22px;
    border-radius: 14px;
    border: 1px solid #e1eaf5;
    margin-bottom: 12px;
    box-shadow: 0 3px 10px rgba(22, 50, 90, 0.03);
}

.abc-card h4 {
    color: #e63950 !important;
    margin: 0 0 6px 0;
    font-size: 17px;
}

.abc-card p {
    color: #5d7087 !important;
    margin: 0;
    font-size: 14px;
}

/* Footer */
.footer {
    background: #102d50;
    border-radius: 18px;
    padding: 35px;
    text-align: center;
    margin-top: 40px;
    box-shadow: 0 10px 30px rgba(16, 45, 80, 0.15);
}

.footer h3 {
    color: white !important;
    margin-bottom: 8px;
}

.footer p {
    color: #d3e3f5 !important;
    font-size: 14px;
    margin: 4px 0;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# 3. LOAD CNN MODEL
# ==================================================

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(
        "cnn_model.keras",
        compile=False
    )
    return model

try:
    model = load_model()
except Exception as e:
    st.error(f"Model loading error: {e}")
    st.stop()


# ==================================================
# 4. CLASS NAMES
# ==================================================

CLASS_NAMES = ["Benign", "Malignant"]


# ==================================================
# 5. IMAGE PREPROCESSING
# ==================================================

def preprocess_image(image):
    image = ImageOps.exif_transpose(image)
    image = image.convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image, dtype=np.float32)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array


# ==================================================
# 6. PREDICTION FUNCTION
# ==================================================

def predict_image(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image, verbose=0)
    probability = float(np.asarray(prediction).reshape(-1)[0])
    predicted_class = 1 if probability >= 0.5 else 0
    confidence = probability if predicted_class == 1 else 1 - probability
    class_name = CLASS_NAMES[predicted_class]
    return class_name, confidence, probability


# ==================================================
# 7. NAVIGATION BAR
# ==================================================

st.markdown("""
<div class="navbar">
    <h2>🔬 Derma<span>AI</span> — Skin Cancer Screening System</h2>
</div>
""", unsafe_allow_html=True)


# ==================================================
# 8. HERO SECTION
# ==================================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">AI POWERED SKIN ANALYSIS</div>
    <h1>Early Detection Saves Lives</h1>
    <p>
        Explore intelligent skin lesion image classification using Deep Learning 
        and Convolutional Neural Networks. Upload a clear dermatoscopic image 
        to view an educational model prediction and confidence score.
    </p>
</div>
""", unsafe_allow_html=True)


# ==================================================
# 9. ABOUT SECTION
# ==================================================

st.markdown("""
<div class="section-heading">About Our Project</div>
<div class="section-description">Intelligent image classification powered by advanced CNN technology.</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <h3>Deep Learning</h3>
        <p>CNN architecture analyzes hidden image patterns and visual textures from skin lesion samples.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔬</div>
        <h3>Image Preprocessing</h3>
        <p>Uploaded images are automatically normalized, transposed, and resized to 224 × 224 pixels.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>Instant Prediction</h3>
        <p>Examine model output class predictions and confidence probabilities in a user-friendly format.</p>
    </div>
    """, unsafe_allow_html=True)


# ==================================================
# 10. PREDICTION SECTION
# ==================================================

st.markdown("""
<div class="section-heading">🔍 Skin Image Analysis</div>
<div class="section-description">Upload your skin lesion photograph below to run the prediction pipeline.</div>
""", unsafe_allow_html=True)

left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown("""
    <div class="upload-card">
        <h3>📤 Upload Image</h3>
        <p style="color:#64748b; font-size:14px; margin-bottom:15px;">
            Choose a clear, well-lit JPG, JPEG or PNG image.
        </p>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose skin image",
        type=["jpg", "jpeg", "png"],
        key="image_upload",
        label_visibility="collapsed"
    )

    image = None
    image_hash = None

    if uploaded_file is not None:
        image_bytes = uploaded_file.getvalue()
        image_hash = hashlib.md5(image_bytes).hexdigest()
        image = Image.open(uploaded_file)
        
        st.write("")
        st.image(
            image,
            caption="Uploaded Skin Lesion",
            use_container_width=True
        )
    else:
        st.write("")
        st.markdown("""
        <div class="info-box">
            <b>💡 Image Guidelines</b><br>
            • Format: JPG, JPEG or PNG<br>
            • Ensure optimal focus and lighting<br>
            • Close-up shot of the lesion works best<br>
            • Automatic resizing applied pre-inference
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)


with right:
    st.markdown("""
    <div class="upload-card">
        <h3>📊 Prediction Results</h3>
        <p style="color:#64748b; font-size:14px; margin-bottom:20px;">
            Model outputs and likelihood metrics appear here.
        </p>
    """, unsafe_allow_html=True)

    if uploaded_file is not None:
        if st.button("🔬 Run Skin Analysis", use_container_width=True):
            with st.spinner("Analyzing image features with CNN..."):
                try:
                    class_name, confidence, probability = predict_image(image)
                    st.session_state["result"] = {
                        "class_name": class_name,
                        "confidence": confidence,
                        "probability": probability,
                        "image_hash": image_hash
                    }
                except Exception as e:
                    st.error(f"Prediction failed: {e}")

        result = st.session_state.get("result")

        if result is not None and result["image_hash"] == image_hash:
            class_name = result["class_name"]
            confidence = result["confidence"]
            probability = result["probability"]

            css_class = "benign" if class_name == "Benign" else "malignant"

            st.markdown(f"""
            <div class="result-card" style="margin-top: 15px;">
                <h2>Classification Result</h2>
                <div class="result-name {css_class}">
                    {class_name}
                </div>
                <div class="result-confidence">
                    Confidence: {confidence:.2%}
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.write("")
            st.markdown("**Class Probability Breakdown**")

            st.markdown(f'<div class="prob-label">Benign: {(1-probability):.2%}</div>', unsafe_allow_html=True)
            st.progress(1 - probability)

            st.markdown(f'<div class="prob-label">Malignant: {probability:.2%}</div>', unsafe_allow_html=True)
            st.progress(probability)

            st.caption("Note: These are experimental model probabilities, not clinical diagnoses.")

        elif result is None:
            st.info("Click 'Run Skin Analysis' to process your uploaded image.")

    else:
        st.info("Please upload a skin image on the left panel to begin.")
    
    st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# 11. WHY SKIN CANCER OCCURS
# ==================================================

st.markdown("---")
st.markdown("""
<div class="section-heading">🧬 Why Does Skin Cancer Occur?</div>
<div class="section-description">Key environmental and genetic risk factors associated with skin cell mutations.</div>
""", unsafe_allow_html=True)

causes = [
    ("☀️", "UV Radiation", "Ultraviolet radiation from sunlight damages cellular DNA, triggering abnormal tissue growth."),
    ("🔥", "Severe Sunburn", "History of blistering sunburns, particularly during childhood, highly elevates melanoma risk."),
    ("🧬", "Family History", "Genetic predisposition and close relatives diagnosed with skin cancer increase personal vulnerability."),
    ("🛏️", "Tanning Beds", "Artificial UV ray tanning devices emit concentrated radiation that accelerates skin aging and damage."),
    ("👤", "Skin Characteristics", "Fair complexion, light eye color, and skin prone to freckling burn much more easily under the sun."),
    ("🩺", "Weakened Immunity", "Immunosuppressed individuals face higher risks of developing aggressive skin malignancies.")
]

cols = st.columns(3)
for i, (emoji, title, description) in enumerate(causes):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{emoji}</div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)


# ==================================================
# 12. PREVENTION
# ==================================================

st.markdown("""
<div class="section-heading">🛡️ How Can You Prevent Skin Cancer?</div>
<div class="section-description">Practical everyday habits to protect your skin from harmful UV exposure.</div>
""", unsafe_allow_html=True)

prevention = [
    ("🧴", "Apply Sunscreen", "Use broad-spectrum SPF 30+ sunscreen daily. Reapply every two hours or post-swimming."),
    ("🌳", "Seek Shade", "Limit direct sun exposure during peak UV intensity hours, typically between 10 AM and 4 PM."),
    ("👕", "Protective Gear", "Wear UV-blocking sunglasses, long-sleeved apparel, and wide-brimmed hats outdoors."),
    ("🚫", "Avoid Tanning Beds", "Completely steer clear of artificial tanning booths and intentional sunbathing."),
    ("🔎", "Self-Examinations", "Perform regular skin checks to spot new, unusual, or rapidly changing moles and marks."),
    ("👨‍⚕️", "Dermatologist Visits", "Schedule annual professional skin checks and consult specialists for unusual lesions.")
]

cols = st.columns(3)
for i, (emoji, title, description) in enumerate(prevention):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{emoji}</div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)


# ==================================================
# 13. ABCDE WARNING SIGNS
# ==================================================

st.markdown("""
<div class="section-heading">🚨 ABCDE Warning Signs of Melanoma</div>
<div class="section-description">A helpful checklist to identify atypical moles that require medical evaluation.</div>
""", unsafe_allow_html=True)

abcde = [
    ("A — Asymmetry", "One half of the mole does not mirror or match the shape of the other half."),
    ("B — Border", "Edges are often ragged, notched, blurred, or irregular instead of smooth."),
    ("C — Color", "Varied shades of brown, black, tan, red, white, or blue across a single spot."),
    ("D — Diameter", "Spot size is typically larger than 6 millimeters (about the size of a pencil eraser), though they can be smaller."),
    ("E — Evolving", "The mole is changing in size, shape, color, elevation, or starts bleeding and itching.")
]

for title, description in abcde:
    st.markdown(f"""
    <div class="abc-card">
        <h4>{title}</h4>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)


# ==================================================
# 14. MEDICAL DISCLAIMER
# ==================================================

st.markdown("---")
st.markdown("""
<div class="warning-box">
    <b>⚠️ Important Medical Disclaimer</b><br><br>
    This web application is built strictly as an educational machine learning project and is 
    <b>not a clinically validated medical diagnostic tool</b>.<br><br>
    Model predictions can be prone to errors. A "Benign" outcome does not guarantee absolute safety, 
    and a "Malignant" outcome does not confirm cancer.<br><br>
    Never delay professional medical advice, diagnosis, or treatment based on results from this app. 
    Always consult a board-certified dermatologist for any skin health concerns.
</div>
""", unsafe_allow_html=True)


# ==================================================
# 15. FOOTER
# ==================================================

st.markdown("""
<div class="footer">
    <h3>🔬 DermaAI</h3>
    <p>AI-Powered Skin Cancer Screening & Educational System</p>
    <p>Built using Python | TensorFlow | CNN | Streamlit</p>
    <p>Empowering Awareness through Technology</p>
</div>
""", unsafe_allow_html=True)