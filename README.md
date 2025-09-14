# INGRES ChatBot MVP: AI-Driven Virtual Assistant for Groundwater Resources 🤖

## 🌊 Overview

The **INGRES ChatBot** is a prototype of a conversational AI assistant designed for the **India Ground Water Resource Estimation System (INGRES)**. It enables a wide range of users, including citizens, researchers, and government officials, to interact with complex groundwater data using simple, natural language queries. Instead of needing to know SQL or navigate raw datasets, users can ask questions like *"Show me critical areas"* or *"What is the water level in Chennai?"* This MVP demonstrates how a simple chat interface can provide real-time, accessible, and visual insights from intricate data.

**Developed for:** Ministry of Jal Shakti, Central Ground Water Board (CGWB)
**Problem Statement ID:** 25066
**Category:** Software | Smart Automation

---

## ✨ Features

### Current Prototype Capabilities:

* **Conversational Queries:** Interact with the bot using plain English for queries about states, districts, or blocks.
* **Instant Statistics:** Quickly get the status of groundwater, identify safe/critical areas, and see extraction and recharge rates.
* **Historical Trends:** Query and analyze data trends between specific years (using sample data from 2020–2024).
* **Interactive Web UI:** A user-friendly chat interface with quick action buttons for common queries.
* **Live Connection Indicator:** A visual status that shows *"Connected"* or *"Disconnected"*.
* **Smooth Chat Flow:** Typing animations and scrolling to create a user experience similar to modern messaging apps.
* **Mock Database:** The bot comes preloaded with sample data in the style of the INGRES dataset for easy testing.

---

## 🚀 Quick Start

### Prerequisites

* **Python:** Version 3.8 or higher
* **Web Browser:** Chrome, Firefox, or Edge is recommended

### Setup & Run

```bash
# Navigate to the project directory
cd ingres-chatbot-mvp

# Create & activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate      # For Windows
source venv/bin/activate   # For Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Initialize the database (creates ingres_mock.db in /data)
python data/init_database.py

# Run the backend server
cd backend
python app.py
```

The server will start at `http://127.0.0.1:5000`. Endpoints are automatically listed in the terminal.

### Launch the frontend

* Open `frontend/index.html` in your browser.
* Use a "Live Server" extension (like VS Code) or double-click the file.

---

## 💬 Sample Queries

* **General:** `Show me critical areas`, `Which areas are safe?`, `What is the groundwater status of Delhi?`
* **Location-based:** `Groundwater status of Karnataka`, `What is the water level in Chennai district?`, `List critical blocks in Rajasthan.`
* **Advanced:** `Show historical data for Punjab`, `Annual recharge rate in Gujarat`, `How much groundwater is extracted in Maharashtra?`

---

## 📁 Project Structure

```bash
ingres-chatbot-mvp/
│
├── backend/
│   ├── app.py              # Flask API server
│   └── query_processor.py  # Query classification & DB access
│
├── frontend/
│   ├── index.html          # Chat interface
│   ├── script.js           # Chat logic & API calls
│   └── styles.css          # Styling
│
├── data/
│   ├── ingres_mock.db      # SQLite mock DB (auto-created)
│   └── init_database.py    # Script to populate the DB
│
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

---

## 🔧 Technical Architecture

### Backend (Flask/Python)

* Uses **Flask** to create a REST API.
* **SQLite database** serves as a mock INGRES dataset.
* Query Processor handles **natural language understanding** through regex and pattern matching.

#### Endpoints:

* `/api/chat` - Processes user queries.
* `/api/health` - Reports the backend's status.
* `/api/stats` - Provides a summary of the database.
* `/api/history` - Manages chat history.
* `/api/clear` - Resets the chat history.

### Frontend (HTML/JS/CSS)

* Built with **Vanilla JavaScript** for a lightweight approach.
* Features an **interactive chat UI** with typing indicators and quick action buttons.
* **Responsive design** for multiple screen sizes.

### Database Schema (Mocked)

* **10 States**
* **20 Districts**
* **81 Blocks**
* **405 records** for groundwater assessment (2020–2024)

---

## 🎯 Key Benefits

* **Simplified Access:** Query data in plain English without technical expertise.
* **Data-Driven Decisions:** Provides fast insights for citizens and officials.
* **Research Support:** Enables historical trend analysis and structured, export-ready data.
* **Future Ready:** Scalable architecture for real INGRES database integration.

---

## 🔄 Future Enhancements

* ✅ Integration with the real INGRES dataset.
* ✅ Advanced NLP using **spaCy** or **BERT** for multilingual support.
* ✅ Visualizations (charts, GIS maps).
* ✅ Integration with voice interfaces & messaging platforms (WhatsApp/Telegram).
* ✅ Cloud deployment (AWS/Azure + Docker).

---

## 🧪 Testing

1. Run the backend: `python app.py`
2. Open the frontend: `index.html`
3. Test queries from the sample list.
4. Verify results match the mock database.
5. Check status indicator shows correct connection state.

---

## 🐛 Troubleshooting

* **Backend won't start:**

  * Port 5000 in use → Kill the existing process.
  * Dependencies missing → Run `pip install -r requirements.txt`.

* **Frontend shows "Disconnected":**

  * Backend not running → Start with `python app.py`.
  * Incorrect URL → Use `http://127.0.0.1:5000` not `file://`.

* **Queries return no data:**

  * Empty DB → Run `python data/init_database.py`.
  * Wrong file path → Ensure `query_processor.py` points to `ingres_mock.db`.

---

## 📝 Notes

* This is a **Minimum Viable Product (MVP)**, not production-ready.
* Uses **mock data**, not the official INGRES dataset.
* Developed for **Smart India Hackathon 2024–25**.
* Backend & frontend tested locally.

---

## 📄 License

This project was developed as part of the **Smart India Hackathon 2024–25** submission.
