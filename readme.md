# MERN Stack Project with Docker

This project is a full-stack application using the MERN (MongoDB, Express.js, React, Node.js) stack, containerized with Docker.

## Project Structure

```
MERNASSIGNMENT/
├── backend/
│   ├── config/
│   ├── models/
│   ├── routes/
│   ├── app-with-mongodb.js
│   ├── app.js
│   ├── mongodb-script.js
│   ├── server.js
│   ├── Dockerfile
│   ├── package.json
│   └── package-lock.json
├── frontend/
│   ├── public/
│   ├── src/
│   ├── Dockerfile
│   ├── package.json
│   └── package-lock.json
├── docker-compose.yml
└── README.md
```

## Prerequisites

- Docker
- Docker Compose

## Setup and Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd MERNASSIGNMENT
   ```

2. Build and start the Docker containers:
   ```
   docker-compose up --build
   ```

3. The application will be available at:
   - Frontend: http://localhost:3001
   - Backend API: http://localhost:3000
   - MongoDB: localhost:27017

## Docker Configuration

The project uses Docker to containerize the application. Key files:

- `docker-compose.yml`: Defines the multi-container Docker application
- `backend/Dockerfile`: Instructions for building the backend container
- `frontend/Dockerfile`: Instructions for building the frontend container

To rebuild the containers after changes:
```
docker-compose down
docker-compose up --build
```

## Development

### Backend
- The main server file is `app-with-mongodb.js` in the `backend` directory.
- MongoDB connection is established in this file.
- API routes are defined here.

### Frontend
- The React application is in the `frontend` directory.
- It's set up to run on port 3001.

## Environment Variables

Ensure the following environment variables are set in your `docker-compose.yml`:

- `MONGODB_URI`: The connection string for your MongoDB database

## Troubleshooting

If you encounter any issues:

1. Check Docker logs:
   ```
   docker-compose logs
   ```

2. Ensure all containers are running:
   ```
   docker-compose ps
   ```

3. Verify the MongoDB connection string in the backend configuration.

4. For frontend issues, check the console in your web browser's developer tools.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request