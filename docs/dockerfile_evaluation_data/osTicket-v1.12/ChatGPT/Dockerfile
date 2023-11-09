# Use an official PHP image as base
FROM php:7.4-apache

# Install required PHP extensions
RUN docker-php-ext-install mysqli && \
    docker-php-ext-install gd && \
    docker-php-ext-install gettext && \
    docker-php-ext-install intl

# Set recommended PHP.ini settings
RUN { \
        echo 'date.timezone = "UTC"'; \
        echo 'memory_limit = 256M'; \
        echo 'upload_max_filesize = 100M'; \
        echo 'post_max_size = 100M'; \
        echo 'max_execution_time = 600'; \
    } > /usr/local/etc/php/php.ini

# Download and install osTicket v1.12
WORKDIR /var/www/html
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://github.com/osTicket/osTicket/releases/download/v1.12/osTicket-v1.12.zip && \
    unzip osTicket-v1.12.zip && \
    rm osTicket-v1.12.zip && \
    chown -R www-data:www-data upload include && \
    a2enmod rewrite

# Expose ports
EXPOSE 80

# Start Apache
CMD ["apache2-foreground"]
