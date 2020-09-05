# Create image based on the official Node image from dockerhub
FROM node:10
# Create a directory where our app will be placed
RUN mkdir -p /usr/src/app
# Change directory so that our commands run inside this new directory
WORKDIR /usr/src/app
# Copy dependency definitions
COPY package*.json ./
# Install dependecies
RUN npm install && npm install -g @quasar/cli
# Get all the code needed to run the app
COPY . .

RUN quasar build

WORKDIR /usr/src/app/dist/spa

# Expose the port the app runs in
EXPOSE 8083
# Serve the app
CMD ["quasar", "serve", ".", "-p", "8083"]