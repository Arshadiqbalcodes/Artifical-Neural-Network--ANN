import streamlit as st
import numpy as np
import tensorflow as tf

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ANN Prediction System",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("ann_model.keras")

model = load_model()

# =========================================================
# HEADER
# =========================================================

st.title("🧠 Artificial Neural Network Prediction System")

st.markdown(
    """
    This application uses an **Artificial Neural Network (ANN)**
    to make predictions based on five input features.
    """
)

st.divider()

# =========================================================
# SIDEBAR - MODEL INFORMATION
# =========================================================

st.sidebar.title("🧠 Model Information")

st.sidebar.info(
    """
    **Model:** Artificial Neural Network (ANN)

    **Framework:** TensorFlow / Keras

    **Input Features:** 5

    **Hidden Layers:** 2

    **Activation:** ReLU

    **Output Activation:** Sigmoid

    **Optimizer:** Adam

    **Loss:** Binary Crossentropy

    **Epochs:** 20

    **Batch Size:** 32
    """
)

# =========================================================
# MODEL ARCHITECTURE
# =========================================================

st.subheader("🏗️ Model Architecture")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Input Features", "5")

with col2:
    st.metric("Hidden Layers", "2")

with col3:
    st.metric("Output Layer", "1")

st.code(
    """
Input Layer
     ↓
Dense Layer (16 neurons, ReLU)
     ↓
Dense Layer (8 neurons, ReLU)
     ↓
Output Layer (1 neuron, Sigmoid)
    """,
    language="text"
)

st.divider()

# =========================================================
# INPUT SECTION
# =========================================================

st.subheader("📥 Enter Input Values")

col1, col2 = st.columns(2)

with col1:
    feature1 = st.number_input(
        "Feature 1",
        value=0.0
    )

    feature2 = st.number_input(
        "Feature 2",
        value=0.0
    )

    feature3 = st.number_input(
        "Feature 3",
        value=0.0
    )

with col2:
    feature4 = st.number_input(
        "Feature 4",
        value=0.0
    )

    feature5 = st.number_input(
        "Feature 5",
        value=0.0
    )

# =========================================================
# PREDICTION
# =========================================================

st.divider()

if st.button("🔮 Make Prediction", use_container_width=True):

    input_data = np.array([
        [
            feature1,
            feature2,
            feature3,
            feature4,
            feature5
        ]
    ], dtype=np.float32)

    # Model prediction
    prediction = model.predict(
        input_data,
        verbose=0
    )

    probability = float(prediction[0][0])

    # =====================================================
    # RESULT
    # =====================================================

    st.subheader("🎯 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Prediction Probability",
            f"{probability:.2%}"
        )

    with col2:

        if probability >= 0.5:
            predicted_class = "Class 1"
            st.success("✅ Prediction: Class 1")
        else:
            predicted_class = "Class 0"
            st.warning("⚠️ Prediction: Class 0")

    # Progress bar
    st.write("Prediction Confidence")

    st.progress(
        min(max(probability, 0.0), 1.0)
    )

    # Raw model output
    with st.expander("🔍 View Raw Model Output"):
        st.write(prediction)

    # Input values
    with st.expander("📊 View Input Data"):
        st.write(input_data)