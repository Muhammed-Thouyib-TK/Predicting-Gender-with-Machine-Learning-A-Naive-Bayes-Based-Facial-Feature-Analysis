# 👥 Gender Prediction Using Naive Bayes & Streamlit  

A clean, interpretable, and efficient approach to **gender classification using facial and physical features** with the **Naive Bayes algorithm**, now extended into a **deployed web application** via **Streamlit** 🚀  

This project demonstrates the **end-to-end machine learning workflow** — from **data preprocessing → EDA → model training → evaluation → deployment**, making the model not just theoretical but practically usable.  

---

## 📌 Project Overview  
This project predicts an individual’s gender using structured binary and numerical facial/physical attributes such as **hair length, nose shape, forehead width, and more**.  

By applying a **Gaussian Naive Bayes classifier**, the case study highlights how even a simple model can achieve strong performance when combined with proper **data preprocessing, exploratory data analysis (EDA), and evaluation**.  

---

## 🎯 Objectives  
- Clean and preprocess a structured facial feature dataset  
- Visualize data to uncover patterns and class separability  
- Train and evaluate a **Naive Bayes classifier** for gender prediction  
- Deploy the trained model as an interactive **Streamlit web app**  

---

## 🗂️ Dataset  
- **Binary Features**: Hair_Length (Short/Long), Nose_Shape (Pointed/Round)  
- **Continuous Features**: Forehead_Width, Eye_Size, Jaw_Angle  
- **Target Variable**: Gender (0 = Female, 1 = Male)  
- **Source**: Public facial structure datasets (or hypothetical academic demonstration data)  

---

## 🔍 Key Highlights  

### ✅ Data Cleaning & Preprocessing  
- Verified datatypes and handled missing values  
- Encoded target variable (Gender: 0/1)  
- Standardized continuous features with `StandardScaler`  
- Train-test split (80-20 ratio)  

### 📊 Exploratory Data Analysis (EDA)  
- Countplot of gender distribution (balanced classes)  
- Histograms & pairplots for feature distributions  
- Correlation heatmap to detect inter-feature relationships  

### 🤖 Model Building: Naive Bayes Classifier  
- Implemented **Gaussian Naive Bayes** via `scikit-learn`  
- Combined binary + continuous features for training  
- Predicted gender labels on unseen test data  

### 📈 Model Evaluation  
- **Accuracy Score**  
- **Confusion Matrix**  
- **Classification Report (Precision, Recall, F1-score)**  
- Focused on correct vs. incorrect classification patterns  

---

## 🛠 Tools & Technologies Used  
- Python  
- pandas, numpy – data manipulation  
- matplotlib, seaborn – visualization  
- scikit-learn – modeling & evaluation  
- Streamlit – deployment  
- Jupyter Notebook – analysis & storytelling  

---

## 🌐 Deployment  

### 🔗 [Live Demo] https://gender-prediction-web.streamlit.app/ 

### 🚀 Deployment Highlights  
- Interactive **Streamlit interface** for real-time predictions  
- Simple **input fields** for binary & numerical attributes (e.g., hair length, forehead size, nose shape)  
- Integrated the trained **Naive Bayes model** for instant classification results  
- Hosted for easy public access — no coding setup required
- 
---

## ⚠️ Disclaimer  
This project is created purely for **educational and skill enhancement purposes**.  
I do not endorse or encourage the real-world use of gender classification systems.  
Please treat this as a **learning exercise** in ML pipelines and deployment.  

