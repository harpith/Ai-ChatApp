
## ⚛️ **Frontend (React) – `README.md`**

```text
# AI Chat App Frontend – React + Tailwind CSS

This is the frontend of a Fullstack AI Chat Application built with React and Tailwind CSS. It provides a sleek and responsive chat interface that communicates with a Django REST API and the GPT-4 model via OpenAI.

## ⚙️ Tech Stack
- React (with Vite)
- Tailwind CSS + Shadcn ui
- Axios
- OpenAI (indirectly via backend)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/CodeWithClinton/ai_chat_app_frontend.git

cd ai_chat_app_frontend
````

### 2. Install Dependencies

```bash
npm install
```


### 3. Run the Development Server

```bash
npm run dev
```

Visit: `http://localhost:5173`

## 🖼️ Features

* Clean chat UI with scrollable message history
* Message input and loading spinner
* Displays AI responses in real time
* Handles API loading states and errors
* Works with any GPT-4 powered backend

## 🧠 How It Works

* The frontend sends user messages to the Django API
* Django relays them to OpenAI GPT-4 and returns the response
* React renders the conversation in a chat-style UI
