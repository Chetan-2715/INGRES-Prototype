# INGRES ChatBot MVP - AI-Driven Virtual Assistant for Groundwater Resources

## 🌊 Overview

INGRES ChatBot is an AI-powered virtual assistant designed for the India Ground Water Resource Estimation System (INGRES). This MVP demonstrates how users can easily query groundwater data, access historical and current assessments, and obtain instant insights without navigating complex datasets.

**Developed for**: Ministry of Jal Shakti, Central Ground Water Board (CGWB)  
**Problem Statement ID**: 25066  
**Category**: Software | Smart Automation

## ✨ Features

### Current MVP Features:
- **Natural Language Query Processing**: Understands various types of groundwater-related queries
- **Real-time Data Access**: Retrieves current groundwater assessment data
- **Historical Trends**: Shows groundwater trends over multiple years
- **Category Classification**: Identifies Safe, Semi-Critical, Critical, and Over-Exploited areas
- **Location-based Queries**: Search by state, district, or block
- **Interactive Web Interface**: User-friendly chat interface with quick action buttons
- **Visual Status Indicators**: Color-coded status for easy understanding

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Web browser (Chrome, Firefox, Safari, or Edge)

### Installation

1. **Clone or navigate to the project directory**:
```bash
cd ingres-chatbot-mvp
```

2. **Install Python dependencies**:
```bash
pip install flask flask-cors pandas numpy python-dateutil
```

3. **Initialize the database** (if not already done):
```bash
python data/init_database.py
```

4. **Start the backend server**:
```bash
cd backend
python app.py
```
The backend will start on `http://localhost:5000`

5. **Open the frontend**:
Open `frontend/index.html` in your web browser

## 💬 Sample Queries

Try these queries in the chatbot:

### Basic Queries:
- "What is the groundwater status of Delhi?"
- "Show me critical areas"
- "Which areas are safe?"
- "What is the water level in Gurugram?"

### Advanced Queries:
- "Show historical data for Punjab"
- "What is the annual recharge rate?"
- "How much groundwater is being extracted in Maharashtra?"
- "Show water level trends"
- "Compare groundwater status between 2020 and 2024"

### Location-based Queries:
- "Show groundwater status of Karnataka"
- "What is the water level in Chennai district?"
- "List critical blocks in Rajasthan"

## 📁 Project Structure

```
ingres-chatbot-mvp/
│
├── backend/
│   ├── app.py                 # Flask API server
│   └── query_processor.py     # NLP and query processing
│
├── frontend/
│   ├── index.html             # Main chat interface
│   ├── styles.css             # Styling
│   └── script.js              # Frontend JavaScript
│
├── data/
│   ├── init_database.py       # Database initialization script
│   └── ingres_mock.db         # SQLite database (created after init)
│
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Technical Architecture

### Backend (Python/Flask):
- **Flask**: Lightweight web framework for API endpoints
- **SQLite**: File-based database for mock groundwater data
- **Pattern-based NLP**: Simple intent recognition without heavy ML models
- **RESTful API**: Clean API design for frontend communication

### Frontend (HTML/CSS/JavaScript):
- **Vanilla JavaScript**: No framework dependencies for simplicity
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Updates**: Async communication with backend
- **Modern UI**: Clean, professional interface with animations

### Database Schema:
- **States**: 10 major Indian states
- **Districts**: 20 districts across states
- **Blocks**: 81 assessment blocks
- **Assessments**: 405 groundwater assessment records (2020-2024)
- **Historical Data**: Monthly water level and rainfall data

## 🎯 Key Capabilities

1. **Groundwater Status Assessment**
   - Category classification (Safe/Critical/Over-Exploited)
   - Stage of extraction percentages
   - Water level measurements

2. **Historical Analysis**
   - Year-over-year trends
   - Average extraction rates
   - Water level variations

3. **Resource Management**
   - Annual recharge rates
   - Extractable resources
   - Total extraction data

4. **Geographic Coverage**
   - State-level aggregations
   - District-wise analysis
   - Block-level detailed data

## 🚦 API Endpoints

- `POST /api/chat` - Process chat messages
- `GET /api/health` - Health check
- `GET /api/stats` - Database statistics
- `GET /api/history` - Chat history
- `POST /api/clear` - Clear chat history

## 🔄 Future Enhancements

### Phase 2 - Enhanced NLP
- [ ] Integrate advanced NLP models (spaCy/BERT)
- [ ] Multi-language support (Hindi, regional languages)
- [ ] Context-aware conversations
- [ ] Sentiment analysis

### Phase 3 - Data Integration
- [ ] Connect to actual INGRES database
- [ ] Real-time data synchronization
- [ ] GIS map integration
- [ ] Data visualization charts

### Phase 4 - Advanced Features
- [ ] Voice input/output
- [ ] WhatsApp/Telegram integration
- [ ] Predictive analytics
- [ ] Alert notifications for critical areas
- [ ] Export reports (PDF/Excel)
- [ ] User authentication and roles

### Phase 5 - Deployment
- [ ] Cloud deployment (AWS/Azure)
- [ ] Containerization (Docker)
- [ ] Load balancing
- [ ] SSL/HTTPS security
- [ ] API rate limiting

## 🧪 Testing

To test the chatbot:

1. Start the backend server
2. Open the frontend in a browser
3. Try various queries from the sample list
4. Test edge cases and error handling
5. Verify data accuracy with database

## 🐛 Troubleshooting

### Backend won't start:
- Check if port 5000 is already in use
- Verify Python dependencies are installed
- Ensure database file exists in `data/` folder

### Frontend shows "Disconnected":
- Verify backend is running on port 5000
- Check browser console for errors
- Ensure CORS is enabled in backend

### No data returned:
- Run `python data/init_database.py` to reinitialize database
- Check query processor patterns match your input
- Verify database path in configuration

## 📝 Notes

- This is an MVP (Minimum Viable Product) demonstration
- Uses mock data instead of real INGRES database
- Pattern-based NLP for simplicity (not using AI models)
- Designed for local development and testing

## 🤝 Contributing

This MVP can be extended with:
- Additional query patterns
- More comprehensive mock data
- Enhanced UI features
- Integration with real INGRES API
- Machine learning models for better NLP

## 📄 License

Developed as part of Smart India Hackathon 2024 submission.

## 👥 Contact

For questions or suggestions regarding this MVP, please contact the development team.

---

**Note**: This is a demonstration MVP. For production deployment, additional security, scalability, and data integration features would be required.
