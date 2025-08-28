# MYMETRIC

Scrape Metric Tools

## NODE_EXPORTER

```sh
wget https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz
tar xvfz node_exporter-1.9.1.linux-amd64.tar.gz
cd node_exporter-1.9.1.linux-amd64
cp node_exporter  /usr/local/bin/node_exporter
```

## RUN 

```sh
nohup /usr/local/bin/node_exporter > /var/log/node_exporter.log 2>&1 &

./node_exporter --web.listen-address=":9200"
```
