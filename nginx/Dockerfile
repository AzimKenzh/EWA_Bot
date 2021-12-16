# Admin project build
FROM node:14.16.0-alpine3.10 as build_admin

COPY admin-app /app_admin
WORKDIR /app_admin
RUN npm install
RUN npm run build
COPY . .



# Final build
FROM nginx:1.19.0-alpine
WORKDIR /app
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build_admin /app_admin/build /usr/share/nginx/admin_html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
