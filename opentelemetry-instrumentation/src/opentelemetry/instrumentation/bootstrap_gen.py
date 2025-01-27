# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT. THIS FILE WAS AUTOGENERATED FROM INSTRUMENTATION PACKAGES.
# RUN `python scripts/generate_instrumentation_bootstrap.py` TO REGENERATE.

libraries = [
    {
        "library": "openai >= 1.26.0",
        "instrumentation": "opentelemetry-instrumentation-openai-v2==2.2b0.dev",
    },
    {
        "library": "google-cloud-aiplatform >= 1.64",
        "instrumentation": "opentelemetry-instrumentation-vertexai==2.1b0.dev",
    },
    {
        "library": "aio_pika >= 7.2.0, < 10.0.0",
        "instrumentation": "opentelemetry-instrumentation-aio-pika==0.51b0.dev",
    },
    {
        "library": "aiohttp ~= 3.0",
        "instrumentation": "opentelemetry-instrumentation-aiohttp-client==0.51b0.dev",
    },
    {
        "library": "aiohttp ~= 3.0",
        "instrumentation": "opentelemetry-instrumentation-aiohttp-server==0.51b0.dev",
    },
    {
        "library": "aiokafka >= 0.8, < 1.0",
        "instrumentation": "opentelemetry-instrumentation-aiokafka==0.51b0.dev",
    },
    {
        "library": "aiopg >= 0.13.0, < 2.0.0",
        "instrumentation": "opentelemetry-instrumentation-aiopg==0.51b0.dev",
    },
    {
        "library": "asgiref ~= 3.0",
        "instrumentation": "opentelemetry-instrumentation-asgi==0.51b0.dev",
    },
    {
        "library": "asyncpg >= 0.12.0",
        "instrumentation": "opentelemetry-instrumentation-asyncpg==0.51b0.dev",
    },
    {
        "library": "boto~=2.0",
        "instrumentation": "opentelemetry-instrumentation-boto==0.51b0.dev",
    },
    {
        "library": "boto3 ~= 1.0",
        "instrumentation": "opentelemetry-instrumentation-boto3sqs==0.51b0.dev",
    },
    {
        "library": "botocore ~= 1.0",
        "instrumentation": "opentelemetry-instrumentation-botocore==0.51b0.dev",
    },
    {
        "library": "cassandra-driver ~= 3.25",
        "instrumentation": "opentelemetry-instrumentation-cassandra==0.51b0.dev",
    },
    {
        "library": "scylla-driver ~= 3.25",
        "instrumentation": "opentelemetry-instrumentation-cassandra==0.51b0.dev",
    },
    {
        "library": "celery >= 4.0, < 6.0",
        "instrumentation": "opentelemetry-instrumentation-celery==0.51b0.dev",
    },
    {
        "library": "click >= 8.1.3, < 9.0.0",
        "instrumentation": "opentelemetry-instrumentation-click==0.51b0.dev",
    },
    {
        "library": "confluent-kafka >= 1.8.2, <= 2.7.0",
        "instrumentation": "opentelemetry-instrumentation-confluent-kafka==0.51b0.dev",
    },
    {
        "library": "django >= 1.10",
        "instrumentation": "opentelemetry-instrumentation-django==0.51b0.dev",
    },
    {
        "library": "elasticsearch >= 6.0",
        "instrumentation": "opentelemetry-instrumentation-elasticsearch==0.51b0.dev",
    },
    {
        "library": "falcon >= 1.4.1, < 5.0.0",
        "instrumentation": "opentelemetry-instrumentation-falcon==0.51b0.dev",
    },
    {
        "library": "fastapi ~= 0.58",
        "instrumentation": "opentelemetry-instrumentation-fastapi==0.51b0.dev",
    },
    {
        "library": "flask >= 1.0",
        "instrumentation": "opentelemetry-instrumentation-flask==0.51b0.dev",
    },
    {
        "library": "grpcio >= 1.42.0",
        "instrumentation": "opentelemetry-instrumentation-grpc==0.51b0.dev",
    },
    {
        "library": "httpx >= 0.18.0",
        "instrumentation": "opentelemetry-instrumentation-httpx==0.51b0.dev",
    },
    {
        "library": "jinja2 >= 2.7, < 4.0",
        "instrumentation": "opentelemetry-instrumentation-jinja2==0.51b0.dev",
    },
    {
        "library": "kafka-python >= 2.0, < 3.0",
        "instrumentation": "opentelemetry-instrumentation-kafka-python==0.51b0.dev",
    },
    {
        "library": "kafka-python-ng >= 2.0, < 3.0",
        "instrumentation": "opentelemetry-instrumentation-kafka-python==0.51b0.dev",
    },
    {
        "library": "mysql-connector-python >= 8.0, < 10.0",
        "instrumentation": "opentelemetry-instrumentation-mysql==0.51b0.dev",
    },
    {
        "library": "mysqlclient < 3",
        "instrumentation": "opentelemetry-instrumentation-mysqlclient==0.51b0.dev",
    },
    {
        "library": "pika >= 0.12.0",
        "instrumentation": "opentelemetry-instrumentation-pika==0.51b0.dev",
    },
    {
        "library": "psycopg >= 3.1.0",
        "instrumentation": "opentelemetry-instrumentation-psycopg==0.51b0.dev",
    },
    {
        "library": "psycopg2 >= 2.7.3.1",
        "instrumentation": "opentelemetry-instrumentation-psycopg2==0.51b0.dev",
    },
    {
        "library": "psycopg2-binary >= 2.7.3.1",
        "instrumentation": "opentelemetry-instrumentation-psycopg2==0.51b0.dev",
    },
    {
        "library": "pymemcache >= 1.3.5, < 5",
        "instrumentation": "opentelemetry-instrumentation-pymemcache==0.51b0.dev",
    },
    {
        "library": "pymongo >= 3.1, < 5.0",
        "instrumentation": "opentelemetry-instrumentation-pymongo==0.51b0.dev",
    },
    {
        "library": "pymssql >= 2.1.5, < 3",
        "instrumentation": "opentelemetry-instrumentation-pymssql==0.51b0.dev",
    },
    {
        "library": "PyMySQL < 2",
        "instrumentation": "opentelemetry-instrumentation-pymysql==0.51b0.dev",
    },
    {
        "library": "pyramid >= 1.7",
        "instrumentation": "opentelemetry-instrumentation-pyramid==0.51b0.dev",
    },
    {
        "library": "redis >= 2.6",
        "instrumentation": "opentelemetry-instrumentation-redis==0.51b0.dev",
    },
    {
        "library": "remoulade >= 0.50",
        "instrumentation": "opentelemetry-instrumentation-remoulade==0.51b0.dev",
    },
    {
        "library": "requests ~= 2.0",
        "instrumentation": "opentelemetry-instrumentation-requests==0.51b0.dev",
    },
    {
        "library": "sqlalchemy >= 1.0.0, < 2.1.0",
        "instrumentation": "opentelemetry-instrumentation-sqlalchemy==0.51b0.dev",
    },
    {
        "library": "starlette ~= 0.13.0",
        "instrumentation": "opentelemetry-instrumentation-starlette==0.51b0.dev",
    },
    {
        "library": "psutil >= 5",
        "instrumentation": "opentelemetry-instrumentation-system-metrics==0.51b0.dev",
    },
    {
        "library": "tornado >= 5.1.1",
        "instrumentation": "opentelemetry-instrumentation-tornado==0.51b0.dev",
    },
    {
        "library": "tortoise-orm >= 0.17.0",
        "instrumentation": "opentelemetry-instrumentation-tortoiseorm==0.51b0.dev",
    },
    {
        "library": "pydantic >= 1.10.2",
        "instrumentation": "opentelemetry-instrumentation-tortoiseorm==0.51b0.dev",
    },
    {
        "library": "urllib3 >= 1.0.0, < 3.0.0",
        "instrumentation": "opentelemetry-instrumentation-urllib3==0.51b0.dev",
    },
]
default_instrumentations = [
    "opentelemetry-instrumentation-asyncio==0.51b0.dev",
    "opentelemetry-instrumentation-dbapi==0.51b0.dev",
    "opentelemetry-instrumentation-logging==0.51b0.dev",
    "opentelemetry-instrumentation-sqlite3==0.51b0.dev",
    "opentelemetry-instrumentation-threading==0.51b0.dev",
    "opentelemetry-instrumentation-urllib==0.51b0.dev",
    "opentelemetry-instrumentation-wsgi==0.51b0.dev",
]
