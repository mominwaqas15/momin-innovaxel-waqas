# URL Shortener API

A simple, fast, and functional URL shortening REST API built with **FastAPI** and **PostgreSQL** for the Innovaxel Assessment.

---

## 🚀 Features

- Shorten long URLs into unique, random short codes
- Retrieve original URLs using short codes
- Update long URLs tied to a short code
- Delete short URLs
- Track and retrieve access statistics (`access_count`)
- CORS-enabled for frontend integration

---

## 🛠 Tech Stack

- **Backend**: Python 3.11, FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Environment**: dotenv
- **Web Server**: Uvicorn

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/mominwaqas15/momin-innovaxel-waqas.git
cd momin-innovaxel-waqas
```

### 2. Create & activate virtual environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your `.env` file

Create a `.env` file in the root folder:

```
DATABASE_URL=postgresql://<user>:<password>@localhost/<dbname>
HOST=127.0.0.1
PORT=8000
```

### 5. Run the application

```bash
uvicorn init:app --reload
```

App will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📬 API Endpoints

| Method     | Endpoint                                     | Description                                    |
| ---------- | -------------------------------------------- | ---------------------------------------------- |
| `POST`   | `/shorten-url`                             | Create a new short URL                         |
| `GET`    | `/get-url-by-shorten-code/{short_code}`    | Retrieve original URL + increment access count |
| `PUT`    | `/update-url-by-shorten-code/{short_code}` | Update original URL                            |
| `DELETE` | `/delete-url-by-shorten-code/{short_code}` | Delete a short URL                             |
| `GET`    | `/get-shorten-url-stats/{short_code}`      | Get stats (`access_count`, timestamps, etc.) |

---

## 🧪 Sample Request (JSON)

### Create Short URL

**POST** `/shorten-url`

```json
{
  "url": "https://example.com/very/long/url"
}
```

---

## 📂 Branch Strategy

- `main`: Contains only the `README.md`
- `dev`: All code and working implementation

---

## 👨‍💻 Author

- **Name**: Momin Waqas
- **Email**: mominwaqas15@gmail.com

---

## 📘 License

MIT License
