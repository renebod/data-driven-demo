#!/usr/bin/env bash

docker compose up -d && docker compose logs -f
# docker compose run --rm jupyter ansible-playbook -i hosts playbook.yml
# docker compose run --rm jupyter ansible-playbook -i hosts site.yml --tags test_01