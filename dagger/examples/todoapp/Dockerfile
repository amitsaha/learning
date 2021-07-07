FROM node:12-alpine as build

RUN apk update && apk upgrade && \
  apk add --no-cache bash git yarn

RUN mkdir /app

WORKDIR /app

COPY package.json yarn.lock .
RUN --mount=target=/app/node_modules,type=cache \
  yarn install --production

COPY . .
RUN --mount=target=/app/node_modules,type=cache \
  yarn build

FROM nginx:1.12-alpine

WORKDIR /usr/share/nginx/html

# Remove default nginx static assets
RUN rm -rf ./*

COPY --from=build /app/build .
