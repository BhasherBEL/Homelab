# Personal HomeLab

This repository contains the configuration and setup for various services running on my homelabs.

The services runs on two differents locations. Each location has a dedicated folder.
- A HP server (`bxl-shp/`), which run most of the services.
- A VPS (`vps/`), which run mainly the mail server.

Each location directory contains the same structure:
 - `system/`, that contains all the services required for the server to works correctly.
 - `apps/`, that contains all the applications.
 - `config/`, that contains all the public config files and directories mounted into services.
 - `deploy.sh`, that start all the services of the server.

The repository also contains old locations under `archive/`, using the same structure as explained before.

Finally, a directory `builds/` contains the custom services.

## Services 

| Category | Service | State | Accessibility | Description |
| :-: | :-: | :-: | :-: | :- |
| Media | Jellyfin | ✅ | P+A | Media streaming server |
| Media | Radarr | ✅ | L+A | Movie download and management |
| Media | Sonarr | ✅ | L+A | TV series download and management |
| Media | Lidarr | ✅ | L+A | Music download and management |
| Media | Bazarr | ✅ | L+A | Subtitle download and management |
| Media | Transmission | ✅ | L+A | BitTorrent client |
| Media | Prowlarr | ✅ | L+A | Indexer manager |
| Media | Flaresolverr | ✅ | - | CAPTCHA solver |
| Media | Sonarr ytdlp | ❌ | - | Custom Sonarr yt-dlp addon |
| Home | Home Assistant | ✅ | L+A* | Home automation and smart home control platform |
| Home | Node RED | ✅ | L+A | Flow-based development for IoT and automation |
| Home | Zigbee2mqtt | ✅ | - | Zigbee to MQTT bridge for home automation |
| Home | Mosquitto | ✅ | - | MQTT broker |
| Home | Pi-Hole | ✅ | L+(A) | Network-wide ad blocker and DNS sinkhole |
| Pro | Dashy SD | ✅ | L+A | Services dashboard |
| Pro | Invoiceplane | ✅ | L+A* | Invoicing and billing software |
| Pro | Portfolio | ❌ | P | Personal portfolio |
| Tools | Joplin | ✅ | L | Note-taking and to-do list application |
| Tools | Vaultwarden | ✅ | P+A* | Bitwarden password manager |
| Tools | Mealie | ✅ | L+(A*) | Recipe management and meal planning |
| Tools | Dashy | ✅ | L+A | Dashboard for data visualization and control |
| Tools | Focalboard | ✅ | L+A* | Projects and tasks management |
| Tools | Baikal | ✅ | P+A* | CalDAV and CardDAV server |
| Tools | Seafile | ✅ | L+A | Cloud file storage |
| Tools | Onlyoffice-editor | ✅ | P+A* | Online realtime office collaboration |
| Script | tg2 | ✅ | - | Telegram bot for Too Good To Go|
| VPN | Wireguard | ✅ | P+A* | Secure and easy-to-configure VPN solution |
| Monitoring | Grafana | ✅ | L+A | Platform for monitoring and observability |
| Monitoring | Grafana Renderer | ✅ | - | Grafana panel rendering service |
| Monitoring | Grafana Reporter | ✅ | - | Grafana report generation service |
| Monitoring | Grafana SendReport | ✅ | - | Grafana report delivery service |
| Monitoring | Prometheus | ✅ | L+A | Monitoring and alerting toolkit |
| Monitoring | Cadvisor | ✅ | - | Container resource usage and performance analysis |
| Monitoring | Mikrotik Exporter | ✅ | - | Prometheus exporter for MikroTik router metrics |
| Monitoring | Node Exporter | ✅ | - | Prometheus exporter for system and hardware metrics |
| Monitoring | Portainer | ✅ | P+A | Container management and orchestration platform |
| Monitoring | Trakr | ✅ | L+A | Pixel tracker app |
| Auth | OpenLDAP | ✅ | - | Open-source LDAP directory server |
| Auth | LDAPUserManager | ✅ | L+A | User and group management for LDAP |
| Auth | Authelia | ✅ | P+A | Multi-factor authentication and SSO proxy |
| Storage | Postgres | ✅ | - | Relational database management system |
| Storage | MariaDB | ✅ | - | Relational database management system |
| Storage | Redis | ✅ | - | In-memory data structure store |
| Storage | Registry | ✅ | L | Docker image registry |
| Storage | Registry UI | ✅ | L | UI for docker image registry |
| Backup | Borgmatic | ✅ | - | Automatic backup |
| Backup | Borgmatic VPS | ✅ | - | Automatic backup for VPS |
| Reverse Proxy | Traefik | ✅ | P+(A) | Reverse proxy for containerized applications |
| Reverse Proxy | wellknown-nginx | ✅ | P | Serve well-known services |
| Update | Watchtower | ✅ | - | Automatic container image updating |


### Accessibility legend

| Symbol | Meaning | Description |
| ------ | ------- | ----------- |
| P      | Publicly accessible | The service can be accessed by anyone without restrictions. |
| L      | Local-only | The service is accessible only within a local network or environment, not publicly. |
| A      | Authenticated through SSO/LDAP | Access requires authentication via Single Sign-On (SSO) or Lightweight Directory Access Protocol (LDAP). |
| A*     | Authenticated through another way | Access requires authentication using a method other than SSO/LDAP. |
