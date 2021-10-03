import logging, logging.config
import json
import subprocess
# import uvicorn

def configure_logging():
    logging.config.dictConfig(app_logging)
    return

def read_config():
    global env_shared
    env_shared = json.load(open('./config/env.shared.json', 'r'))
    global env_environment
    env_environment = json.load(open(f"{env_shared['configsPath']}/env.{env_shared['environment']}.json", 'r'))
    global env_secrets
    env_secrets = json.load(open(f"{env_shared['configsPath']}/env.secrets.json", 'r'))
    global app_logging
    app_logging = json.load(open(f"{env_shared['configsPath']}/log.{env_shared['environment']}.json", 'r'))
    return

if __name__ == '__main__':
    read_config()
    configure_logging()
    subprocess.run('uvicorn --factory app.server:create_app --reload --ssl-certfile ./config/localhost.pem --ssl-keyfile ./config/localhost-key.pem')
    # uvicorn.run("app.main:app",
    #             host="127.0.0.1",
    #             port=8000,
    #             reload=True,
    #             ssl_keyfile="./config/localhost-key.pem", 
    #             ssl_certfile="./config/localhost.pem"
    #             )