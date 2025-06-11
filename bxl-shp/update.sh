cd ~/homelab/bxl-shp
cmd=$(find . -type f \( -name "docker-compose.*.yaml" \) | awk '{printf "-f %s \0", $0}' | xargs -0 -I{} echo "docker compose {} --env-file .env up --pull always -d")
echo $cmd
eval $cmd
# -name "docker-compose.yaml" -o 
