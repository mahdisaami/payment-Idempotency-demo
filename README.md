# 💳 Django Payment Idempotency Demo

This project demonstrates **idempotent payment processing** using Django REST Framework (DRF) and a simulated external payment gateway.

The goal is to show how to handle **unreliable external APIs** with retry logic, exponential backoff, and idempotent responses.

---

## 🚀 Features

- **Payment API** to start and track payments.
- **Fake Gateway** simulates a 30% failure rate and random latency.
- **Retry Logic** with exponential backoff for resilience.
- **Idempotent Design** — repeated requests for the same `order_id` won’t trigger duplicate payments.
- Uses **PostgreSQL** as the database.

---

## 🧩 Project Structure

```
core/
├── core/                 # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── payments/             # Main payment service
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
└── fake_gateway/         # Unstable external API simulator
    ├── views.py
    ├── urls.py
    └── ...
```

---

## ⚙️ Setup

```bash
git clone <repo-url>
cd <project-folder>

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🧠 Endpoints

### 1. Start Payment
`POST /payments/start/`

**Request:**
```json
{
  "order_id": "ORD123",
  "amount": 100.0
}
```

**Response (Success):**
```json
{
  "payment_id": "a4395b0f-8002-4767-b852-e2221e28b5f2"
}
```

**Response (Failure):**
```json
{
  "error": "Gateway error"
}
```

### 2. Fake Gateway
`POST /fake-gateway/start/`

Returns either a 200 or 500 randomly to simulate instability.

---

## 🧪 Example Flow

1. Client calls `/payments/start/`
2. Django calls `/fake-gateway/start/`
3. If the gateway fails → retry up to 3 times
4. If all fail → mark payment as `FAILED`
5. If success → mark payment as `COMPLETED`

---

## 🧰 Tech Stack

- Django (latest)
- Django REST Framework
- PostgreSQL
- Python 3.11+

---
