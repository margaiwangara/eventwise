# Use an official Node.js base image
FROM node:18-alpine

# Set working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the Next.js app code into the container
COPY . .

# Build the Next.js app for production
RUN npm run build

# Set the environment variable to indicate production mode
ENV NODE_ENV production

# Expose the port on which the Next.js app will run (change it to your desired port)
EXPOSE 3000

# Command to start the Next.js app in production mode
CMD ["npm", "start"]
