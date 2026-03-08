# 🚀 Scriptoria - Deployment Guide

Complete guide for deploying Scriptoria to various platforms.

---

## 📋 Pre-Deployment Checklist

- [ ] Code tested locally
- [ ] All dependencies in requirements.txt
- [ ] .env.example file present
- [ ] .gitignore configured
- [ ] README.md complete
- [ ] No hardcoded secrets
- [ ] API key management ready

---

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended - Free)

**Best for:** Quick deployment, free hosting, automatic updates

#### Steps:

1. **Prepare Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/yourusername/scriptoria.git
   git push -u origin main
   ```

3. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect GitHub account
   - Select repository: `yourusername/scriptoria`
   - Main file: `app.py`
   - Click "Deploy"

4. **Add Secrets**
   - In Streamlit Cloud dashboard
   - Go to App Settings → Secrets
   - Add:
   ```toml
   HF_API_KEY = "your_huggingface_token_here"
   ```

5. **Access Your App**
   - URL: `https://yourusername-scriptoria.streamlit.app`

#### Pros:
✅ Free hosting
✅ Automatic HTTPS
✅ Easy updates (git push)
✅ Built-in secrets management
✅ No server management

#### Cons:
⚠️ Resource limits on free tier
⚠️ Public by default
⚠️ Cold starts possible

---

### Option 2: Hugging Face Spaces (Free)

**Best for:** AI-focused projects, integrated with HF ecosystem

#### Steps:

1. **Create Space**
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Name: `scriptoria`
   - SDK: Streamlit
   - Visibility: Public or Private

2. **Upload Files**
   - Clone the Space repository
   ```bash
   git clone https://huggingface.co/spaces/yourusername/scriptoria
   cd scriptoria
   ```
   
   - Copy all files except .env
   ```bash
   cp -r ../scriptoria/* .
   ```

3. **Create README.md Header**
   Add to top of README.md:
   ```yaml
   ---
   title: Scriptoria
   emoji: 🎬
   colorFrom: purple
   colorTo: blue
   sdk: streamlit
   sdk_version: 1.31.0
   app_file: app.py
   pinned: false
   ---
   ```

4. **Add Secrets**
   - In Space settings
   - Add secret: `HF_API_KEY`
   - Value: Your token

5. **Push and Deploy**
   ```bash
   git add .
   git commit -m "Deploy Scriptoria"
   git push
   ```

6. **Access Your Space**
   - URL: `https://huggingface.co/spaces/yourusername/scriptoria`

#### Pros:
✅ Free hosting
✅ Integrated with HF
✅ GPU options available
✅ Good for AI projects
✅ Community visibility

#### Cons:
⚠️ Slower cold starts
⚠️ Less customization
⚠️ HF-specific setup

---

### Option 3: Heroku (Paid)

**Best for:** Production apps, custom domains, scaling

#### Steps:

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Windows
   # Download from heroku.com
   ```

2. **Create Heroku App**
   ```bash
   heroku login
   heroku create scriptoria-app
   ```

3. **Add Buildpack**
   ```bash
   heroku buildpacks:set heroku/python
   ```

4. **Create Procfile**
   ```bash
   echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile
   ```

5. **Set Environment Variables**
   ```bash
   heroku config:set HF_API_KEY=your_token_here
   ```

6. **Deploy**
   ```bash
   git push heroku main
   ```

7. **Open App**
   ```bash
   heroku open
   ```

#### Pros:
✅ Professional hosting
✅ Custom domains
✅ Scalable
✅ Add-ons available
✅ Good uptime

#### Cons:
⚠️ Paid (after free tier)
⚠️ More complex setup
⚠️ Requires credit card

---

### Option 4: AWS EC2 (Advanced)

**Best for:** Full control, enterprise deployment, custom infrastructure

#### Steps:

1. **Launch EC2 Instance**
   - Ubuntu 22.04 LTS
   - t2.medium or larger
   - Open port 8501

2. **Connect and Setup**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python
   sudo apt install python3-pip python3-venv -y
   ```

3. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/scriptoria.git
   cd scriptoria
   ```

4. **Setup Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Configure Environment**
   ```bash
   nano .env
   # Add: HF_API_KEY=your_token
   ```

6. **Run with Systemd**
   Create `/etc/systemd/system/scriptoria.service`:
   ```ini
   [Unit]
   Description=Scriptoria Streamlit App
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/scriptoria
   Environment="PATH=/home/ubuntu/scriptoria/venv/bin"
   ExecStart=/home/ubuntu/scriptoria/venv/bin/streamlit run app.py --server.port=8501 --server.address=0.0.0.0

   [Install]
   WantedBy=multi-user.target
   ```

7. **Start Service**
   ```bash
   sudo systemctl enable scriptoria
   sudo systemctl start scriptoria
   ```

8. **Setup Nginx (Optional)**
   ```bash
   sudo apt install nginx -y
   ```
   
   Configure reverse proxy for custom domain.

#### Pros:
✅ Full control
✅ Scalable
✅ Custom configuration
✅ Enterprise-ready
✅ Private deployment

#### Cons:
⚠️ Requires DevOps knowledge
⚠️ Manual maintenance
⚠️ Higher cost
⚠️ Security responsibility

---

### Option 5: Docker (Containerized)

**Best for:** Consistent deployment, microservices, Kubernetes

#### Steps:

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.10-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create .dockerignore**
   ```
   .env
   .git
   __pycache__
   *.pyc
   venv/
   ```

3. **Build Image**
   ```bash
   docker build -t scriptoria:latest .
   ```

4. **Run Container**
   ```bash
   docker run -p 8501:8501 \
     -e HF_API_KEY=your_token \
     scriptoria:latest
   ```

5. **Docker Compose (Optional)**
   Create `docker-compose.yml`:
   ```yaml
   version: '3.8'
   services:
     scriptoria:
       build: .
       ports:
         - "8501:8501"
       environment:
         - HF_API_KEY=${HF_API_KEY}
       restart: unless-stopped
   ```

   Run:
   ```bash
   docker-compose up -d
   ```

#### Pros:
✅ Consistent environment
✅ Easy scaling
✅ Portable
✅ Version control
✅ Kubernetes-ready

#### Cons:
⚠️ Docker knowledge required
⚠️ Additional layer
⚠️ Resource overhead

---

## 🔒 Security Best Practices

### Environment Variables

**Never commit secrets:**
```bash
# .gitignore should include:
.env
*.env
secrets/
```

**Use secrets management:**
- Streamlit Cloud: Built-in secrets
- Heroku: Config vars
- AWS: Secrets Manager
- Docker: Environment files

### API Key Rotation

```python
# Implement key rotation
import os
from datetime import datetime

def check_key_age():
    key_created = os.getenv("KEY_CREATED_DATE")
    # Rotate every 90 days
```

### Rate Limiting

```python
# Add rate limiting
from functools import lru_cache
import time

@lru_cache(maxsize=100)
def rate_limited_api_call(prompt):
    time.sleep(1)  # Prevent abuse
    return api_call(prompt)
```

---

## 📊 Monitoring

### Streamlit Cloud

- Built-in analytics
- View logs in dashboard
- Monitor resource usage

### Custom Monitoring

```python
# Add logging
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger.info(f"User generated project: {title}")
```

### Error Tracking

```python
# Add error tracking
try:
    result = generate_content()
except Exception as e:
    logger.error(f"Generation failed: {str(e)}")
    # Send to error tracking service
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions Example

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Streamlit Cloud

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run tests
        run: |
          python -m pytest tests/
      
      - name: Deploy
        run: |
          # Streamlit Cloud auto-deploys on push
          echo "Deployed to Streamlit Cloud"
```

---

## 🧪 Pre-Deployment Testing

### Local Testing

```bash
# Test production mode
streamlit run app.py --server.port=8501 --server.address=0.0.0.0

# Test with production API key
export HF_API_KEY=prod_key
streamlit run app.py
```

### Load Testing

```python
# Simple load test
import concurrent.futures
import requests

def test_endpoint():
    response = requests.get("http://localhost:8501")
    return response.status_code

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(test_endpoint) for _ in range(100)]
    results = [f.result() for f in futures]
```

---

## 📈 Scaling Considerations

### Horizontal Scaling

- Use load balancer
- Multiple instances
- Session state management

### Vertical Scaling

- Increase instance size
- More CPU/RAM
- Better network

### Caching Strategy

```python
# Implement Redis caching
import redis
import streamlit as st

@st.cache_resource
def get_redis_client():
    return redis.Redis(host='localhost', port=6379)

def cached_generation(prompt):
    client = get_redis_client()
    cached = client.get(prompt)
    if cached:
        return cached
    result = generate(prompt)
    client.setex(prompt, 3600, result)  # 1 hour cache
    return result
```

---

## 🎯 Post-Deployment

### Checklist

- [ ] App accessible via URL
- [ ] All features working
- [ ] API calls successful
- [ ] Export functions working
- [ ] Mobile responsive
- [ ] Error handling tested
- [ ] Monitoring setup
- [ ] Backup strategy
- [ ] Documentation updated
- [ ] Team notified

### Maintenance

**Weekly:**
- Check logs
- Monitor API usage
- Review errors

**Monthly:**
- Update dependencies
- Rotate API keys
- Review performance

**Quarterly:**
- Security audit
- Cost optimization
- Feature updates

---

## 💰 Cost Estimation

### Streamlit Cloud
- Free tier: $0/month
- Team: $250/month

### Hugging Face Spaces
- Free tier: $0/month
- Pro: $9/month

### Heroku
- Hobby: $7/month
- Standard: $25-50/month

### AWS EC2
- t2.medium: ~$30/month
- t2.large: ~$60/month
- + bandwidth costs

---

## 🆘 Troubleshooting Deployment

### Common Issues

**Build Fails:**
```bash
# Check requirements.txt
pip install -r requirements.txt --dry-run
```

**App Won't Start:**
```bash
# Check logs
streamlit run app.py --logger.level=debug
```

**API Key Not Working:**
```bash
# Verify environment
echo $HF_API_KEY
```

**Port Conflicts:**
```bash
# Use different port
streamlit run app.py --server.port=8502
```

---

## 📚 Additional Resources

- [Streamlit Deployment Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Hugging Face Spaces Docs](https://huggingface.co/docs/hub/spaces)
- [Heroku Python Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)

---

**Ready to deploy? Choose your platform and follow the guide!** 🚀
