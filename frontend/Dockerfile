# Use an official Node runtime as a parent image
FROM node:16.20.2-alpine
   
# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the current directory contents into the container at /app
COPY . .

# Set the port environment variable
ENV PORT=3001

# Expose port 3001
EXPOSE 3001

# Command to run the application
CMD ["npm", "start"]