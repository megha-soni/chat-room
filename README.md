# chat-room
# Django WebSocket Chat App

## Features
- Dummy login using just a username
- WebSocket chat room (general)
- Message broadcasting with timestamp
- Stores last 20 messages

## Setup
```bash
git clone <repo_url>
cd chatapp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

| Task                            | Status |
|-------------------------------|--------|
| Dummy Login                    | ✅     |
| WebSocket Setup                | ✅     |
| Broadcast Messages             | ✅     |
| Store Last 20 Messages         | ✅     |
| Use Django Channels            | ✅     |
| URL Format (WebSocket)         | ✅     |
| README + Flow + Postman (if any API) | ✅     |
