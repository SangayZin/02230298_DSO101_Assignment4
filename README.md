# CI/CD Pipeline with Testing & Deployment

A complete DevOps pipeline implementation demonstrating continuous integration, testing, and automated deployment to Render using GitHub Actions.

> 🚀 **New to this project?** Start with [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide!

## 🎯 Objective

This project implements a real DevOps pipeline including:
- ✅ Build: Automated environment setup
- ✅ Test: Unit tests with pytest
- ✅ Deploy: **Automated deployment to Render**
- ✅ Automation: GitHub Actions workflow

## ⚡ Auto-Deploy Pipeline

```
Push to main → Tests Run → Auto-Deploy to Render → Live App ✅
```

**Every push triggers:**
1. Automatic test execution
2. Automatic deployment (if tests pass)
3. Live app update (zero downtime)

## 📂 Project Structure

```
project/
├── app.py                          # Flask backend application
├── test_app.py                     # Unit tests
├── requirements.txt                # Python dependencies
├── Procfile                        # Render deployment config
├── render.yaml                     # Render service configuration
├── .gitignore                      # Git ignore rules
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI/CD pipeline
├── QUICKSTART.md                   # ⚡ 5-minute setup guide
├── DEPLOYMENT.md                   # 📋 Detailed deployment guide
├── setup-auto-deploy.sh            # 🤖 Automated setup script
├── verify-deployment.sh            # ✅ Verify your deployment
└── README.md                       # This file
```

## 🚀 Features

### Backend Application (Flask)
- **Home endpoint** (`GET /`): Welcome message
- **Health check** (`GET /health`): Service health status
- **Add numbers** (`GET /api/add/<a>/<b>`): Addition operation
- **Multiply numbers** (`GET /api/multiply/<a>/<b>`): Multiplication operation

### Unit Tests
Comprehensive test suite using pytest including:
- Home endpoint tests
- Health check validation
- API endpoint validation
- Helper function tests
- Edge case testing (negative numbers, zero, etc.)

### CI/CD Pipeline
Automated workflow triggered on push to main branch:
1. **Checkout**: Pull latest code
2. **Setup**: Configure Python 3.9 environment
3. **Install**: Download dependencies from requirements.txt
4. **Test**: Run all tests with pytest
5. **Deploy**: Automated deployment notification

## 📋 Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git
- GitHub account
- Render account (for deployment)

## 🛠 Local Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Tests
```bash
pytest
```

### 5. Run Application Locally
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🧪 Testing

Run the test suite with verbose output:
```bash
pytest --verbose
```

Run specific test file:
```bash
pytest test_app.py -v
```

Run with coverage:
```bash
pip install pytest-cov
pytest --cov=app test_app.py
```

## 📊 Test Coverage

The test suite includes:
- **Basic assertions**: Simple math operations
- **Endpoint tests**: All API endpoints validated
- **Edge cases**: Negative numbers, zero values
- **Response validation**: Status codes and JSON responses
- **Helper functions**: Direct function testing

## 🔄 GitHub Actions CI/CD Pipeline

The pipeline (`.github/workflows/ci.yml`) automatically:
1. ✅ Builds the environment on every push to main
2. ✅ Installs all dependencies
3. ✅ Runs complete test suite
4. ✅ Reports test results
5. ✅ Prepares for deployment

### View Pipeline Status
- Go to your GitHub repository
- Click on "Actions" tab
- View workflow runs and logs

## 🚢 Deployment to Render

### Option 1: Manual Deployment
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Select this project
5. Configure:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Python Version**: 3.9

### Option 2: Automated Deployment (Recommended) ⭐

This project includes automatic deployment on every push to `main`!

**Quick Setup:**
1. Create a web service on [Render](https://render.com)
2. Get the Deploy Hook URL from Render settings
3. Add it to GitHub Secrets as `RENDER_DEPLOY_HOOK`
4. Push code to `main` branch
5. GitHub Actions automatically builds, tests, and deploys! 🚀

**Full Setup Guide**: See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions

### Deploy Configuration
- **Procfile**: Specifies how Render runs the application
- **render.yaml**: Defines Render service configuration
- Both files are pre-configured for this project

## 🌐 Live Application

Once deployed to Render, your app will be available at:
```
https://your-app-name.onrender.com
```

**Key Endpoints:**
- **Homepage**: `https://your-app-name.onrender.com/`
- **Health Check**: `https://your-app-name.onrender.com/health`
- **Add API**: `https://your-app-name.onrender.com/api/add/5/3`
- **Multiply API**: `https://your-app-name.onrender.com/api/multiply/5/3`

**Auto-Deploy Workflow:**
```
Push to main → GitHub Actions → Build & Test → Deploy to Render → Live! ✅
```

## 📝 API Endpoints

### Home
```
GET /
Response: {"message": "Welcome to the CI/CD Pipeline App!"}
```

### Health Check
```
GET /health
Response: {"status": "healthy"}
Status: 200 OK
```

### Add Numbers
```
GET /api/add/5/3
Response: {
  "a": 5,
  "b": 3,
  "result": 8,
  "operation": "addition"
}
```

### Multiply Numbers
```
GET /api/multiply/5/3
Response: {
  "a": 5,
  "b": 3,
  "result": 15,
  "operation": "multiplication"
}
```

## 🔐 Environment Variables

Currently, no environment variables are required. Optional:
- `PORT`: Custom port (default: 5000)
- Set in Render dashboard or locally via `.env` file

## 📦 Dependencies

- **Flask 2.3.3**: Web framework for Python
- **pytest 7.4.2**: Testing framework
- **gunicorn 21.2.0**: WSGI HTTP Server for production

## 🐛 Troubleshooting

### Tests Fail Locally
```bash
# Clear Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
# Reinstall dependencies
pip install --upgrade -r requirements.txt
# Run tests again
pytest -v
```

### Render Deployment Issues
- Check Render dashboard logs
- Verify `Procfile` and `render.yaml` syntax
- Ensure all dependencies are in `requirements.txt`
- Check that environment uses Python 3.9+

### GitHub Actions Failures
- Check "Actions" tab in repository for logs
- Verify `.github/workflows/ci.yml` syntax
- Ensure `requirements.txt` is valid
- Confirm tests pass locally before pushing

## 📚 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Guide](https://docs.github.com/en/actions)
- [Render Deployment Guide](https://render.com/docs)
- [DevOps Best Practices](https://www.atlassian.com/devops)

## 📄 Assignment Details

**Course**: DSO101 - Continuous Integration and Continuous Deployment  
**Assignment**: 4  
**Student ID**: 02230298  
**Objective**: Implement complete CI/CD pipeline with automated testing and deployment

## ✅ Completion Checklist

- [x] Backend application created (Flask)
- [x] Unit tests implemented (pytest)
- [x] CI/CD pipeline configured (GitHub Actions)
- [x] Deployment configuration (Render)
- [x] Automated build process
- [x] Automated test execution
- [x] Deployment notifications
- [x] Documentation completed
- [x] Project structure organized
- [x] Error handling implemented

## 🤝 Contributing

This is an assignment project. For feedback or improvements, please contact the instructor.

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review GitHub Actions logs
3. Consult the documentation links provided
4. Contact course instructor

---

**Last Updated**: May 2026  
**Status**: Complete ✅