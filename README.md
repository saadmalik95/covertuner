<p align="center">
  <a href="" rel="noopener">
</p>

<h2 align="center">Cover Tuner</h2>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A lightweight tool to analyze cover letters
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

When applying to jobs, I would routinely ask people to review my cover letter prior to sending it in. When it came to feedback on the writing style, I noticed a few constants. Cover letters could be too "wordy", too "difficult to read", etc. I decided to make a tool to quantify the feedback related to the writing style. Cover Tuner's web app can be accessed at (https://www.covertuner.com/) and an explanation of the metrics can be found here (https://medium.com/@saadmalik95/writing-the-perfect-cover-letter-26b4249243cc)

## 🏁 Getting Started <a name = "getting_started"></a>

### Installing

The only package that needs to be installed prior to running CoverTuner is NLTK. 

```
# Install requirements
pip install -r requirements.txt
```

## 🎈 Usage <a name="usage"></a>

Add your cover letter's text to textForCovertuner.txt. As mentioned, please read (https://medium.com/@saadmalik95/writing-the-perfect-cover-letter-26b4249243cc) to get an idea of what the metrics are trying to signal 

```
# Run Main
python main.py
```

## 🚀 Deployment <a name = "deployment"></a>

The tool has been deployed as a Flask app at (https://www.covertuner.com/)

## ⛏️ Built Using <a name = "built_using"></a>

- [NLTK](https://www.nltk.org/) - Natural Language Toolkit

## ✍️ Authors <a name = "authors"></a>

- [@saadmalik95](https://github.com/saadmalik95) - Idea, development & deployment of (https://www.covertuner.com/)

