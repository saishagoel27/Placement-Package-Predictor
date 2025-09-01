# 💰 Placement Package Predictor
*Because knowing your worth before HR does is always a power move*

Ever wondered if your CGPA actually translates to real money? Wonder no more. This machine learning model takes your GPA and spits out a salary prediction faster than you can say "financial anxiety."

##  What This Does

Predicts your placement package based on CGPA using linear regression. 


## 📁 What's Inside

```
├── Placement Prediction.ipynb    # The brain surgery happens here
├── app.py                       # Streamlit app (because we're fancy)
├── placement-dataset.csv        # 200 students' dreams and realities
├── model.pkl                    # Our trained crystal ball
├── requirements.txt             # Dependencies (aka trust issues)
└── README.md                   # You're reading it, genius
```

##  Getting Started

### Option 1: The "I Trust You" Method
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Option 2: The "I Want to See the Magic" Method
Open `Placement Prediction.ipynb` and run all cells. Watch the model train like it's studying for finals.

## 🧠 The Science Behind It

- **Algorithm:** Linear Regression (keeping it simple, unlike your course curriculum)
- **Dataset:** 200 students with CGPA vs Package data
- **Performance:** MAE of 0.26, which means we're wrong by about ₹26k on average
- **Accuracy:** Good enough to make you question your life choices

### Key Stats
- **Mean Absolute Error:** 0.26 (Not terrible!)
- **Mean Squared Error:** 0.10 (Math likes small numbers)
- **RMSE:** 0.51 (Root Mean Something Error)

## 🎪 Features

✅ **Interactive Web App** - Streamlit because we're not animals  
✅ **Real-time Predictions** - Enter CGPA, get existential crisis  
✅ **Clean UI** - Green buttons because money  
✅ **Model Persistence** - Saved as `model.pkl` for posterity  

## 📊 How It Works

1. **Data Loading:** 200 students' CGPAs and packages (real data, real tears)
2. **Exploration:** Scatter plots that show life isn't fair
3. **Training:** 70% training, 30% testing (standard split, nothing fancy)
4. **Prediction:** Linear regression draws a line through your hopes
5. **Deployment:** Streamlit app for the full experience

## 🎮 Using the App

1. Run `streamlit run app.py`
2. Enter your CGPA (be honest, the model will know if you lie)
3. Hit "Predict" 
4. Accept your fate or improve your grades

## 🤓 For the Curious

The model uses a simple linear relationship:
```
Package = 0.57 × CGPA + some magic constant
```

**Translation:** Every 1 point increase in CGPA ≈ ₹57k increase in package



## 🛠️ Tech Stack

- **Python** - Because what else?
- **Scikit-learn** - For the heavy lifting
- **Pandas & NumPy** - Data wrangling duo
- **Matplotlib & Seaborn** - Pretty charts
- **Streamlit** - Web app magic
- **Joblib** - Model saving wizard

##  Potential Improvements

- [ ] Adding more features (internships, projects, social skills)
- [ ] Trying fancier algorithms (neural networks for neural students)
- [ ] Including college tier data (this is an ancient dataset)
- [ ] Adding confidence intervals (so you know how uncertain we are)

## 📚 What You'll Learn

- Linear regression basics
- Data visualization with Python
- Model evaluation metrics
- Web app deployment
- The correlation between grades and money (spoiler: it exists)

---

*Built with caffeine, deadlines, and the desperate hope that grades actually matter.*

**Remember:** This is just a prediction. Your worth isn't determined by a number, but your bank account might be. 🤷‍♀️
