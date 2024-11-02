import requests
import time

def test_sec_api():
    # Test configuration
    email = "getinformation9@gmail.com"
    headers = {
        'User-Agent': f'Value Investing Tool ({email})',
        'Accept': 'application/json',
        'Host': 'data.sec.gov'
    }
    
    # Test URL (Apple's CIK)
    url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json"
    
    print(f"Testing SEC API with URL: {url}")
    print(f"Using headers: {headers}")
    
    try:
        # Add delay for rate limiting
        time.sleep(0.1)
        
        # Make request
        response = requests.get(url, headers=headers, timeout=10)
        
        print(f"Response status code: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("Successfully retrieved data!")
            print(f"Available keys: {list(data.keys())}")
            return True
        else:
            print(f"Error response: {response.text}")
            return False
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_sec_api() 