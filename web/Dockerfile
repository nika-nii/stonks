FROM node:latest as build
WORKDIR /web
COPY ./app/package*.json .
RUN npm install
COPY ./app/public ./public
COPY ./app/src ./src
RUN npm run build

FROM nginx:1.19.7-alpine
WORKDIR /var/www/app
COPY --from=build /web/build /var/www/app
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf