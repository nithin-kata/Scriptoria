# ⚡ Scriptoria - Quick Start Guide

## 🚀 Get Running in 5 Minutes

### 1️⃣ Install Dependencies (1 min)
```bash
cd scriptoria
pip install -r requirements.txt
```

### 2️⃣ Get API Key (2 min)
1. Go to https://huggingface.co/settings/tokens
2. Create new token
3. Copy the token

### 3️⃣ Configure Environment (1 min)
```bash
# Copy example file
cp .env.example .env

# Edit .env and add your key
HF_API_KEY=your_token_here
```

### 4️⃣ Run Application (1 min)
```bash
streamlit run app.py
```

**Or use the launcher:**
- Windows: Double-click `run.bat`
- Mac/Linux: `./run.sh`

---

## 🎬 Create Your First Film (2 minutes)

### Example Story

**Title:** The Last Signal

**Genre:** Sci-Fi

**Concept:**
```
In a post-apocalyptic world, a lone radio operator 
receives a mysterious signal from space that could 
save humanity or doom it forever.
```

**Characters:** 3

**Duration:** Feature Film

### Click Generate → Wait 60 seconds → Done! 🎉

---

## 📁 Project Structure

```
scriptoria/
├── app.py                 # Main app (run this)
├── utils/
│   ├── ai_generator.py   # AI logic
│   ├── prompts.py        # Prompt templates
│   ├── ui_components.py  # UI styling
│   └── exporter.py       # Export functions
├── requirements.txt       # Dependencies
├── .env                  # Your API key (create this)
└── README.md             # Full documentation
```

---

## 🎯 Key Commands

| Command | Purpose |
|---------|---------|
| `streamlit run app.py` | Start the app |
| `Ctrl+C` | Stop the server |
| `pip install -r requirements.txt` | Install deps |
| `streamlit cache clear` | Clear cache |

---

## ⚠️ Common Issues

### "API key not found"
→ Check `.env` file exists with `HF_API_KEY=your_key`

### "503 Service Unavailable"
→ Normal! Models are loading. Wait 20 seconds.

### "Module not found"
→ Run `pip install -r requirements.txt`

### Port already in use
→ Run `streamlit run app.py --server.port 8502`

---

## 🎨 What You Get

✅ Professional screenplay (3-5 scenes)
✅ 3 detailed character profiles  
✅ 3 AI-generated storyboard images
✅ Sound design for key scenes
✅ Complete production budget
✅ Export as TXT and PDF

---

## 💡 Pro Tips

1. **Be Specific** - Detailed concepts = better results
2. **First Run** - Takes 30-60s (models loading)
3. **Patience** - Image generation takes time
4. **Experiment** - Try different genres and styles
5. **Export Early** - Save your work as you go

---

## 🌐 Access URLs

- **Local:** http://localhost:8501
- **Network:** http://YOUR_IP:8501

---

## 📚 More Help

- Full docs: `README.md`
- Setup guide: `SETUP_GUIDE.md`
- Features: `FEATURES.md`

---

## ✨ That's It!

You're ready to create amazing film projects with AI! 🎬

**Questions?** Check the README or open an issue.

**Enjoying Scriptoria?** Star the repo and share with fellow filmmakers!
