import os.path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
SECRETS_DIR = ".secrets"

def get_file_path(filename):
	return os.path.join(SECRETS_DIR, filename)

def decode_body(data):
	decoded_bytes = base64.urlsafe_b64decode(data)
	decoded_text = decoded_bytes.decode("utf-8")
	return decoded_text

def get_gmail_service():
	# all OAuth code
	# return service
	"""Shows basic usage of the Gmail API.
	Lists the user's Gmail labels.
	"""
	creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	token_filename = get_file_path("token.json")
	credentials_filename = get_file_path("credentials.json")
	if os.path.exists(token_filename):
		creds = Credentials.from_authorized_user_file(token_filename, SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				credentials_filename, SCOPES
			)
			creds = flow.run_local_server(port=0)
	# Save the credentials for the next run
	with open(token_filename, "w") as token:
		token.write(creds.to_json())
	service = build("gmail", "v1", credentials=creds)
	return service

def search_linkedin_job_alerts(service):
    # messages().list(...)
    # return message_ids
	results = service.users().messages().list(
		userId="me",
		q="newer_than:2d from:(jobalerts-noreply@linkedin.com)",
		includeSpamTrash=True,
	).execute()
	message_ids = results.get("messages", [])

	if not message_ids:
		return []
	return message_ids

def get_message(service, message_id):
    # messages().get(...)
	message = service.users().messages().get(
		userId="me",
		id=message_id,
	).execute()
	return message

def get_header_value(message, header_name):
	headers = message.get("payload", {}).get("headers", [])
	for header in headers:
		if header["name"] == header_name:
			return header["value"]
	return ""

def get_message_body_text(message):
    # find text/plain part
    # decode body
    # return clean body text
	parts = message.get("payload", {}).get("parts", [])
	for part in parts:
		if part.get("mimeType") == "text/plain":
			body_data = part.get("body", {}).get("data", "")
			body_text = decode_body(body_data)
			clean_body_text = " ".join(body_text.split())
			return clean_body_text
	return ""

def get_linkedin_job_alert_emails():
	try:
		service = get_gmail_service()
		message_ids = search_linkedin_job_alerts(service)
		emails = []

		for message_info in message_ids:
			message_id = message_info["id"]
			message = get_message(service, message_id)

			email = {
				"message_id": message_id,
				"subject": get_header_value(message, "Subject"),
				"from": get_header_value(message, "From"),
				"date": get_header_value(message, "Date"),
				"snippet": message.get("snippet", ""),
				"body_text": get_message_body_text(message),
			}
			emails.append(email)

		return emails

	except HttpError as error:
		print("Gmail API error:", error)
		return []
