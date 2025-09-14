# 🚀 INGRES ChatBot MVP - Quick Start Guide

## ⚡ Quick Setup (2 minutes)

### Option 1: Automatic Start (Windows)
Simply double-click `start_chatbot.bat` and the chatbot will open automatically!

### Option 2: Manual Start

1. **Install Dependencies** (one-time setup):
```bash
pip install flask flask-cors
```

2. **Start Backend Server**:
```bash
cd backend
python app.py
```

3. **Open ChatBot Interface**:
Open `frontend/index.html` in your web browser

## 🎯 Try These Queries First!

Once the chatbot is running, try these sample queries:

1. **"What is the groundwater status of Delhi?"**
   - Shows groundwater data for Delhi region

2. **"Show me critical areas"**
   - Lists areas with critical groundwater levels

3. **"Which areas are safe?"**
   - Shows areas with good groundwater status

4. **"Help"**
   - Shows what the chatbot can do

## 🧪 Test the System

Run the automated test suite:
```bash
python test_chatbot.py
```

## 📊 Sample Response

When you ask "What is the groundwater status of Delhi?", you'll see:

```
📍 Groundwater Status for Delhi (2024)

🟢 Central Delhi Block-1
   • Category: Safe
   • Extraction: 45.3%
   • Water Level: 12.5m below ground
   • Annual Recharge: 150.2 MCM

🟡 North Delhi Block-2
   • Category: Semi-Critical
   • Extraction: 78.2%
   • Water Level: 22.3m below ground
   • Annual Recharge: 95.8 MCM
```

## 🔧 Troubleshooting

**If chatbot shows "Disconnected":**
- Make sure backend is running (check the terminal window)
- Refresh the browser page

**If no data appears:**
- Run: `python data/init_database.py` to recreate the database

## 📱 Features at a Glance

- ✅ Natural language understanding
- ✅ Real-time groundwater data
- ✅ Historical trends
- ✅ Color-coded status indicators
- ✅ Quick action buttons
- ✅ Mobile-responsive design

## 🎉 You're Ready!

The chatbot is now running. Ask any question about groundwater resources in India!
