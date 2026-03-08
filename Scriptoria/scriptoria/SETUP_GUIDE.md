# 🎬 Scriptoria Setup Guide

Complete step-by-step guide to get Scriptoria running on your machine.

## 📋 Prerequisites Checklist

- [ ] Python 3.8 or higher installed
- [ ] pip package manager
- [ ] Hugging Face account
- [ ] Hugging Face API token

## 🔑 Getting Your Hugging Face API Key

1. Go to [Hugging Face](https://huggingface.co/)
2. Sign up or log in to your account
3. Navigate to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
4. Click "New token"
5. Give it a name (e.g., "Scriptoria")
6. Select "Read" permissions
7. Click "Generate token"
8. Copy your token (you won't see it again!)

## 💻 Installation Steps

### Step 1: Navigate to Project Directory

```bash
cd scriptoria
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Open `.env` in a text editor

3. Replace `your_huggingface_api_key_here` with your actual API key:
```
HF_API_KEY=hf_YourActualTokenHere
```

4. Save the file

## 🚀 Running the Application

### Start the Streamlit Server

```bash
streamlit run app.py
```

### Expected Output

You should see:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

### Open in Browser

The application should automatically open in your default browser. If not, manually navigate to:
```
http://localhost:8501
```

## 🎯 First Time Usage

### Test with Sample Story

1. **Story Title**: "The Last Signal"
2. **Genre**: Sci-Fi
3. **Story Concept**: 
   ```
   In a post-apocalyptic world, a lone radio operator receives a 
   mysterious signal from space that could save humanity or doom 
   it forever. As she decodes the message, she discovers a shocking 
   truth about Earth's past and must make an impossible choice.
   ```
4. **Number of Characters**: 3
5. **Film Duration**: Feature Film

6. Click "Generate Film Package"

7. Wait 30-60 seconds for AI processing

### What to Expect

- **First API Call**: May take 20-30 seconds as models load
- **Subsequent Calls**: Faster (5-15 seconds)
- **Image Generation**: Takes longest (30-60 seconds per image)

## 🔧 Troubleshooting

### Issue: "Module not found" Error

**Solution**: Ensure all dependencies are installed
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "API key not found" Error

**Solution**: 
1. Check `.env` file exists in the scriptoria directory
2. Verify `HF_API_KEY` is set correctly
3. No spaces around the `=` sign
4. No quotes around the key

### Issue: 503 Service Unavailable

**Solution**: This is normal! The AI models are loading. The app automatically retries. Wait 20-30 seconds.

### Issue: Rate Limit Exceeded

**Solution**: 
- Wait a few minutes before trying again
- Free tier has limits
- Consider upgrading to Hugging Face Pro

### Issue: Slow Image Generation

**Solution**: 
- This is normal for Stable Diffusion
- Each image takes 30-60 seconds
- Be patient during storyboard generation

### Issue: Port Already in Use

**Solution**: Run on a different port
```bash
streamlit run app.py --server.port 8502
```

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Free)

1. Push code to GitHub (don't include `.env`)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add secrets in Streamlit Cloud dashboard:
   - Key: `HF_API_KEY`
   - Value: Your Hugging Face token
5. Deploy

### Option 2: Hugging Face Spaces (Free)

1. Create account on [Hugging Face](https://huggingface.co)
2. Create new Space (Streamlit SDK)
3. Upload all files except `.env`
4. Add secret in Space settings:
   - Name: `HF_API_KEY`
   - Value: Your token
5. Space will auto-deploy

### Option 3: Local Network Access

Share with devices on your local network:
```bash
streamlit run app.py --server.address 0.0.0.0
```

Access from other devices using your computer's IP address.

## 📊 Performance Tips

### Optimize API Calls

- Use caching (already implemented)
- Reduce number of storyboard scenes if needed
- Adjust max_tokens in `ai_generator.py`

### Improve UI Performance

- Close unused browser tabs
- Use modern browser (Chrome, Firefox, Edge)
- Ensure stable internet connection

## 🔒 Security Best Practices

1. **Never commit `.env` to version control**
2. **Don't share your API key publicly**
3. **Rotate keys if exposed**
4. **Use environment-specific keys**
5. **Monitor API usage on Hugging Face dashboard**

## 📱 Browser Compatibility

Tested and working on:
- ✅ Google Chrome (Recommended)
- ✅ Mozilla Firefox
- ✅ Microsoft Edge
- ✅ Safari
- ⚠️ Internet Explorer (Not supported)

## 💡 Tips for Best Results

### Writing Story Concepts

- Be specific and detailed
- Include conflict and stakes
- Mention key plot points
- Describe the world/setting
- Aim for 100-300 words

### Choosing Genres

- Select the primary genre
- AI will adapt tone and style
- Mix genres in your concept description

### Character Count

- 1-3: Intimate character studies
- 4-6: Ensemble casts
- 7-10: Epic narratives

## 🆘 Getting Help

### Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Hugging Face Docs](https://huggingface.co/docs)
- [Python Documentation](https://docs.python.org)

### Common Commands

**Stop the server**: Press `Ctrl+C` in terminal

**Restart the server**: 
```bash
streamlit run app.py
```

**Clear cache**:
```bash
streamlit cache clear
```

**Update dependencies**:
```bash
pip install -r requirements.txt --upgrade
```

## ✅ Verification Checklist

Before reporting issues, verify:

- [ ] Python version is 3.8+
- [ ] All dependencies installed
- [ ] `.env` file exists with valid API key
- [ ] Internet connection is stable
- [ ] No firewall blocking port 8501
- [ ] Browser is up to date

## 🎉 Success!

If you see the Scriptoria interface with the cinematic gradient background and can generate content, you're all set!

Start creating amazing film projects! 🎬

---

**Need more help?** Check the main README.md or open an issue on GitHub.
