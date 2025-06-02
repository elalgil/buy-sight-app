# 🛍️ BuySight

**BuySight** is a conversational shopping assistant built during a hackathon to simplify and enhance the online shopping experience using AI. The system leverages the **Gemini API** for natural language understanding and the **eBay API** for retrieving real-time product listings — providing users with tailored product recommendations directly in a chat interface.

---

## 🚀 Overview

BuySight helps users plan events or purchase items by simply describing their needs in natural language (e.g., "I'm planning a garden tea party for 15 people"). The system analyzes the message using **LLM-based NLP** and returns actionable shopping suggestions with direct e-commerce links — all within a clean and interactive chat.

---

## 🔍 Key Features

- **Natural language product discovery** via Gemini API
- **Real-time product retrieval** from eBay API
- **Interactive chat interface** displaying:
  - Product links
  - Price comparisons
  - Customer reviews
  - Product images
- **Future feature (in development)**:
  - **Image composition with DALL·E**: Users can upload a photo (e.g., their living room), and the app visualizes selected products within that image — giving a real-life preview before purchase.

---

## 🧠 Technologies Used

| Component         | Technology             |
|------------------|------------------------|
| Frontend         | HTML/CSS/JavaScript    |
| Backend          | Python + Flask         |
| AI & NLP         | Gemini Pro API         |
| eCommerce Data   | eBay Shopping API      |
| Image Generation | DALL·E API             |
| Deployment       | Localhost / Cloud-ready|
| Communication    | JSON-based exchange    |

---

## 🧩 Architecture

The project is divided into **five Git branches**, each managing a core part of the system:

- `GEMINI`: Processes user input and generates structured product intent
- `EBAY`: Queries eBay’s API using Gemini’s output
- `CORE`: Coordinates backend logic and connects components
- `DEV`: Frontend interface and integration testing
- `MASTER`: Stable production-ready version

Each module can be tested independently and communicates via structured JSON objects.

---

## 📂 Example: Gemini to eBay Flow

Inside the `Core/Gemini/Schemes` folder, you’ll find **example JSON files** demonstrating the expected output from the Gemini module. These outputs are transformed into eBay-compatible queries.

Example:
```json
{
  "event": "tea party",
  "recommended_items": ["teacups", "cake stands", "napkins"],
  "budget": "medium"
}
```

---

## 🧪 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/elalgil/buy-sight-app.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up eBay API access:**
   - Create an [eBay Developer Account](https://developer.ebay.com/api-docs/static/oauth-ui-tokens.html)
   - Generate a **User Token**
   - Add your credentials to the config file:  
     `Core/ebay/Entities/ebayconf.yaml`

---

## 🌐 Future Plans

- Add support for more eCommerce platforms (e.g., Amazon, Etsy)
- Enhance multilingual support
- Allow users to pin and save product bundles
- Integrate image generation more deeply into the chat interface

---

## 🎓 HUJI Hackathon

📅 **29.5.25** – Annual Hackathon hosted by the Computer Science School at Hebrew University (HUJI).  
🎯 Theme: *"The Future of AI in the Next 100 Years"*

BuySight was developed during this event as a prototype for conversational AI-driven eCommerce experiences.
