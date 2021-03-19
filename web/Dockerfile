FROM node:latest as build
WORKDIR /web
COPY ./app/package*.json .
RUN npm install
COPY ./app/ .
RUN npm run build

FROM nginx:1.19.7-alpine
WORKDIR /var/www/app
COPY --from=build /web/dist .
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf