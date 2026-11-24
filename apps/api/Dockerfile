FROM node:22-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY src ./src
COPY ../../packages/shared ./packages/shared
CMD ["npm","run","dev"]