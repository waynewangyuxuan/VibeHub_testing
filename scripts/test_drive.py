#!/usr/bin/env python3
"""Test Google Drive API connection."""

import os
from pathlib import Path

from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive']
TOKEN_PATH = Path(os.getenv('GOOGLE_TOKEN_PATH', './token.json'))


def get_credentials():
    """Get valid credentials, refreshing or creating new ones as needed."""
    creds = None

    # Load existing token if available
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    # Refresh or get new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Create OAuth flow from env vars
            client_config = {
                "installed": {
                    "client_id": os.getenv('GOOGLE_CLIENT_ID'),
                    "client_secret": os.getenv('GOOGLE_CLIENT_SECRET'),
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": ["http://localhost"]
                }
            }
            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save token for future runs
        TOKEN_PATH.write_text(creds.to_json())
        print(f"Token saved to {TOKEN_PATH}")

    return creds


def main():
    print("Connecting to Google Drive...")
    creds = get_credentials()

    service = build('drive', 'v3', credentials=creds)

    # List first 10 files
    print("\nFetching files from Drive...\n")
    results = service.files().list(
        pageSize=10,
        fields="files(id, name, mimeType)"
    ).execute()

    files = results.get('files', [])

    if not files:
        print("No files found in Drive.")
    else:
        print("Found files:")
        for f in files:
            icon = "📁" if f['mimeType'] == 'application/vnd.google-apps.folder' else "📄"
            print(f"  {icon} {f['name']}")

    print("\n✅ Google Drive connection successful!")


if __name__ == '__main__':
    main()
