# buy-sight-app
# 🛍️ BuySight

**BuySight** is a conversational shopping assistant built during a hackathon to simplify and enhance the online shopping experience using AI. The system leverages **Gemini API** for natural language understanding and **eBay API** for retrieving real-time product listings — providing users with tailored product recommendations directly in a chat interface.

---

## 🚀 Overview

BuySight helps users plan events or purchase items by simply describing their needs in natural language (e.g., "I'm planning a garden tea party for 15 people"). The system analyzes the message using **LLM-based NLP** and returns actionable shopping suggestions with direct e-commerce links, all within a clean and interactive chat.

---

## 🔍 Key Features

- **Natural Language Product Discovery** via **Gemini API**
- **Real-time product retrieval** via **eBay API**
- **Interactive chat interface** showing:
  - Product links
  - Price comparisons
  - Customer reviews
  - Product images
- **Future feature (in progress)**:
  - Image composition with **DALL·E**: Users can upload a photo (e.g., their living room), and the app visualizes selected products within the scene before purchase.

---

## 🧠 Technologies Used

| Component | Technology |
|----------|-------------|
| Frontend | HTML/CSS/JavaScript |
| Backend | Python + Flask |
| AI & NLP | Gemini Pro API (LLM) |
| eCommerce Data | eBay Shopping API |
| Image Generation | DALL·E API |
| Deployment | Localhost / Cloud-ready |
| Communication | JSON-based data exchange |

---

## 🧩 Architecture

The project is divided into **5 branches**, each handling a major component:

- `GEMINI`: Responsible for processing free-text input and generating structured product intent
- `EBAY`: Handles querying eBay APIs based on Gemini's structured output
- `CORE`: Business logic, chat coordination, and data handling
- `DEV`: Frontend interface and integration testing
- `MASTER`: Stable merged version

Each module can be tested independently and communicates via structured JSON.

---

## 📂 Example: Gemini to eBay Flow

Inside the `examples/` folder, you'll find example JSON files showing the expected output from the Gemini module. These outputs are transformed into valid eBay search queries. For instance:

```json
{
  "event": "tea party",
  "recommended_items": ["teacups", "cake stands", "napkins"],
  "budget": "medium"
}

# huji_hackathon
29.5.25 HUJI Hackathon

