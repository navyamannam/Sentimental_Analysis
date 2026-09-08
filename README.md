# 🍽️ Restaurant Recommendation System

A full-stack restaurant recommendation web application built using the **MERN stack**.  
The application allows users to discover restaurants, filter them by location, cuisine, and rating, and view restaurant locations on an interactive map.

## 🌐 Live Demo

**Deployed Application:**  
https://restaurant-recommendation-mern.vercel.app/

## 📌 Project Overview

The Restaurant Recommendation System helps users find suitable restaurants based on their preferences.

Users can:

- Browse restaurant recommendations
- Filter restaurants by **location**
- Filter restaurants by **cuisine**
- Filter restaurants by **minimum rating**
- View restaurant locations on an interactive map
- View restaurant details such as cuisine, rating, and location
- Get directions to a selected restaurant using Google Maps
- Use the application through a responsive web interface

## ✨ Features

### 🔎 Restaurant Filtering
Restaurants can be filtered using:

- Location
- Cuisine
- Minimum rating

### 🗺️ Interactive Map
The application uses **Mapbox** to display restaurant locations and the user's current location.

### 📍 Location & Directions
The application can request the user's browser location and provides a **Get Directions** option that opens Google Maps.

### ⭐ Restaurant Ratings
Each restaurant displays its rating to help users compare recommendations.

### 📱 Responsive Interface
The frontend is built with React and Bootstrap-based components for a user-friendly interface.

## 🛠️ Technologies Used

### Frontend

- React.js
- React DOM
- React Bootstrap
- Bootstrap 5
- Axios
- React Map GL
- Mapbox GL
- Leaflet / React Leaflet
- HTML5
- CSS3
- JavaScript

### Backend

- Node.js
- Express.js
- CORS
- MongoDB / Mongoose support

### Development Tools

- Visual Studio Code
- Git
- GitHub
- npm
- Vercel

## 📂 Project Structure

```text
restaurent-recommendation-main/
│
├── backend/
│   ├── models/
│   │   ├── Restaurant.js
│   │   └── restaurants.js
│   ├── package.json
│   ├── package-lock.json
│   ├── seed.js
│   └── server.js
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── CardItem.js
│   │   │   ├── MapComponent.js
│   │   │   └── NavBar.js
│   │   ├── context/
│   │   │   ├── RestaurantContext.js
│   │   │   └── useRestaurant.js
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.css
│   │   └── index.js
│   ├── package.json
│   └── package-lock.json
│
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

- Node.js
- npm
- Git
- MongoDB (if using the database/seed functionality)

Check Node.js and npm:

```bash
node --version
npm --version
```

## 💻 Run the Frontend Locally

Open a terminal and navigate to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm start
```

The frontend will normally run at:

```text
http://localhost:3000
```

## ⚙️ Run the Backend Locally

Open a **second terminal** and navigate to the backend folder:

```bash
cd backend
```

Install dependencies:

```bash
npm install
```

Start the backend:

```bash
npm start
```

The backend will normally run at:

```text
http://localhost:5000
```

### API Endpoint

The backend provides:

```text
GET /api/restaurants
```

Example:

```text
http://localhost:5000/api/restaurants
```

The API supports filtering using query parameters such as:

```text
/api/restaurants?location=Delhi
/api/restaurants?cuisine=Indian
/api/restaurants?minRating=4
```

Filters can also be combined:

```text
/api/restaurants?location=Delhi&cuisine=Indian&minRating=4
```

## 🗄️ Database

The backend includes Mongoose models and a seed script for MongoDB.

The seed script can be run with:

```bash
node seed.js
```

Make sure MongoDB is running before using the database seed functionality.

## 🌍 Deployment

The application frontend is deployed using **Vercel**.

### Live URL

https://restaurant-recommendation-mern.vercel.app/

The source code is available on GitHub:

https://github.com/navyamannam/restaurent-recommendation

## 🔐 Environment Variables

If you configure external services such as Mapbox or MongoDB using environment variables, create a `.env` file locally.

Example:

```env
MONGODB_URI=your_mongodb_connection_string
MAPBOX_TOKEN=your_mapbox_token
```

**Do not commit secret API keys, database passwords, or private credentials to GitHub.**

## 🧪 Available npm Commands

### Frontend

```bash
npm start
npm run build
npm test
```

### Backend

```bash
npm start
npm run dev
```

## 🎯 Future Enhancements

Possible improvements include:

- Connect the React frontend directly to the backend API
- Store restaurant information permanently in MongoDB
- Add user authentication
- Add restaurant search
- Add price-range filtering
- Add restaurant images
- Add favorites/wishlist functionality
- Add restaurant reviews and comments
- Add sorting by rating and distance
- Improve map marker interactions
- Add pagination for large restaurant datasets

## 👩‍💻 Author

**Navya Mannam**

GitHub:  
https://github.com/navyamannam

## 📄 License

This project is intended for educational and demonstration purposes.
