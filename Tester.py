import shodan

def display_netcat_banner():
    """Display a Net Cat banner for the script."""
    print(r"""
     |\---/|
     | o_o |  Shodan API Key Tester
      \_^_/
    """)

def test_shodan_api_key(api_key):
    """Test if a Shodan API key is valid."""
    try:
        # Initialize Shodan API
        api = shodan.Shodan(api_key)

        # Perform a test search to check the key
        api.info()  # Get account info (simple call to verify key)
        print("✅ API key is valid!")
        return True
    except shodan.exception.APIError as e:
        print(f"❌ Invalid API key: {e}")
        return False
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
        return False

if __name__ == "__main__":
    display_netcat_banner()
    
    # Input API key
    api_key = input("Enter your Shodan API key: ").strip()

    # Test the API key
    if test_shodan_api_key(api_key):
        print("You can now use this key with Shodan!")
    else:
        print("Please check your API key and try again.")
