# Tool controllo sicurezza dei config files
Attualmente non esistono tool certificati e/o standard per il controllo dei file di configurazione apache/nginx, tuttavia esistono diverse collezioni di _**tips**_ per evitare gli errori più comuni per quanto riguarda Nginx, tra cui: 
- La repository [nginx-security](https://gist.github.com/1242035/dc01d269e7e41c548b0c314db64a0ced)
- La [documentazione](https://docs.nginx.com/nginx/admin-guide/security-controls/) ufficiale di nginx
- Articolo di [Upguard](https://www.upguard.com/blog/10-tips-for-securing-your-nginx-deployment)

Mentre per la configurazione di Apache possiamo avvalerci di:
- [Security Tips](https://www.upguard.com/blog/10-tips-for-securing-your-nginx-deployment) di Apache
- Articolo di [Acunetix](https://www.acunetix.com/blog/articles/10-tips-secure-apache-installation/)
- Articolo del centro di ricerca governativo Americano [Berkeley Lab Commons](https://commons.lbl.gov/display/cpp/Securing+Apache+Web+Servers)

# Configurazione sicura Apache (httpd.conf)
Esistono diversi fattori più importanti da configurare ed impostare all'interno del file di configurazione httpd.conf, tra cui:

1. Nascondere informazione del server come versione apache e sistema operativo negli header:
   ```apacheconf
   ServerTokens Prod
   ServerSignature Off
   ```

2. Configura l'elenco di file di indice in modo sicuro. Ad esempio, se vuoi consentire solo l'accesso ai file index.html e index.php, puoi specificarlo come segue:
```apacheconf
DirectoryIndex index.html index.php
```

3. Limitare l'accesso a determinate directory usando la direttiva _**Require**_:
```apacheconf
<Directory /var/www/private>
    Require ip 192.168.1.100
</Directory>
```

4. Configurare correttamente SSL/TLS per abilitare SSL e indicare i relativi file per il certificato e la chiave privata del server:
```apacheconf
SSLEngine on
SSLCertificateFile /etc/ssl/certs/server.crt
SSLCertificateKeyFile /etc/ssl/private/server.key
```

5. Personalizzare le pagine di errore per evitare la lettura di informazioni sensibili:
```apacheconf
ErrorDocument 403 /errors/403.html
ErrorDocument 404 /errors/404.html
```

# Configurazione sicura Nginx (nginx.conf)
Anche per Nginx possiamo fare la stessa analisi:

1. Nascondere informazione del server come versione nginx e sistema operativo negli header:
```nginxconf
http {
    server_tokens off;
}
```

2. Limitare le dimensioni del buffer per il body della richiesta per evitare attacchi come DoS:
```nginxconf
http {
    client_body_buffer_size 10K;
}
```

3. Limitare le dimensioni massima del caricamento di file sul server:
```nginxconf
http {
    client_max_body_size 1M;
}
```

4. Limitare connessione massime simultanee da un singolo indirizzo IP:
```nginxconf
http {
    limit_conn_zone $binary_remote_addr zone=conn_limit_per_ip:10m;
    limit_conn conn_limit_per_ip 5;
}
```

5. Configurazione protocolli e cifrari sicuri e standard per SSL/TLS:
```nginxconf
server {
    listen 443 ssl;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256';
}
```

6. Configurare l'header _**X-Content-Type-Options**_ per evitare il _MIME Sniffing_ e l'header _**Content-Security-Policy**_ per mitigare gli attacchi XSS:
```nginxconf
server {
    add_header X-Content-Type-Options nosniff;
    add_header Content-Security-Policy "default-src 'self'";
}

```
