# Grafana Not Displaying Data

This guide is for identifying configuration mistakes in [self-hosted Supabase Grafana installations](https://supabase.com/docs/guides/monitoring-troubleshooting/metrics#deploying-supabase-grafana).

## Step 1: Ping your Grafana endpoint

Use the below cURL command to make sure your metrics endpoint returns data:

```bash
curl https://<YOUR_PROJECT_REF>.supabase.co/customer/v1/privileged/metrics --user 'service_role:<SERVICE_ROLE_KEY>'
```

## Step 2: Set your Grafana Dashboard to auto-refresh in the top right corner

![Grafana auto-refresh setting](https://supabase.com/docs/img/troubleshooting/47998bed-0b77-433a-bfed-63222beb2aee.png)

## Step 3: Make sure your docker container has the default configurations

Run the following command in the terminal:

```bash
docker ps -f name=supabase-grafana
```

The output should look something like this:

```
- CONTAINER ID: <container id>
- IMAGE: supabase-grafana-supabase-grafana
- COMMAND: /entrypoint.sh
- CREATED: <time>
- STATUS: Up <unit of time> ago
- PORTS: 3000/tcp, 0.0.0.0:8000 → 8080/tcp
- NAMES: supabase-grafana-supabase-grafana-1
```

## Step 4: Enter the container

Try running the following terminal command:

```bash
docker exec -it <container id> bash
```

## Step 5: Check the environment variables for errors

Run the following in the docker container:

```bash
printenv | egrep 'GRAFANA_PASSWORD|SUPABASE_PROJECT_REF|SUPABASE_SERVICE_ROLE_KEY'
```

Ensure the values are correct by comparing them with those in the Dashboard. Users have previously encountered issues by accidentally omitting the last character of their strings, so a thorough check is essential.

## Step 6: Go to the root folder and check permissions on the `entrypoint.sh` file

Run the following terminal commands:

```bash
cd /
ls -l | grep entrypoint.sh
```

`entrypoint.sh` should have the following permissions:

```
-rwxr-xr-x
```

If permissions are incorrect, update them:

```bash
chmod +x entrypoint.sh
```
