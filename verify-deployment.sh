#!/bin/bash
# verify-deployment.sh - Verify that your app is deployed and working

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔍 Deployment Verification Tool${NC}"
echo "======================================"
echo ""

# Function to check URL
check_url() {
    local url=$1
    local name=$2
    
    echo -n "Testing $name... "
    if response=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 "$url"); then
        if [ "$response" = "200" ]; then
            echo -e "${GREEN}✅ OK ($response)${NC}"
            return 0
        else
            echo -e "${YELLOW}⚠️  Status: $response${NC}"
            return 1
        fi
    else
        echo -e "${RED}❌ FAILED${NC}"
        return 1
    fi
}

# Get app URL
echo -e "${BLUE}📱 Enter your Render App URL:${NC}"
echo "Example: https://cicd-pipeline-app.onrender.com"
echo -n "URL: "
read APP_URL

if [ -z "$APP_URL" ]; then
    echo -e "${RED}❌ URL cannot be empty${NC}"
    exit 1
fi

# Remove trailing slash if present
APP_URL="${APP_URL%/}"

echo ""
echo -e "${BLUE}Testing endpoints...${NC}"
echo ""

# Test endpoints
check_url "$APP_URL/" "Home endpoint"
check_url "$APP_URL/health" "Health check"
check_url "$APP_URL/api/add/5/3" "Add endpoint (5+3)"
check_url "$APP_URL/api/multiply/4/7" "Multiply endpoint (4*7)"

echo ""
echo -e "${BLUE}📊 Detailed Response Test:${NC}"
echo ""

echo "1. Home Endpoint Response:"
echo -e "${YELLOW}GET $APP_URL/${NC}"
curl -s "$APP_URL/" | python3 -m json.tool 2>/dev/null || echo "(Response not JSON)"
echo ""

echo "2. Health Check Response:"
echo -e "${YELLOW}GET $APP_URL/health${NC}"
curl -s "$APP_URL/health" | python3 -m json.tool 2>/dev/null || echo "(Response not JSON)"
echo ""

echo "3. Math API Test (Add 10 + 20):"
echo -e "${YELLOW}GET $APP_URL/api/add/10/20${NC}"
curl -s "$APP_URL/api/add/10/20" | python3 -m json.tool 2>/dev/null || echo "(Response not JSON)"
echo ""

echo "4. Math API Test (Multiply 3 * 7):"
echo -e "${YELLOW}GET $APP_URL/api/multiply/3/7${NC}"
curl -s "$APP_URL/api/multiply/3/7" | python3 -m json.tool 2>/dev/null || echo "(Response not JSON)"
echo ""

echo -e "${GREEN}✅ Verification Complete!${NC}"
echo ""
echo -e "${BLUE}📝 Next Steps:${NC}"
echo "• If all endpoints returned 200: Your app is working! 🎉"
echo "• If any failed: Check Render logs at dashboard.render.com"
echo "• Monitor deployments at: GitHub Actions"
