FROM node:alpine as builder
WORKDIR /App
COPY . .
RUN yarn
RUN yarn run build

FROM nginx:alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /App/dist/ ./
ENTRYPOINT ["nginx", "-g", "daemon off;"]