<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/asemaikauas/AIDEBATE">
    <img src="images/logo.png" alt="Logo" width="120" height="40">
  </a> 

  <h3 align="center">AI Debate Topic Analyzer</h3>

  <p align="center">
    An AI assistant for debate motion analysis. 
    <br />
    <a href="https://www.youtube.com/watch?v=zewjy05VNL8">View Demo</a>
  </p>
</div>

---

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#demo">View Demo</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

**AI Debate Topic Analyzer** is a web tool that helps debaters and educators get instant motion analysis. It uses OpenAI’s GPT to provide:

- Motion difficulty level and topic category
- 3 strong arguments for both Government and Opposition
- Suggested readings and debate video links (optional)
- Format-specific outputs (BP, WSDC, Public Forum)

This tool is designed for students, debate clubs, and educators who want to save time and improve motion prep.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

### Built With

* [Flask](https://flask.palletsprojects.com/)
* [OpenAI API](https://platform.openai.com/)
* [Bootstrap](https://getbootstrap.com)
* [HTML/CSS/JS](https://developer.mozilla.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Prerequisites

You’ll need:
- Python 3.8+
- A valid OpenAI API Key

### Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/asemaikauas/AIDEBATE.git
   cd AIDEBATE
   ```

2. Set up a virtual environment  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. In the root of your project (same level as app.py), create a file named .env and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your-api-key
   ```

5. Through the terminal, run the app  
   ```bash
   flask run
   ```

6. Visit `http://127.0.0.1:5000`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Usage

1. Input a debate motion.
2. Choose your format: BP / WSDC / PF.
3. Select options:
   - Include suggested readings?
   - Show related YouTube video?
4. Click **Analyze Motion**.

🎯 Output includes:
- Topic difficulty (Easy/Medium/Hard)
- Category tags (e.g., Ethics, IR, Economics)
- Structured arguments for both sides
- Suggested readings if selected 
- Related YouTube Video if selected

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Demo

Watch a quick walkthrough of the AI Debate Topic Analyzer:

[![Watch the demo](https://img.youtube.com/vi/zewjy05VNL8/maxresdefault.jpg)](https://www.youtube.com/watch?v=zewjy05VNL8)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


---

## Roadmap

- [ ] Add Lincoln-Douglas format
- [ ] Save motion history per user
- [ ] User login & profile features
- [ ] Multilingual motion support (Kazakh, Russian, etc.)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contributing

Contributions are what make the open source world amazing!  

1. Fork the repo  
2. Create a feature branch  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes  
4. Push and open a PR  
5. 🌟 Star the project!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Contact

Asemai – kauasasemai05@gmail.com  
Project Link: [AIDEBATE](https://github.com/asemaikauas/AIDEBATE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [OpenAI API](https://platform.openai.com/)
* [Bootstrap](https://getbootstrap.com)
* [Flask](https://flask.palletsprojects.com/en/stable/)
* [Font Awesome](https://fontawesome.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

