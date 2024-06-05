#!/usr/bin/env bash

# https://docs.ansible.com/ansible/latest/collections/ansible/builtin/dict_lookup.html
docker compose up -d && docker compose logs -f