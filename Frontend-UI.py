"""
AI-Powered E-Commerce Listing Generator
Streamlit application that generates product listings using AI analysis of product images.

Features:
- User authentication system
- Image upload and preview
- AI-powered product analysis via LLaVA/Mistral API
- Generated listing formatting
- Session history persistence
- Shareable listing URLs

Environment Requirements:
- Python 3.9+
- Streamlit
- Pillow
- Requests
"""

import streamlit as st
import os
import json
import uuid
import requests
import re
from urllib.parse import urlencode
from PIL import Image

# ─── Session State Initialization ──────────────────────────────────────────────
# Initialize all session state variables and load previous session data

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False  # Track user authentication status
    
if "username" not in st.session_state:
    st.session_state.username = None  # Store authenticated username
    
if "listing_history" not in st.session_state:
    st.session_state.listing_history = {}  # User-specific history storage
    
if "session_state_file" not in st.session_state:
    st.session_state.session_state_file = "session_state.json"  # Persistence file

# Configure page settings
st.set_page_config(
    page_title="AI E-Commerce Listing Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Session Persistence Functions ────────────────────────────────────────────

def save_session():
    """Serialize and save session state to JSON file"""
    session_data = {
        "logged_in": st.session_state.logged_in,
        "username": st.session_state.username,
        "listing_history": st.session_state.listing_history
    }
    try:
        with open(st.session_state.session_state_file, 'w') as f:
            json.dump(session_data, f, indent=2)
    except Exception as e:
        st.error(f"Error saving session: {str(e)}")

def load_session():
    """Load and deserialize session state from JSON file"""
    if os.path.exists(st.session_state.session_state_file):
        try:
            with open(st.session_state.session_state_file, 'r') as f:
                data = json.load(f)
                st.session_state.logged_in = data.get('logged_in', False)
                st.session_state.username = data.get('username')
                st.session_state.listing_history = data.get('listing_history', {})
        except Exception as e:
            st.error(f"Error loading session: {str(e)}")

# Load existing session on startup
load_session()

# ─── Authentication System ────────────────────────────────────────────────────

def authenticate(username: str, password: str) -> bool:
    """
    Validate user credentials against hardcoded values (for demo purposes)
    
    Args:
        username (str): User's login name
        password (str): User's password
        
    Returns:
        bool: True if credentials are valid, False otherwise
    """
    # In production, replace with secure authentication mechanism
    valid_users = {
        "admin": "password123",
        "user": "testpass"
    }
    return valid_users.get(username) == password

def login():
    """Render login form and handle authentication flow"""
    with st.sidebar:
        st.subheader("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.listing_history.setdefault(username, [])
                save_session()
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials!")

def logout():
    """Clear session state and handle user logout"""
    st.session_state.logged_in = False
    st.session_state.username = None
    save_session()
    st.rerun()

# ─── Sidebar Components ──────────────────────────────────────────────────────

# Render sidebar content based on authentication state
with st.sidebar:
    st.title("📌 AI Listing Generator")
    
    if not st.session_state.logged_in:
        login()
        st.write("Or continue as Guest—history won’t be saved.")
    else:
        st.write(f"Logged in as **{st.session_state.username}**")
        if st.button("Logout"):
            logout()
    
    # Display listing history for authenticated users
    if st.session_state.logged_in:
        st.subheader("Listing History")
        history = st.session_state.listing_history.get(st.session_state.username, [])
        
        if history:
            for chat in reversed(history):
                url_params = urlencode({'chat_id': chat['chat_id']})
                st.markdown(f"[📝 {chat['title']}](/?{url_params})")
        else:
            st.write("No history yet.")

# ─── Main Application Logic ──────────────────────────────────────────────────

st.title("🛍️ AI-Powered E-Commerce Listing Generator")
st.markdown("Upload product images to get AI-driven listings!")

# Configure API endpoint with fallback options
API_URL = os.getenv(
    "LLAVA_API_URL",
    st.secrets.get("LLAVA_API_URL", "ENTER-LLAVA-NGROK-API-URL")
)

# ─── Historical Chat Handling ────────────────────────────────────────────────

# Check for existing chat ID in URL parameters
current_query = st.query_params()
chat_id = current_query.get('chat_id', [None])[0]

if chat_id and st.session_state.logged_in:
    # Search for matching chat history
    for entry in st.session_state.listing_history[st.session_state.username]:
        if entry['chat_id'] == chat_id:
            st.subheader(f"📝 {entry['title']}")
            st.markdown(f"**📜 Description:** {entry['description']}")
            st.markdown(f"**📌 Attributes:** {entry['attributes']}")
            st.stop()  # Stop execution to show historical entry

# ─── New Listing Generation Flow ──────────────────────────────────────────────

uploaded_files = st.file_uploader(
    "Upload product images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True,
    help="Upload clear product images from multiple angles"
)

# Display uploaded images in responsive grid
if uploaded_files:
    image_columns = st.columns(3)
    for index, file in enumerate(uploaded_files):
        with image_columns[index % 3]:
            img = Image.open(file)
            st.image(img, use_column_width=True, caption=file.name)

# Handle listing generation request
if st.button("Generate Product Listing", type="primary"):
    if not uploaded_files:
        st.error("Please upload at least one product image.")
        st.stop()
        
    with st.spinner("Analyzing images and generating listing..."):
        try:
            # Prepare multipart/form-data payload
            files_payload = [
                ("images", (file.name, file.getvalue(), file.type))
                for file in uploaded_files
            ]
            
            # Send request to AI API
            response = requests.post(
                f"{API_URL}/analyze-product",
                files=files_payload,
                timeout=30  # Set timeout for API call
            )
            response.raise_for_status()  # Raise exception for HTTP errors
            
            api_data = response.json()
            
        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {str(e)}")
            st.stop()
        except json.JSONDecodeError:
            st.error("Invalid response from API server")
            st.stop()

    # Process API response
    if "listing_section" in api_data:
        raw_listing = api_data["listing_section"]
        
        # Safe JSON parsing with cleanup
        try:
            if isinstance(raw_listing, str):
                # Remove control characters before parsing
                sanitized = re.sub(r"[\x00-\x1f\x7f]", "", raw_listing)
                parsed_listing = json.loads(sanitized)
            else:
                parsed_listing = raw_listing
        except json.JSONDecodeError:
            parsed_listing = {"Raw Listing": raw_listing}
            
        # Display formatted results
        st.markdown("### 🏷️ Generated Product Listing")
        
        # Iterate through listing components
        for section, content in parsed_listing.items():
            if not content:
                continue  # Skip empty sections
                
            section_title = section.replace("_", " ").title()
            st.markdown(f"**{section_title}**")
            
            # Handle different content types
            if isinstance(content, list):
                for item in content:
                    st.markdown(f"- {item}")
            elif isinstance(content, dict):
                for key, value in content.items():
                    st.markdown(f"- **{key.title()}:** {value}")
            else:
                st.write(content)
                
        st.success("Listing generated successfully!")
        
        # Save to history if authenticated
        if st.session_state.logged_in:
            new_entry_id = str(uuid.uuid4())
            history_entry = {
                'chat_id': new_entry_id,
                'title': parsed_listing.get('title', 'New Listing'),
                'description': parsed_listing.get('product_description', ''),
                'attributes': json.dumps(parsed_listing.get('attributes', {}))
            }
            
            st.session_state.listing_history[st.session_state.username].append(history_entry)
            save_session()
            
            # Update URL with new chat ID
            st.experimental_set_query_params(chat_id=new_entry_id)
            st.experimental_rerun()
            
    else:
        st.error("Failed to generate listing - missing 'listing_section' in API response")
