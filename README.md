<!-- Header -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=AI-Powered%20E-commerce%20Product%20Listing%20Generator&fontSize=30&fontAlignY=40&desc=Transform%20Images%20into%20SEO-Optimized%20Product%20Listings&descAlignY=55&descAlign=50" alt="Project Banner">
</p>

<!-- Badges -->
<p align="center">
  <a href="https://github.com/GothiProCoder/AI-Powered-Ecommerce-Product-Listing-Generator/stargazers">
    <img src="https://img.shields.io/github/stars/GothiProCoder/AI-Powered-Ecommerce-Product-Listing-Generator?style=social" alt="Stars">
  </a>
  <a href="https://github.com/GothiProCoder/AI-Powered-Ecommerce-Product-Listing-Generator/issues">
    <img src="https://img.shields.io/github/issues/GothiProCoder/AI-Powered-Ecommerce-Product-Listing-Generator" alt="Issues">
  </a>
  <a href="https://github.com/GothiProCoder/AI-Powered-Ecommerce-Product-Listing-Generator/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/GothiProCoder/AI-Powered-Ecommerce-Product-Listing-Generator" alt="License">
  </a>
</p>

<hr>

<h2>🚀 Project Overview</h2>
<p>
  The <strong>AI-Powered E-commerce Product Listing Generator</strong> is a groundbreaking project that automates the generation of product titles and bullet-point descriptions using AI. It takes a product image as input and returns a well-written, SEO-optimized product listing ready for any e-commerce platform.
</p>

<hr>

<h2 style="font-size: 28px; color: #5A189A;">🧠 Key Features</h2>
<ul style="font-size: 18px; line-height: 1.8; color: #333;">
  <li><span style="font-weight: bold; color: #0077b6;">✨ End-to-End AI Workflow:</span> Transforms product images into SEO-optimized titles and listings with zero manual input.</li>
  
  <li><span style="font-weight: bold; color: #f15bb5;">🖼️ Visual Intelligence with LLAVA:</span> Performs deep visual analysis using LLAVA’s multimodal AI to extract detailed product insights from images.</li>
  
  <li><span style="font-weight: bold; color: #00b4d8;">✍️ Human-Like Text Generation:</span> Utilizes the Mistral model to create fluent, engaging, and context-aware product descriptions and titles.</li>
  
  <li><span style="font-weight: bold; color: #06d6a0;">💻 Intuitive Streamlit Interface:</span> Upload, preview, and generate product listings through a sleek, responsive frontend that’s beginner-friendly.</li>
  
  <li><span style="font-weight: bold; color: #ef476f;">🔐 Token-Based API Authentication:</span> Ensures secure communication between the models and frontend using Hugging Face and ngrok tokens.</li>
  
  <li><span style="font-weight: bold; color: #ffa62b;">☁️ 100% Free & Cloud-Based:</span> Powered entirely by free-tier services like Google Colab, Hugging Face Spaces, and ngrok — no local setup required.</li>
  
  <li><span style="font-weight: bold; color: #7209b7;">⚡ Plug-and-Play Ready:</span> Lightweight and modular design makes it easy to integrate with your e-commerce backend or inventory systems.</li>
</ul>

<hr>

<h2>🖼️ Demo</h2>
<p align="center">
  <img src="assets/demo.gif" width="700" alt="Demo GIF">
</p>

<hr>

<h2>🛠️ Technologies Used</h2>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/LLAVA-000000?style=for-the-badge&logo=OpenAI&logoColor=white">
  <img src="https://img.shields.io/badge/Mistral-000000?style=for-the-badge&logo=OpenAI&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/ngrok-1F1F1F?style=for-the-badge&logo=ngrok&logoColor=white">
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black">
</p>

<hr>

<h2>📁 Project Structure</h2>
<pre>
AI-Powered-Ecommerce-Product-Listing-Generator/
├── LLAVA-Model.ipynb                 # Image understanding using LLAVA
├── Mistral-Model.ipynb                # Product listing generation using Mistral
├── Frontend-UI.py                    # Streamlit frontend
├── assets/
│   └── demo.gif                       # Demonstration GIF
└── README.md                          # Documentation
</pre>

<hr>

<h2>🔧 Prerequisites</h2>
<ul>
  <li>Hugging Face Token: <a href="https://huggingface.co/settings/tokens">Create one here</a></li>
  <li>ngrok Token: <a href="https://dashboard.ngrok.com/get-started/setup">Create one here</a></li>
</ul>

<hr>

<h2>⚙️ Installation & Setup</h2>

<h4>1. Clone the Repository</h4>
<pre><code>git clone https://github.com/GothiProCoder/AI-Powered-Ecommerce-Product-Listing-Generator.git
cd AI-Powered-Ecommerce-Product-Listing-Generator
</code></pre>

<h4>2. Run Mistral Notebook</h4>
<ul>
  <li>Open <code>Mistral-Model.ipynb</code> in Google Colab</li>
  <li>Enter Hugging Face and ngrok tokens in their respective placeholder values within the codes itself</li>
  <li>Run all cells sequentially</li>
  <li>Copy the final Mistral API URL</li>
</ul>

<h4>3. Run LLAVA Notebook</h4>
<ul>
  <li>Open <code>LLAVA-Model.ipynb</code></li>
  <li>Enter Hugging Face and ngrok tokens in their respective placeholder values within the codes itself</li>
  <li>Paste Mistral API URL in the last cell by replacing the MISTRAL-MODEL-NGROK-API-URL placeholder text</li>
  <li>Run all cells sequentially</li>
  <li>Copy the LLAVA API URL</li>
</ul>

<h4>4. Launch Streamlit Frontend</h4>
<ul>
  <li>Replace 'ENTER-LLAVA-NGROK-API-URL' with the actual LLAVA API URL</li>
  <li><pre><code>streamlit run Frontend-UI.py</code></pre></li>

<p></p>

<hr>

<h2>📈 Example Output</h2>
<ul>
  <li><strong>Input:</strong> Image of a T-shirt</li>
  <li><strong>Generated Title:</strong> Classic Cotton Round Neck T-Shirt - Unisex Fit</li>
  <li><strong>Description:</strong> Crafted from 100% breathable cotton, this round-neck t-shirt offers unmatched comfort and a stylish fit for all-day wear.</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>We welcome contributions! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.</p>

<hr>

<h2>📄 License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

<hr>

<h2>📬 Contact</h2>
<p>
  Developed by <strong>GothiProCoder</strong><br>
  Reach me on <a href="mailto: gotham123283@gmail.com">Email</a> | <a href="https://www.linkedin.com/in/gotham-chand">LinkedIn</a>
</p>

<!-- Footer -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="Footer Image">
</p>
