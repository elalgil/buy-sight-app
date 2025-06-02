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

Inside the `Core/Gemini/Schemes` folder, you'll find example JSON files showing the expected output from the Gemini module. These outputs are transformed into valid eBay search queries. For instance:

```json
{
  "event": "tea party",
  "recommended_items": ["teacups", "cake stands", "napkins"],
  "budget": "medium"
}

## How to run locally:
- 1. clone the repository: git clone https://github.com/elal-gilboa/buy-sight-app.git
- 2. pip install -r requirements.txt
- 3. Open an Ebay developer account - create an account to receive a User's token and add it in the Core/ebay/Enteties/ebayconf.yaml , this is the configuration file to access the Ebay API.
**Link to register**
https://developer.ebay.com/api-docs/static/oauth-ui-tokens.html#:~:text=the%20Developer%20Portal%3A-,Navigate%20to%20your%20Application%20Keys%20page%20on%20the%20eBay%20Developer,click%20the%20sign%2Din%20button.


## 🌐 Future Plans
- Add support for more eCommerce platforms (e.g., Amazon, Etsy)
- Enhance multilingual support
- Allow users to pin and save product sets
- Integrate image generation more deeply into user experience

## huji_hackathon
29.5.25 HUJI Hackathon - Hebrew University Computer Science School's annual Hackathon
This year's Hachathon's subject was AI future in the next 100 years

