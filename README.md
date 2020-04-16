# blackbox exporter to kinesis
Script to run blackbox exporter and send the output to AWS Kinesis without Prometheus.

## How use:
    - configure on blackbox_exporter 
    - set url address of blackbox exporter into probe.py 
    - configure cron to execute at minute
