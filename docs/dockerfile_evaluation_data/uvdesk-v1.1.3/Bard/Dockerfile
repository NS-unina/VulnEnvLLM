FROM php:7.4-apache

# Install Uvdesk dependencies
RUN apt-get update && apt-get install -y \
    libapache2-mod-php \
    libcurl4-openssl-dev \
    libgd-dev \
    libjpeg-dev \
    libpng-dev \
    libzip-dev \
    mysql-client \
    sqlite3

# Install Uvdesk
RUN curl -sL https://github.com/uvdesk/uvdesk/archive/v1.1.3.tar.gz | tar -xzC /var/www/html

# Configure Uvdesk
RUN chown -R www-data:www-data /var/www/html/uvdesk
RUN chmod -R 755 /var/www/html/uvdesk/upload

# Copy Uvdesk configuration file
COPY ./uvdesk.conf /etc/apache2/sites-available/uvdesk.conf

# Enable Uvdesk site
RUN a2ensite uvdesk

# Restart Apache
RUN service apache2 restart
